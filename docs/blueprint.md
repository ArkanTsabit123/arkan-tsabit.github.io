# ARKAN TSABIT - PORTFOLIO WEBSITE BLUEPRINT

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0.0 |
| Last Updated | 2026-08-06 |
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
|  |  - Metrics: 10 Professional Certifications, 1 Achievement,        |   |
|  |             4 Data Projects, 4 Work Experience                     |   |
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
|  |  - Each certification has a "Verify" button linking to official   |   |
|  |    credential page                                                  |   |
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
| Hero | Name, Title, Tagline, Metrics (10, 1, 4, 4), Call-to-action buttons |
| Skills List | Orchestration: Airflow, Data Warehousing: PostgreSQL, DuckDB, Programming: Python, Pandas, SQL, Containerization: Docker Compose, Visualization: Streamlit, Plotly, Matplotlib |
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
    "badge": "Open to Work",
    "greeting": "Hello, I'm",
    "title": "Data Engineer | Cloud Data Engineer",
    "tagline": "Hi, I'm Arkan — Data Engineer with expertise in ETL pipelines, data warehousing, and cloud architecture. Certified Oracle Multicloud Architect, IBM Data Engineer, and Meta Database Engineer.",
    "subtagline": "I am also proficient in modern data engineering tools and technologies, including:",
    "metrics": {
      "certs": "Professional Certifications",
      "achievement": "Achievement",
      "projects": "Data Projects",
      "experience": "Work Experience"
    },
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
    "badge": "Terbuka untuk Kerja",
    "greeting": "Halo, Saya",
    "title": "Data Engineer | Cloud Data Engineer",
    "tagline": "Halo, saya Arkan — Data Engineer dengan keahlian di pipeline ETL, pergudangan data, dan arsitektur cloud. Tersertifikasi Oracle Multicloud Architect, IBM Data Engineer, dan Meta Database Engineer.",
    "subtagline": "Saya juga mahir dalam berbagai alat dan teknologi data engineering modern, di antaranya:",
    "metrics": {
      "certs": "Sertifikasi Profesional",
      "achievement": "Prestasi",
      "projects": "Proyek Data",
      "experience": "Pengalaman Kerja"
    },
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
|  |  2. Generate Embedding (bge-small-en-v1.5)                         |   |
|  |     - Convert question to vector (384 dimensions)                  |   |
|  +---------------------------------------------------------------------+   |
|                                     |                                       |
|                                     v                                       |
|  +---------------------------------------------------------------------+   |
|  |  3. Vector Search (Cloudflare Vectorize)                           |   |
|  |     - Search knowledge base for relevant documents                 |   |
|  |     - Top K: 5 matches with metadata                               |   |
|  +---------------------------------------------------------------------+   |
|                                     |                                       |
|                                     v                                       |
|  +---------------------------------------------------------------------+   |
|  |  4. Context Building                                               |   |
|  |     - Extract content from metadata                                |   |
|  |     - Filter scores > 0.3                                          |   |
|  |     - Join content as context                                      |   |
|  +---------------------------------------------------------------------+   |
|                                     |                                       |
|                                     v                                       |
|  +---------------------------------------------------------------------+   |
|  |  5. LLM Response (Cloudflare Workers AI)                           |   |
|  |     - Generate response based on context only                      |   |
|  |     - Model: Mistral 7B v0.2 (testing better models)              |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Knowledge Base Structure

The knowledge base contains 30 documents organized by category:

```
{
  "documents": [
    {
      "id": "profile_001",
      "content": "Arkan Tsabit is a Data Engineer with expertise...",
      "metadata": {
        "category": "profile",
        "keywords": "profile, introduction, data engineer",
        "content": "Arkan Tsabit is a Data Engineer..."
      }
    },
    {
      "id": "project_batchetl",
      "content": "BatchETL Pipeline is a data engineering project...",
      "metadata": {
        "category": "projects",
        "name": "BatchETL Pipeline",
        "keywords": "BatchETL, NYC Taxi, Airflow",
        "content": "BatchETL Pipeline processes 2.96M rows..."
      }
    },
    {
      "id": "cert_oracle_001",
      "content": "Oracle Multicloud Architect Professional...",
      "metadata": {
        "category": "certifications",
        "provider": "Oracle",
        "keywords": "Oracle, Multicloud Architect",
        "content": "Oracle Multicloud Architect Professional..."
      }
    }
  ]
}
```

### Chatbot UI

The chatbot widget appears as a floating button on all pages.

```
<!-- Chatbot Widget -->
<div id="chatbot-widget">
  <div id="chatbot-header">
    <span>AI Assistant</span>
    <button id="chatbotClose">✕</button>
  </div>
  <div id="chatbotMessages">
    <div class="message bot">
      Hello! Ask me about Arkan's experience, projects, certifications, or skills.
    </div>
  </div>
  <div id="chatbot-input-area">
    <input type="text" id="chatbotInput" placeholder="Type your question...">
    <button id="chatbotSend">Send</button>
  </div>
</div>
```

### Cloudflare Worker (worker.js)

```javascript
export default {
  async fetch(request, env, ctx) {
    // CORS handling
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type',
        },
      });
    }

    const url = new URL(request.url);

    // Health check
    if (url.pathname === '/health') {
      return new Response(JSON.stringify({
        status: 'healthy',
        service: 'arkan-chatbot',
        version: '2.0.0',
        timestamp: new Date().toISOString(),
      }), {
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
      });
    }

    // Chat endpoint
    if (url.pathname === '/api/chat' && request.method === 'POST') {
      const body = await request.json();
      const question = body.question;

      // Generate embedding
      const embeddingResponse = await env.AI.run('@cf/baai/bge-small-en-v1.5', {
        text: question.trim(),
      });
      const embedding = embeddingResponse.data[0];

      // Query Vectorize
      const vectorResults = await env.VECTORIZE.query(embedding, {
        topK: 5,
        returnValues: false,
        returnMetadata: true,
      });

      // Build context
      let context = '';
      if (vectorResults.matches && vectorResults.matches.length > 0) {
        const contents = vectorResults.matches
          .map(match => match.metadata?.content || '')
          .filter(content => content);
        context = contents.join('\n\n');
      }

      if (!context) {
        return new Response(JSON.stringify({
          response: "I don't have specific information about that topic. Please ask about Arkan's experience, projects, certifications, or skills.",
          source: 'default',
        }), {
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
          },
        });
      }

      // Generate response using LLM
      const llmResponse = await env.AI.run('@cf/mistral/mistral-7b-instruct-v0.2-lora', {
        messages: [
          {
            role: 'system',
            content: 'You are a helpful assistant. Answer based ONLY on the context given. Be concise.',
          },
          {
            role: 'user',
            content: `Answer based ONLY on this context: ${context}\n\nQuestion: ${question}\n\nAnswer:`,
          },
        ],
        temperature: 0.2,
        max_tokens: 150,
      });

      return new Response(JSON.stringify({
        response: llmResponse.response || 'No response from LLM.',
        source: 'llm',
      }), {
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
      });
    }

    return new Response(JSON.stringify({
      error: 'Not found',
      message: 'The requested endpoint does not exist.',
    }), {
      status: 404,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });
  },
};
```

### Cloudflare Worker Configuration (wrangler.toml)

```toml
name = "arkan-chatbot"
main = "worker.js"
compatibility_date = "2025-08-01"

[vars]
ENVIRONMENT = "production"

[[vectorize]]
binding = "VECTORIZE"
index_name = "arkan-knowledge-base"

[ai]
binding = "AI"

[observability]
enabled = true

[[env.production]]
route = "arkan-chatbot.workers.dev"
```

---

## LLM Testing Summary

The following 22 LLM models are being tested for compatibility with Cloudflare Workers AI:

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
# Settings -> Pages -> Branch: main -> / (root)
```

### Step 2: Cloudflare Workers Setup

```
# 1. Install Wrangler CLI
npm install -g wrangler

# 2. Login
wrangler login

# 3. Create Vectorize index
wrangler vectorize create arkan-knowledge-base --preset @cf/baai/bge-small-en-v1.5

# 4. Upload knowledge base
node convert-to-ndjson.js
wrangler vectorize insert arkan-knowledge-base --file knowledge-upload.ndjson

# 5. Deploy worker
wrangler deploy
```

### Step 3: Environment Variables

```
# .env for Cloudflare Workers
CLOUDFLARE_ACCOUNT_ID=1ac4476c492b63bf4eeb0fb1523aab34
CLOUDFLARE_API_TOKEN=your_api_token_here
VECTORIZE_INDEX_NAME=arkan-knowledge-base
AI_MODEL=@cf/baai/bge-small-en-v1.5
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
| Vector Search | Top K limited to 5 matches |
| LLM Tokens | Limited to 150 tokens for faster response |

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
| Chatbot not responding | Check Cloudflare Worker logs (`wrangler tail`) |
| Dark mode not saving | Check localStorage permission |
| Images not loading | Verify file paths and extensions |
| Language toggle not working | Check i18n JSON files |
| LLM model deprecated | Update model in `worker.js` |
| Vectorize index empty | Check `stored_vectors` in dashboard |

---

## Future Enhancements

| Enhancement | Priority | Complexity |
|-------------|----------|------------|
| Blog Section | Medium | Low |
| Video Demos | Medium | Low |
| Interactive Charts | Low | Medium |
| Newsletter Signup | Low | Low |
| Real-time Analytics Dashboard | Low | High |
| Custom Domain | Medium | Low |

---

## Quick Links

| Resource | URL |
|----------|-----|
| Website | https://arkan-tsabit.github.io |
| GitHub | https://github.com/ArkanTsabit123 |
| LinkedIn | https://linkedin.com/in/arkan-tsabit |
| Worker | https://arkan-chatbot.arkan-chatbot.workers.dev |
| Health Check | https://arkan-chatbot.arkan-chatbot.workers.dev/health |
| Cloudflare Dashboard | https://dash.cloudflare.com |

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer