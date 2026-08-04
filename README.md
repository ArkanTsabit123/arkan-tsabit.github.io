# 🌐 Arkan Tsabit - Data Engineer Portfolio

## Personal Portfolio Website Showcasing Data Engineering Projects, Certifications, and Professional Experience

[![Website](https://img.shields.io/badge/Website-arkan--tsabit.github.io-blue)](https://arkan-tsabit.github.io)
[![GitHub](https://img.shields.io/badge/GitHub-ArkanTsabit123-lightgrey)](https://github.com/ArkanTsabit123)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-arkan--tsabit-blue)](https://linkedin.com/in/arkan-tsabit)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Deployment](https://img.shields.io/badge/Deployment-GitHub%20Pages-brightgreen)](https://pages.github.com)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Deployment](#deployment)
- [Chatbot Integration](#chatbot-integration)
- [File Structure](#file-structure)
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

### Key Metrics

| Metric | Value |
|--------|-------|
| Projects | 4 |
| Certifications | 10 |
| Languages | 2 (ID, EN) |
| Pages | 6 |
| Chatbot | RAG-powered |
| Deployment | GitHub Pages |

---

## Features

### Core Features

| Feature | Description |
|---------|-------------|
| **Landing Page** | Professional introduction with key metrics and call-to-action buttons |
| **About Me** | Professional summary, career transition story, and technical skills |
| **Projects** | 4 detailed project cards with metrics, tech stack, and GitHub links |
| **Certifications** | 10 certifications organized by provider (Oracle, IBM, Meta) |
| **Achievements** | Oracle Race to Certification awards and teaching recognition |
| **Contact** | Contact information and downloadable documents (CV, Job Application) |

### Interactive Features

| Feature | Description |
|---------|-------------|
| **Dark/Light Mode** | Theme toggle with persistent preference |
| **Multi-Language** | Indonesian and English toggle with persistent preference |
| **AI Chatbot** | RAG-powered question-answering about experience and skills |
| **Responsive Design** | Optimized for all screen sizes |

### Technical Features

| Feature | Description |
|---------|-------------|
| **Static Hosting** | GitHub Pages for fast, reliable deployment |
| **Cloudflare Workers** | Serverless AI chatbot backend |
| **RAG Implementation** | Vector search + LLM for accurate responses |
| **Performance Optimized** | Lazy loading, minification, caching |

---

## Technology Stack

### Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| HTML5 | - | Structure |
| CSS3 | - | Styling |
| JavaScript | ES6 | Interactivity |
| Font Awesome | 6.4.0 | Icons |
| Inter Font | - | Typography |

### Backend

| Technology | Purpose |
|------------|---------|
| Cloudflare Workers | AI Chatbot API |
| Cloudflare Vectorize | Knowledge base storage |
| Cloudflare Workers AI | LLM for response generation |

### Deployment

| Technology | Purpose |
|------------|---------|
| GitHub Pages | Static site hosting |
| Cloudflare | Worker hosting |

---

## Project Structure

```
arkan-tsabit-portfolio/
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
│   │   ├── logo.svg               # Logo
│   │   ├── favicon.ico            # Browser icon
│   │   ├── projects/
│   │   │   ├── batchetl/
│   │   │   ├── uber/
│   │   │   ├── amazon/
│   │   │   └── expense/
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
│   ├── worker.js                  # Cloudflare Worker
│   ├── wrangler.toml              # Worker config
│   └── knowledge-base/
│       ├── cv-data.json
│       ├── projects-data.json
│       └── certifications-data.json
│
├── data/
│   ├── projects.json              # Project data
│   ├── certifications.json        # Certification data
│   ├── achievements.json          # Achievement data
│   └── i18n/
│       ├── en.json                # English translations
│       └── id.json                # Indonesian translations
│
├── .gitignore
├── README.md                      # This file
├── LICENSE                        # MIT License
├── blueprint.md                   # Technical documentation
├── cheatsheet.md                  # Quick reference
├── checklist.md                   # Completion checklist
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

### Cloudflare Worker Setup

```bash
# Install Wrangler CLI
npm install -g wrangler

# Login to Cloudflare
wrangler login

# Deploy worker
cd chatbot
wrangler deploy
```

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
curl https://arkan-chatbot.workers.dev/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What projects has Arkan built?"}'
```

---

## Chatbot Integration

### How It Works

1. **User Question** sent to Cloudflare Worker
2. **Vector Search** finds relevant context in knowledge base
3. **Context Building** formats retrieved information
4. **LLM Response** generated using Cloudflare Workers AI

### Knowledge Base

| File | Content |
|------|---------|
| cv-data.json | Professional summary, skills, experience |
| projects-data.json | Project descriptions and metrics |
| certifications-data.json | Certification details |

### Example Questions

```
- "What projects has Arkan built?"
- "What certifications does Arkan have?"
- "What is Arkan's tech stack?"
- "Tell me about the BatchETL Pipeline project."
- "How can I contact Arkan?"
```

---

## File Structure Reference

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

### Update Images

| File | Description |
|------|-------------|
| assets/images/profile.jpg | Profile photo |
| assets/images/logo.svg | Logo |
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

### Debug Commands

```bash
# Clear browser cache
# Chrome: Ctrl+Shift+Delete
# Firefox: Ctrl+Shift+Delete

# Open browser console
# F12 -> Console tab

# Check Cloudflare Worker logs
wrangler tail

# Check GitHub Pages deployment
# Settings -> Pages -> GitHub Pages
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-08-05 | Initial release |

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Cloudflare for Workers and AI services
- GitHub for Pages hosting
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