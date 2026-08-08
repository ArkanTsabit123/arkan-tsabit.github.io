# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-08-08

### Added
- Google Sheets integration for contact form
  - Apps Script backend with `doPost()` handler
  - Web App deployment with `Anyone` access
  - Form submission with `Name`, `Email`, `Subject`, `Message`, `Date`, `Time` fields
  - Real-time data storage in Google Sheets
  - Success/error feedback for users
- Environment variables support (`.env` file)
  - `CLOUDFLARE_ACCOUNT_ID` for Cloudflare authentication
  - `CLOUDFLARE_API_TOKEN` for API access
  - `VECTORIZE_INDEX_NAME` for Vectorize index
  - `EMBEDDING_MODEL` for embedding generation
- Technical Skills section on About page
  - 5 categories: Cloud & Data Architecture, Data Engineering, Databases, AI/ML, Visualization
  - Skills matching CV and professional experience
- Working Experience section on About page
  - Reordered from newest to oldest (BRI SD-WAN → Satu Benih → Bejagoo → Airport)
  - Bullet points format matching CV
  - Detailed role descriptions
- Open Graph tags for social media sharing
  - `og:title`, `og:description`, `og:type`, `og:url`, `og:image`
- Twitter Card tags for Twitter/X sharing
  - `twitter:card`, `twitter:title`, `twitter:description`
- JSON-LD structured data for SEO
  - Person schema with name, jobTitle, url, email, sameAs
  - knowsAbout with key skills
- New assets
  - `logo-2.ico` as alternative logo
  - `logo.ico` as primary logo
  - Updated profile photo (2.2 MB)
  - Updated favicon (30 KB)
  - Updated Oracle, IBM, Meta certification logos
  - Project screenshots for all 4 projects

### Changed
- **Contact Page**: Replaced downloads section with contact form
  - Removed CV and Job Application PDF downloads
  - Removed duplicate Social Section
  - Added Google Sheets powered form
  - Email link updated to Gmail compose (opens in new tab)
- **About Page**: Replaced "My Career Transition" with "Working Experience"
  - Updated timeline order (newest to oldest)
  - Added bullet points matching CV
  - Added Technical Skills section
- **Home Page**: Hero section improvements
  - Removed "Download CV" button
  - Removed "Open to Work" badge
  - Updated call-to-action buttons
- **Footer**: Professional updates
  - Changed credit text to "Data Engineer | Cloud Data Engineer"
  - Email link to Gmail compose (opens in new tab)
- **Documentation**: Updated all docs
  - `blueprint.md`: Added contact form integration, updated tech stack, new file structure
  - `cheatsheets.md`: Added Google Sheets and environment variables sections
  - `checklist.md`: Updated to 99% completion with 229/231 tasks done
- **Chatbot**: Security and functionality improvements
  - `upload_vectors.py`: Migrated to environment variables (`.env`)
  - `worker.js`: Fixed context building from metadata.content
  - `test_all.py`: Fixed validation logic (source == "llm")
  - Removed hardcoded API keys from source code
- **CSS**: Contact form styling
  - Added `.contact-form` styles
  - Added `.form-group` styles
  - Dark mode support for form inputs
- **i18n**: Translation updates
  - `en.json`: Added contact form translations, updated footer
  - `id.json`: Added contact form translations, updated footer

### Fixed
- Vectorize upload format issue (`values` field was missing)
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
- Hardcoded credentials from `upload_vectors.py`
- Duplicate `.env` from chatbot folder
- `chatbot/.wrangler/` cache folder from repository

### Security
- Migrated all secrets to `.env` file (NOT committed)
- Added `.env` to `.gitignore`
- Removed all hardcoded credentials from source code
- Web App access set to "Anyone" for form submissions

---

## [1.2.0] - 2026-08-06

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

## [1.1.0] - 2026-08-05

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

## [1.0.0] - 2026-07-25

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

## Model Testing History

### LLM Models Tested (2026-08-06)

| # | Model ID | Status | Notes |
|---|----------|--------|-------|
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

### [2.1.0] - Planned
- CSS and JavaScript minification
- Remove console logs for production
- Lighthouse performance optimization
- Additional LLM model testing

---

**Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer**