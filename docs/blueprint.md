# ARKAN TSABIT - PORTFOLIO WEBSITE BLUEPRINT

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0.0 |
| Last Updated | 2026-08-05 |
| Status | Production Ready |
| Domain | arkan-tsabit.github.io |
| Hosting | GitHub Pages |
| AI Chatbot | Cloudflare Workers + RAG |

---

## Project Overview

### Core Objectives

1. Build a personal portfolio website to showcase data engineering projects.
2. Display 10 professional certifications from Oracle, IBM, and Meta.
3. Provide multi-language support (Indonesian and US English).
4. Implement an AI-powered chatbot using Cloudflare Workers with RAG.
5. Highlight achievements including Oracle Race to Certification (Top 108 Global, Top 3 Indonesia).
6. Enable CV and job application letter downloads.
7. Support dark and light mode toggle.

### Target Audience

- Recruiters and hiring managers.
- Technical interviewers.
- Data engineering peers.
- Potential clients.

### Success Metrics

| Metric | Target |
|--------|--------|
| Page Load Time | Under 2 seconds |
| Theme Toggle | Functional dark/light mode |
| Language Switch | Instant toggle between ID and EN |
| Chatbot Response Time | Under 3 seconds |
| Mobile Responsiveness | 100 percent across all devices |
| SEO Score | 90+ on Google Lighthouse |

---

## System Architecture

### Architecture Overview

```
+---------------------------------------------------------------------------------+
|                              USER BROWSER                                        |
|  +-----------------------------------------------------------------------------+|
|  |  arkan-tsabit.github.io                                                      ||
|  +-----------------------------------------------------------------------------+|
|                                     |                                            |
|                                     v                                            |
|  +-----------------------------------------------------------------------------+|
|  |                         GITHUB PAGES HOSTING                                  ||
|  |                                                                             ||
|  |  +-------------------------------------------------------------------------+||
|  |  |  Static HTML, CSS, JavaScript                                           |||
|  |  |  - Landing Page                                                         |||
|  |  |  - About Me                                                             |||
|  |  |  - Projects (4)                                                         |||
|  |  |  - Certifications (10)                                                  |||
|  |  |  - Achievements                                                         |||
|  |  |  - Contact                                                              |||
|  |  +-------------------------------------------------------------------------+||
|  +-----------------------------------------------------------------------------+|
|                                     |                                            |
|                                     v                                            |
|  +-----------------------------------------------------------------------------+|
|  |                         CLOUDFLARE WORKERS                                   ||
|  |                                                                             ||
|  |  +-------------------------------------------------------------------------+||
|  |  |  RAG Chatbot API                                                        |||
|  |  |  - User question -> Vector search -> AI response                        |||
|  |  |  - Knowledge base: CV, Projects, Certifications                         |||
|  |  +-------------------------------------------------------------------------+||
|  +-----------------------------------------------------------------------------+|
|                                                                                 |
+---------------------------------------------------------------------------------+
```

### Component Details

| Layer | Component | Technology | Purpose |
|-------|-----------|------------|---------|
| Frontend | Website | HTML5, CSS3, JavaScript | User interface |
| Styling | Theme | CSS Custom Properties | Dark and light mode |
| Languages | Internationalization | JavaScript | Indonesian and English |
| Hosting | Deployment | GitHub Pages | Static site hosting |
| AI Chatbot | Backend | Cloudflare Workers | RAG-powered question and answer |
| Vector Database | Storage | Cloudflare Vectorize | Knowledge base storage |
| LLM | AI Model | Cloudflare Workers AI | Response generation |

---

## Website Structure

### Page Architecture

```
+-----------------------------------------------------------------------------+
|                              HEADER                                          |
|  +---------------------------------------------------------------------+   |
|  |  [Logo AT]    [Home] [About] [Projects] [Certifications] [Contact] |   |
|  |                                            [Theme] [Language]       |   |
|  +---------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
                                     |
                                     v
+-----------------------------------------------------------------------------+
|                             MAIN CONTENT                                     |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  HERO SECTION                                                       |   |
|  |  - Name: Arkan Tsabit                                               |   |
|  |  - Title: Data Engineer | Cloud Data Engineer                      |   |
|  |  - Tagline: Building production-ready data pipelines              |   |
|  |  - Metrics: 2.96M+ records, under 30 seconds execution, 100% data quality |   |
|  |  - Buttons: View Projects, Download CV, Contact Me                |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  ABOUT ME                                                           |   |
|  |  - Profile photo (placeholder)                                      |   |
|  |  - Professional summary                                              |   |
|  |  - Tech stack: Airflow, PostgreSQL, DuckDB, Python, Docker          |   |
|  |  - Certifications: Oracle, IBM, Meta (10 total)                     |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  PROJECTS (4)                                                       |   |
|  |  +-----------------------------------------------------------------+   |
|  |  |  BatchETL Pipeline                                              |   |
|  |  |  - 2.96M rows, under 30 seconds execution, 100% data quality   |   |
|  |  |  - Stack: Airflow, PostgreSQL, Streamlit, Docker               |   |
|  |  |  - 5 KPIs, 4 charts, 5 filters                                |   |
|  |  +-----------------------------------------------------------------+   |
|  |  +-----------------------------------------------------------------+   |
|  |  |  Uber Data Pipeline                                              |   |
|  |  |  - Airflow orchestration, DuckDB warehouse                      |   |
|  |  |  - Star Schema: 4 dimension tables and 1 fact table            |   |
|  |  |  - 4 KPIs, 4 charts, 3 filters                                 |   |
|  |  +-----------------------------------------------------------------+   |
|  |  +-----------------------------------------------------------------+   |
|  |  |  Amazon Web Scraping                                             |   |
|  |  |  - Python, Requests, BeautifulSoup4                             |   |
|  |  |  - 5 data points per product, 95+ percent success rate         |   |
|  |  |  - 2 to 5 seconds per product                                  |   |
|  |  +-----------------------------------------------------------------+   |
|  |  +-----------------------------------------------------------------+   |
|  |  |  Daily Expense Tracker                                           |   |
|  |  |  - CLI with 12 menus and GUI with 6 tabs                       |   |
|  |  |  - SQLite: 5 tables, 5 indexes                                 |   |
|  |  |  - 277 test cases, 100 percent pass rate                      |   |
|  |  +-----------------------------------------------------------------+   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  CERTIFICATIONS (10)                                                |   |
|  |  Oracle (8) and IBM (1) and Meta (1)                               |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  ACHIEVEMENTS                                                       |   |
|  |  - Oracle Race to Certification: Top 108 Global (2025)              |   |
|  |  - Oracle Race to Certification: Top 3 Indonesia (2025)             |   |
|  |  - Best Teacher Award - Satu Benih Boarding School (2025)          |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  CONTACT                                                            |   |
|  |  - Email: arkantsabit025@gmail.com                                 |   |
|  |  - Phone: +62 81295709620                                          |   |
|  |  - GitHub: github.com/ArkanTsabit123                              |   |
|  |  - LinkedIn: linkedin.com/in/arkan-tsabit                         |   |
|  |  - Downloads: CV PDF, Job Application Letter PDF                  |   |
|  +---------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
                                     |
                                     v
+-----------------------------------------------------------------------------+
|                              FOOTER                                          |
|  +---------------------------------------------------------------------+   |
|  |  2026 Arkan Tsabit | Data Engineer Portfolio                       |   |
|  +---------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
                                     |
                                     v
+-----------------------------------------------------------------------------+
|                           CHATBOT WIDGET                                    |
|  +---------------------------------------------------------------------+   |
|  |  Chat with Arkan's AI                                                |   |
|  |                                                                     |   |
|  |  [Type your question...] [Send]                                   |   |
|  |                                                                     |   |
|  |  Ask about experience, projects, certifications, or skills        |   |
|  +---------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
```

---

## Technology Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Frontend | HTML5 | - | Structure |
| Styling | CSS3 | - | Styling |
| JavaScript | Vanilla JS | ES6 | Interactivity |
| Icons | Font Awesome | 6.4.0 | Icons |
| Font | Inter | Google Fonts | Typography |
| Hosting | GitHub Pages | - | Deployment |
| AI Chatbot | Cloudflare Workers | - | RAG question and answer |
| Vector Database | Cloudflare Vectorize | - | Knowledge storage |
| LLM | Cloudflare Workers AI | - | Response generation |

---

## Color Palette

### Light Mode

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | White | FFFFFF |
| Text | Black | 111827 |
| Primary | Blue | 2563EB |
| Secondary | Gray | 6B7280 |
| Accent | Green | 10B981 |
| Border | Light Gray | E5E7EB |

### Dark Mode

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Dark | 0F172A |
| Text | White | F8FAFC |
| Primary | Blue | 3B82F6 |
| Secondary | Gray | 9CA3AF |
| Accent | Green | 34D399 |
| Border | Dark Gray | 1E293B |

---

## File Structure

```
arkan-tsabit-portfolio/
|
+-- index.html
+-- about.html
+-- projects.html
+-- certifications.html
+-- achievements.html
+-- contact.html
+-- 404.html
|
+-- css/
|   +-- style.css
|   +-- dark-mode.css
|   +-- responsive.css
|   +-- chatbot.css
|
+-- js/
|   +-- main.js
|   +-- dark-mode.js
|   +-- i18n.js
|   +-- chatbot.js
|   +-- projects.js
|
+-- assets/
|   +-- images/
|   |   +-- profile.jpg
|   |   +-- logo.svg
|   |   +-- favicon.ico
|   |   +-- projects/
|   |   |   +-- batchetl/
|   |   |   |   +-- architecture.png
|   |   |   |   +-- dashboard.png
|   |   |   |   +-- erd.png
|   |   |   +-- uber/
|   |   |   |   +-- pipeline-flow.png
|   |   |   |   +-- star-schema.png
|   |   |   |   +-- dashboard.png
|   |   |   +-- amazon/
|   |   |   |   +-- scraping-result.png
|   |   |   |   +-- csv-output.png
|   |   |   +-- expense/
|   |   |       +-- gui-dashboard.png
|   |   |       +-- cli-summary.png
|   |   +-- certifications/
|   |       +-- oracle.png
|   |       +-- ibm.png
|   |       +-- meta.png
|   |
|   +-- icons/
|   |   +-- github.svg
|   |   +-- linkedin.svg
|   |   +-- email.svg
|   |   +-- download.svg
|   |   +-- chatbot.svg
|   |
|   +-- fonts/
|       +-- inter.woff2
|
+-- docs/
|   +-- CV/
|   |   +-- Arkan-Tsabit_Data-Engineer.pdf
|   +-- Job-Application/
|       +-- Arkan-Tsabit_Job-Application.pdf
|
+-- chatbot/
|   +-- worker.js
|   +-- wrangler.toml
|   +-- knowledge-base/
|       +-- cv-data.json
|       +-- projects-data.json
|       +-- certifications-data.json
|
+-- data/
|   +-- projects.json
|   +-- certifications.json
|   +-- achievements.json
|   +-- i18n/
|       +-- en.json
|       +-- id.json
|
+-- .gitignore
+-- README.md
+-- LICENSE
+-- blueprint.md
+-- CNAME
```

---

## Page Content Details

### 1. Landing Page

| Section | Content |
|---------|---------|
| Hero | Name, Title, Tagline, Metrics, Call-to-action buttons |
| Quick Stats | 2.96M+ records, under 30 seconds execution, 100 percent data quality |
| Featured Project | BatchETL Pipeline (highlighted) |
| Skills Overview | 4 technology categories with icons |
| Certifications Preview | 10 certifications with logos |
| Chatbot Call-to-action | Ask Arkan's AI button |

### 2. About Me

| Section | Content |
|---------|---------|
| Profile | Photo and professional summary |
| Story | Career transition from IT to Data Engineering |
| Skills | Technical skills with categories |
| Stats | Years of experience, projects, certifications |
| Tools | Technology stack with icons |

### 3. Projects

| Project | Description | Metrics | Stack |
|---------|-------------|---------|-------|
| BatchETL Pipeline | End-to-end ETL for NYC Taxi data | 2.96M rows, under 30 seconds, 100 percent quality | Airflow, PostgreSQL, Streamlit, Docker |
| Uber Data Pipeline | Star schema data warehouse | 4 dimension and 1 fact tables | Airflow, DuckDB, Streamlit, Docker |
| Amazon Web Scraping | Product data extraction | 5 fields per product, 95+ percent success | Python, BeautifulSoup, Requests, Pandas |
| Daily Expense Tracker | Full-stack expense application | 277 tests, 100 percent pass | Python, SQLite, Tkinter, Matplotlib |

### 4. Certifications

| Provider | Count | List |
|----------|-------|------|
| Oracle | 8 | OCI Multicloud Architect, Generative AI, AI Vector Search, Autonomous DB, Cloud DB Services, AI Foundations, Foundations, Data Platform |
| IBM | 1 | Data Engineering Professional Certificate |
| Meta | 1 | Database Engineer Professional Certificate |

### 5. Achievements

| Achievement | Year | Description |
|-------------|------|-------------|
| Top 108 Global | 2025 | Oracle Race to Certification - Global Leaderboard |
| Top 3 Indonesia | 2025 | Oracle Race to Certification - Indonesia Region |
| Best Teacher Award | 2025 | Satu Benih Boarding School |

### 6. Contact

| Method | Value |
|--------|-------|
| Email | arkantsabit025@gmail.com |
| Phone | +62 81295709620 |
| GitHub | github.com/ArkanTsabit123 |
| LinkedIn | linkedin.com/in/arkan-tsabit |
| Downloads | CV PDF, Job Application PDF |

---

## Multi-Language Implementation

### Language Support

| Code | Language |
|------|----------|
| en | English (US) |
| id | Indonesian |

### Translation Structure

```
// en.json
{
  "nav": {
    "home": "Home",
    "about": "About Me",
    "projects": "Projects",
    "certifications": "Certifications",
    "achievements": "Achievements",
    "contact": "Contact"
  },
  "hero": {
    "title": "Data Engineer | Cloud Data Engineer",
    "tagline": "Building production-ready data pipelines",
    "cta_projects": "View Projects",
    "cta_cv": "Download CV",
    "cta_contact": "Contact Me"
  }
}

// id.json
{
  "nav": {
    "home": "Beranda",
    "about": "Tentang Saya",
    "projects": "Proyek",
    "certifications": "Sertifikasi",
    "achievements": "Prestasi",
    "contact": "Kontak"
  },
  "hero": {
    "title": "Data Engineer | Cloud Data Engineer",
    "tagline": "Membangun pipeline data siap produksi",
    "cta_projects": "Lihat Proyek",
    "cta_cv": "Unduh CV",
    "cta_contact": "Hubungi Saya"
  }
}
```

---

## Dark and Light Mode Implementation

### CSS Variables

```
:root {
  --bg-primary: #FFFFFF;
  --bg-secondary: #F8FAFC;
  --text-primary: #111827;
  --text-secondary: #6B7280;
  --border-color: #E5E7EB;
  --accent-blue: #2563EB;
  --accent-green: #10B981;
}

[data-theme="dark"] {
  --bg-primary: #0F172A;
  --bg-secondary: #1E293B;
  --text-primary: #F8FAFC;
  --text-secondary: #9CA3AF;
  --border-color: #1E293B;
  --accent-blue: #3B82F6;
  --accent-green: #34D399;
}
```

### Toggle Logic

```
function toggleTheme() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  html.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}
```

---

## RAG Chatbot Implementation

### Architecture

```
+-----------------------------------------------------------------------------+
|                         CLOUDFLARE WORKERS                                   |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  1. User Question                                                  |   |
|  |     "What projects has Arkan built?"                               |   |
|  +---------------------------------------------------------------------+   |
|                                     |                                       |
|                                     v                                       |
|  +---------------------------------------------------------------------+   |
|  |  2. Vector Search (Cloudflare Vectorize)                           |   |
|  |     - Convert question to embedding                                |   |
|  |     - Search knowledge base for relevant documents                 |   |
|  +---------------------------------------------------------------------+   |
|                                     |                                       |
|                                     v                                       |
|  +---------------------------------------------------------------------+   |
|  |  3. Context Building                                               |   |
|  |     - Retrieve relevant text chunks from knowledge base            |   |
|  |     - Format as context for LLM                                    |   |
|  +---------------------------------------------------------------------+   |
|                                     |                                       |
|                                     v                                       |
|  +---------------------------------------------------------------------+   |
|  |  4. LLM Response (Cloudflare Workers AI)                           |   |
|  |     - Generate response based on context only                      |   |
|  |     - "Arkan has built 4 major projects: BatchETL Pipeline..."    |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Knowledge Base Structure

```
{
  "documents": [
    {
      "id": "cv_001",
      "content": "Arkan Tsabit is a Data Engineer with experience building production-ready ETL pipelines...",
      "metadata": {
        "source": "CV",
        "category": "professional_summary"
      }
    },
    {
      "id": "project_001",
      "content": "BatchETL Pipeline processes 2.96M NYC taxi records in under 30 seconds...",
      "metadata": {
        "source": "project",
        "name": "BatchETL Pipeline"
      }
    },
    {
      "id": "cert_001",
      "content": "Oracle Certified Multicloud Architect Professional - earned October 2025...",
      "metadata": {
        "source": "certification",
        "provider": "Oracle"
      }
    }
  ]
}
```

### Chatbot UI

```
<!-- Chatbot Widget -->
<div id="chatbot-widget">
  <div id="chatbot-header">
    <span>Chat with Arkan's AI</span>
    <button id="chatbot-toggle">Close</button>
  </div>
  <div id="chatbot-messages">
    <div class="message bot">
      Hello. Ask me about Arkan's experience, projects, certifications, or skills.
    </div>
  </div>
  <div id="chatbot-input">
    <input type="text" placeholder="Type your question..." id="chatbot-input-field">
    <button id="chatbot-send">Send</button>
  </div>
</div>
```

### Cloudflare Worker Template

```
// worker.js
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    if (url.pathname === '/api/chat') {
      const { question } = await request.json();
      
      const embedding = await env.AI.run('@cf/baai/bge-small-en-v1.5', {
        text: question
      });
      
      const vectorResults = await env.VECTORIZE.query(embedding, {
        topK: 5,
        returnValues: true
      });
      
      const context = vectorResults.matches
        .map(match => match.value)
        .join('\n\n');
      
      const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
        messages: [
          {
            role: 'system',
            content: 'You are Arkan\'s AI assistant. Answer questions based ONLY on the provided context. If the answer is not in the context, say "I do not have that information."'
          },
          {
            role: 'user',
            content: 'Context: ${context}\n\nQuestion: ${question}'
          }
        ]
      });
      
      return new Response(JSON.stringify({ response: response.response }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    return new Response('Not found', { status: 404 });
  }
}
```

---

## Deployment Guide

### Step 1: GitHub Pages Setup

```
# 1. Create repository
git init
git remote add origin https://github.com/ArkanTsabit123/arkan-tsabit.github.io.git

# 2. Push code
git add .
git commit -m "Initial portfolio website"
git push -u origin main

# 3. Enable GitHub Pages
# Settings -> Pages -> Branch: main -> /docs or / (root)
```

### Step 2: Cloudflare Workers Setup

```
# 1. Install Wrangler CLI
npm install -g wrangler

# 2. Login
wrangler login

# 3. Create Vectorize database
wrangler vectorize create arkan-knowledge-base

# 4. Deploy worker
wrangler deploy
```

### Step 3: Environment Variables

```
# .env for Cloudflare Workers
CLOUDFLARE_ACCOUNT_ID=your_account_id
CLOUDFLARE_API_TOKEN=your_api_token
VECTORIZE_INDEX_NAME=arkan-knowledge-base
AI_MODEL=@cf/meta/llama-3-8b-instruct
```

---

## Performance Optimization

| Technique | Implementation |
|-----------|----------------|
| Lazy Loading | Images load on scroll |
| Minification | CSS and JavaScript minified |
| CDN | Font Awesome and Google Fonts via CDN |
| Caching | Browser cache for static assets |
| Compression | Gzip and Brotli compression |
| Image Optimization | WebP format with responsive sizes |

---

## SEO Strategy

| Element | Implementation |
|---------|----------------|
| Title | Arkan Tsabit - Data Engineer Portfolio |
| Description | Data Engineer portfolio showcasing ETL pipelines, data warehousing, and cloud architecture projects. |
| Keywords | Data Engineer, ETL, Airflow, PostgreSQL, Python, Portfolio |
| Open Graph | Social media preview cards |
| Schema Markup | Person, Project, Certification JSON-LD |
| Sitemap | sitemap.xml for search engines |

---

## Accessibility

| Standard | Implementation |
|----------|----------------|
| ARIA Labels | All interactive elements |
| Keyboard Navigation | Full keyboard support |
| Color Contrast | WCAG AA compliant |
| Focus Indicators | Visible focus states |
| Alt Text | All images have alt text |
| Semantic HTML | Proper heading hierarchy |

---

## Analytics

| Tool | Purpose |
|------|---------|
| Google Analytics | Track visitors and behavior |
| Cloudflare Analytics | Worker performance monitoring |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| GitHub Pages not loading | Check branch settings and wait 5 minutes |
| Chatbot not responding | Check Cloudflare Worker logs |
| Dark mode not saving | Check localStorage permission |
| Images not loading | Verify file paths and extensions |
| Language toggle not working | Check i18n JSON files |

---

## Future Enhancements

| Enhancement | Priority | Complexity |
|-------------|----------|------------|
| Blog Section | Medium | Low |
| Video Demos | Medium | Low |
| Interactive Charts | Low | Medium |
| Newsletter Signup | Low | Low |
| Real-time Analytics Dashboard | Low | High |

---

## Quick Links

| Resource | URL |
|----------|-----|
| Website | https://arkan-tsabit.github.io |
| GitHub | https://github.com/ArkanTsabit123 |
| LinkedIn | https://linkedin.com/in/arkan-tsabit |
| Cloudflare Dashboard | https://dash.cloudflare.com |

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer