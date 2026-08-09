# CHANGELOG.md

## Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## Table of Contents

1. [Version 2.1.0 - 2026-08-09](#version-210---2026-08-09)
2. [Version 2.0.0 - 2026-08-08](#version-200---2026-08-08)
3. [Version 1.2.0 - 2026-08-06](#version-120---2026-08-06)
4. [Version 1.1.0 - 2026-08-05](#version-110---2026-08-05)
5. [Version 1.0.0 - 2026-07-25](#version-100---2026-07-25)
6. [LLM Models Tested](#llm-models-tested)
7. [Upcoming Features](#upcoming-features)

---

## Version 2.1.0 - 2026-08-09

### Added

**Domain Setup Phase**
- Cloudflare Registrar domain purchase (arkantsabit.com)
- DNS records configuration (A records to GitHub Pages IP)
- CNAME file configuration
- GitHub Pages custom domain setup
- HTTPS enforcement

**SEO Phase**
- Google Search Console registration and verification
- Sitemap.xml creation (6 pages)
- Robots.txt creation
- Meta tags optimization (title, description)
- Open Graph tags (og:title, og:description, og:url, og:image)
- Twitter Card tags (summary_large_image)
- JSON-LD structured data (Person schema)

**Content Optimization Phase**
- Keyword optimization (Arkan Tsabit, Data Engineer)
- Alt text for images
- Internal linking across all pages

**Backlink Strategy Phase**
- LinkedIn profile link update
- GitHub profile link update
- Medium profile link update
- Community posting strategy
- Article writing plan

**Monitoring and Analytics Phase**
- Google Analytics 4 setup
- Cloudflare Web Analytics setup
- Core Web Vitals monitoring
- Broken link checking

**Maintenance Phase**
- Domain renewal tracking
- Content update schedule
- URL submission process
- SSL certificate monitoring

**Documentation Restructuring**
- Created INDEX.md as central navigation for all documentation
- Created TECHNICAL.md (merged ARCHITECTURE.md + API.md + PERFORMANCE.md)
- Created OPERATIONS.md (merged MAINTENANCE.md + COSTS.md + SECURITY.md)
- Created GUIDE.md (merged USER-FLOW.md + CONTRIBUTING.md)
- Moved all documentation files to /docs/ directory
- Restructured README.md as concise overview with preview image
- Updated blueprint.md as comprehensive project documentation

### Changed

- **Documentation Structure**: Reorganized from 16 files to 9 files
  - Root: README.md only
  - /docs/: INDEX.md, blueprint.md, TECHNICAL.md, OPERATIONS.md, GUIDE.md, CHECKLIST.md, CHANGELOG.md, cheatsheets.md
- **README.md**: Simplified to concise overview with website preview image
- **blueprint.md**: Expanded to contain all comprehensive project documentation
- **CHANGELOG.md**: Updated version history

### Removed

- ARCHITECTURE.md (merged into TECHNICAL.md)
- API.md (merged into TECHNICAL.md)
- PERFORMANCE.md (merged into TECHNICAL.md)
- MAINTENANCE.md (merged into OPERATIONS.md)
- COSTS.md (merged into OPERATIONS.md)
- SECURITY.md (merged into OPERATIONS.md)
- USER-FLOW.md (merged into GUIDE.md)
- CONTRIBUTING.md (merged into GUIDE.md)
- PROJECT-FILES-INDEX.md (replaced by INDEX.md)

### Fixed

- Documentation inconsistency across multiple files
- Version numbers updated to 2.1.0
- Document information tables updated with new dates

### Pending

- Domain purchase on Cloudflare Registrar
- DNS records configuration
- GitHub Pages custom domain update
- Google Search Console registration and verification
- Sitemap.xml creation and upload
- Robots.txt creation and upload
- Meta tags update on all pages
- Open Graph tags update
- Twitter Card tags update
- JSON-LD structured data update
- Content optimization (keywords, alt text)
- Backlink strategy implementation
- Google Analytics setup
- Cloudflare Web Analytics setup
- CSS minification
- JavaScript minification
- Console log removal

---

## Version 2.0.0 - 2026-08-08

### Added

**Google Sheets Contact Form Integration**
- Apps Script backend with `doPost()` handler
- Web App deployment with Anyone access
- Form submission with Name, Email, Subject, Message, Date, Time fields
- Real-time data storage in Google Sheets
- Success/error feedback for users

**Environment Variables Support**
- CLOUDFLARE_ACCOUNT_ID for Cloudflare authentication
- CLOUDFLARE_API_TOKEN for API access
- VECTORIZE_INDEX_NAME for Vectorize index
- EMBEDDING_MODEL for embedding generation

**Technical Skills Section on About Page**
- 5 categories: Cloud & Data Architecture, Data Engineering, Databases, AI/ML, Visualization
- Skills matching CV and professional experience

**Working Experience Section on About Page**
- Reordered from newest to oldest (BRI SD-WAN → Satu Benih → Bejagoo → Airport)
- Bullet points format matching CV
- Detailed role descriptions

**Open Graph Tags**
- og:title, og:description, og:type, og:url, og:image

**Twitter Card Tags**
- twitter:card, twitter:title, twitter:description

**JSON-LD Structured Data**
- Person schema with name, jobTitle, url, email, sameAs
- knowsAbout with key skills

**New Assets**
- logo-2.ico as alternative logo
- logo.ico as primary logo
- Updated profile photo (2.2 MB)
- Updated favicon (30 KB)
- Updated Oracle, IBM, Meta certification logos
- Project screenshots for all 4 projects

### Changed

**Contact Page**
- Replaced downloads section with contact form
- Removed CV and Job Application PDF downloads
- Removed duplicate Social Section
- Added Google Sheets powered form
- Email link updated to Gmail compose (opens in new tab)

**About Page**
- Replaced "My Career Transition" with "Working Experience"
- Updated timeline order (newest to oldest)
- Added bullet points matching CV
- Added Technical Skills section

**Home Page**
- Removed "Download CV" button
- Removed "Open to Work" badge
- Updated call-to-action buttons

**Footer**
- Changed credit text to "Data Engineer | Cloud Data Engineer"
- Email link to Gmail compose (opens in new tab)

**Chatbot**
- Security and functionality improvements
- upload_vectors.py: Migrated to environment variables (.env)
- worker.js: Fixed context building from metadata.content
- test_all.py: Fixed validation logic (source == "llm")
- Removed hardcoded API keys from source code

**CSS**
- Added .contact-form styles
- Added .form-group styles
- Dark mode support for form inputs

**i18n Translations**
- en.json: Added contact form translations, updated footer
- id.json: Added contact form translations, updated footer

### Fixed

- Vectorize upload format issue (values field was missing)
- H1 detection in HTML validation
- DOCTYPE detection in HTML validation (case-insensitive regex)
- SystemExit errors in checker script
- Wrangler configuration path issues
- Context building from Vectorize metadata
- Email link behavior (now opens Gmail in new tab)

### Removed

- Download CV button from Home page
- "Open to Work" badge from Home page
- CV and Job Application PDF download links from Contact page
- Social Section from Contact page (duplicate)
- Hardcoded credentials from upload_vectors.py
- Duplicate .env from chatbot folder
- chatbot/.wrangler/ cache folder from repository

### Security

- Migrated all secrets to .env file (NOT committed)
- Added .env to .gitignore
- Removed all hardcoded credentials from source code
- Web App access set to "Anyone" for form submissions

---

## Version 1.2.0 - 2026-08-06

### Added

- Complete RAG chatbot implementation with Cloudflare Workers
- Knowledge base with 30 documents (profile, projects, certifications, achievements, experience, skills, contact)
- Vectorize index `arkan-knowledge-base` (384 dimensions, bge-small-en-v1.5)
- Embedding generation script `upload_vectors.py`
- JSON to NDJSON converter `convert-to-ndjson.js`
- Test suite `test_all.py` with 34 questions
- Health check endpoint `/health`
- Debug script for AI Chat `Chatbot RAG Debugger.py`
- CORS headers support
- Certification verification links for 10 certifications

### Changed

- `worker.js`: Full RAG logic (embedding, vector search, context, LLM)
- `chatbot.js`: Frontend API integration
- `index.html`: Hero section with new metrics (10, 1, 4, 4)
- `certifications.html`: Verify buttons with credential links
- `style.css`: Hero skills list and metric cards
- `certifications.json`: Verification links for 10 certifications
- `en.json`, `id.json`: Updated hero translations

### Fixed

- CORS headers for cross-origin requests
- Vector search context building
- Embedding dimension validation
- Worker deployment configuration

### Removed

- `test_high.py`, `test_medium.py`, `test_low.py`

---

## Version 1.1.0 - 2026-08-05

### Added

- Cloudflare Worker with Vectorize integration
- Vectorize index creation with preset model
- Knowledge base upload via NDJSON
- Worker deployment with Wrangler CLI
- API endpoint `/api/chat` for chatbot
- Embedding generation with Workers AI
- Vector search with topK results
- LLM integration for response generation

### Changed

- Updated `wrangler.toml` with Vectorize and AI bindings
- Enhanced `worker.js` with RAG pipeline
- Updated `wrangler.toml` compatibility date
- Modified worker deployment process

### Fixed

- Vectorize index binding configuration
- AI model selection and integration
- CORS handling in worker
- Error handling for API requests

---

## Version 1.0.0 - 2026-07-25

### Added

- Initial portfolio website structure
- HTML pages: index, about, projects, certifications, achievements, contact, 404
- CSS styles: main, dark mode, responsive, chatbot
- JavaScript modules: main, dark-mode, i18n, chatbot, projects
- JSON data: projects, certifications, achievements, i18n
- Assets: images, icons, fonts
- Documentation: README, blueprint, cheatsheet, checklist, changelog
- Configuration: gitignore, env.example, CNAME, LICENSE
- Multi-language support (EN/ID)
- Dark/light mode toggle
- Project filtering
- Responsive design
- Featured project section
- Skills overview
- Certifications preview
- Footer with social links
- Chatbot widget foundation

---

## LLM Models Tested

### Model Testing History (2026-08-06)

| No | Model ID | Status | Notes |
|----|----------|--------|-------|
| 1 | `@cf/meta/llama-4-scout-17b-16e-instruct` | 🔄 Testing | Pending evaluation |
| 2 | `@cf/meta/llama-3.2-3b-instruct` | 🔄 Testing | Pending evaluation |
| 3 | `@cf/meta/llama-3.1-8b-instruct-fp8` | 🔄 Testing | Pending evaluation |
| 4 | `@cf/meta/llama-3.2-1b-instruct` | 🔄 Testing | Pending evaluation |
| 5 | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | 🔄 Testing | Pending evaluation |
| 6 | `@cf/mistralai/mistral-small-3.1-24b-instruct` | 🔄 Testing | Pending evaluation |
| 7 | `@cf/mistral/mistral-7b-instruct-v0.2-lora` | ✅ Active | Currently in production |
| 8 | `@cf/qwen/qwen2.5-coder-32b-instruct` | 🔄 Testing | Pending evaluation |
| 9 | `@cf/qwen/qwen3-30b-a3b-fp8` | 🔄 Testing | Pending evaluation |
| 10 | `@cf/qwen/qwq-32b` | 🔄 Testing | Pending evaluation |
| 11 | `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | 🔄 Testing | Pending evaluation |
| 12 | `@cf/google/gemma-4-26b-a4b-it` | 🔄 Testing | Pending evaluation |
| 13 | `@cf/google/gemma-7b-it-lora` | 🔄 Testing | Pending evaluation |
| 14 | `@cf/aisingapore/gemma-sea-lion-v4-27b-it` | 🔄 Testing | Pending evaluation |
| 15 | `@cf/ibm-granite/granite-4.0-h-micro` | 🔄 Testing | Pending evaluation |
| 16 | `@cf/moonshotai/kimi-k2.6` | 🔄 Testing | Pending evaluation |
| 17 | `@cf/moonshotai/kimi-k2.7-code` | 🔄 Testing | Pending evaluation |
| 18 | `@cf/zai-org/glm-4.7-flash` | 🔄 Testing | Pending evaluation |
| 19 | `@cf/zai-org/glm-5.2` | 🔄 Testing | Pending evaluation |
| 20 | `@cf/nvidia/nemotron-3-120b-a12b` | 🔄 Testing | Pending evaluation |
| 21 | `@cf/openai/gpt-oss-20b` | 🔄 Testing | Pending evaluation |
| 22 | `@cf/openai/gpt-oss-120b` | 🔄 Testing | Pending evaluation |

---

## Upcoming Features

### Version 2.2.0 - Planned

- CSS and JavaScript minification
- Remove console logs for production
- Lighthouse performance optimization
- Additional LLM model testing
- Domain purchase and configuration
- Google Search Console verification
- SEO optimization implementation
- Google Analytics setup

### Version 3.0.0 - Future

- Blog section
- Video demos
- Interactive charts
- Newsletter signup
- Real-time analytics dashboard

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer