# upload_vectors.py
"""
Upload vectors to Cloudflare Vectorize.

This script generates embeddings for documents and uploads them
to a Cloudflare Vectorize index using the NDJSON format.
"""

import os
import json
import sys
import requests
from typing import List, Dict, Any, Optional

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not installed. Install with: pip install python-dotenv")

# Get credentials from environment variables
ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
INDEX_NAME = os.getenv("VECTORIZE_INDEX_NAME", "arkan-knowledge-base")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "@cf/baai/bge-small-en-v1.5")

# Validate credentials
if not ACCOUNT_ID or not API_TOKEN:
    print("ERROR: Missing Cloudflare credentials.")
    print("Create a .env file with:")
    print("  CLOUDFLARE_ACCOUNT_ID=your_account_id")
    print("  CLOUDFLARE_API_TOKEN=your_api_token")
    sys.exit(1)


def load_documents(file_path: str) -> List[Dict[str, Any]]:
    """
    Load documents from a JSON file.

    Args:
        file_path: Path to the JSON file containing documents.

    Returns:
        List of document objects.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data.get("documents", [])


def generate_embedding(text: str) -> Optional[List[float]]:
    """
    Generate embedding for text using Cloudflare AI.

    Args:
        text: Input text to generate embedding for.

    Returns:
        Embedding vector as list of floats, or None if failed.
    """
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/{EMBEDDING_MODEL}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {"text": text}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        if not data.get("success"):
            print(f"Embedding API error: {data.get('errors')}")
            return None

        return data["result"]["data"][0]

    except requests.exceptions.RequestException as error:
        print(f"Embedding request failed: {error}")
        return None


def build_vector_entry(doc: Dict[str, Any], embedding: List[float]) -> Dict[str, Any]:
    """
    Build vector entry for upload.

    Args:
        doc: Document object containing id and metadata.
        embedding: Embedding vector.

    Returns:
        Vector entry ready for upload.
    """
    return {
        "id": doc["id"],
        "values": embedding,
        "metadata": doc.get("metadata", {}),
    }


def upload_vectors(vectors: List[Dict[str, Any]]) -> bool:
    """
    Upload vectors to Cloudflare Vectorize.

    Args:
        vectors: List of vector entries.

    Returns:
        True if upload succeeded, False otherwise.
    """
    if not vectors:
        print("No vectors to upload")
        return False

    ndjson_lines = []
    for vector in vectors:
        entry = {
            "id": vector["id"],
            "values": vector["values"],
            "metadata": vector.get("metadata", {}),
        }
        ndjson_lines.append(json.dumps(entry))

    ndjson_payload = "\n".join(ndjson_lines)

    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/vectorize/v2/indexes/{INDEX_NAME}/insert"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/x-ndjson",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            data=ndjson_payload,
            timeout=120
        )
        response.raise_for_status()

        result = response.json()
        if result.get("success"):
            mutation_id = result.get("result", {}).get("mutationId")
            print(f"Upload successful. Mutation ID: {mutation_id}")
            print(f"Vectors uploaded: {len(vectors)}")
            return True

        print(f"Upload failed: {result.get('errors')}")
        return False

    except requests.exceptions.RequestException as error:
        print(f"Upload request failed: {error}")
        return False


def process_documents(documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Process documents and generate embeddings.

    Args:
        documents: List of documents.

    Returns:
        List of vector entries.
    """
    vectors = []
    total = len(documents)

    for index, doc in enumerate(documents, start=1):
        content = doc.get("metadata", {}).get("content", "")

        if not content:
            print(f"Skipping document {doc.get('id')} - no content")
            continue

        print(f"Processing {index}/{total}: {doc.get('id')}")
        embedding = generate_embedding(content)

        if embedding is None:
            print(f"Failed to generate embedding for {doc.get('id')}")
            continue

        vectors.append(build_vector_entry(doc, embedding))

    return vectors


def main() -> None:
    """Main execution function."""
    print("Vectorize Uploader")
    print(f"Account ID: {ACCOUNT_ID[:8]}...")  # Hanya tampilkan 8 karakter pertama
    print(f"Index Name: {INDEX_NAME}")
    print(f"Model: {EMBEDDING_MODEL}")
    print("-" * 50)

    print("Loading documents...")
    documents = load_documents("knowledge-upload.json")
    print(f"Loaded {len(documents)} documents")

    print("Generating embeddings...")
    vectors = process_documents(documents)
    print(f"Generated {len(vectors)} embeddings")

    if not vectors:
        print("No vectors to upload")
        sys.exit(1)

    print("Uploading vectors...")
    success = upload_vectors(vectors)

    if success:
        print("All vectors uploaded successfully")
        sys.exit(0)
    else:
        print("Upload failed")
        sys.exit(1)


if __name__ == "__main__":
    main()