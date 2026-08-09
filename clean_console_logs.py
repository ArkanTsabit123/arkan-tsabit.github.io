#clean_console_logs.py

"""
Clean console.log statements from JavaScript files.

This script removes unnecessary console.log statements while preserving
critical ones needed for production debugging. It supports dry-run mode,
creates automatic backups, and generates a JSON report of all changes.

Usage:
    python clean_console_logs.py
"""

import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any


# ============================================================================
# Configuration
# ============================================================================

FILES_TO_CLEAN: List[str] = [
    "js/chatbot.js",
    "js/dark-mode.js",
    "js/i18n.js",
    "js/main.js",
    "js/projects.js",
    "chatbot/convert-to-ndjson.js",
    "chatbot/upload-knowledge.js",
    "chatbot/worker.js",
]

# Console.log statements that must be preserved for production debugging
KEEP_PATTERNS: List[str] = [
    r"console\.log\s*\(\s*['\"]No matches found['\"]\s*\)",
    r"console\.log\s*\(\s*['\"]No content extracted from matches['\"]\s*\)",
]


# ============================================================================
# Core Functions
# ============================================================================

def should_keep_log(line: str) -> bool:
    """
    Determine if a console.log statement should be preserved.

    Args:
        line: The source code line to evaluate.

    Returns:
        True if the log should be kept, False otherwise.
    """
    stripped = line.strip()
    for pattern in KEEP_PATTERNS:
        if re.search(pattern, stripped, re.IGNORECASE):
            return True
    return False


def create_backup(file_path: str) -> Path:
    """
    Create a timestamped backup of the given file.

    Args:
        file_path: Path to the file to backup.

    Returns:
        Path object pointing to the backup file.
    """
    backup_dir = Path("backups/console_logs")
    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = Path(file_path).name
    backup_path = backup_dir / f"{filename}.{timestamp}.bak"

    shutil.copy2(file_path, backup_path)
    return backup_path


def analyze_file(file_path: str) -> Dict[str, Any]:
    """
    Analyze a JavaScript file for console.log statements.

    Args:
        file_path: Path to the JavaScript file.

    Returns:
        A dictionary containing analysis results.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        total_logs = 0
        keep_logs = 0
        remove_logs = 0
        keep_lines: List[Dict[str, Any]] = []
        remove_lines: List[Dict[str, Any]] = []

        for i, line in enumerate(lines, 1):
            if "console.log(" in line:
                total_logs += 1
                stripped = line.strip()
                if should_keep_log(line):
                    keep_logs += 1
                    keep_lines.append({"line": i, "content": stripped})
                else:
                    remove_logs += 1
                    remove_lines.append({"line": i, "content": stripped})

        return {
            "file": file_path,
            "total": total_logs,
            "keep": keep_logs,
            "remove": remove_logs,
            "keep_lines": keep_lines,
            "remove_lines": remove_lines,
            "has_changes": remove_logs > 0,
        }
    except Exception as e:
        return {"file": file_path, "error": str(e)}


def clean_file(file_path: str, dry_run: bool = True) -> Dict[str, Any]:
    """
    Remove unnecessary console.log statements from a file.

    Args:
        file_path: Path to the JavaScript file.
        dry_run: If True, preview changes without modifying the file.

    Returns:
        A dictionary containing the operation result.
    """
    analysis = analyze_file(file_path)
    if "error" in analysis:
        return {"file": file_path, "error": analysis["error"]}

    if not analysis["has_changes"]:
        return {
            "file": file_path,
            "status": "no_change",
            "message": "No unnecessary logs found",
        }

    if dry_run:
        return {
            "file": file_path,
            "status": "dry_run",
            "total": analysis["total"],
            "keep": analysis["keep"],
            "remove": analysis["remove"],
            "keep_lines": analysis["keep_lines"],
            "remove_lines": analysis["remove_lines"],
        }

    backup_path = create_backup(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    removed_count = 0
    for line in lines:
        if "console.log(" in line and not should_keep_log(line):
            removed_count += 1
            continue
        new_lines.append(line)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return {
        "file": file_path,
        "status": "success",
        "backup": str(backup_path),
        "removed": removed_count,
        "total": analysis["total"],
        "keep": analysis["keep"],
        "removed_lines": analysis["remove_lines"],
        "kept_lines": analysis["keep_lines"],
    }


def save_report(results: List[Dict[str, Any]], dry_run: bool) -> Path:
    """
    Save the operation results to a JSON report.

    Args:
        results: List of result dictionaries.
        dry_run: Whether the operation was a dry run.

    Returns:
        Path to the generated report file.
    """
    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    mode = "dryrun" if dry_run else "executed"
    report_path = report_dir / f"console_log_cleanup_{mode}_{timestamp}.json"

    successful_results = [r for r in results if "error" not in r]
    total_removed = sum(r.get("remove", 0) for r in successful_results)
    total_kept = sum(r.get("keep", 0) for r in successful_results)

    report = {
        "timestamp": datetime.now().isoformat(),
        "mode": "dry_run" if dry_run else "executed",
        "summary": {
            "total_files": len(successful_results),
            "total_removed": total_removed,
            "total_kept": total_kept,
        },
        "results": results,
    }

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return report_path


def display_rules() -> None:
    """Display the keep/remove rules for console.log statements."""
    print("=" * 70)
    print("CLEAN CONSOLE.LOG - SAFE MODE WITH JSON REPORT")
    print("=" * 70)
    print()
    print("RULES:")
    print("  KEPT (critical for debugging):")
    for pattern in KEEP_PATTERNS:
        print(f"    - {pattern}")
    print()
    print("  REMOVED (unnecessary):")
    print("    - All other console.log statements")
    print()
    print("=" * 70)
    print()


def get_user_choice() -> Optional[str]:
    """
    Prompt the user for the operation mode.

    Returns:
        '1' for dry run, '2' for execute, or None if invalid.
    """
    print("Select mode:")
    print("  1. Dry Run (preview only, no changes) + JSON report")
    print("  2. Execute (apply changes with backup) + JSON report")
    print()
    choice = input("Enter choice (1/2): ").strip()

    if choice not in ["1", "2"]:
        print("Invalid choice. Exiting.")
        return None

    return choice


def confirm_execution() -> bool:
    """
    Request confirmation before executing changes.

    Returns:
        True if confirmed, False otherwise.
    """
    print()
    print("WARNING: You are about to remove console.log statements.")
    print("  - Backups will be created in backups/console_logs/")
    print("  - A JSON report will be saved in reports/")
    print("  - You can restore from backup at any time")
    confirm = input("  Proceed? (y/n): ").strip().lower()
    return confirm == "y"


def display_dry_run_results(results: List[Dict[str, Any]]) -> None:
    """Display dry run results in a readable format."""
    for result in results:
        if "error" in result:
            print(f"  ERROR: {result['file']} - {result['error']}")
            continue

        file_path = result.get("file", "unknown")
        remove_count = result.get("remove", 0)
        keep_count = result.get("keep", 0)

        print(f"  {file_path}")
        print(f"    Will remove: {remove_count} log(s)")
        print(f"    Will keep: {keep_count} log(s)")

        removed_lines = result.get("remove_lines", [])
        if removed_lines:
            for entry in removed_lines[:3]:
                content = entry["content"][:60]
                if len(entry["content"]) > 60:
                    content += "..."
                print(f"      - Line {entry['line']}: {content}")
            if len(removed_lines) > 3:
                print(f"      ... and {len(removed_lines) - 3} more")
        print()


def display_execution_results(results: List[Dict[str, Any]]) -> None:
    """Display execution results in a readable format."""
    for result in results:
        if "error" in result:
            print(f"  ERROR: {result['file']} - {result['error']}")
            continue

        status = result.get("status")
        file_path = result.get("file", "unknown")

        if status == "no_change":
            print(f"  {file_path}: No unnecessary logs found")
        elif status == "success":
            print(f"  {file_path}: SUCCESS")
            print(f"    Removed: {result.get('removed', 0)} log(s)")
            print(f"    Kept: {result.get('keep', 0)} log(s)")
            print(f"    Backup: {result.get('backup', 'N/A')}")
        else:
            print(f"  {file_path}: Unknown status")


def display_summary(results: List[Dict[str, Any]], dry_run: bool, report_path: Path) -> None:
    """Display the final summary of the operation."""
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    successful = [r for r in results if "error" not in r]
    total_removed = sum(r.get("remove", 0) for r in successful)
    total_kept = sum(r.get("keep", 0) for r in successful)

    if dry_run:
        print(f"  DRY RUN - No files were modified")
        print(f"  Would remove: {total_removed} log(s)")
        print(f"  Would keep: {total_kept} log(s)")
    else:
        print(f"  Processed: {len(successful)} file(s)")
        print(f"  Removed: {total_removed} log(s)")
        print(f"  Kept: {total_kept} log(s)")
        print()
        print("  Backups saved in: backups/console_logs/")
        print("  To restore: copy backup file to original location")

    print()
    print(f"  JSON report saved: {report_path}")
    print("=" * 70)


# ============================================================================
# Main Entry Point
# ============================================================================

def main() -> None:
    """Main entry point for the console log cleaner script."""
    display_rules()

    choice = get_user_choice()
    if choice is None:
        return

    dry_run = choice == "1"

    if not dry_run and not confirm_execution():
        print("Operation cancelled.")
        return

    print()
    print("=" * 70)
    print("  DRY RUN MODE" if dry_run else "  EXECUTE MODE (with backup)")
    print("=" * 70)
    print()

    results: List[Dict[str, Any]] = []

    for file_path in FILES_TO_CLEAN:
        if not os.path.exists(file_path):
            print(f"  File not found: {file_path}")
            results.append({"file": file_path, "error": "File not found"})
            continue

        print(f"  Processing: {file_path}")
        result = clean_file(file_path, dry_run=dry_run)
        results.append(result)

        if "error" in result:
            print(f"    ERROR: {result['error']}")
        elif result.get("status") == "no_change":
            print(f"    No unnecessary logs found")
        elif result.get("status") == "dry_run":
            print(f"    Will remove: {result.get('remove', 0)} log(s)")
            print(f"    Will keep: {result.get('keep', 0)} log(s)")
        elif result.get("status") == "success":
            print(f"    SUCCESS: Removed {result.get('removed', 0)} log(s)")
            print(f"    Backup: {result.get('backup', 'N/A')}")
        print()

    report_path = save_report(results, dry_run)

    if dry_run:
        display_dry_run_results(results)
    else:
        display_execution_results(results)

    display_summary(results, dry_run, report_path)


if __name__ == "__main__":
    main()