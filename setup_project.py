#!/usr/bin/env python3
"""
Project Setup Script

Creates project structure, configuration files, and development environment.
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


class ProjectSetup:
    """Set up project structure and environment."""

    def __init__(self):
        self.root_dir = Path.cwd()  
        self.files_created: List[str] = []
        self.dirs_created: List[str] = []

    def create_directories(self) -> None:
        """Create project directory structure."""
        directories = [
            "css",
            "js",
            "assets/images/projects/batchetl",
            "assets/images/projects/uber",
            "assets/images/projects/amazon",
            "assets/images/projects/expense",
            "assets/images/certifications",
            "assets/icons",
            "assets/fonts",
            "docs/CV",
            "docs/Job-Application",
            "chatbot/knowledge-base",
            "data/i18n",
            "screenshots",
            "backups",
            "logs",
        ]

        for directory in directories:
            dir_path = self.root_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            self.dirs_created.append(str(dir_path))

            # Create .gitkeep file to keep empty directories
            keep_file = dir_path / ".gitkeep"
            keep_file.touch(exist_ok=True)

    def create_config_files(self) -> None:
        """Create configuration files."""
        config_files = {
            ".gitignore": """# Python
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.coverage
htmlcov/
.tox/
.mypy_cache/

# IDE
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# Environment
.env
.env.local
.env.*.local

# Logs and temp
logs/
*.log
*.tmp
*.temp

# Node
node_modules/
package-lock.json

# Build
dist/
build/
*.egg-info/

# Project specific
backups/
*.duckdb
*.db
""",
            ".env.example": """# Cloudflare
CLOUDFLARE_ACCOUNT_ID=your_account_id
CLOUDFLARE_API_TOKEN=your_api_token
VECTORIZE_INDEX_NAME=arkan-knowledge-base
AI_MODEL=@cf/meta/llama-3-8b-instruct

# Website
DOMAIN=arkan-tsabit.github.io
SITE_NAME=Arkan Tsabit Portfolio

# Analytics
GA_MEASUREMENT_ID=G-XXXXXXXXXX
""",
            "CNAME": "arkan-tsabit.github.io",
        }

        for filename, content in config_files.items():
            file_path = self.root_dir / filename
            file_path.write_text(content)
            self.files_created.append(str(file_path))

    def create_placeholder_files(self) -> None:
        """Create placeholder files for images."""
        placeholders = [
            "assets/images/profile.jpg",
            "assets/images/logo.svg",
            "assets/images/favicon.ico",
            "assets/images/projects/batchetl/architecture.png",
            "assets/images/projects/batchetl/dashboard.png",
            "assets/images/projects/batchetl/erd.png",
            "assets/images/projects/uber/pipeline-flow.png",
            "assets/images/projects/uber/star-schema.png",
            "assets/images/projects/uber/dashboard.png",
            "assets/images/projects/amazon/scraping-result.png",
            "assets/images/projects/amazon/csv-output.png",
            "assets/images/projects/expense/gui-dashboard.png",
            "assets/images/projects/expense/cli-summary.png",
            "assets/images/certifications/oracle.png",
            "assets/images/certifications/ibm.png",
            "assets/images/certifications/meta.png",
            "assets/icons/github.svg",
            "assets/icons/linkedin.svg",
            "assets/icons/email.svg",
            "assets/icons/download.svg",
            "assets/icons/chatbot.svg",
            "assets/fonts/inter.woff2",
        ]

        for placeholder in placeholders:
            file_path = self.root_dir / placeholder
            if not file_path.exists():
                # Create empty placeholder file
                file_path.touch()
                self.files_created.append(str(file_path))

    def create_documentation_files(self) -> None:
        """Create documentation files."""
        docs_files = {
            "README.md": "# Arkan Tsabit - Portfolio Website\n\nPersonal portfolio website.\n",
            "LICENSE": """MIT License

Copyright (c) 2026 Arkan Tsabit

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
            "CHANGELOG.md": """# Changelog

## [1.0.0] - 2026-08-05

### Added
- Initial release
- Portfolio website with 6 pages
- Dark/light mode toggle
- Multi-language support
- RAG chatbot integration
""",
        }

        for filename, content in docs_files.items():
            file_path = self.root_dir / filename
            file_path.write_text(content)
            self.files_created.append(str(file_path))

    def create_data_files(self) -> None:
        """Create data JSON files."""
        data_files = {
            "data/projects.json": """{
  "projects": [
    {
      "id": "batchetl",
      "name": "BatchETL Pipeline",
      "description": "End-to-end ETL pipeline for NYC Taxi data",
      "metrics": {
        "rows": "2.96M",
        "execution": "<30s",
        "quality": "100%"
      }
    }
  ]
}
""",
            "data/certifications.json": """{
  "certifications": [
    {
      "id": "oci-multicloud",
      "provider": "Oracle",
      "name": "OCI Multicloud Architect Professional",
      "year": 2025
    }
  ]
}
""",
            "data/achievements.json": """{
  "achievements": [
    {
      "id": "oracle-race-2025",
      "title": "Oracle Race to Certification",
      "description": "Top 108 Global, Top 3 Indonesia",
      "year": 2025
    }
  ]
}
""",
            "data/i18n/en.json": """{
  "nav": {
    "home": "Home",
    "about": "About Me",
    "projects": "Projects",
    "certifications": "Certifications",
    "achievements": "Achievements",
    "contact": "Contact"
  }
}
""",
            "data/i18n/id.json": """{
  "nav": {
    "home": "Beranda",
    "about": "Tentang Saya",
    "projects": "Proyek",
    "certifications": "Sertifikasi",
    "achievements": "Prestasi",
    "contact": "Kontak"
  }
}
""",
        }

        for filename, content in data_files.items():
            file_path = self.root_dir / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
            self.files_created.append(str(file_path))

    def create_chatbot_files(self) -> None:
        """Create chatbot files."""
        chatbot_files = {
            "chatbot/worker.js": "// Cloudflare Worker - RAG Chatbot\n\nexport default {\n  async fetch(request, env, ctx) {\n    return new Response('Hello from Arkan\\'s AI Chatbot!');\n  }\n};\n",
            "chatbot/wrangler.toml": """name = "arkan-chatbot"
main = "worker.js"
compatibility_date = "2025-01-01"

[[vectorize]]
binding = "VECTORIZE"
index_name = "arkan-knowledge-base"

[[ai]]
binding = "AI"
""",
            "chatbot/knowledge-base/cv-data.json": "{}",
            "chatbot/knowledge-base/projects-data.json": "{}",
            "chatbot/knowledge-base/certifications-data.json": "{}",
        }

        for filename, content in chatbot_files.items():
            file_path = self.root_dir / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
            self.files_created.append(str(file_path))

    def create_html_files(self) -> None:
        """Create HTML files."""
        html_files = {
            "index.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Arkan Tsabit - Data Engineer</title>\n</head>\n<body>\n    <h1>Arkan Tsabit</h1>\n    <p>Data Engineer | Cloud Data Engineer</p>\n</body>\n</html>",
            "about.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>About Me - Arkan Tsabit</title>\n</head>\n<body>\n    <h1>About Me</h1>\n</body>\n</html>",
            "projects.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Projects - Arkan Tsabit</title>\n</head>\n<body>\n    <h1>Projects</h1>\n</body>\n</html>",
            "certifications.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Certifications - Arkan Tsabit</title>\n</head>\n<body>\n    <h1>Certifications</h1>\n</body>\n</html>",
            "achievements.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Achievements - Arkan Tsabit</title>\n</head>\n<body>\n    <h1>Achievements</h1>\n</body>\n</html>",
            "contact.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Contact - Arkan Tsabit</title>\n</head>\n<body>\n    <h1>Contact</h1>\n</body>\n</html>",
            "404.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Page Not Found</title>\n</head>\n<body>\n    <h1>404 - Page Not Found</h1>\n    <a href=\"/\">Go Home</a>\n</body>\n</html>",
        }

        for filename, content in html_files.items():
            file_path = self.root_dir / filename
            file_path.write_text(content)
            self.files_created.append(str(file_path))

    def create_css_files(self) -> None:
        """Create CSS files."""
        css_files = {
            "css/style.css": "/* Main Styles */\n\nbody {\n    font-family: 'Inter', sans-serif;\n    margin: 0;\n    padding: 0;\n}",
            "css/dark-mode.css": "/* Dark Mode Styles */\n\n[data-theme=\"dark\"] {\n    background-color: #0F172A;\n    color: #F8FAFC;\n}",
            "css/responsive.css": "/* Responsive Styles */\n\n@media (max-width: 768px) {\n    body {\n        font-size: 14px;\n    }\n}",
            "css/chatbot.css": "/* Chatbot Styles */\n\n#chatbot-widget {\n    position: fixed;\n    bottom: 20px;\n    right: 20px;\n    z-index: 1000;\n}",
        }

        for filename, content in css_files.items():
            file_path = self.root_dir / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
            self.files_created.append(str(file_path))

    def create_js_files(self) -> None:
        """Create JavaScript files."""
        js_files = {
            "js/main.js": "// Main JavaScript\n\ndocument.addEventListener('DOMContentLoaded', function() {\n    console.log('Website loaded');\n});",
            "js/dark-mode.js": "// Dark Mode Toggle\n\nfunction toggleTheme() {\n    const html = document.documentElement;\n    const current = html.getAttribute('data-theme');\n    const next = current === 'dark' ? 'light' : 'dark';\n    html.setAttribute('data-theme', next);\n    localStorage.setItem('theme', next);\n}",
            "js/i18n.js": "// Multi-language Support\n\nfunction setLanguage(lang) {\n    localStorage.setItem('lang', lang);\n    location.reload();\n}",
            "js/chatbot.js": "// Chatbot Integration\n\nfunction sendMessage() {\n    const input = document.getElementById('chatbot-input');\n    const message = input.value;\n    // Send to Cloudflare Worker\n    console.log('Sending:', message);\n}",
            "js/projects.js": "// Projects Filter\n\nfunction filterProjects(category) {\n    console.log('Filtering by:', category);\n}",
        }

        for filename, content in js_files.items():
            file_path = self.root_dir / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
            self.files_created.append(str(file_path))

    def display_summary(self) -> None:
        """Display setup summary."""
        print("=" * 60)
        print("PROJECT SETUP COMPLETE")
        print("=" * 60)
        print(f"Location: {self.root_dir}")
        print(f"Directories created: {len(self.dirs_created)}")
        print(f"Files created: {len(self.files_created)}")
        print("=" * 60)

        print("\nNext steps:")
        print("1. Activate virtual environment")
        print("2. Install dependencies")
        print("3. Start development server")
        print("4. Open browser at http://localhost:8000")

    def run(self) -> None:
        """Run the setup process."""
        print("=" * 60)
        print("PROJECT SETUP")
        print("=" * 60)

        self.create_directories()
        self.create_config_files()
        self.create_placeholder_files()
        self.create_documentation_files()
        self.create_data_files()
        self.create_chatbot_files()
        self.create_html_files()
        self.create_css_files()
        self.create_js_files()

        self.display_summary()


def main():
    """Main entry point."""
    setup = ProjectSetup()
    setup.run()


if __name__ == "__main__":
    main()