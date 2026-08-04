#structure.py

"""
Project Structure Display Script

Displays the folder structure of the project.
Excludes:
    - Virtual environment (venv/)
    - Git directory (.git/)
    - Cache directories (__pycache__, .pytest_cache)
    - IDE directories (.vscode, .idea)
    - Logs directory (logs/)
    - Temporary files
"""

import os
from pathlib import Path
from typing import List, Set


class ProjectStructure:
    """Display project folder structure."""

    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir).resolve()
        self.exclude_patterns: Set[str] = {
            "venv",
            ".git",
            "__pycache__",
            ".pytest_cache",
            ".vscode",
            ".idea",
            "logs",
            "node_modules",
            ".DS_Store",
            "*.pyc",
            "*.pyo",
            "*.pyd",
            "*.so",
            "*.dylib",
            "*.dll",
            "*.exe",
            "*.log",
            "*.tmp",
            "*.temp",
            "*.swp",
            "*.swo",
            ".env",
            ".env.local",
        }

        self.exclude_extensions: Set[str] = {
            ".pyc",
            ".pyo",
            ".pyd",
            ".so",
            ".dylib",
            ".dll",
            ".exe",
            ".log",
            ".tmp",
            ".temp",
            ".swp",
            ".swo",
        }

        self.exclude_dirs: Set[str] = {
            "venv",
            ".git",
            "__pycache__",
            ".pytest_cache",
            ".vscode",
            ".idea",
            "logs",
            "node_modules",
        }

    def is_excluded(self, path: Path) -> bool:
        """Check if a path should be excluded."""
        # Exclude directories
        if path.is_dir():
            if path.name in self.exclude_dirs:
                return True
            return False

        # Exclude files
        if any(pattern in path.name for pattern in self.exclude_patterns):
            return True

        # Exclude by extension
        if path.suffix in self.exclude_extensions:
            return True

        return False

    def generate_tree(
        self,
        directory: Path,
        prefix: str = "",
        is_last: bool = True,
        depth: int = 0,
        max_depth: int = 4,
    ) -> str:
        """Generate directory tree recursively."""
        if depth > max_depth:
            return ""

        tree = ""
        items = sorted(directory.iterdir())

        # Filter excluded items
        items = [item for item in items if not self.is_excluded(item)]

        for index, item in enumerate(items):
            is_last_item = index == len(items) - 1
            current_prefix = "└── " if is_last_item else "├── "

            tree += f"{prefix}{current_prefix}{item.name}"

            if item.is_dir():
                tree += "/\n"
                next_prefix = prefix + ("    " if is_last_item else "│   ")
                tree += self.generate_tree(
                    item,
                    next_prefix,
                    is_last_item,
                    depth + 1,
                    max_depth,
                )
            else:
                tree += "\n"

        return tree

    def display(self) -> None:
        """Display the project structure."""
        print("=" * 60)
        print("PROJECT STRUCTURE")
        print("=" * 60)
        print(f"Root: {self.root_dir}\n")

        tree = self.generate_tree(self.root_dir)
        print(tree)

        print("=" * 60)
        print("Legend:")
        print("  ├── file.py    - Regular file")
        print("  └── folder/    - Directory")
        print("=" * 60)


def main():
    """Main entry point."""
    structure = ProjectStructure()
    structure.display()


if __name__ == "__main__":
    main()