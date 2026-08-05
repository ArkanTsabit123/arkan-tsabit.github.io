#chatbot RAG Debugger.py
"""
Chatbot RAG Debugger - Diagnostic Tool
Runs comprehensive tests and provides recommendations for fixing issues.
Does not perform any automatic fixes without user confirmation.
"""

import requests
import json
import os
import sys
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

ACCOUNT_ID = "" # Replace with your Cloudflare account ID
API_TOKEN = "" # Replace with your Cloudflare API token
WORKER_URL = "https://arkan-chatbot.arkan-chatbot.workers.dev"
INDEX_NAME = "arkan-knowledge-base"
EMBEDDING_MODEL = "@cf/baai/bge-small-en-v1.5"
LLM_MODEL = "@cf/meta/llama-3-8b-instruct"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}"

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def print_result(status, message, detail=""):
    """Print a formatted result with status indicator."""
    icons = {"pass": "✅", "fail": "❌", "warn": "⚠️", "info": "ℹ️"}
    icon = icons.get(status, "•")
    print(f" {icon} {message}")
    if detail:
        print(f"    {detail}")

# ============================================================
# TEST 1: Generate Embedding
# ============================================================

def test_embedding():
    """Test embedding generation for a sample question."""
    print_section("TEST 1: Generate Embedding")
    
    question = "What projects has Arkan built?"
    print(f"Question: {question}")
    
    response = requests.post(
        f"{BASE_URL}/ai/run/{EMBEDDING_MODEL}",
        headers=HEADERS,
        json={"text": question}
    )
    
    if response.status_code != 200:
        print_result("fail", f"Failed to generate embedding: {response.status_code}")
        print(response.text)
        return None
    
    data = response.json()
    if not data.get("success"):
        print_result("fail", "API error", str(data.get("errors")))
        return None
    
    embedding = data["result"]["data"][0]
    print_result("pass", f"Embedding generated: {len(embedding)} dimensions")
    print(f"    Sample: {embedding[:5]}...")
    return embedding

# ============================================================
# TEST 2: Query Vectorize
# ============================================================

def test_vectorize_query(embedding):
    """Test Vectorize query with the generated embedding."""
    print_section("TEST 2: Vectorize Query")
    
    response = requests.post(
        f"{BASE_URL}/vectorize/v2/indexes/{INDEX_NAME}/query",
        headers=HEADERS,
        json={
            "vector": embedding,
            "topK": 5,
            "returnMetadata": True
        }
    )
    
    if response.status_code != 200:
        print_result("fail", f"Vectorize query failed: {response.status_code}")
        print(response.text)
        return None
    
    data = response.json()
    if not data.get("success"):
        print_result("fail", "API error", str(data.get("errors")))
        return None
    
    matches = data.get("result", {}).get("matches", [])
    print_result("pass", f"Vectorize returned {len(matches)} matches")
    
    for i, match in enumerate(matches[:3]):
        score = match.get("score", "N/A")
        doc_id = match.get("id", "unknown")
        metadata = match.get("metadata", {})
        content = metadata.get("content", "")
        
        print(f"\n  Match {i+1}:")
        print(f"    ID: {doc_id}")
        print(f"    Score: {score}")
        print(f"    Content: {content[:100]}...")
    
    return data

# ============================================================
# TEST 3: Check Index Information
# ============================================================

def test_index_info():
    """Retrieve and display Vectorize index information."""
    print_section("TEST 3: Index Information")
    
    response = requests.get(
        f"{BASE_URL}/vectorize/v2/indexes/{INDEX_NAME}",
        headers=HEADERS
    )
    
    if response.status_code != 200:
        print_result("fail", f"Failed to get index info: {response.status_code}")
        return
    
    data = response.json()
    if not data.get("success"):
        print_result("fail", "API error", str(data.get("errors")))
        return
    
    info = data.get("result", {})
    stored_vectors = info.get("stored_vectors", 0)
    
    print_result("pass", f"Index: {INDEX_NAME}")
    print(f"    Stored Vectors: {stored_vectors}")
    print(f"    Dimensions: {info.get('dimensions', 'N/A')}")
    
    if stored_vectors == 0:
        print_result("fail", "Index is EMPTY! No vectors found.")
    else:
        print_result("pass", f"Index contains {stored_vectors} vectors")

# ============================================================
# TEST 4: Test Worker API
# ============================================================

def test_worker():
    """Test the deployed Cloudflare Worker API."""
    print_section("TEST 4: Worker API Test")
    
    question = "What projects has Arkan built?"
    
    try:
        response = requests.post(
            f"{WORKER_URL}/api/chat",
            headers={"Content-Type": "application/json"},
            json={"question": question},
            timeout=30
        )
        
        if response.status_code != 200:
            print_result("fail", f"Worker error: {response.status_code}")
            return
        
        data = response.json()
        source = data.get("source", "unknown")
        answer = data.get("response", "")
        
        print_result("pass", f"Worker responded: source={source}")
        print(f"    Response: {answer[:200]}...")
        
        if source == "default":
            print_result("fail", "Worker returned default response (context not found)")
        elif source == "llm":
            print_result("pass", "Worker successfully responded with LLM!")
        
    except Exception as e:
        print_result("fail", f"Worker error: {e}")

# ============================================================
# TEST 5: Check Local Data Files
# ============================================================

def test_local_files():
    """Check if required local data files exist."""
    print_section("TEST 5: Local Files Check")
    
    files_to_check = [
        "chatbot/knowledge-upload.json",
        "chatbot/knowledge-upload.ndjson",
        "chatbot/convert-to-ndjson.js",
        "chatbot/upload_vectors.py"
    ]
    
    all_exist = True
    for file_path in files_to_check:
        exists = os.path.exists(file_path)
        if exists:
            size = os.path.getsize(file_path)
            print_result("pass", f"{file_path} exists", f"{size} bytes")
        else:
            print_result("fail", f"{file_path} not found")
            all_exist = False
    
    return all_exist

# ============================================================
# TEST 6: Validate Worker Configuration
# ============================================================

def test_worker_config():
    """Validate the worker configuration file."""
    print_section("TEST 6: Worker Configuration")
    
    config_path = "chatbot/wrangler.toml"
    if not os.path.exists(config_path):
        print_result("fail", f"{config_path} not found")
        return
    
    try:
        with open(config_path, "r") as f:
            content = f.read()
        
        required_bindings = ["VECTORIZE", "AI"]
        found_bindings = []
        
        if "VECTORIZE" in content:
            found_bindings.append("VECTORIZE")
        if "AI" in content:
            found_bindings.append("AI")
        
        if len(found_bindings) == len(required_bindings):
            print_result("pass", "All required bindings found", ", ".join(found_bindings))
        else:
            print_result("fail", "Missing bindings", f"Found: {', '.join(found_bindings)}")
            
    except Exception as e:
        print_result("fail", f"Error reading config: {e}")

# ============================================================
# TEST 7: Validate LLM Model
# ============================================================

def test_llm_availability():
    """Check if the configured LLM model is available."""
    print_section("TEST 7: LLM Model Availability")
    
    test_prompt = "Hello, this is a test."
    
    try:
        response = requests.post(
            f"{BASE_URL}/ai/run/{LLM_MODEL}",
            headers=HEADERS,
            json={
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": test_prompt}
                ],
                "max_tokens": 10
            },
            timeout=30
        )
        
        if response.status_code == 200:
            print_result("pass", f"LLM model is available: {LLM_MODEL}")
        elif response.status_code == 500:
            error_data = response.json()
            error_msg = error_data.get("errors", [{}])[0].get("message", "")
            if "deprecated" in error_msg.lower():
                print_result("fail", f"LLM model DEPRECATED: {LLM_MODEL}")
                print(f"    {error_msg}")
                print("\n    Recommended alternative models:")
                print("    - @cf/meta/llama-4-scout-17b-16e-instruct")
                print("    - @cf/mistralai/mistral-small-3.1-24b-instruct")
                print("    - @cf/google/gemma-4-26b-a4b-it")
            else:
                print_result("fail", f"LLM model error: {response.status_code}")
        else:
            print_result("fail", f"LLM model check failed: {response.status_code}")
            
    except Exception as e:
        print_result("fail", f"LLM availability check error: {e}")

# ============================================================
# DIAGNOSTIC SUMMARY
# ============================================================

def display_recommendations():
    """Display diagnostic recommendations."""
    print_section("RECOMMENDATIONS")
    
    print("Based on the diagnostic results, check the following:")
    print()
    print("1. INDEX STATUS")
    print("   - If 'Stored Vectors = 0': Upload knowledge base to Vectorize")
    print("   - Run: cd chatbot && python upload_vectors.py")
    print()
    print("2. WORKER CONFIGURATION")
    print("   - Ensure wrangler.toml has VECTORIZE and AI bindings")
    print("   - Run: cd chatbot && npx wrangler deploy")
    print()
    print("3. LLM MODEL")
    print("   - If model is deprecated, update worker.js with a newer model")
    print("   - Recommended: @cf/meta/llama-4-scout-17b-16e-instruct")
    print()
    print("4. LOCAL FILES")
    print("   - Ensure knowledge-upload.json and related files exist")
    print("   - Run: cd chatbot && node convert-to-ndjson.js")
    print()
    print("5. KNOWLEDGE BASE")
    print("   - Verify documents have 'metadata.content' field")
    print("   - Check content is properly formatted in knowledge-upload.json")

# ============================================================
# MAIN
# ============================================================

def main():
    """Main diagnostic execution."""
    print("\n" + "=" * 70)
    print(" CHATBOT RAG DIAGNOSTIC TOOL")
    print("=" * 70)
    print(f"Account ID: {ACCOUNT_ID}")
    print(f"Index: {INDEX_NAME}")
    print(f"Worker: {WORKER_URL}")
    print("=" * 70)
    print("\nThis tool only diagnoses issues. No automatic fixes will be applied.")
    print("All actions require manual confirmation.\n")
    
    # Run all tests
    embedding = test_embedding()
    
    if embedding:
        test_vectorize_query(embedding)
    else:
        print_result("fail", "Skipping Vectorize query - embedding generation failed")
    
    test_index_info()
    test_worker()
    test_local_files()
    test_worker_config()
    test_llm_availability()
    
    display_recommendations()
    
    print("\n" + "=" * 70)
    print(" DIAGNOSTIC COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()