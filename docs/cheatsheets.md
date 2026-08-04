# PORTFOLIO WEBSITE - CHEATSHEET

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0.0 |
| Last Updated | 2026-08-05 |
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
# Create vectorize index
wrangler vectorize create arkan-knowledge-base

# List indexes
wrangler vectorize list

# Insert vectors
wrangler vectorize insert arkan-knowledge-base --file=vectors.json

# Query vectors
wrangler vectorize query arkan-knowledge-base --query="What projects has Arkan built?"
```

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
# Chatbot API endpoint
POST https://arkan-chatbot.workers.dev/api/chat
Content-Type: application/json

{
  "question": "What projects has Arkan built?"
}

# Response
{
  "response": "Arkan has built 4 major projects..."
}
```

### Test API

```bash
# Test with curl
curl -X POST https://arkan-chatbot.workers.dev/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What projects has Arkan built?"}'

# Test with Python
python -c "
import requests
response = requests.post(
    'https://arkan-chatbot.workers.dev/api/chat',
    json={'question': 'What projects has Arkan built?'}
)
print(response.json())
"
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| GitHub Pages not loading | Check branch settings, wait 5 minutes |
| Chatbot not responding | Check Cloudflare Worker logs |
| Dark mode not saving | Check localStorage permission |
| Images not loading | Verify file paths and extensions |
| Language toggle not working | Check i18n JSON files |
| CSS not applying | Clear browser cache (Ctrl+Shift+R) |
| JavaScript errors | Check browser console (F12) |
| 404 errors | Verify file paths and links |

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

### URLs

| Resource | URL |
|----------|-----|
| Website | https://arkan-tsabit.github.io |
| GitHub | https://github.com/ArkanTsabit123 |
| LinkedIn | https://linkedin.com/in/arkan-tsabit |
| Cloudflare Dashboard | https://dash.cloudflare.com |
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

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-08-05 | Initial release |

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

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer