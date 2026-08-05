# test_all.py
"""
Test all chatbot questions against the Cloudflare Worker API.
"""

import requests
import json
import sys
import time
from typing import List, Dict, Any, Tuple


WORKER_URL = "https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat"
HEADERS = {"Content-Type": "application/json"}


def load_questions() -> List[str]:
    """Return a list of all test questions."""
    return [
        # Profile
        "Who is Arkan Tsabit?",
        "What is Arkan's background?",
        "What does Arkan specialize in?",
        # Projects
        "What data engineering projects has Arkan built?",
        "What is BatchETL Pipeline?",
        "What is Uber Data Pipeline?",
        "What is Amazon Web Scraping?",
        "What is Daily Expense Tracker?",
        # Certifications
        "What certifications does Arkan have?",
        "What Oracle certifications does Arkan have?",
        "Does Arkan have IBM certification?",
        "Does Arkan have Meta certification?",
        "What is Oracle Multicloud Architect Professional?",
        "What is Oracle Generative AI Professional?",
        "What is Oracle AI Vector Search Certified Professional?",
        "What is Oracle Autonomous Database Cloud Professional?",
        "What is Oracle Cloud Database Services Professional?",
        "What is Oracle OCI AI Foundations Associate?",
        "What is Oracle OCI Foundations Associate?",
        "What is Oracle Data Platform Foundations Associate?",
        # Achievements
        "What achievements does Arkan have?",
        "What is Oracle Race to Certification?",
        "What is Best Teacher Award?",
        # Experience
        "What is Arkan's work experience?",
        "What did Arkan do at BRI SD-WAN?",
        "What did Arkan do at Satu Benih?",
        "What did Arkan do at Bejagoo?",
        "What did Arkan do at Soekarno-Hatta Airport?",
        # Skills
        "What is Arkan's tech stack?",
        "What data engineering skills does Arkan have?",
        "What cloud skills does Arkan have?",
        # Contact
        "How to contact Arkan?",
        # General
        "Tell me about Arkan",
        "What does Arkan do?"
    ]


def is_valid_answer(answer: str) -> bool:
    """
    Check if the answer is meaningful (not a default refusal).

    Returns:
        True if answer contains meaningful information, False otherwise.
    """
    refusal_phrases = [
        "i don't have that information",
        "i don't have specific information",
        "i don't have information",
        "not further described",
        "not defined or explained",
        "unspecified",
        "does not provide",
        "not mentioned",
        "no information"
    ]

    answer_lower = answer.lower()
    for phrase in refusal_phrases:
        if phrase in answer_lower:
            return False

    return True


def ask_question(question: str) -> Tuple[str, str, bool]:
    """
    Send a question to the chatbot API.

    Returns:
        Tuple: (response_text, source, is_success)
    """
    payload = {"question": question}

    try:
        response = requests.post(
            WORKER_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            return f"HTTP {response.status_code}", "error", False

        data = response.json()
        source = data.get("source", "unknown")
        answer = data.get("response", "No response")

        if source == "llm" and is_valid_answer(answer):
            return answer, source, True
        else:
            return answer, source, False

    except requests.exceptions.Timeout:
        return "Request timeout", "error", False
    except Exception as error:
        return f"Error: {error}", "error", False


def print_result(index: int, total: int, question: str, answer: str, source: str, success: bool) -> None:
    """Print a formatted test result."""
    status = "PASS" if success else "FAIL"
    status_color = "\033[92m" if success else "\033[91m"
    reset = "\033[0m"

    print(f"\n[{index}/{total}] {question}")
    print("-" * 50)
    print(f"Status: {status_color}{status}{reset}")
    print(f"Source: {source}")

    if len(answer) > 200:
        print(f"Response: {answer[:200]}...")
    else:
        print(f"Response: {answer}")


def run_tests() -> None:
    """Run all tests and print summary."""
    questions = load_questions()
    total = len(questions)

    print("=" * 60)
    print("CHATBOT API TEST")
    print("=" * 60)
    print(f"Total questions: {total}")
    print("=" * 60)

    passed = 0
    failed = 0
    results = []

    for index, question in enumerate(questions, start=1):
        answer, source, success = ask_question(question)
        results.append((question, answer, source, success))

        if success:
            passed += 1
        else:
            failed += 1

        print_result(index, total, question, answer, source, success)
        time.sleep(0.1)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total:  {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Rate:   {((passed / total) * 100):.1f}%")

    if failed == 0:
        print("\nAll tests passed successfully.")
    else:
        print(f"\n{failed} tests failed. Please review the output above.")
        sys.exit(1)


if __name__ == "__main__":
    run_tests()