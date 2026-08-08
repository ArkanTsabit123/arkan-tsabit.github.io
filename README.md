# Arkan Tsabit - Data Engineer Portfolio

## Personal Portfolio Website Showcasing Data Engineering Projects, Certifications, and Professional Experience

[![Website](https://img.shields.io/badge/Website-arkan--tsabit.github.io-blue)](https://arkan-tsabit.github.io)
[![GitHub](https://img.shields.io/badge/GitHub-ArkanTsabit123-lightgrey)](https://github.com/ArkanTsabit123)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-arkan--tsabit-blue)](https://linkedin.com/in/arkan-tsabit)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Deployment](https://img.shields.io/badge/Deployment-GitHub%20Pages-brightgreen)](https://pages.github.com)
[![Chatbot](https://img.shields.io/badge/Chatbot-RAG%20Powered-blueviolet)](https://arkan-chatbot.arkan-chatbot.workers.dev)
[![Tests](https://img.shields.io/badge/Tests-34%20Passed-success)](https://github.com/ArkanTsabit123/arkan-tsabit.github.io)
[![Contact](https://img.shields.io/badge/Contact-Google%20Sheets-green)](https://docs.google.com/spreadsheets/d/1zcck8oaWyw5aWOpNl4JqstaLFYhjMvh_aNvrr0adqAg/edit)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Deployment](#deployment)
- [Chatbot Integration](#chatbot-integration)
- [Knowledge Base](#knowledge-base)
- [Testing](#testing)
- [LLM Models Tested](#llm-models-tested)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Version History](#version-history)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

This repository contains the source code for my professional portfolio website. It showcases my work as a Data Engineer, featuring:

- **4 Data Engineering Projects** with detailed descriptions and metrics
- **10 Professional Certifications** from Oracle, IBM, and Meta
- **Professional Experience** and career transition story
- **Achievements** including Oracle Race to Certification (Top 108 Global, Top 3 Indonesia)
- **AI-Powered Chatbot** using RAG (Retrieval-Augmented Generation)
- **Multi-Language Support** (Indonesian and US English)
- **Dark/Light Mode** toggle for optimal viewing
- **Contact Form** with Google Sheets integration

### Key Metrics

| Metric | Value |
|--------|-------|
| Projects | 4 |
| Certifications | 10 |
| Languages | 2 (ID, EN) |
| Pages | 6 |
| Chatbot | RAG-powered |
| Knowledge Base Documents | 30 |
| Test Questions | 34 |
| Deployment | GitHub Pages |
| Contact Form | Google Sheets |

---

## Features

### Core Features

| Feature | Description |
|---------|-------------|
| **Landing Page** | Professional introduction with key metrics and call-to-action buttons |
| **About Me** | Professional summary, working experience, and technical skills |
| **Projects** | 4 detailed project cards with metrics, tech stack, and GitHub links |
| **Certifications** | 10 certifications with "Verify" buttons linking to official credentials |
| **Achievements** | Oracle Race to Certification awards and teaching recognition |
| **Contact** | Contact information and Google Sheets powered contact form |

### Interactive Features

| Feature | Description |
|---------|-------------|
| **Dark/Light Mode** | Theme toggle with persistent preference |
| **Multi-Language** | Indonesian and English toggle with persistent preference |
| **AI Chatbot** | RAG-powered question-answering about experience, projects, and skills |
| **Responsive Design** | Optimized for all screen sizes |
| **Contact Form** | Google Sheets integration with real-time data storage |

### Technical Features

| Feature | Description |
|---------|-------------|
| **Static Hosting** | GitHub Pages for fast, reliable deployment |
| **Cloudflare Workers** | Serverless AI chatbot backend |
| **RAG Implementation** | Vector search + LLM for accurate responses |
| **Performance Optimized** | Lazy loading, minification, caching |
| **Knowledge Base** | 30 documents with embedded vectors |
| **Contact Form** | Google Apps Script backend with Web App deployment |

---

## Technology Stack

### Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| HTML5 | HTML Living Standard | Structure |
| CSS3 | CSS Level 3 | Styling |
| JavaScript | ECMAScript 2021 (ES12) | Interactivity |
| Font Awesome | 6.4.0 | Icons |
| Inter Font | Google Fonts API | Typography |

### Backend

| Technology | Purpose |
|------------|---------|
| Cloudflare Workers | AI Chatbot API |
| Cloudflare Vectorize | Knowledge base storage (384 dimensions) |
| Cloudflare Workers AI | Embedding generation + LLM responses |
| Google Apps Script | Contact form backend |

### Deployment

| Technology | Purpose |
|------------|---------|
| GitHub Pages | Static site hosting |
| Cloudflare | Worker hosting |

---

## Project Structure

```
arkan-tsabit.github.io/
│
├── index.html                     # Landing page
├── about.html                     # About Me page
├── projects.html                  # Projects page
├── certifications.html            # Certifications page
├── achievements.html              # Achievements page
├── contact.html                   # Contact page
├── 404.html                       # Error page
│
├── css/
│   ├── style.css                  # Main styles
│   ├── dark-mode.css              # Dark theme
│   ├── responsive.css             # Mobile responsive
│   └── chatbot.css                # Chatbot widget
│
├── js/
│   ├── main.js                    # Core functionality
│   ├── dark-mode.js               # Theme toggle
│   ├── i18n.js                    # Multi-language
│   ├── chatbot.js                 # Chatbot integration
│   └── projects.js                # Project filtering
│
├── assets/
│   ├── images/
│   │   ├── profile.jpg            # Profile photo
│   │   ├── logo.ico               # Logo
│   │   ├── favicon.ico            # Browser icon
│   │   ├── projects/
│   │   │   ├── batchetl/
│   │   │   │   ├── architecture.png
│   │   │   │   ├── dashboard.png
│   │   │   │   └── erd.png
│   │   │   ├── uber/
│   │   │   │   ├── pipeline-flow.png
│   │   │   │   ├── star-schema.png
│   │   │   │   └── dashboard.png
│   │   │   ├── amazon/
│   │   │   │   ├── scraping-result.png
│   │   │   │   └── csv-output.png
│   │   │   └── expense/
│   │   │       ├── gui-dashboard.png
│   │   │       └── cli-summary.png
│   │   └── certifications/
│   │       ├── oracle.png
│   │       ├── ibm.png
│   │       └── meta.png
│   ├── icons/
│   │   ├── github.svg
│   │   ├── linkedin.svg
│   │   ├── email.svg
│   │   ├── download.svg
│   │   └── chatbot.svg
│   └── fonts/
│       └── inter.woff2
│
├── docs/
│   ├── CV/
│   │   └── Arkan-Tsabit_Data-Engineer.pdf
│   └── Job-Application/
│       └── Arkan-Tsabit_Job-Application.pdf
│
├── chatbot/
│   ├── worker.js                  # Cloudflare Worker (RAG logic)
│   ├── wrangler.toml              # Worker configuration
│   ├── knowledge-upload.json      # 30 documents knowledge base
│   ├── upload_vectors.py          # Vector embedding & upload script
│   ├── test_all.py                # 34 test questions suite
│   └── package.json               # Node.js dependencies
│
├── data/
│   ├── projects.json              # Project data
│   ├── certifications.json        # Certification data
│   ├── achievements.json          # Achievement data
│   └── i18n/
│       ├── en.json                # English translations
│       └── id.json                # Indonesian translations
│
├── .env                           # Environment variables (DO NOT COMMIT)
├── .gitignore
├── README.md                      # This file
├── LICENSE                        # MIT License
├── blueprint.md                   # Technical documentation
├── cheatsheets.md                 # Quick reference
├── checklist.md                   # Completion checklist
├── CHANGELOG.md                   # Version history
├── checker.py                     # Portfolio validation script
├── structure.py                   # Project structure display
└── CNAME                          # Custom domain (optional)
```

---

## Quick Start

### Prerequisites

| Item | Check Command |
|------|---------------|
| Git | `git --version` |
| Python 3.x | `python --version` |
| Node.js (optional) | `node --version` |

### Local Development

```bash
# Clone repository
git clone https://github.com/ArkanTsabit123/arkan-tsabit.github.io.git
cd arkan-tsabit.github.io

# Start local server (Python)
python -m http.server 8000

# Open browser
# http://localhost:8000
```

### Environment Setup

Create `.env` file in root:
```
CLOUDFLARE_ACCOUNT_ID=your_account_id
CLOUDFLARE_API_TOKEN=your_api_token
VECTORIZE_INDEX_NAME=arkan-knowledge-base
EMBEDDING_MODEL=@cf/baai/bge-small-en-v1.5
```

### Cloudflare Worker Setup

```bash
# Install Wrangler CLI
npm install -g wrangler

# Login to Cloudflare
wrangler login

# Create Vectorize index
wrangler vectorize create arkan-knowledge-base --preset @cf/baai/bge-small-en-v1.5

# Upload knowledge base
cd chatbot
python upload_vectors.py

# Deploy worker
wrangler deploy
```

### Google Sheets Contact Form Setup

1. Create Google Sheet with headers: `Name, Email, Subject, Message, Date, Time`
2. Open Apps Script from Extensions menu
3. Copy `doPost()` handler code from blueprint.md
4. Deploy as Web App with access set to "Anyone"
5. Update `scriptURL` in `contact.html`

---

## Deployment

### GitHub Pages

```bash
# Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main

# Enable GitHub Pages
# Settings -> Pages -> Branch: main -> / (root)
# Wait 2-5 minutes for deployment
# https://arkan-tsabit.github.io
```

### Cloudflare Worker

```bash
# Navigate to chatbot directory
cd chatbot

# Deploy worker
wrangler deploy

# Test API endpoint
curl https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What projects has Arkan built?"}'
```

---

## Chatbot Integration

### How It Works

1. **User Question** sent to Cloudflare Worker
2. **Generate Embedding** using `bge-small-en-v1.5` (384 dimensions)
3. **Vector Search** finds relevant context in Vectorize
4. **Context Building** retrieves matching documents
5. **LLM Response** generated using Workers AI

### Knowledge Base Categories

| Category | Count | Description |
|----------|-------|-------------|
| Profile | 3 | Professional summary, specialization, background |
| Projects | 4 | BatchETL, Uber, Amazon, Expense Tracker |
| Certifications | 11 | Oracle, IBM, Meta |
| Achievements | 3 | Oracle Race Top 108, Top 3, Best Teacher |
| Experience | 5 | BRI SD-WAN, Satu Benih, Bejagoo, Airport |
| Skills | 3 | Tech stack, Data Engineering, Cloud |
| Contact | 1 | Email, phone, GitHub, LinkedIn |
| **Total** | **30** | |

### Example Questions

```
- "Who is Arkan Tsabit?"
- "What projects has Arkan built?"
- "What certifications does Arkan have?"
- "What is Arkan's tech stack?"
- "Tell me about the BatchETL Pipeline project."
- "What did Arkan do at BRI SD-WAN?"
- "How can I contact Arkan?"
- "What Oracle certifications does Arkan have?"
- "What achievements does Arkan have?"
```

---

## Testing

### Chatbot Test Suite

```bash
# Run all 34 test questions
cd chatbot
python test_all.py

# Output example
============================================================
CHATBOT API TEST
============================================================
Total questions: 34
============================================================

[1/34] Who is Arkan Tsabit?
--------------------------------------------------
Status: PASS
Source: llm
Response: Arkan Tsabit is a Data Engineer with expertise...

[2/34] What projects has Arkan built?
--------------------------------------------------
Status: PASS
Source: llm
Response: Arkan has built 4 major projects...

============================================================
SUMMARY
============================================================
Total:  34
Passed: 34
Failed: 0
Rate:   100.0%
```

### Portfolio Validation

```bash
# Run full portfolio validation
python checker.py

# Output example
============================================================
FINAL SUMMARY
============================================================
Check Statistics:
  Total Checks:  153
  Passed:        153
  Failed:        0
  Critical:      0
  Success Rate:  100.0%

Overall Grade:
  EXCELLENT - 100% Complete!
============================================================
```

### Test Questions Categories

| Category | Count |
|----------|-------|
| Profile | 3 |
| Projects | 5 |
| Certifications | 12 |
| Achievements | 3 |
| Experience | 5 |
| Skills | 3 |
| Contact | 1 |
| General | 2 |
| **Total** | **34** |

---

## LLM Models Tested

The following 22 LLM models have been tested for compatibility:

| # | Model ID | Status |
|---|----------|--------|
| 1 | `@cf/meta/llama-4-scout-17b-16e-instruct` | 🔄 Testing |
| 2 | `@cf/meta/llama-3.2-3b-instruct` | 🔄 Testing |
| 3 | `@cf/meta/llama-3.1-8b-instruct-fp8` | 🔄 Testing |
| 4 | `@cf/meta/llama-3.2-1b-instruct` | 🔄 Testing |
| 5 | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | 🔄 Testing |
| 6 | `@cf/mistralai/mistral-small-3.1-24b-instruct` | 🔄 Testing |
| 7 | `@cf/mistral/mistral-7b-instruct-v0.2-lora` | ✅ Active |
| 8 | `@cf/qwen/qwen2.5-coder-32b-instruct` | 🔄 Testing |
| 9 | `@cf/qwen/qwen3-30b-a3b-fp8` | 🔄 Testing |
| 10 | `@cf/qwen/qwq-32b` | 🔄 Testing |
| 11 | `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | 🔄 Testing |
| 12 | `@cf/google/gemma-4-26b-a4b-it` | 🔄 Testing |
| 13 | `@cf/google/gemma-7b-it-lora` | 🔄 Testing |
| 14 | `@cf/aisingapore/gemma-sea-lion-v4-27b-it` | 🔄 Testing |
| 15 | `@cf/ibm-granite/granite-4.0-h-micro` | 🔄 Testing |
| 16 | `@cf/moonshotai/kimi-k2.6` | 🔄 Testing |
| 17 | `@cf/moonshotai/kimi-k2.7-code` | 🔄 Testing |
| 18 | `@cf/zai-org/glm-4.7-flash` | 🔄 Testing |
| 19 | `@cf/zai-org/glm-5.2` | 🔄 Testing |
| 20 | `@cf/nvidia/nemotron-3-120b-a12b` | 🔄 Testing |
| 21 | `@cf/openai/gpt-oss-20b` | 🔄 Testing |
| 22 | `@cf/openai/gpt-oss-120b` | 🔄 Testing |

---

## Customization

### Update Content

| File | What to Update |
|------|----------------|
| data/projects.json | Project details, metrics, links |
| data/certifications.json | Certification names, dates, links |
| data/achievements.json | Achievement details |
| data/i18n/en.json | English translations |
| data/i18n/id.json | Indonesian translations |
| chatbot/knowledge-upload.json | Knowledge base documents |

### Update Images

| File | Description |
|------|-------------|
| assets/images/profile.jpg | Profile photo |
| assets/images/logo.ico | Logo |
| assets/images/projects/ | Project screenshots |
| assets/images/certifications/ | Certification images |

### Update Colors

```css
/* css/style.css */
:root {
  --bg-primary: #FFFFFF;
  --text-primary: #111827;
  --accent-blue: #2563EB;
  --accent-green: #10B981;
}
```

### Update LLM Model

```javascript
// chatbot/worker.js - Line ~135
const response = await env.AI.run('@cf/mistral/mistral-7b-instruct-v0.2-lora', {
  // Change model ID here
});
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| GitHub Pages not loading | Check branch settings, wait 5 minutes |
| Chatbot not responding | Check Cloudflare Worker logs (`wrangler tail`) |
| Dark mode not saving | Check localStorage permission |
| Images not loading | Verify file paths and extensions |
| Language toggle not working | Check i18n JSON files |
| LLM model deprecated | Update model in `worker.js` |
| Vectorize index empty | Check `stored_vectors` in dashboard |
| API token error | Regenerate token with proper permissions |
| Contact form not working | Check Google Apps Script deployment and permissions |
| .env not loading | Ensure `python-dotenv` is installed |

### Debug Commands

```bash
# Clear browser cache
# Chrome: Ctrl+Shift+Delete
# Firefox: Ctrl+Shift+Delete

# Open browser console
# F12 -> Console tab

# Check Cloudflare Worker logs
wrangler tail

# Test API endpoint
curl -X POST "https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"question":"Who is Arkan Tsabit?"}'

# Test Google Sheets form
curl -X POST "https://script.google.com/macros/s/YOUR_ID/exec" \
  -d "Name=Test" \
  -d "Email=test@email.com" \
  -d "Subject=Test" \
  -d "Message=Hello"
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-08-08 | Google Sheets integration, UI improvements, security updates |
| 1.2.0 | 2026-08-06 | RAG chatbot, knowledge base, LLM testing |
| 1.1.0 | 2026-08-05 | Cloudflare Worker, Vectorize integration |
| 1.0.0 | 2026-07-25 | Initial release |

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Cloudflare for Workers, Vectorize, and Workers AI
- GitHub for Pages hosting
- Google for Sheets and Apps Script
- Font Awesome for icons
- Google Fonts for typography

---

## Contact

- **Email**: arkantsabit025@gmail.com
- **GitHub**: https://github.com/ArkanTsabit123
- **LinkedIn**: https://linkedin.com/in/arkan-tsabit
- **Website**: https://arkan-tsabit.github.io

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer