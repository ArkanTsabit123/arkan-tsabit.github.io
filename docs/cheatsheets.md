# CHEATSHEETS.md

## Portfolio Website - Quick Reference and Commands

### Document Information

| Property | Value |
|----------|-------|
| Version | 2.1.0 |
| Last Updated | 2026-08-09 |
| Status | Production Ready |
| Domain | arkan-tsabit.github.io |
| Hosting | GitHub Pages |

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Development Commands](#development-commands)
3. [Git Commands](#git-commands)
4. [Deployment Commands](#deployment-commands)
5. [Cloudflare Worker Commands](#cloudflare-worker-commands)
6. [Vectorize Commands](#vectorize-commands)
7. [Testing Commands](#testing-commands)
8. [SEO Commands](#seo-commands)
9. [API Testing Commands](#api-testing-commands)
10. [Contact Form Commands](#contact-form-commands)
11. [Domain Setup Commands](#domain-setup-commands)
12. [Troubleshooting Commands](#troubleshooting-commands)
13. [Quick Reference Tables](#quick-reference-tables)

---

## Quick Start

### One Command Setup

```bash
# Clone repository
git clone https://github.com/ArkanTsabit123/arkan-tsabit.github.io.git
cd arkan-tsabit.github.io

# Start local development
python -m http.server 8000

# Open browser
# http://localhost:8000
```

### Prerequisites Check

```bash
# Check Git
git --version

# Check Python
python --version

# Check Node.js
node --version

# Check Wrangler
wrangler --version
```

---

## Development Commands

### Local Server

```bash
# Python HTTP Server
python -m http.server 8000

# Python HTTP Server with different port
python -m http.server 3000

# Node.js Serve
npx serve .

# VS Code Live Server
# Right-click index.html -> Open with Live Server
```

### Browser Access

```bash
# Open browser (Windows)
start http://localhost:8000

# Open browser (Mac)
open http://localhost:8000

# Open browser (Linux)
xdg-open http://localhost:8000
```

---

## Git Commands

### Basic Git Commands

```bash
# Check status
git status

# Add all changes
git add .

# Add specific file
git add index.html

# Commit with message
git commit -m "feat: description of changes"

# Push to remote
git push origin main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline

# View commit history with details
git log --oneline --graph --decorate
```

### Branch Management

```bash
# Create new branch
git checkout -b feature/name

# Switch branch
git checkout main

# List branches
git branch -a

# Delete branch
git branch -d feature/name

# Merge branch
git merge feature/name
```

### Advanced Git Commands

```bash
# Force rebuild deployment
git commit --amend --no-edit
git push --force

# Stash changes
git stash

# Pop stash
git stash pop

# View changes
git diff

# Undo last commit
git reset --soft HEAD~1
```

---

## Deployment Commands

### GitHub Pages

```bash
# Deploy to GitHub Pages
# Automatic on push to main branch

# Check deployment status
# Settings -> Pages -> GitHub Pages

# Force rebuild (optional)
git commit --amend --no-edit
git push --force

# Check GitHub Pages URL
# https://arkantsabit123.github.io/arkan-tsabit.github.io/
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

# Check account ID
wrangler whoami
```

### Worker Development

```bash
# Develop locally
wrangler dev

# Develop with specific port
wrangler dev --port 8787

# Deploy worker
wrangler deploy

# Deploy with environment
wrangler deploy --env production

# View logs
wrangler tail

# View logs with filter
wrangler tail --filter "error"

# List workers
wrangler worker list

# Delete worker
wrangler worker delete

# Get worker info
wrangler worker get
```

---

## Vectorize Commands

### Index Management

```bash
# Create vectorize index with preset
wrangler vectorize create arkan-knowledge-base --preset @cf/baai/bge-small-en-v1.5

# List indexes
wrangler vectorize list

# Get index info
wrangler vectorize get arkan-knowledge-base

# Delete index
wrangler vectorize delete arkan-knowledge-base

# Get index stats
wrangler vectorize get arkan-knowledge-base --stats
```

### Vector Operations

```bash
# Insert vectors
wrangler vectorize insert arkan-knowledge-base --file knowledge-upload.ndjson

# Query vectors
wrangler vectorize query arkan-knowledge-base --query="What projects has Arkan built?"

# Query with metadata filter
wrangler vectorize query arkan-knowledge-base --query="certifications" --metadata="category=certifications"

# Get vectors
wrangler vectorize get arkan-knowledge-base --ids "id1,id2,id3"

# Delete vectors
wrangler vectorize delete arkan-knowledge-base --ids "id1,id2,id3"
```

### Knowledge Base Upload

```bash
# Convert JSON to NDJSON
node convert-to-ndjson.js

# Upload to Vectorize
npx wrangler vectorize insert arkan-knowledge-base --file knowledge-upload.ndjson

# Generate embeddings and upload
python upload_vectors.py

# Check uploaded vectors
wrangler vectorize get arkan-knowledge-base --stats
```

---

## Testing Commands

### Chatbot Testing

```bash
# Run all 34 test questions
cd chatbot
python test_all.py

# Run specific test
python test_all.py --test "Who is Arkan Tsabit?"

# Run with verbose output
python test_all.py --verbose
```

### Portfolio Validation

```bash
# Run full portfolio validation
python checker.py

# Check specific file
python checker.py --file index.html

# Run with verbose output
python checker.py --verbose

# Run with specific checks
python checker.py --checks html,css,js

# Run with output file
python checker.py --output report.txt
```

### HTML Validation

```bash
# Validate specific HTML file
npx html-validator --file index.html

# Validate all HTML files
for file in *.html; do npx html-validator --file $file; done

# Validate with W3C standards
npx html-validator --file index.html --format=json
```

### CSS Linting

```bash
# Lint all CSS files
npx stylelint "css/*.css"

# Lint with fix
npx stylelint "css/*.css" --fix

# Lint specific file
npx stylelint css/style.css
```

### JavaScript Linting

```bash
# Lint all JS files
npx eslint "js/*.js"

# Lint with fix
npx eslint "js/*.js" --fix

# Lint specific file
npx eslint js/main.js
```

### Link Checking

```bash
# Check all links
npx link-checker http://localhost:8000

# Check recursive
npx link-checker https://arkantsabit123.github.io/arkan-tsabit.github.io/ --recursive

# Check specific page
npx link-checker https://arkantsabit123.github.io/arkan-tsabit.github.io//projects.html
```

---

## SEO Commands

### Sitemap Generation

```bash
# Generate sitemap manually
# Create sitemap.xml with all pages

# Use sitemap generator
npx sitemap-generator-cli http://localhost:8000 --output sitemap.xml

# Validate sitemap
npx sitemap-validator sitemap.xml
```

### Robots.txt

```bash
# Create robots.txt
cat > robots.txt << EOF
User-agent: *
Allow: /
Sitemap: https://arkantsabit.com/sitemap.xml
EOF

# Validate robots.txt
# Visit: https://www.google.com/webmasters/tools/robots-testing-tool
```

### SEO Validation Tools

```bash
# Meta tags validator
# Visit: https://metatags.io/

# Rich Results Test
# Visit: https://search.google.com/test/rich-results

# Schema Markup Validator
# Visit: https://validator.schema.org/

# Google Search Console
# Visit: https://search.google.com/search-console

# Bing Webmaster Tools
# Visit: https://www.bing.com/webmasters

# Security Headers Test
# Visit: https://securityheaders.com/?q=arkan-tsabit.github.io

# CSP Evaluator
# Visit: https://csp-evaluator.withgoogle.com/?url=arkan-tsabit.github.io

# SSL Labs Test
# Visit: https://www.ssllabs.com/ssltest/analyze.html?d=arkan-tsabit.github.io
```

---

## API Testing Commands

### Health Check

```bash
# Test health endpoint
curl https://arkan-chatbot.arkan-chatbot.workers.dev/health

# Test with Python
python -c "
import requests
response = requests.get('https://arkan-chatbot.arkan-chatbot.workers.dev/health')
print(response.json())
"
```

### Chatbot API

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

# Test with JavaScript
node -e "
fetch('https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ question: 'Who is Arkan Tsabit?' })
})
.then(r => r.json())
.then(console.log)
"
```

### API Performance Testing

```bash
# Test response time
curl -w "@curl-format.txt" https://arkan-chatbot.arkan-chatbot.workers.dev/health

# Create curl-format.txt file
cat > curl-format.txt << EOF
time_namelookup:  %{time_namelookup}s
time_connect:     %{time_connect}s
time_appconnect:  %{time_appconnect}s
time_pretransfer: %{time_pretransfer}s
time_redirect:    %{time_redirect}s
time_starttransfer: %{time_starttransfer}s
time_total:       %{time_total}s
EOF

# Test with multiple requests
for i in {1..10}; do
  curl -X POST https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat \
    -H "Content-Type: application/json" \
    -d '{"question":"What projects has Arkan built?"}' \
    -w "\nTime: %{time_total}s\n"
done
```

---

## Contact Form Commands

### Google Apps Script

```bash
# Test form submission
curl -X POST "https://script.google.com/macros/s/YOUR_ID/exec" \
  -d "Name=Test" \
  -d "Email=test@email.com" \
  -d "Subject=Test" \
  -d "Message=Hello"

# Test with Python
python -c "
import requests
data = {
    'Name': 'Test',
    'Email': 'test@email.com',
    'Subject': 'Test',
    'Message': 'Hello'
}
response = requests.post('https://script.google.com/macros/s/YOUR_ID/exec', data=data)
print(response.text)
"

# Check Google Sheets
# Open: https://docs.google.com/spreadsheets/d/1zcck8oaWyw5aWOpNl4JqstaLFYhjMvh_aNvrr0adqAg/edit
```

---

## Domain Setup Commands

### Cloudflare Registrar

```bash
# Buy domain
# Go to Cloudflare Registrar
# Search for arkantsabit.com
# Add to cart and checkout (~$10.44/year)

# Add DNS records
# A record: @ -> 185.199.108.153
# A record: @ -> 185.199.109.153
# A record: @ -> 185.199.110.153
# A record: @ -> 185.199.111.153
# CNAME: www -> arkan-tsabit.github.io

# Update CNAME file
echo "arkantsabit.com" > CNAME

# Update GitHub Pages
# Settings -> Pages -> Custom domain -> arkantsabit.com

# Enforce HTTPS
# Settings -> Pages -> Enforce HTTPS -> Check
```

### DNS Propagation Check

```bash
# Check DNS propagation
nslookup arkantsabit.com
dig arkantsabit.com
ping arkantsabit.com

# Check with online tools
# https://www.whatsmydns.net/
# https://dnschecker.org/

# Check specific record
dig arkantsabit.com A
dig arkantsabit.com CNAME
```

---

## Troubleshooting Commands

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

# Check environment variables
cat .env

# Test Cloudflare Worker locally
wrangler dev

# Test API endpoint locally
curl http://localhost:8787/api/chat -H "Content-Type: application/json" -d '{"question":"Who is Arkan Tsabit?"}'
```

### Common Issue Fixes

```bash
# GitHub Pages not loading
# Check branch settings, wait 5 minutes

# Chatbot not responding
wrangler tail --format=json | grep -i error

# Dark mode not saving
# Check localStorage permission
# F12 -> Application -> Local Storage

# Images not loading
# Verify file paths
find assets/images/ -name "*.png" -o -name "*.jpg"

# Language toggle not working
# Check i18n JSON files
cat data/i18n/en.json
cat data/i18n/id.json

# LLM model deprecated
# Update model in worker.js
nano chatbot/worker.js

# Vectorize index empty
wrangler vectorize get arkan-knowledge-base --stats

# API token error
# Regenerate token with proper permissions
# Cloudflare Dashboard -> API Tokens -> Create Token

# Contact form not working
# Check Google Apps Script permissions
# Apps Script -> Deploy -> Manage deployments

# Domain not resolving
nslookup arkantsabit.com

# SSL certificate error
# Check Cloudflare SSL/TLS settings
```

---

## Quick Reference Tables

### File Locations

| File | Path | Purpose |
|------|------|---------|
| Landing Page | index.html | Main entry point |
| About Page | about.html | Professional summary |
| Projects Page | projects.html | Project showcase |
| Certifications Page | certifications.html | Certification display |
| Achievements Page | achievements.html | Achievement showcase |
| Contact Page | contact.html | Contact form |
| CV PDF | docs/CV/Arkan-Tsabit_Data-Engineer.pdf | Downloadable CV |
| Job Application | docs/Job-Application/Arkan-Tsabit_Job-Application.pdf | Downloadable application |
| Projects Data | data/projects.json | All project information |
| Certifications Data | data/certifications.json | All certifications |
| Achievements Data | data/achievements.json | All achievements |
| Worker | chatbot/worker.js | Cloudflare Worker |
| Knowledge Base | chatbot/knowledge-upload.json | 30 documents for RAG |
| Environment Variables | .env | API keys and tokens |
| Checker | checker.py | Portfolio validation script |
| Structure | structure.py | Project structure display |
| Sitemap | sitemap.xml | SEO sitemap |
| Robots | robots.txt | SEO robots file |

### URLs

| Resource | URL |
|----------|-----|
| Website | https://arkantsabit123.github.io/arkan-tsabit.github.io/ |
| Domain | https://arkantsabit.com (Pending) |
| GitHub | https://github.com/ArkanTsabit123 |
| LinkedIn | https://www.linkedin.com/in/arkan-tsabit-0b12b9407/ |
| Cloudflare Dashboard | https://dash.cloudflare.com |
| Worker Health | https://arkan-chatbot.arkan-chatbot.workers.dev/health |
| Chat API | https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat |
| Google Sheets | https://docs.google.com/spreadsheets/d/1zcck8oaWyw5aWOpNl4JqstaLFYhjMvh_aNvrr0adqAg/edit |
| Google Search Console | https://search.google.com/search-console |
| Google Analytics | https://analytics.google.com |

### Colors

| Element | Light Mode | Dark Mode |
|---------|------------|-----------|
| Background | #FFFFFF | #0F172A |
| Text | #111827 | #F8FAFC |
| Primary | #2563EB | #3B82F6 |
| Secondary | #6B7280 | #9CA3AF |
| Accent | #10B981 | #34D399 |
| Border | #E5E7EB | #1E293B |

### Environment Variables

| Variable | Description |
|----------|-------------|
| CLOUDFLARE_ACCOUNT_ID | Cloudflare account ID |
| CLOUDFLARE_API_TOKEN | Cloudflare API token |
| VECTORIZE_INDEX_NAME | Vectorize index name |
| EMBEDDING_MODEL | Embedding model ID |
| LLM_MODEL | LLM model ID |

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
| Validation Checks | 153 |
| LLM Models Tested | 22 |
| Documentation Files | 9 |

### Status Badges

| Badge | Status |
|-------|--------|
| Website | Active |
| GitHub | Active |
| LinkedIn | Active |
| License | MIT |
| Deployment | GitHub Pages |
| Chatbot | RAG Powered |
| Tests | 34 Passed |
| Contact | Google Sheets |
| Domain | Pending |
| SEO | Pending |

---

## Useful Resources

| Resource | URL |
|----------|-----|
| Font Awesome | https://fontawesome.com |
| Google Fonts | https://fonts.google.com |
| Cloudflare Workers | https://developers.cloudflare.com/workers/ |
| GitHub Pages | https://pages.github.com |
| HTML5 Validator | https://validator.w3.org |
| CSS Validator | https://jigsaw.w3.org/css-validator/ |
| Cloudflare Vectorize | https://developers.cloudflare.com/vectorize/ |
| Workers AI Models | https://developers.cloudflare.com/workers-ai/models/ |
| Google Sheets API | https://developers.google.com/apps-script |
| Open Graph | https://ogp.me/ |
| Schema.org | https://schema.org |
| Cloudflare Registrar | https://www.cloudflare.com/registrar/ |
| Google Search Console | https://search.google.com/search-console |
| Google Analytics | https://analytics.google.com |

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer