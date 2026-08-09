# BLUEPRINT.md

## Arkan Tsabit Portfolio - Complete Project Documentation

### Document Information

| Property | Value |
|----------|-------|
| Version | 2.1.0 |
| Last Updated | 2026-08-09 |
| Status | Production Ready |
| Domain | https://arkantsabit.com (Pending) |
| Hosting | GitHub Pages |
| AI Chatbot | Cloudflare Workers + RAG |

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Core Objectives](#core-objectives)
3. [Target Audience](#target-audience)
4. [Success Metrics](#success-metrics)
5. [System Architecture](#system-architecture)
6. [Technology Stack](#technology-stack)
7. [Website Structure](#website-structure)
8. [Color Palette](#color-palette)
9. [File Structure](#file-structure)
10. [Page Content Details](#page-content-details)
11. [Multi-Language Implementation](#multi-language-implementation)
12. [Dark and Light Mode Implementation](#dark-and-light-mode-implementation)
13. [RAG Chatbot Implementation](#rag-chatbot-implementation)
14. [Knowledge Base Structure](#knowledge-base-structure)
15. [Contact Form Integration](#contact-form-integration)
16. [Domain Setup](#domain-setup)
17. [SEO Implementation](#seo-implementation)
18. [Google Search Console Setup](#google-search-console-setup)
19. [Google Analytics Setup](#google-analytics-setup)
20. [Backlink Strategy](#backlink-strategy)
21. [Deployment Guide](#deployment-guide)
22. [Performance Optimization](#performance-optimization)
23. [Accessibility](#accessibility)
24. [Troubleshooting](#troubleshooting)
25. [Future Enhancements](#future-enhancements)

---

## Project Overview

This repository contains the source code for a professional portfolio website showcasing data engineering work. It serves as a comprehensive platform to display projects, certifications, professional experience, and achievements.

### Core Features

- 4 Data Engineering Projects with detailed descriptions and metrics
- 10 Professional Certifications from Oracle, IBM, and Meta
- Professional Experience and career transition story
- Achievements including Oracle Race to Certification (Top 108 Global, Top 3 Indonesia)
- AI-Powered Chatbot using RAG (Retrieval-Augmented Generation)
- Multi-Language Support (Indonesian and US English)
- Dark/Light Mode toggle for optimal viewing
- Contact Form with Google Sheets integration

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

## Core Objectives

1. Build a personal portfolio website to showcase data engineering projects.
2. Display 10 professional certifications from Oracle, IBM, and Meta.
3. Provide multi-language support (Indonesian and US English).
4. Implement an AI-powered chatbot using Cloudflare Workers with RAG.
5. Highlight achievements including Oracle Race to Certification (Top 108 Global, Top 3 Indonesia).
6. Support dark and light mode toggle.
7. Integrate contact form with Google Sheets.
8. Set up custom domain and SEO optimization for better visibility.

---

## Target Audience

- Recruiters and hiring managers.
- Technical interviewers.
- Data engineering peers.
- Potential clients.

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Page Load Time | Under 2 seconds |
| Theme Toggle | Functional dark/light mode |
| Language Switch | Instant toggle between ID and EN |
| Chatbot Response Time | Under 3 seconds |
| Mobile Responsiveness | 100 percent across all devices |
| SEO Score | 90+ on Google Lighthouse |
| Domain Active | arkantsabit.com |
| Google Indexing | All pages indexed |

---

## System Architecture

### Architecture Overview

```
+---------------------------------------------------------------------------------+
|                              USER BROWSER                                        |
|  +-----------------------------------------------------------------------------+|
|  |  arkantsabit.com (Custom Domain)                                            ||
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
|                                     |                                            |
|                                     v                                            |
|  +-----------------------------------------------------------------------------+|
|  |                         GOOGLE SHEETS                                        ||
|  |                                                                             ||
|  |  +-------------------------------------------------------------------------+||
|  |  |  Contact Form Storage                                                    |||
|  |  |  - Name, Email, Subject, Message, Date, Time                            |||
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
| Contact Form | Backend | Google Apps Script | Form submission storage |
| Domain | Registrar | Cloudflare Registrar | Custom domain management |
| Analytics | Monitoring | Google Analytics | Visitor tracking |

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
| Cloudflare Registrar | Domain registration (Pending) |

---

## Website Structure

### Page Architecture

```
+-----------------------------------------------------------------------------+
|                              HEADER                                          |
|  +---------------------------------------------------------------------+   |
|  |  [Logo]    [Home] [About] [Projects] [Certifications] [Contact]    |   |
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
|  |  - Metrics: 10 Professional Certifications, 1 Achievement,        |   |
|  |             4 Data Projects, 4 Work Experience                     |   |
|  |  - Buttons: View Projects, Contact Me                             |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  ABOUT ME                                                           |   |
|  |  - Profile photo                                                    |   |
|  |  - Professional summary                                             |   |
|  |  - Working Experience (newest to oldest)                           |   |
|  |  - Technical Skills with 5 categories                              |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
|  +---------------------------------------------------------------------+   |
|  |  PROJECTS (4)                                                       |   |
|  |  +-----------------------------------------------------------------+   |
|  |  |  BatchETL Pipeline                                              |   |
|  |  |  - 2.96M rows, under 30 seconds execution, 100% data quality   |   |
|  |  |  - Stack: Airflow, PostgreSQL, Streamlit, Docker               |   |
|  |  +-----------------------------------------------------------------+   |
|  |  +-----------------------------------------------------------------+   |
|  |  |  Uber Data Pipeline                                              |   |
|  |  |  - Airflow orchestration, DuckDB warehouse                      |   |
|  |  |  - Star Schema: 4 dimension tables and 1 fact table            |   |
|  |  +-----------------------------------------------------------------+   |
|  |  +-----------------------------------------------------------------+   |
|  |  |  Amazon Web Scraping                                             |   |
|  |  |  - Python, Requests, BeautifulSoup4                             |   |
|  |  |  - 5 data points per product, 95+ percent success rate         |   |
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
|  |  Oracle (8), IBM (1), Meta (1)                                     |   |
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
|  |  - Contact Form with Google Sheets integration                    |   |
|  +---------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
                                     |
                                     v
+-----------------------------------------------------------------------------+
|                              FOOTER                                          |
|  +---------------------------------------------------------------------+   |
|  |  Arkan Tsabit | Data Engineer | Cloud Data Engineer                |   |
|  +---------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
                                     |
                                     v
+-----------------------------------------------------------------------------+
|                           CHATBOT WIDGET                                    |
|  +---------------------------------------------------------------------+   |
|  |  Chat with Arkan's AI                                                |   |
|  |  [Type your question...] [Send]                                   |   |
|  |  Ask about experience, projects, certifications, or skills        |   |
|  +---------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
```

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
arkan-tsabit.github.io/
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
|   |   +-- logo.ico
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
|   +-- knowledge-upload.json
|   +-- upload_vectors.py
|   +-- test_all.py
|   +-- package.json
|
+-- data/
|   +-- projects.json
|   +-- certifications.json
|   +-- achievements.json
|   +-- i18n/
|       +-- en.json
|       +-- id.json
|
+-- .env
+-- .gitignore
+-- README.md
+-- LICENSE
+-- blueprint.md
+-- cheatsheets.md
+-- checklist.md
+-- CHANGELOG.md
+-- checker.py
+-- structure.py
+-- CNAME
+-- sitemap.xml (Pending)
+-- robots.txt (Pending)
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
| Working Experience | BRI SD-WAN -> Satu Benih -> Bejagoo -> Airport (newest to oldest) |
| Technical Skills | 5 categories: Cloud, Data Engineering, Databases, AI/ML, Visualization |
| Stats | Projects, certifications, records processed, industries |

### 3. Projects

| Project | Description | Metrics | Stack |
|---------|-------------|---------|-------|
| BatchETL Pipeline | End-to-end ETL for NYC Taxi data | 2.96M rows, under 30 seconds, 100% quality | Airflow, PostgreSQL, Streamlit, Docker |
| Uber Data Pipeline | Star schema data warehouse | 4 dimension and 1 fact tables | Airflow, DuckDB, Streamlit, Docker |
| Amazon Web Scraping | Product data extraction | 5 fields per product, 95%+ success | Python, BeautifulSoup, Requests, Pandas |
| Daily Expense Tracker | Full-stack expense application | 277 tests, 100% pass | Python, SQLite, Tkinter, Matplotlib |

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
| Contact Form | Google Sheets integration (Name, Email, Subject, Message, Date, Time) |

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
  },
  "featured": {
    "title": "Featured Project",
    "subtitle": "My most comprehensive data engineering work",
    "description": "End-to-end ETL pipeline for NYC Taxi trip data with automated orchestration, data quality validation, and real-time analytics dashboard.",
    "cta": "View All Projects"
  },
  "skills": {
    "title": "Technical Skills",
    "subtitle": "Technologies and tools I work with",
    "cloud": "Cloud & Data Architecture",
    "engineering": "Data Engineering",
    "databases": "Databases",
    "visualization": "Visualization & Tools"
  },
  "certs": {
    "title": "Certifications",
    "subtitle": "10 professional certifications from industry leaders",
    "oracle_desc": "8 professional certifications in cloud architecture, AI, and database services",
    "ibm_desc": "Professional certificate in data engineering",
    "meta_desc": "Professional certificate in database engineering",
    "cta": "View All Certifications"
  },
  "chatbot": {
    "title": "Ask Arkan's AI",
    "description": "Have questions about my experience, projects, or skills? Chat with my AI assistant to learn more.",
    "cta": "Open Chat"
  },
  "footer": {
    "credit": "Data Engineer | Cloud Data Engineer"
  },
  "about": {
    "page_title": "About Me",
    "page_subtitle": "Get to know the person behind the data",
    "who_am_i": "Who I Am",
    "bio_1": "I am a Data Engineer with hands-on experience building production-ready ETL pipelines that process 2.96M+ records in under 30 seconds with 100% data quality. I specialize in data warehousing, dimensional modeling, and data integration.",
    "bio_2": "I transitioned from IT infrastructure and network engineering to data engineering through intensive self-study and hands-on projects. My background in IT operations gives me a unique perspective on system reliability and data pipeline performance.",
    "bio_3": "I am certified as an Oracle Multicloud Architect, IBM Data Engineer, and Meta Database Engineer. I am passionate about building scalable and reliable data solutions that turn raw data into actionable insights.",
    "stats": {
      "projects": "Data Projects",
      "certs": "Certifications",
      "rows": "Records Processed",
      "domains": "Industries"
    },
    "work_title": "Working Experience",
    "work_subtitle": "From IT infrastructure to data engineering",
    "skills_title": "Technical Skills",
    "skills_subtitle": "Technologies and tools I work with"
  },
  "projects": {
    "page_title": "Projects",
    "page_subtitle": "End-to-end data engineering projects built with industry-standard tools",
    "filter": {
      "all": "All",
      "airflow": "Airflow",
      "postgresql": "PostgreSQL",
      "python": "Python",
      "docker": "Docker",
      "streamlit": "Streamlit"
    }
  },
  "achievements": {
    "page_title": "Achievements",
    "page_subtitle": "Recognition and awards from my professional journey"
  },
  "contact": {
    "page_title": "Contact",
    "page_subtitle": "Get in touch for opportunities and collaborations",
    "connect_title": "Let's Connect",
    "connect_desc": "I am always open to new opportunities, collaborations, and conversations about data engineering, cloud architecture, and data-driven solutions.",
    "form_title": "Send Me a Message",
    "form_desc": "I'll get back to you as soon as possible.",
    "form_name": "Your Name",
    "form_email": "Your Email",
    "form_subject": "Subject",
    "form_message": "Message",
    "form_send": "Send Message"
  },
  "error": {
    "title": "Page Not Found",
    "description": "The page you are looking for does not exist or has been moved.",
    "cta": "Return Home"
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
  },
  "featured": {
    "title": "Proyek Unggulan",
    "subtitle": "Pekerjaan data engineering paling komprehensif saya",
    "description": "Pipeline ETL end-to-end untuk data perjalanan NYC Taxi dengan otomatisasi, validasi kualitas data, dan dashboard analitik real-time.",
    "cta": "Lihat Semua Proyek"
  },
  "skills": {
    "title": "Keterampilan Teknis",
    "subtitle": "Teknologi dan alat yang saya gunakan",
    "cloud": "Cloud & Arsitektur Data",
    "engineering": "Data Engineering",
    "databases": "Database",
    "visualization": "Visualisasi & Alat"
  },
  "certs": {
    "title": "Sertifikasi",
    "subtitle": "10 sertifikasi profesional dari pemimpin industri",
    "oracle_desc": "8 sertifikasi profesional di arsitektur cloud, AI, dan layanan database",
    "ibm_desc": "Sertifikat profesional di data engineering",
    "meta_desc": "Sertifikat profesional di database engineering",
    "cta": "Lihat Semua Sertifikasi"
  },
  "chatbot": {
    "title": "Tanya AI Arkan",
    "description": "Ada pertanyaan tentang pengalaman, proyek, atau keterampilan saya? Ngobrol dengan asisten AI saya untuk belajar lebih lanjut.",
    "cta": "Buka Chat"
  },
  "footer": {
    "credit": "Data Engineer | Cloud Data Engineer"
  },
  "about": {
    "page_title": "Tentang Saya",
    "page_subtitle": "Kenali orang di balik data",
    "who_am_i": "Siapa Saya",
    "bio_1": "Saya adalah Data Engineer dengan pengalaman membangun pipeline ETL produksi yang memproses 2.96M+ rekaman dalam waktu kurang dari 30 detik dengan kualitas data 100%. Saya berspesialisasi dalam pergudangan data, pemodelan dimensional, dan integrasi data.",
    "bio_2": "Saya beralih dari infrastruktur IT dan rekayasa jaringan ke data engineering melalui belajar mandiri dan proyek langsung. Latar belakang saya di operasi IT memberi saya perspektif unik tentang keandalan sistem dan kinerja pipeline data.",
    "bio_3": "Saya tersertifikasi sebagai Oracle Multicloud Architect, IBM Data Engineer, dan Meta Database Engineer. Saya bersemangat membangun solusi data yang skalabel dan andal yang mengubah data mentah menjadi wawasan yang dapat ditindaklanjuti.",
    "stats": {
      "projects": "Proyek Data",
      "certs": "Sertifikasi",
      "rows": "Rekaman Diproses",
      "domains": "Industri"
    },
    "work_title": "Pengalaman Kerja",
    "work_subtitle": "Dari infrastruktur IT ke data engineering",
    "skills_title": "Keterampilan Teknis",
    "skills_subtitle": "Teknologi dan alat yang saya gunakan"
  },
  "projects": {
    "page_title": "Proyek",
    "page_subtitle": "Proyek data engineering end-to-end yang dibangun dengan alat standar industri",
    "filter": {
      "all": "Semua",
      "airflow": "Airflow",
      "postgresql": "PostgreSQL",
      "python": "Python",
      "docker": "Docker",
      "streamlit": "Streamlit"
    }
  },
  "achievements": {
    "page_title": "Prestasi",
    "page_subtitle": "Pengakuan dan penghargaan dari perjalanan profesional saya"
  },
  "contact": {
    "page_title": "Kontak",
    "page_subtitle": "Hubungi saya untuk peluang dan kolaborasi",
    "connect_title": "Mari Terhubung",
    "connect_desc": "Saya selalu terbuka untuk peluang baru, kolaborasi, dan diskusi tentang data engineering, arsitektur cloud, dan solusi berbasis data.",
    "form_title": "Kirim Pesan",
    "form_desc": "Saya akan merespon sesegera mungkin.",
    "form_name": "Nama Anda",
    "form_email": "Email Anda",
    "form_subject": "Subjek",
    "form_message": "Pesan",
    "form_send": "Kirim Pesan"
  },
  "error": {
    "title": "Halaman Tidak Ditemukan",
    "description": "Halaman yang Anda cari tidak ada atau telah dipindahkan.",
    "cta": "Kembali ke Beranda"
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
|  |     - Join content as context                                      |   |
|  +---------------------------------------------------------------------+   |
|                                     |                                       |
|                                     v                                       |
|  +---------------------------------------------------------------------+   |
|  |  5. LLM Response (Cloudflare Workers AI)                           |   |
|  |     - Generate response based on context only                      |   |
|  |     - Model: Mistral 7B v0.2                                      |   |
|  +---------------------------------------------------------------------+   |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Knowledge Base Structure

The knowledge base contains 30 documents organized by 7 categories:

| Category | Documents |
|----------|-----------|
| Profile | 3 |
| Projects | 4 |
| Certifications | 11 |
| Achievements | 3 |
| Experience | 5 |
| Skills | 3 |
| Contact | 1 |
| **Total** | **30** |

---

## Contact Form Integration

### Google Sheets Setup

**Headers:**
| Name | Email | Subject | Message | Date | Time |

**Apps Script Endpoint:**
- Web App URL: `https://script.google.com/macros/s/.../exec`
- Access: Anyone
- Method: POST

### Google Apps Script Code

```
const sheetName = 'Sheet1';

function doPost(e) {
  try {
    const doc = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = doc.getSheetByName(sheetName);
    
    if (!sheet) {
      const newSheet = doc.insertSheet(sheetName);
      const headers = ['Name', 'Email', 'Subject', 'Message', 'Date', 'Time'];
      newSheet.getRange(1, 1, 1, headers.length).setValues([headers]);
    }
    
    const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    const nextRow = sheet.getLastRow() + 1;
    
    const now = new Date();
    const newRow = headers.map((header) => {
      if (header === 'Date') {
        return Utilities.formatDate(now, Session.getScriptTimeZone(), "yyyy-MM-dd");
      }
      if (header === 'Time') {
        return Utilities.formatDate(now, Session.getScriptTimeZone(), "HH:mm:ss");
      }
      return e.parameter[header] || '';
    });
    
    sheet.getRange(nextRow, 1, 1, newRow.length).setValues([newRow]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'success', row: nextRow }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'error', error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

---

## Domain Setup

### Cloudflare Registrar Setup

1. **Buy Domain**: Purchase `arkantsabit.com` on Cloudflare Registrar (~$10.44/year)
2. **DNS Records**: Configure A record pointing to GitHub Pages IP
3. **CNAME File**: Create CNAME file with `arkantsabit.com`
4. **GitHub Pages**: Update custom domain in Settings → Pages
5. **HTTPS**: Enforce HTTPS in GitHub Pages settings

### DNS Configuration

| Record Type | Name | Value | TTL |
|-------------|------|-------|-----|
| A | @ | 185.199.108.153 | Auto |
| A | @ | 185.199.109.153 | Auto |
| A | @ | 185.199.110.153 | Auto |
| A | @ | 185.199.111.153 | Auto |
| CNAME | www | arkan-tsabit.github.io | Auto |

---

## SEO Implementation

### Meta Tags

| Tag | Content |
|-----|---------|
| Title | Arkan Tsabit - Data Engineer Portfolio |
| Description | Data Engineer portfolio showcasing ETL pipelines, data warehousing, and cloud architecture projects. Certified Oracle Multicloud Architect, IBM Data Engineer, and Meta Database Engineer. |
| Keywords | Data Engineer, ETL Pipeline, Data Warehouse, Cloud Architecture, Oracle, IBM, Meta |

### Open Graph Tags

```html
<meta property="og:title" content="Arkan Tsabit - Data Engineer Portfolio" />
<meta property="og:description" content="Data Engineer portfolio showcasing ETL pipelines, data warehousing, and cloud architecture projects." />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://arkantsabit.com" />
<meta property="og:image" content="https://arkantsabit.com/assets/images/profile.jpg" />
```

### Twitter Card Tags

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Arkan Tsabit - Data Engineer Portfolio" />
<meta name="twitter:description" content="Data Engineer portfolio showcasing ETL pipelines, data warehousing, and cloud architecture projects." />
<meta name="twitter:image" content="https://arkantsabit.com/assets/images/profile.jpg" />
```

### JSON-LD Structured Data

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Arkan Tsabit",
  "jobTitle": "Data Engineer",
  "url": "https://arkantsabit.com",
  "email": "arkantsabit025@gmail.com",
  "sameAs": [
    "https://github.com/ArkanTsabit123",
    "https://www.linkedin.com/in/arkan-tsabit-0b12b9407/"
  ],
  "knowsAbout": [
    "Data Engineering",
    "ETL Pipelines",
    "Data Warehousing",
    "Cloud Architecture",
    "SQL",
    "Python"
  ]
}
</script>
```

### Sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://arkantsabit.com/</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://arkantsabit.com/about.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://arkantsabit.com/projects.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://arkantsabit.com/certifications.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://arkantsabit.com/achievements.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://arkantsabit.com/contact.html</loc>
    <lastmod>2026-08-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

### Robots.txt

```
User-agent: *
Allow: /
Sitemap: https://arkantsabit.com/sitemap.xml
```

---

## Google Search Console Setup

### Steps

1. **Register**: Go to https://search.google.com/search-console
2. **Add Property**: Domain → `arkantsabit.com`
3. **Verify Domain**: Add TXT record in Cloudflare DNS
4. **Submit Sitemap**: Sitemaps → Add → `sitemap.xml`
5. **Request Indexing**: URL Inspection → Request Indexing for each page

### Pages to Index

1. Homepage: `https://arkantsabit.com/`
2. About: `https://arkantsabit.com/about.html`
3. Projects: `https://arkantsabit.com/projects.html`
4. Certifications: `https://arkantsabit.com/certifications.html`
5. Achievements: `https://arkantsabit.com/achievements.html`
6. Contact: `https://arkantsabit.com/contact.html`

---

## Google Analytics Setup

### GA4 Configuration

1. **Create Account**: https://analytics.google.com
2. **Create Property**: GA4 property for `arkantsabit.com`
3. **Get Measurement ID**: G-XXXXXXXXXX
4. **Add Tracking Code** to all pages:

```javascript
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Events to Track

| Event | Trigger |
|-------|---------|
| Page View | Every page load |
| Theme Toggle | Click on dark/light mode button |
| Language Switch | Click on EN/ID button |
| Chatbot Open | Click on chatbot icon |
| Chatbot Message | Send message in chatbot |
| Contact Form Submit | Submit contact form |
| Project Click | Click on project card |
| Certification Verify | Click on verify button |

---

## Backlink Strategy

### Platforms to Update

| Platform | Action |
|----------|--------|
| LinkedIn | Add `arkantsabit.com` to profile |
| GitHub | Add `arkantsabit.com` to bio |
| Medium | Add `arkantsabit.com` to profile |
| Dev.to | Add `arkantsabit.com` to profile |
| Reddit | Share projects with link |
| Kaskus | Discuss data engineering with link |

### Content Strategy

1. Write articles on Medium about data engineering projects
2. Create tutorials on ETL pipelines and data warehousing
3. Share project demos on YouTube
4. Post on LinkedIn about certifications and achievements
5. Participate in data engineering communities

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
python upload_vectors.py

# 5. Deploy worker
wrangler deploy
```

### Step 3: Environment Variables

Create `.env` file:
```
CLOUDFLARE_ACCOUNT_ID=1ac4476c492b63bf4eeb0fb1523aab34
CLOUDFLARE_API_TOKEN=your_api_token_here
VECTORIZE_INDEX_NAME=arkan-knowledge-base
EMBEDDING_MODEL=@cf/baai/bge-small-en-v1.5
```

---

## Performance Optimization

| Technique | Implementation |
|-----------|----------------|
| Lazy Loading | Images load on scroll |
| Minification | CSS and JavaScript minified (Pending) |
| CDN | Font Awesome and Google Fonts via CDN |
| Caching | Browser cache for static assets |
| Compression | Gzip and Brotli compression |
| Image Optimization | WebP format with responsive sizes |
| Vector Search | Top K limited to 5 matches |
| LLM Tokens | Limited to 250 tokens for faster response |

### Lighthouse Targets

| Metric | Target |
|--------|--------|
| Performance | 90+ |
| Accessibility | 95+ |
| Best Practices | 95+ |
| SEO | 100 |

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
| Contact form not working | Check Google Apps Script deployment and permissions |
| Domain not resolving | Check DNS records and Cloudflare configuration |
| SEO not indexed | Check robots.txt and sitemap.xml |

---

## Future Enhancements

| Enhancement | Priority | Complexity |
|-------------|----------|------------|
| Blog Section | Medium | Low |
| Video Demos | Medium | Low |
| Interactive Charts | Low | Medium |
| Newsletter Signup | Low | Low |
| Real-time Analytics Dashboard | Low | High |
| Custom Domain | High | Low (Pending) |
| SEO Optimization | High | Medium (Pending) |
| CSS/JS Minification | High | Low (Pending) |

---

## Quick Links

| Resource | URL |
|----------|-----|
| Website | https://arkantsabit123.github.io/arkan-tsabit.github.io/ |
| Domain | https://arkantsabit.com (Pending) |
| GitHub | https://github.com/ArkanTsabit123 |
| LinkedIn | https://www.linkedin.com/in/arkan-tsabit-0b12b9407/ |
| Worker | https://arkan-chatbot.arkan-chatbot.workers.dev |
| Health Check | https://arkan-chatbot.arkan-chatbot.workers.dev/health |
| Cloudflare Dashboard | https://dash.cloudflare.com |
| Google Sheets | https://docs.google.com/spreadsheets/d/1zcck8oaWyw5aWOpNl4JqstaLFYhjMvh_aNvrr0adqAg/edit |
| Google Search Console | https://search.google.com/search-console |
| Google Analytics | https://analytics.google.com |

---

## Domain & SEO Setup Checklist

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 1: Domain & Hosting Setup | Pending | 0% |
| Phase 2: Google Search Console Setup | Pending | 0% |
| Phase 3: SEO On-Page Optimization | Pending | 0% |
| Phase 4: Sitemap & Robots.txt | Pending | 0% |
| Phase 5: Content Optimization | Pending | 0% |
| Phase 6: Backlink Strategy | Pending | 0% |
| Phase 7: Monitoring & Analytics | Pending | 0% |
| Phase 8: Maintenance | Pending | 0% |

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer