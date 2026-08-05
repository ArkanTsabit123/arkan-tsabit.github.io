# PORTFOLIO WEBSITE - CHEATSHEET

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0.0 |
| Last Updated | 2026-08-06 |
| Status | Production Ready |
| Domain | arkan-tsabit.github.io |
| Hosting | GitHub Pages |

---

## Quick Start

### One Command Setup

```bash
# Clone repository
git clone https://github.com/ArkanTsabit123/arkan-tsabit.github.io.git
cd arkan-tsabit.github.io

# Install dependencies (if any)
npm install

# Start local development
python -m http.server 8000

# Open browser
# http://localhost:8000
```

---

## Development Commands

### Local Development

```bash
# Start local server (Python)
python -m http.server 8000

# Start local server (Node.js)
npx serve .

# Start local server (VS Code Live Server)
# Right-click index.html -> Open with Live Server

# Open browser
start http://localhost:8000   # Windows
open http://localhost:8000    # Mac
xdg-open http://localhost:8000 # Linux
```

### Git Commands

```bash
# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "feat: description of changes"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline

# Create new branch
git checkout -b feature/name

# Switch branch
git checkout main
```

### Deployment Commands

```bash
# Deploy to GitHub Pages
# Automatic on push to main branch

# Check deployment status
# Settings -> Pages -> GitHub Pages

# Force rebuild (optional)
# git commit --amend --no-edit
# git push --force
```

---

## Cloudflare Worker Commands

### Installation and Setup

```bash
# Install Wrangler CLI
npm install -g wrangler

# Login to Cloudflare
wrangler login

# Verify login
wrangler whoami
```

### Worker Development

```bash
# Create new worker
wrangler init

# Develop locally
wrangler dev

# Deploy worker
wrangler deploy

# Deploy with environment
wrangler deploy --env production

# View logs
wrangler tail

# List workers
wrangler worker list
```

### Vectorize Commands

```bash
# Create vectorize index with preset
wrangler vectorize create arkan-knowledge-base --preset @cf/baai/bge-small-en-v1.5

# List indexes
wrangler vectorize list

# Delete index
wrangler vectorize delete arkan-knowledge-base

# Insert vectors
wrangler vectorize insert arkan-knowledge-base --file knowledge-upload.ndjson

# Query vectors
wrangler vectorize query arkan-knowledge-base --query="What projects has Arkan built?"
```

### Knowledge Base Upload

```bash
# Convert JSON to NDJSON
node convert-to-ndjson.js

# Upload to Vectorize
npx wrangler vectorize insert arkan-knowledge-base --file knowledge-upload.ndjson

# Generate embeddings and upload
python upload_vectors.py
```

### LLM Model Testing

```bash
# Test different LLM models
# Update worker.js with model ID and deploy:
npx wrangler deploy
```

**Model IDs to test:**

| # | Model ID |
|---|----------|
| 1 | `@cf/meta/llama-4-scout-17b-16e-instruct` |
| 2 | `@cf/meta/llama-3.2-3b-instruct` |
| 3 | `@cf/meta/llama-3.1-8b-instruct-fp8` |
| 4 | `@cf/meta/llama-3.2-1b-instruct` |
| 5 | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` |
| 6 | `@cf/mistralai/mistral-small-3.1-24b-instruct` |
| 7 | `@cf/mistral/mistral-7b-instruct-v0.2-lora` |
| 8 | `@cf/qwen/qwen2.5-coder-32b-instruct` |
| 9 | `@cf/qwen/qwen3-30b-a3b-fp8` |
| 10 | `@cf/qwen/qwq-32b` |
| 11 | `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` |
| 12 | `@cf/google/gemma-4-26b-a4b-it` |
| 13 | `@cf/google/gemma-7b-it-lora` |
| 14 | `@cf/aisingapore/gemma-sea-lion-v4-27b-it` |
| 15 | `@cf/ibm-granite/granite-4.0-h-micro` |
| 16 | `@cf/moonshotai/kimi-k2.6` |
| 17 | `@cf/moonshotai/kimi-k2.7-code` |
| 18 | `@cf/zai-org/glm-4.7-flash` |
| 19 | `@cf/zai-org/glm-5.2` |
| 20 | `@cf/nvidia/nemotron-3-120b-a12b` |
| 21 | `@cf/openai/gpt-oss-20b` |
| 22 | `@cf/openai/gpt-oss-120b` |

---

## Website Structure Commands

### Generate Structure

```bash
# Create directory structure (Windows PowerShell)
New-Item -ItemType Directory -Path css, js, assets, docs, data, chatbot -Force

# Create directory structure (Linux/Mac)
mkdir -p css js assets docs data chatbot

# Create subdirectories
mkdir -p assets/images/projects/batchetl
mkdir -p assets/images/projects/uber
mkdir -p assets/images/projects/amazon
mkdir -p assets/images/projects/expense
mkdir -p assets/images/certifications
mkdir -p docs/CV docs/Job-Application
mkdir -p chatbot/knowledge-base
mkdir -p data/i18n
```

### Create Files

```bash
# HTML files
touch index.html about.html projects.html certifications.html achievements.html contact.html 404.html

# CSS files
touch css/style.css css/dark-mode.css css/responsive.css css/chatbot.css

# JavaScript files
touch js/main.js js/dark-mode.js js/i18n.js js/chatbot.js js/projects.js

# Data files
touch data/projects.json data/certifications.json data/achievements.json
touch data/i18n/en.json data/i18n/id.json

# Chatbot files
touch chatbot/worker.js chatbot/wrangler.toml
touch chatbot/knowledge-base/cv-data.json
touch chatbot/knowledge-base/projects-data.json
touch chatbot/knowledge-base/certifications-data.json

# Documentation
touch README.md LICENSE blueprint.md cheatsheet.md checklist.md

# Git
touch .gitignore CNAME
```

---

## Content Commands

### Update Content

```bash
# Edit project data
nano data/projects.json

# Edit certification data
nano data/certifications.json

# Edit achievement data
nano data/achievements.json

# Edit English translations
nano data/i18n/en.json

# Edit Indonesian translations
nano data/i18n/id.json
```

---

## Testing Commands

### Chatbot Testing

```bash
# Run all 34 test questions
python test_all.py

# Test single question with curl
curl -X POST "https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"question":"Who is Arkan Tsabit?"}'

# Test in PowerShell
$body = @{ question = "Who is Arkan Tsabit?" } | ConvertTo-Json
Invoke-RestMethod -Uri "https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat" -Method Post -Body $body -ContentType "application/json"

# Test health check
curl https://arkan-chatbot.arkan-chatbot.workers.dev/health
```

### Local Testing

```bash
# Test HTML validation
npx html-validator --file index.html

# Test CSS linting
npx stylelint "css/*.css"

# Test JavaScript linting
npx eslint "js/*.js"

# Test link checking
npx link-checker http://localhost:8000

# Test responsive design
# Chrome DevTools -> Toggle Device Toolbar
```

### Performance Testing

```bash
# Lighthouse testing
# Chrome DevTools -> Lighthouse tab

# PageSpeed Insights
# https://pagespeed.web.dev/

# GTmetrix
# https://gtmetrix.com/

# WebPageTest
# https://www.webpagetest.org/
```

---

## SEO Commands

### Generate Sitemap

```bash
# Generate sitemap.xml
# https://www.xml-sitemaps.com/

# Or use sitemap generator
npx sitemap-generator-cli http://localhost:8000 --output sitemap.xml
```

### Validate SEO

```bash
# Google Search Console
# https://search.google.com/search-console

# Bing Webmaster Tools
# https://www.bing.com/webmasters

# Meta tags validator
# https://metatags.io/
```

---

## Cloudflare Worker API

### Endpoints

```bash
# Health check
GET https://arkan-chatbot.arkan-chatbot.workers.dev/health

# Chatbot API endpoint
POST https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat
Content-Type: application/json

{
  "question": "What projects has Arkan built?"
}

# Response
{
  "response": "Arkan has built 4 major projects...",
  "source": "llm"
}
```

### Test API

```bash
# Test with curl
curl -X POST https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What projects has Arkan built?"}'

# Test with Python
python -c "
import requests
response = requests.post(
    'https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat',
    json={'question': 'What projects has Arkan built?'}
)
print(response.json())
"

# Test with PowerShell
$body = @{ question = "Who is Arkan Tsabit?" } | ConvertTo-Json
Invoke-RestMethod -Uri "https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat" -Method Post -Body $body -ContentType "application/json"
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
| CSS not applying | Clear browser cache (Ctrl+Shift+R) |
| JavaScript errors | Check browser console (F12) |
| 404 errors | Verify file paths and links |
| LLM model deprecated | Update model in `worker.js` |
| Vectorize index empty | Check `stored_vectors` in dashboard |
| API token error | Regenerate token with proper permissions |

### Debug Commands

```bash
# Clear browser cache
# Chrome: Ctrl+Shift+Delete
# Firefox: Ctrl+Shift+Delete

# Open browser console
# F12 -> Console tab

# Check network requests
# F12 -> Network tab

# Check localStorage
# F12 -> Application -> Local Storage

# Check Cloudflare Worker logs
wrangler tail

# Check deployment status
# Settings -> Pages -> GitHub Pages

# Run debug script
python debug.py
```

---

## Quick Reference

### Key Files

| File | Path | Purpose |
|------|------|---------|
| Landing Page | index.html | Main entry point |
| CV PDF | docs/CV/Arkan-Tsabit_Data-Engineer.pdf | Downloadable CV |
| Job Application | docs/Job-Application/Arkan-Tsabit_Job-Application.pdf | Downloadable application |
| Projects Data | data/projects.json | All project information |
| Certifications Data | data/certifications.json | All certifications |
| Achievements Data | data/achievements.json | All achievements |
| Worker | chatbot/worker.js | Cloudflare Worker |
| Knowledge Base | chatbot/knowledge-upload.json | 30 documents for RAG |

### URLs

| Resource | URL |
|----------|-----|
| Website | https://arkan-tsabit.github.io |
| GitHub | https://github.com/ArkanTsabit123 |
| LinkedIn | https://linkedin.com/in/arkan-tsabit |
| Cloudflare Dashboard | https://dash.cloudflare.com |
| Worker Health | https://arkan-chatbot.arkan-chatbot.workers.dev/health |
| Chat API | https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat |

### Colors

| Element | Light Mode | Dark Mode |
|---------|------------|-----------|
| Background | #FFFFFF | #0F172A |
| Text | #111827 | #F8FAFC |
| Primary | #2563EB | #3B82F6 |
| Secondary | #6B7280 | #9CA3AF |
| Accent | #10B981 | #34D399 |
| Border | #E5E7EB | #1E293B |

### Metrics

| Metric | Value |
|--------|-------|
| Professional Certifications | 10 |
| Achievement | 1 |
| Data Projects | 4 |
| Work Experience | 4 |
| Languages | 2 (ID, EN) |
| Pages | 6 |
| Knowledge Base Documents | 30 |
| Test Questions | 34 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-08-06 | Initial release |

---

## Useful Resources

| Resource | URL |
|----------|-----|
| Font Awesome | https://fontawesome.com |
| Google Fonts | https://fonts.google.com |
| Cloudflare Workers | https://workers.cloudflare.com |
| GitHub Pages | https://pages.github.com |
| HTML5 Validator | https://validator.w3.org |
| CSS Validator | https://jigsaw.w3.org/css-validator/ |
| Cloudflare Vectorize | https://developers.cloudflare.com/vectorize/ |
| Workers AI Models | https://developers.cloudflare.com/workers-ai/models/ |

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer