# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-05

### Added
- Initial release of portfolio website
- Landing page with hero section, metrics, and call-to-action buttons
- About page with professional summary, skills, and career timeline
- Projects page with 4 project cards and filtering functionality
- Certifications page displaying 10 certifications from Oracle, IBM, and Meta
- Achievements page showcasing Oracle Race and teaching awards
- Contact page with contact information and document downloads
- 404 error page with navigation
- Dark and light mode toggle with persistent preference
- Multi-language support (Indonesian and US English) with persistent preference
- RAG-powered AI chatbot using Cloudflare Workers
- Fully responsive design for all screen sizes

### Added - Assets
- Profile photo placeholder
- Project screenshots placeholders for all 4 projects
- Certification logos for Oracle, IBM, and Meta
- Technology icons (GitHub, LinkedIn, Email, Download, Chatbot)
- Inter font from Google Fonts

### Added - Documentation
- README.md with project overview and deployment guide
- blueprint.md with technical architecture and implementation details
- cheatsheet.md with quick reference commands
- checklist.md with completion checklist

### Added - Configuration
- CNAME file for custom domain configuration
- .gitignore for Python, IDE, and environment exclusions
- .env.example for environment variables template

### Added - Chatbot
- Cloudflare Worker with RAG implementation
- Knowledge base with CV, projects, and certifications data
- Wrangler configuration for Cloudflare deployment

### Technical
- Built with vanilla HTML5, CSS3, and JavaScript (ES6)
- Uses CSS custom properties for theming
- Implements Font Awesome for icons
- Uses Inter font from Google Fonts
- Deployed on GitHub Pages
- Backend powered by Cloudflare Workers

### Changed
- Updated all HTML files with complete content
- Updated all CSS files with dark mode and responsive design
- Updated all JavaScript files with full functionality
- Updated data JSON files with actual content
- Updated chatbot files with complete implementation

## [Unreleased]

### Planned
- Replace placeholder images with actual content
- Upload CV and Job Application PDFs
- Deploy Cloudflare Worker
- Add Google Analytics
- Implement custom domain
- Add blog section
- Add interactive charts
- Add video demos for projects