# upload_vectors.py
"""
Upload vectors to Cloudflare Vectorize with proper error handling and logging.
"""

import requests
import json
import sys
from typing import List, Dict, Any, Optional


ACCOUNT_ID = ""  # Replace with your Cloudflare account ID
API_TOKEN = "" # Replace with your Cloudflare API token
INDEX_NAME = "arkan-knowledge-base"
EMBEDDING_MODEL = "@cf/baai/bge-small-en-v1.5"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/x-ndjson"
}


def load_documents(file_path: str) -> List[Dict[str, Any]]:
    """Load documents from a JSON file."""
    with open(file_path, "r") as file:
        data = json.load(file)
    return data.get("documents", [])


def generate_embedding(text: str) -> Optional[List[float]]:
    """Generate embedding for a given text using Cloudflare AI."""
    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/{EMBEDDING_MODEL}",
        headers={"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"},
        json={"text": text},
        timeout=30
    )

    if response.status_code != 200:
        print(f"Embedding API error: {response.status_code}")
        return None

    data = response.json()
    if not data.get("success"):
        print(f"Embedding API error: {data.get('errors')}")
        return None

    return data["result"]["data"][0]


def create_vector_entry(doc: Dict[str, Any], embedding: List[float]) -> Dict[str, Any]:
    """Create a vector entry for upload."""
    return {
        "id": doc["id"],
        "metadata": doc.get("metadata", {}),
        "values": embedding
    }


def upload_vectors(vectors: List[Dict[str, Any]]) -> bool:
    """Upload vectors to Cloudflare Vectorize."""
    if not vectors:
        print("No vectors to upload")
        return False

    ndjson_data = "\n".join([json.dumps(v) for v in vectors])

    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/vectorize/v2/indexes/{INDEX_NAME}/insert",
        headers=HEADERS,
        data=ndjson_data,
        timeout=60
    )

    if response.status_code != 200:
        print(f"Upload failed: {response.status_code}")
        print(response.text)
        return False

    result = response.json()
    if result.get("success"):
        print(f"Upload successful. Mutation ID: {result.get('result', {}).get('mutationId')}")
        return True

    print(f"Upload failed: {result.get('errors')}")
    return False


def main():
    """Main execution function."""
    print("Loading documents...")
    documents = load_documents("knowledge-upload.json")
    print(f"Loaded {len(documents)} documents")

    vectors = []
    for idx, doc in enumerate(documents):
        content = doc.get("metadata", {}).get("content", "")
        if not content:
            print(f"Skipping document {doc.get('id')} - no content")
            continue

        embedding = generate_embedding(content)
        if embedding is None:
            print(f"Failed to generate embedding for {doc.get('id')}")
            continue

        vectors.append(create_vector_entry(doc, embedding))

        if (idx + 1) % 10 == 0:
            print(f"Processed {idx + 1}/{len(documents)} documents")

    print(f"Generated {len(vectors)} embeddings")

    if not vectors:
        print("No vectors to upload")
        sys.exit(1)

    success = upload_vectors(vectors)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()