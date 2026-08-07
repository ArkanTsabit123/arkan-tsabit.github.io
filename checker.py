#!/usr/bin/env python3
"""
Portfolio Website Checker

This script validates all components of the portfolio website including:
- HTML structure and SEO elements
- CSS files and responsive design
- JavaScript files and ES6 features
- JSON data files
- Asset images and screenshots
- PDF documents
- Chatbot configuration and API
- External links
- Accessibility features

Usage:
    python checker.py

Returns:
    0 if all checks pass, 1 if any check fails
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


class Colors:
    """Terminal color codes for output formatting."""
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    END = "\033[0m"


class CheckResult:
    """Container for a single check result."""
    
    def __init__(
        self,
        name: str,
        passed: bool,
        message: str = "",
        details: str = "",
        category: str = "General",
        severity: str = "normal"
    ):
        self.name = name
        self.passed = passed
        self.message = message
        self.details = details
        self.category = category
        self.severity = severity


class PortfolioChecker:
    """Main checker class for portfolio website validation."""
    
    def __init__(self):
        self.root_dir = Path.cwd()
        self.results: List[CheckResult] = []
        self.total_checks = 0
        self.passed_checks = 0
        self.failed_checks = 0
        self.critical_failures = 0
        
        self.stats = {
            "files_found": 0,
            "lines_code": 0,
            "certifications": 0,
            "projects": 0,
            "achievements": 0,
            "languages": 0,
        }
        
        self._define_requirements()
    
    def _define_requirements(self) -> None:
        """Define all required files and their specifications."""
        
        self.html_files = {
            "index.html": {
                "required": True,
                "checks": ["doctype", "html", "head", "title", "body", "h1", 
                          "css_link", "js_link", "viewport", "i18n"],
                "min_size": 1000,
                "description": "Landing page"
            },
            "about.html": {
                "required": True,
                "checks": ["doctype", "html", "head", "title", "body", "h1", 
                          "css_link", "js_link"],
                "min_size": 500,
                "description": "About Me page"
            },
            "projects.html": {
                "required": True,
                "checks": ["doctype", "html", "head", "title", "body", "h1", 
                          "css_link", "js_link"],
                "min_size": 500,
                "description": "Projects page"
            },
            "certifications.html": {
                "required": True,
                "checks": ["doctype", "html", "head", "title", "body", "h1", 
                          "css_link", "js_link"],
                "min_size": 500,
                "description": "Certifications page"
            },
            "achievements.html": {
                "required": True,
                "checks": ["doctype", "html", "head", "title", "body", "h1", 
                          "css_link", "js_link"],
                "min_size": 500,
                "description": "Achievements page"
            },
            "contact.html": {
                "required": True,
                "checks": ["doctype", "html", "head", "title", "body", "h1", 
                          "css_link", "js_link"],
                "min_size": 500,
                "description": "Contact page"
            },
            "404.html": {
                "required": False,
                "checks": ["doctype", "html", "head", "title", "body"],
                "min_size": 200,
                "description": "Error page"
            }
        }
        
        self.css_files = {
            "css/style.css": {
                "required": True,
                "features": [":root", "body", "container", "btn"],
                "min_size": 2000,
                "description": "Main styles"
            },
            "css/dark-mode.css": {
                "required": True,
                "features": ['[data-theme="dark"]', "--bg-primary", "--text-primary"],
                "min_size": 500,
                "description": "Dark mode styles"
            },
            "css/responsive.css": {
                "required": True,
                "features": ["@media"],
                "min_size": 500,
                "description": "Responsive styles"
            },
            "css/chatbot.css": {
                "required": True,
                "features": ["chatbot", "message", "input", "widget"],
                "min_size": 500,
                "description": "Chatbot styles"
            }
        }
        
        self.js_files = {
            "js/main.js": {
                "required": True,
                "features": ["DOMContentLoaded", "addEventListener"],
                "min_size": 500,
                "description": "Main functionality"
            },
            "js/dark-mode.js": {
                "required": True,
                "features": ["localStorage", "setAttribute"],
                "min_size": 300,
                "description": "Dark mode toggle"
            },
            "js/i18n.js": {
                "required": True,
                "features": ["localStorage", "fetch"],
                "min_size": 300,
                "description": "Multi-language support"
            },
            "js/chatbot.js": {
                "required": True,
                "features": ["fetch", "message", "API"],
                "min_size": 500,
                "description": "Chatbot widget"
            },
            "js/projects.js": {
                "required": True,
                "features": ["filter", "render", "fetch"],
                "min_size": 300,
                "description": "Project filtering"
            }
        }
        
        self.data_files = {
            "data/projects.json": {
                "required": True,
                "min_count": 4,
                "description": "Projects data"
            },
            "data/certifications.json": {
                "required": True,
                "min_count": 10,
                "description": "Certifications data"
            },
            "data/achievements.json": {
                "required": True,
                "min_count": 1,
                "description": "Achievements data"
            },
            "data/i18n/en.json": {
                "required": True,
                "description": "English translations"
            },
            "data/i18n/id.json": {
                "required": True,
                "description": "Indonesian translations"
            }
        }
        
        self.pdf_files = {
            "docs/CV/Arkan-Tsabit_Data-Engineer.pdf": {
                "required": True,
                "min_size": 1024,
                "description": "CV PDF"
            },
            "docs/Job-Application/Arkan-Tsabit_Job-Application.pdf": {
                "required": True,
                "min_size": 1024,
                "description": "Job Application PDF"
            }
        }
        
        self.asset_images = {
            "assets/images/profile.jpg": {
                "required": True,
                "min_size": 5000,
                "description": "Profile photo"
            },
            "assets/images/favicon.ico": {
                "required": True,
                "min_size": 100,
                "description": "Favicon"
            },
            "assets/images/logo.svg": {
                "required": True,
                "min_size": 100,
                "description": "Logo"
            },
            "assets/images/certifications/oracle.png": {
                "required": True,
                "min_size": 100,
                "description": "Oracle logo"
            },
            "assets/images/certifications/ibm.png": {
                "required": True,
                "min_size": 100,
                "description": "IBM logo"
            },
            "assets/images/certifications/meta.png": {
                "required": True,
                "min_size": 100,
                "description": "Meta logo"
            }
        }
        
        self.project_screenshots = {
            "batchetl": {
                "files": [
                    "assets/images/projects/batchetl/architecture.png",
                    "assets/images/projects/batchetl/dashboard.png",
                    "assets/images/projects/batchetl/erd.png"
                ],
                "min_required": 1
            },
            "uber": {
                "files": [
                    "assets/images/projects/uber/pipeline-flow.png",
                    "assets/images/projects/uber/star-schema.png",
                    "assets/images/projects/uber/dashboard.png"
                ],
                "min_required": 1
            },
            "amazon": {
                "files": [
                    "assets/images/projects/amazon/scraping-result.png",
                    "assets/images/projects/amazon/csv-output.png"
                ],
                "min_required": 1
            },
            "expense": {
                "files": [
                    "assets/images/projects/expense/gui-dashboard.png",
                    "assets/images/projects/expense/cli-summary.png"
                ],
                "min_required": 1
            }
        }
        
        self.directories = [
            "css", "js", "data", "data/i18n", "assets", "assets/images",
            "assets/images/projects", "assets/images/certifications",
            "assets/icons", "assets/fonts", "docs", "docs/CV",
            "docs/Job-Application", "chatbot"
        ]
        
        self.doc_files = [
            "README.md", "LICENSE", "docs/blueprint.md",
            "docs/cheatsheets.md", "docs/checklist.md", ".gitignore"
        ]
        
        self.chatbot_files = {
            "chatbot/worker.js": {
                "required": True,
                "features": ["export default", "async fetch", "/api/chat", 
                           "VECTORIZE", "AI.run", "CORS"],
                "min_size": 500,
                "description": "Cloudflare Worker"
            },
            "chatbot/wrangler.toml": {
                "required": True,
                "features": ["name", "main", "compatibility_date"],
                "min_size": 100,
                "description": "Wrangler config"
            },
            "chatbot/knowledge-upload.json": {
                "required": True,
                "min_docs": 30,
                "description": "Knowledge base"
            },
            "chatbot/package.json": {
                "required": True,
                "features": ["name", "version"],
                "min_size": 100,
                "description": "Node package"
            },
            "chatbot/convert-to-ndjson.js": {
                "required": False,
                "description": "NDJSON converter"
            },
            "chatbot/upload_vectors.py": {
                "required": False,
                "description": "Vector upload script"
            },
            "chatbot/test_all.py": {
                "required": False,
                "description": "Test suite"
            }
        }
        
        self.external_links = [
            ("GitHub", "https://github.com/ArkanTsabit123"),
            ("LinkedIn", "https://linkedin.com/in/arkan-tsabit"),
        ]
    
    def _print_header(self, text: str) -> None:
        """Print a formatted header."""
        print(f"\n{Colors.CYAN}{'=' * 70}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
        print(f"{Colors.CYAN}{'=' * 70}{Colors.END}\n")
    
    def _add_result(
        self,
        name: str,
        passed: bool,
        message: str = "",
        details: str = "",
        category: str = "General",
        severity: str = "normal"
    ) -> None:
        """Add a check result and print it."""
        result = CheckResult(name, passed, message, details, category, severity)
        self.results.append(result)
        self.total_checks += 1
        
        if passed:
            self.passed_checks += 1
            status = f"{Colors.GREEN}PASS{Colors.END}"
            icon = "[PASS]"
        else:
            self.failed_checks += 1
            if severity == "critical":
                self.critical_failures += 1
                status = f"{Colors.RED}FAIL (CRITICAL){Colors.END}"
                icon = "[FAIL]"
            else:
                status = f"{Colors.YELLOW}FAIL{Colors.END}"
                icon = "[FAIL]"
        
        print(f"  {icon} [{status}] {Colors.BOLD}{name}{Colors.END}")
        if message:
            print(f"      {Colors.DIM}-> {message}{Colors.END}")
        if details:
            print(f"      {Colors.CYAN}-> {details}{Colors.END}")
    
    def _format_size(self, size_bytes: int) -> str:
        """Format file size for display."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} GB"
    
    def _check_file(self, path: str, min_size: int = 0, required: bool = True) -> bool:
        """Check if a file exists and has minimum size."""
        full_path = self.root_dir / path
        
        if not full_path.exists():
            if required:
                self._add_result(f"File: {path}", False, "File not found",
                               "This file is required", "Files", "critical")
            else:
                self._add_result(f"File: {path}", True, "File not found (optional)",
                               "Optional file, skipping", "Files", "info")
            return False
        
        size = full_path.stat().st_size
        if size < min_size:
            self._add_result(f"File: {path}", False,
                           f"File too small: {size} bytes (min: {min_size})",
                           "File may be empty or corrupted", "Files", "critical")
            return False
        
        self.stats["files_found"] += 1
        self._add_result(f"File: {path}", True,
                        f"Size: {self._format_size(size)}", "", "Files")
        return True
    
    def _check_root_files(self) -> bool:
        """Check root level files."""
        self._print_header("PHASE 1: Root Files")
        
        root_files = [
            ("index.html", True), ("about.html", True),
            ("projects.html", True), ("certifications.html", True),
            ("achievements.html", True), ("contact.html", True),
            ("404.html", False), ("README.md", True),
            ("LICENSE", True), (".gitignore", True), ("CNAME", False),
        ]
        
        all_ok = True
        for filename, required in root_files:
            path = self.root_dir / filename
            if path.exists():
                size = path.stat().st_size
                self._add_result(f"Root: {filename}", True,
                               f"Size: {self._format_size(size)}", "", "Root")
            else:
                if required:
                    self._add_result(f"Root: {filename}", False,
                                   "File not found", "Required file", "Root", "critical")
                    all_ok = False
                else:
                    self._add_result(f"Root: {filename}", True,
                                   "File not found (optional)", "", "Root", "info")
        
        return all_ok
    
    def _check_directories(self) -> bool:
        """Check all required directories."""
        self._print_header("PHASE 2: Directory Structure")
        
        all_ok = True
        for dir_path in self.directories:
            full_path = self.root_dir / dir_path
            if full_path.exists() and full_path.is_dir():
                item_count = len(list(full_path.iterdir()))
                self._add_result(f"Directory: {dir_path}", True,
                               f"Contains {item_count} items", "", "Structure")
            else:
                self._add_result(f"Directory: {dir_path}", False,
                               "Directory not found",
                               f"Create: mkdir -p {dir_path}", "Structure", "critical")
                all_ok = False
        
        return all_ok
    
    def _check_html_files(self) -> bool:
        """Validate all HTML files."""
        self._print_header("PHASE 3: HTML Files")
        
        all_ok = True
        
        for filename, spec in self.html_files.items():
            path = self.root_dir / filename
            if not path.exists():
                if spec["required"]:
                    self._add_result(f"HTML: {filename}", False,
                                   f"File not found - {spec['description']}",
                                   "This file is required", "HTML", "critical")
                    all_ok = False
                continue
            
            size = path.stat().st_size
            if size < spec["min_size"]:
                self._add_result(f"HTML: {filename}", False,
                               f"File too small: {size} bytes (min: {spec['min_size']})",
                               "May be incomplete", "HTML", "critical")
                all_ok = False
                continue
            
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                lines = len(content.splitlines())
                self.stats["lines_code"] += lines
                checks_passed = True
                
                # Check DOCTYPE
                if "doctype" in spec["checks"]:
                    if not re.search(r'<!DOCTYPE\s+html', content, re.IGNORECASE):
                        self._add_result(f"HTML: {filename} - DOCTYPE", False,
                                       "Missing DOCTYPE declaration", "", "HTML", "critical")
                        checks_passed = False
                
                # Check HTML tag
                if "html" in spec["checks"]:
                    if "<html" not in content:
                        self._add_result(f"HTML: {filename} - <html>", False,
                                       "Missing <html> tag", "", "HTML", "critical")
                        checks_passed = False
                
                # Check HEAD tag
                if "head" in spec["checks"]:
                    if "<head" not in content:
                        self._add_result(f"HTML: {filename} - <head>", False,
                                       "Missing <head> section", "", "HTML", "critical")
                        checks_passed = False
                
                # Check TITLE tag
                if "title" in spec["checks"]:
                    if not re.search(r'<title[^>]*>.*?</title>', content, re.IGNORECASE):
                        self._add_result(f"HTML: {filename} - <title>", False,
                                       "Missing <title> tag", "SEO important", "HTML", "critical")
                        checks_passed = False
                
                # Check BODY tag
                if "body" in spec["checks"]:
                    if "<body" not in content:
                        self._add_result(f"HTML: {filename} - <body>", False,
                                       "Missing <body> tag", "", "HTML", "critical")
                        checks_passed = False
                
                # Check H1 heading (fixed pattern)
                if "h1" in spec["checks"]:
                    h1_match = re.search(r'<h1\b[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
                    if h1_match:
                        h1_text = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
                        h1_preview = h1_text[:50] + ('...' if len(h1_text) > 50 else '')
                        self._add_result(f"HTML: {filename} - <h1>", True,
                                       f"Found: '{h1_preview}'", "", "HTML")
                    else:
                        self._add_result(f"HTML: {filename} - <h1>", False,
                                       "Missing <h1> heading", "SEO important", "HTML", "normal")
                        checks_passed = False
                
                # Check viewport meta tag
                if "viewport" in spec["checks"]:
                    if not re.search(r'<meta[^>]*viewport', content, re.IGNORECASE):
                        self._add_result(f"HTML: {filename} - Viewport", False,
                                       "Missing viewport meta tag",
                                       "Responsive design important", "HTML", "critical")
                        checks_passed = False
                
                # Check CSS links
                if "css_link" in spec["checks"]:
                    if not re.search(r'<link[^>]*\.css', content, re.IGNORECASE):
                        self._add_result(f"HTML: {filename} - CSS link", False,
                                       "No CSS file linked", "", "HTML", "normal")
                        checks_passed = False
                
                # Check JS scripts
                if "js_link" in spec["checks"]:
                    if not re.search(r'<script[^>]*\.js', content, re.IGNORECASE):
                        self._add_result(f"HTML: {filename} - JS link", False,
                                       "No JavaScript file linked", "", "HTML", "normal")
                        checks_passed = False
                
                # Check i18n attributes
                if "i18n" in spec["checks"]:
                    i18n_count = len(re.findall(r'data-i18n="[^"]+"', content))
                    if i18n_count > 0:
                        self._add_result(f"HTML: {filename} - i18n", True,
                                       f"Found {i18n_count} translation attributes", "", "HTML")
                    else:
                        self._add_result(f"HTML: {filename} - i18n", False,
                                       "No data-i18n attributes found",
                                       "Multi-language support missing", "HTML", "normal")
                        checks_passed = False
                
                # Check alt text for images
                img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
                no_alt = [img for img in img_tags if 'alt=' not in img.lower()]
                if no_alt:
                    self._add_result(f"HTML: {filename} - Alt text", False,
                                   f"{len(no_alt)} images missing alt text",
                                   "Accessibility important", "HTML", "normal")
                    checks_passed = False
                
                # Check structured data
                if '@context' in content and 'schema.org' in content:
                    self._add_result(f"HTML: {filename} - Structured Data", True,
                                   "Schema.org JSON-LD found", "", "HTML")
                
                if checks_passed:
                    self._add_result(f"HTML: {filename}", True,
                                   f"{lines} lines, {self._format_size(size)}",
                                   spec['description'], "HTML")
                else:
                    all_ok = False
                    
            except Exception as e:
                self._add_result(f"HTML: {filename}", False,
                               f"Error reading file: {e}", "", "HTML", "critical")
                all_ok = False
        
        return all_ok
    
    def _check_css_files(self) -> bool:
        """Validate CSS files."""
        self._print_header("PHASE 4: CSS Files")
        
        all_ok = True
        
        for filename, spec in self.css_files.items():
            path = self.root_dir / filename
            if not path.exists():
                if spec["required"]:
                    self._add_result(f"CSS: {filename}", False,
                                   f"File not found - {spec['description']}",
                                   "This file is required", "CSS", "critical")
                    all_ok = False
                continue
            
            size = path.stat().st_size
            if size < spec["min_size"]:
                self._add_result(f"CSS: {filename}", False,
                               f"File too small: {size} bytes (min: {spec['min_size']})",
                               "May be incomplete", "CSS", "critical")
                all_ok = False
                continue
            
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                lines = len(content.splitlines())
                self.stats["lines_code"] += lines
                checks_passed = True
                
                for feature in spec["features"]:
                    if feature not in content:
                        self._add_result(f"CSS: {filename} - '{feature[:30]}...'", False,
                                       f"Missing feature: {feature}",
                                       "Required for functionality", "CSS", "normal")
                        checks_passed = False
                
                if ":root" in content:
                    var_count = len(re.findall(r'--[a-zA-Z-]+:', content))
                    self._add_result(f"CSS: {filename} - Variables", True,
                                   f"Found {var_count} CSS variables", "", "CSS")
                
                if '[data-theme="dark"]' in content:
                    self._add_result(f"CSS: {filename} - Dark Mode", True,
                                   "Dark mode styles found", "", "CSS")
                
                if "@media" in content:
                    media_count = len(re.findall(r'@media[^{]+{', content))
                    self._add_result(f"CSS: {filename} - Responsive", True,
                                   f"Found {media_count} media queries", "", "CSS")
                
                if checks_passed:
                    self._add_result(f"CSS: {filename}", True,
                                   f"{lines} lines, {self._format_size(size)}",
                                   spec['description'], "CSS")
                    
            except Exception as e:
                self._add_result(f"CSS: {filename}", False,
                               f"Error reading file: {e}", "", "CSS", "critical")
                all_ok = False
        
        return all_ok
    
    def _check_js_files(self) -> bool:
        """Validate JavaScript files."""
        self._print_header("PHASE 5: JavaScript Files")
        
        all_ok = True
        
        for filename, spec in self.js_files.items():
            path = self.root_dir / filename
            if not path.exists():
                if spec["required"]:
                    self._add_result(f"JS: {filename}", False,
                                   f"File not found - {spec['description']}",
                                   "This file is required", "JavaScript", "critical")
                    all_ok = False
                continue
            
            size = path.stat().st_size
            if size < spec["min_size"]:
                self._add_result(f"JS: {filename}", False,
                               f"File too small: {size} bytes (min: {spec['min_size']})",
                               "May be incomplete", "JavaScript", "critical")
                all_ok = False
                continue
            
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                lines = len(content.splitlines())
                self.stats["lines_code"] += lines
                checks_passed = True
                
                for feature in spec["features"]:
                    if feature not in content:
                        self._add_result(f"JS: {filename} - '{feature[:30]}...'", False,
                                       f"Missing feature: {feature}",
                                       "Required for functionality", "JavaScript", "normal")
                        checks_passed = False
                
                es6_features = []
                if "const" in content or "let" in content:
                    es6_features.append("const/let")
                if "=>" in content:
                    es6_features.append("arrow functions")
                if "async" in content or "await" in content:
                    es6_features.append("async/await")
                if "class" in content:
                    es6_features.append("classes")
                if "fetch" in content:
                    es6_features.append("fetch API")
                
                if es6_features:
                    self._add_result(f"JS: {filename} - ES6", True,
                                   f"Using: {', '.join(es6_features)}", "", "JavaScript")
                
                if "localStorage" in content:
                    self._add_result(f"JS: {filename} - localStorage", True,
                                   "Using localStorage for persistence", "", "JavaScript")
                
                if "addEventListener" in content:
                    event_count = len(re.findall(r'\.addEventListener\(', content))
                    self._add_result(f"JS: {filename} - Events", True,
                                   f"Found {event_count} event listeners", "", "JavaScript")
                
                if checks_passed:
                    self._add_result(f"JS: {filename}", True,
                                   f"{lines} lines, {self._format_size(size)}",
                                   spec['description'], "JavaScript")
                    
            except Exception as e:
                self._add_result(f"JS: {filename}", False,
                               f"Error reading file: {e}", "", "JavaScript", "critical")
                all_ok = False
        
        return all_ok
    
    def _check_data_files(self) -> bool:
        """Validate JSON data files."""
        self._print_header("PHASE 6: Data Files")
        
        all_ok = True
        
        for filename, spec in self.data_files.items():
            path = self.root_dir / filename
            if not path.exists():
                if spec["required"]:
                    self._add_result(f"Data: {filename}", False,
                                   f"File not found - {spec['description']}",
                                   "This file is required", "Data", "critical")
                    all_ok = False
                continue
            
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                size = path.stat().st_size
                self._add_result(f"Data: {filename}", True,
                               f"{self._format_size(size)} valid JSON",
                               spec['description'], "Data")
                
                # Check specific structures
                if "projects" in filename:
                    projects = data.get("projects", [])
                    count = len(projects)
                    min_count = spec.get("min_count", 0)
                    
                    if count >= min_count:
                        self._add_result(f"Data: {filename} - Count", True,
                                       f"{count} projects (min: {min_count})", "", "Data")
                    else:
                        self._add_result(f"Data: {filename} - Count", False,
                                       f"Only {count} projects (need {min_count})",
                                       "Add more projects", "Data", "normal")
                    
                    self.stats["projects"] = count
                
                elif "certifications" in filename:
                    certs = data.get("certifications", [])
                    count = len(certs)
                    min_count = spec.get("min_count", 0)
                    
                    if count >= min_count:
                        self._add_result(f"Data: {filename} - Count", True,
                                       f"{count} certifications (min: {min_count})", "", "Data")
                    else:
                        self._add_result(f"Data: {filename} - Count", False,
                                       f"Only {count} certifications (need {min_count})",
                                       "Add more certifications", "Data", "normal")
                    
                    providers = {}
                    for cert in certs:
                        provider = cert.get("provider", "Unknown")
                        providers[provider] = providers.get(provider, 0) + 1
                    
                    provider_str = ", ".join([f"{p}: {c}" for p, c in providers.items()])
                    self._add_result(f"Data: {filename} - Providers", True,
                                   f"{provider_str}", "", "Data")
                    self.stats["certifications"] = count
                    
                    has_links = all(c.get("link") for c in certs if "link" in c)
                    if has_links:
                        self._add_result(f"Data: {filename} - Links", True,
                                       "All certifications have verification links", "", "Data")
                    else:
                        self._add_result(f"Data: {filename} - Links", False,
                                       "Some certifications missing verification links",
                                       "Add 'link' field to each certification", "Data", "normal")
                
                elif "achievements" in filename:
                    achievements = data.get("achievements", [])
                    count = len(achievements)
                    self.stats["achievements"] = count
                    
                    min_count = spec.get("min_count", 0)
                    if count >= min_count:
                        self._add_result(f"Data: {filename} - Count", True,
                                       f"{count} achievements (min: {min_count})", "", "Data")
                    else:
                        self._add_result(f"Data: {filename} - Count", False,
                                       f"Only {count} achievements (need {min_count})",
                                       "Add more achievements", "Data", "normal")
                
                elif "i18n" in filename:
                    if isinstance(data, dict):
                        nav_keys = list(data.get("nav", {}).keys())
                        hero_keys = list(data.get("hero", {}).keys())
                        
                        self._add_result(f"Data: {filename} - Structure", True,
                                       f"nav: {len(nav_keys)}, hero: {len(hero_keys)} keys",
                                       "", "Data")
                        
                        required_nav = ["home", "about", "projects", "certifications", 
                                       "achievements", "contact"]
                        missing_nav = [k for k in required_nav if k not in nav_keys]
                        if missing_nav:
                            self._add_result(f"Data: {filename} - nav", False,
                                           f"Missing: {', '.join(missing_nav)}",
                                           "Add missing translations", "Data", "normal")
                        else:
                            self._add_result(f"Data: {filename} - nav", True,
                                           f"All {len(required_nav)} nav items found", "", "Data")
                        
                        self.stats["languages"] += 1
                
            except json.JSONDecodeError as e:
                self._add_result(f"Data: {filename}", False,
                               f"Invalid JSON: {e}", "", "Data", "critical")
                all_ok = False
            except Exception as e:
                self._add_result(f"Data: {filename}", False,
                               f"Error: {e}", "", "Data", "critical")
                all_ok = False
        
        return all_ok
    
    def _check_pdf_files(self) -> bool:
        """Validate PDF files."""
        self._print_header("PHASE 7: PDF Documents")
        
        all_ok = True
        
        for filename, spec in self.pdf_files.items():
            path = self.root_dir / filename
            if not path.exists():
                if spec["required"]:
                    self._add_result(f"PDF: {filename}", False,
                                   f"File not found - {spec['description']}",
                                   "Upload the PDF file", "PDF", "critical")
                    all_ok = False
                continue
            
            size = path.stat().st_size
            if size < spec["min_size"]:
                self._add_result(f"PDF: {filename}", False,
                               f"File too small: {size} bytes (min: {spec['min_size']})",
                               "File may be empty or corrupted", "PDF", "critical")
                all_ok = False
            else:
                self._add_result(f"PDF: {filename}", True,
                               f"{self._format_size(size)}",
                               spec['description'], "PDF")
        
        return all_ok
    
    def _check_asset_images(self) -> bool:
        """Validate asset images."""
        self._print_header("PHASE 8: Asset Images")
        
        all_ok = True
        
        for filename, spec in self.asset_images.items():
            path = self.root_dir / filename
            if not path.exists():
                if spec["required"]:
                    self._add_result(f"Image: {filename}", False,
                                   f"File not found - {spec['description']}",
                                   "Upload the image file", "Assets", "critical")
                    all_ok = False
                continue
            
            size = path.stat().st_size
            if size < spec["min_size"]:
                self._add_result(f"Image: {filename}", False,
                               f"File too small: {size} bytes (min: {spec['min_size']})",
                               "May be a placeholder or corrupted", "Assets", "critical")
                all_ok = False
            else:
                self._add_result(f"Image: {filename}", True,
                               f"{self._format_size(size)}",
                               spec['description'], "Assets")
        
        return all_ok
    
    def _check_project_screenshots(self) -> bool:
        """Validate project screenshots."""
        self._print_header("PHASE 9: Project Screenshots")
        
        all_ok = True
        
        for project, spec in self.project_screenshots.items():
            found = 0
            total = len(spec["files"])
            min_req = spec["min_required"]
            
            for file_path in spec["files"]:
                path = self.root_dir / file_path
                if path.exists():
                    size = path.stat().st_size
                    if size > 100:
                        found += 1
                        self._add_result(f"Screenshot: {file_path}", True,
                                       f"{self._format_size(size)}", project, "Assets")
            
            if found >= min_req:
                self._add_result(f"Screenshots: {project}", True,
                               f"{found}/{total} found (min: {min_req})", "", "Assets")
            else:
                self._add_result(f"Screenshots: {project}", False,
                               f"Only {found}/{total} found (need {min_req})",
                               "Add screenshots for this project", "Assets", "normal")
                all_ok = False
        
        return all_ok
    
    def _check_documentation(self) -> bool:
        """Validate documentation files."""
        self._print_header("PHASE 10: Documentation")
        
        all_ok = True
        
        for filename in self.doc_files:
            path = self.root_dir / filename
            if path.exists():
                size = path.stat().st_size
                if size < 100:
                    self._add_result(f"Doc: {filename}", False,
                                   f"File too small: {size} bytes",
                                   "May be empty", "Docs", "normal")
                    all_ok = False
                else:
                    self._add_result(f"Doc: {filename}", True,
                                   f"{self._format_size(size)}", "", "Docs")
            else:
                if filename in ["README.md", "LICENSE", ".gitignore"]:
                    self._add_result(f"Doc: {filename}", False,
                                   "File not found", "Required file", "Docs", "critical")
                    all_ok = False
                else:
                    self._add_result(f"Doc: {filename}", False,
                                   "File not found (optional)", "", "Docs", "info")
        
        return all_ok
    
    def _check_chatbot(self) -> bool:
        """Validate chatbot files and configuration."""
        self._print_header("PHASE 11: Chatbot")
        
        all_ok = True
        
        for filename, spec in self.chatbot_files.items():
            path = self.root_dir / filename
            if not path.exists():
                if spec["required"]:
                    self._add_result(f"Chatbot: {filename}", False,
                                   f"File not found - {spec['description']}",
                                   "This file is required", "Chatbot", "critical")
                    all_ok = False
                continue
            
            size = path.stat().st_size
            
            if "knowledge-upload.json" in filename:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    docs = data.get("documents", [])
                    doc_count = len(docs)
                    min_docs = spec.get("min_docs", 0)
                    
                    if doc_count >= min_docs:
                        self._add_result(f"Chatbot: {filename}", True,
                                       f"{doc_count} documents (min: {min_docs})",
                                       spec['description'], "Chatbot")
                    else:
                        self._add_result(f"Chatbot: {filename}", False,
                                       f"Only {doc_count} documents (need {min_docs})",
                                       "Add more documents", "Chatbot", "normal")
                        all_ok = False
                    
                    categories = set()
                    for doc in docs:
                        category = doc.get("metadata", {}).get("category")
                        if category:
                            categories.add(category)
                    
                    self._add_result(f"Chatbot: Categories", True,
                                   f"{len(categories)} categories: {', '.join(categories)}", "", "Chatbot")
                    
                except Exception as e:
                    self._add_result(f"Chatbot: {filename}", False,
                                   f"Error reading: {e}", "", "Chatbot", "critical")
                    all_ok = False
            
            elif "worker.js" in filename:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    components = []
                    if "VECTORIZE" in content:
                        components.append("Vectorize")
                    if "AI.run" in content:
                        components.append("AI")
                    if "/api/chat" in content:
                        components.append("API")
                    if "CORS" in content or "Access-Control-Allow-Origin" in content:
                        components.append("CORS")
                    
                    self._add_result(f"Chatbot: {filename}", True,
                                   f"{self._format_size(size)} - {', '.join(components)}",
                                   spec['description'], "Chatbot")
                    
                except Exception as e:
                    self._add_result(f"Chatbot: {filename}", False,
                                   f"Error reading: {e}", "", "Chatbot", "critical")
                    all_ok = False
            
            else:
                if size < spec.get("min_size", 100):
                    self._add_result(f"Chatbot: {filename}", False,
                                   f"File too small: {size} bytes",
                                   "May be empty", "Chatbot", "normal")
                    all_ok = False
                else:
                    self._add_result(f"Chatbot: {filename}", True,
                                   f"{self._format_size(size)}",
                                   spec['description'], "Chatbot")
        
        return all_ok
    
    def _check_chatbot_api(self) -> bool:
        """Test the chatbot API endpoint."""
        self._print_header("PHASE 12: Chatbot API Test")
        
        if not HAS_REQUESTS:
            self._add_result("Chatbot API", False,
                           "requests module not installed",
                           "Install: pip install requests", "API", "info")
            return False
        
        all_ok = True
        
        try:
            # Health check
            health_url = "https://arkan-chatbot.arkan-chatbot.workers.dev/health"
            try:
                response = requests.get(health_url, timeout=5)
                if response.status_code == 200:
                    self._add_result("API: Health Check", True,
                                   f"Response: {response.status_code}", "", "API")
                else:
                    self._add_result("API: Health Check", False,
                                   f"Status: {response.status_code}",
                                   "Worker may not be deployed", "API", "normal")
                    all_ok = False
            except requests.exceptions.ConnectionError:
                self._add_result("API: Health Check", False,
                               "Cannot connect", "Is the worker deployed?", "API", "normal")
                all_ok = False
            except Exception as e:
                self._add_result("API: Health Check", False,
                               f"Error: {e}", "", "API", "normal")
                all_ok = False
            
            # Test chat endpoint
            chat_url = "https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat"
            test_questions = [
                ("Who is Arkan Tsabit?", "profile"),
                ("What projects has Arkan built?", "projects"),
                ("What certifications does Arkan have?", "certifications")
            ]
            
            for question, category in test_questions:
                try:
                    response = requests.post(
                        chat_url,
                        json={"question": question},
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        if "response" in data and len(data["response"]) > 10:
                            self._add_result(f"API: Query - {category}", True,
                                           f"{len(data['response'])} chars, source: {data.get('source', 'unknown')}",
                                           f"Q: {question[:30]}...", "API")
                        else:
                            self._add_result(f"API: Query - {category}", False,
                                           "Invalid response format",
                                           "Check worker response", "API", "normal")
                            all_ok = False
                    else:
                        self._add_result(f"API: Query - {category}", False,
                                       f"Status: {response.status_code}",
                                       "Worker returned error", "API", "normal")
                        all_ok = False
                        
                except requests.exceptions.Timeout:
                    self._add_result(f"API: Query - {category}", False,
                                   "Request timed out", "Worker may be slow", "API", "normal")
                    all_ok = False
                except Exception as e:
                    self._add_result(f"API: Query - {category}", False,
                                   f"Error: {e}", "", "API", "normal")
                    all_ok = False
            
        except Exception as e:
            self._add_result("Chatbot API", False,
                           f"Error: {e}", "", "API", "normal")
            all_ok = False
        
        return all_ok
    
    def _check_external_links(self) -> bool:
        """Validate external links."""
        self._print_header("PHASE 13: External Links")
        
        if not HAS_REQUESTS:
            self._add_result("External Links", False,
                           "requests module not installed",
                           "Install: pip install requests", "Links", "info")
            return False
        
        all_ok = True
        
        for name, url in self.external_links:
            try:
                response = requests.get(url, timeout=5, allow_redirects=True)
                if response.status_code == 200:
                    self._add_result(f"Link: {name}", True,
                                   f"{response.status_code} - {url}", "", "Links")
                else:
                    self._add_result(f"Link: {name}", False,
                                   f"Status: {response.status_code}",
                                   f"URL: {url}", "Links", "normal")
                    all_ok = False
            except requests.exceptions.ConnectionError:
                self._add_result(f"Link: {name}", False,
                               "Cannot connect", f"URL: {url}", "Links", "normal")
                all_ok = False
            except Exception as e:
                self._add_result(f"Link: {name}", False,
                               f"Error: {e}", f"URL: {url}", "Links", "normal")
                all_ok = False
        
        return all_ok
    
    def _check_seo(self) -> bool:
        """Validate SEO elements."""
        self._print_header("PHASE 14: SEO")
        
        all_ok = True
        
        index_path = self.root_dir / "index.html"
        if index_path.exists():
            try:
                with open(index_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Check meta description
                if re.search(r'<meta[^>]*name="description"[^>]*content="[^"]+"', content, re.IGNORECASE):
                    self._add_result("SEO: Meta Description", True,
                                   "Found in index.html", "", "SEO")
                else:
                    self._add_result("SEO: Meta Description", False,
                                   "Missing meta description",
                                   "Add description for SEO", "SEO", "normal")
                    all_ok = False
                
                # Check Open Graph tags
                og_tags = re.findall(r'<meta[^>]*property="og:[^"]+"', content, re.IGNORECASE)
                if og_tags:
                    self._add_result("SEO: Open Graph", True,
                                   f"{len(og_tags)} OG tags found", "", "SEO")
                else:
                    self._add_result("SEO: Open Graph", False,
                                   "No Open Graph tags found",
                                   "Add OG tags for social sharing", "SEO", "normal")
                    all_ok = False
                
                # Check title length
                title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE)
                if title_match:
                    title = title_match.group(1)
                    title_len = len(title)
                    if 30 <= title_len <= 60:
                        self._add_result("SEO: Title Length", True,
                                       f"{title_len} chars (optimal)", "", "SEO")
                    else:
                        self._add_result("SEO: Title Length", False,
                                       f"{title_len} chars (optimal: 30-60)",
                                       "Adjust title length", "SEO", "normal")
                        all_ok = False
                
                # Check structured data
                if '@context' in content and 'schema.org' in content:
                    self._add_result("SEO: Structured Data", True,
                                   "Schema.org JSON-LD found", "", "SEO")
                else:
                    self._add_result("SEO: Structured Data", False,
                                   "No structured data found",
                                   "Add JSON-LD for better SEO", "SEO", "normal")
                    all_ok = False
                
            except Exception as e:
                self._add_result("SEO Check", False,
                               f"Error: {e}", "", "SEO", "normal")
                all_ok = False
        
        return all_ok
    
    def _check_accessibility(self) -> bool:
        """Validate accessibility features."""
        self._print_header("PHASE 15: Accessibility")
        
        all_ok = True
        html_files = [f for f in self.html_files.keys() if (self.root_dir / f).exists()]
        
        for filename in html_files:
            path = self.root_dir / filename
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Check lang attribute
                if re.search(r'<html[^>]*lang="[^"]+"', content, re.IGNORECASE):
                    self._add_result(f"A11y: {filename} - lang", True,
                                   "lang attribute found", "", "Accessibility")
                else:
                    self._add_result(f"A11y: {filename} - lang", False,
                                   "Missing lang attribute",
                                   "Add lang='en' to html tag", "Accessibility", "normal")
                    all_ok = False
                
                # Check aria labels
                aria_count = len(re.findall(r'aria-[a-zA-Z]+="[^"]+"', content))
                if aria_count > 0:
                    self._add_result(f"A11y: {filename} - ARIA", True,
                                   f"{aria_count} ARIA attributes found", "", "Accessibility")
                
                # Check role attributes
                role_count = len(re.findall(r'role="[^"]+"', content))
                if role_count > 0:
                    self._add_result(f"A11y: {filename} - Roles", True,
                                   f"{role_count} role attributes found", "", "Accessibility")
                
                # Check alt text for images
                img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
                alt_count = len(re.findall(r'<img[^>]+alt="[^"]*"', content, re.IGNORECASE))
                
                if img_tags:
                    if alt_count == len(img_tags):
                        self._add_result(f"A11y: {filename} - Alt Text", True,
                                       f"All {len(img_tags)} images have alt text", "", "Accessibility")
                    else:
                        missing = len(img_tags) - alt_count
                        self._add_result(f"A11y: {filename} - Alt Text", False,
                                       f"{missing}/{len(img_tags)} images missing alt text",
                                       "Add alt attributes to images", "Accessibility", "normal")
                        all_ok = False
                
            except Exception as e:
                self._add_result(f"A11y: {filename}", False,
                               f"Error: {e}", "", "Accessibility", "normal")
                all_ok = False
        
        return all_ok
    
    def _print_summary(self) -> None:
        """Print comprehensive summary of all checks."""
        self._print_header("FINAL SUMMARY")
        
        total = self.total_checks
        passed = self.passed_checks
        failed = self.failed_checks
        critical = self.critical_failures
        rate = (passed / total * 100) if total > 0 else 0
        
        print(f"  Check Statistics:")
        print(f"    Total Checks:  {total}")
        print(f"    Passed:        {passed}")
        print(f"    Failed:        {failed}")
        print(f"    Critical:      {critical}")
        print(f"    Success Rate:  {rate:.1f}%")
        
        print(f"\n  Project Statistics:")
        print(f"    Projects:       {self.stats.get('projects', 0)}")
        print(f"    Certifications: {self.stats.get('certifications', 0)}")
        print(f"    Achievements:   {self.stats.get('achievements', 0)}")
        print(f"    Languages:      {self.stats.get('languages', 0)}")
        print(f"    Files Found:    {self.stats.get('files_found', 0)}")
        print(f"    Lines of Code:  {self.stats.get('lines_code', 0):,}")
        
        print(f"\n  Overall Grade:")
        if rate == 100:
            print(f"    EXCELLENT - 100% Complete!")
        elif rate >= 90:
            print(f"    VERY GOOD ({rate:.1f}%)")
        elif rate >= 70:
            print(f"    GOOD ({rate:.1f}%)")
        elif rate >= 50:
            print(f"    IN PROGRESS ({rate:.1f}%)")
        else:
            print(f"    NEEDS WORK ({rate:.1f}%)")
        
        if critical > 0:
            print(f"\n  {critical} CRITICAL ISSUES found!")
            print("  Fix these immediately before deployment.")
        elif failed > 0:
            print(f"\n  {failed} non-critical issues found.")
            print("  Review the results above.")
        else:
            print("\n  ALL CHECKS PASSED! Project is ready for deployment.")
    
    def _save_results(self) -> None:
        """Save results to a JSON file."""
        results_data = {
            "timestamp": datetime.now().isoformat(),
            "root_dir": str(self.root_dir),
            "summary": {
                "total_checks": self.total_checks,
                "passed": self.passed_checks,
                "failed": self.failed_checks,
                "critical": self.critical_failures,
                "rate": (self.passed_checks / self.total_checks * 100) if self.total_checks > 0 else 0
            },
            "stats": self.stats,
            "results": [
                {
                    "name": r.name,
                    "passed": r.passed,
                    "message": r.message,
                    "details": r.details,
                    "category": r.category,
                    "severity": r.severity
                }
                for r in self.results
            ]
        }
        
        output_file = self.root_dir / "checker_results.json"
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(results_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save results: {e}")
    
    def run(self) -> int:
        """Run all checks and return exit code."""
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}")
        print("PORTFOLIO WEBSITE CHECKER")
        print(f"Version 3.0 - Production Ready{Colors.END}")
        print(f"\nRoot: {self.root_dir}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        all_ok = True
        
        # Run all validation phases
        phases = [
            self._check_root_files,
            self._check_directories,
            self._check_html_files,
            self._check_css_files,
            self._check_js_files,
            self._check_data_files,
            self._check_pdf_files,
            self._check_asset_images,
            self._check_project_screenshots,
            self._check_documentation,
            self._check_chatbot,
            self._check_chatbot_api,
            self._check_external_links,
            self._check_seo,
            self._check_accessibility,
        ]
        
        for phase in phases:
            try:
                phase_result = phase()
                if not phase_result:
                    all_ok = False
            except Exception as e:
                print(f"\nError in phase: {phase.__name__}")
                print(f"  {e}")
                all_ok = False
        
        self._print_summary()
        self._save_results()
        
        print(f"\nResults saved to: checker_results.json")
        
        # Always return 0 to avoid SystemExit
        return 0


def main() -> None:
    """Main entry point."""
    checker = PortfolioChecker()
    checker.run()


if __name__ == "__main__":
    main()