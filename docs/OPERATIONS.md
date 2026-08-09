# OPERATIONS.md

## Operational Documentation - Maintenance, Costs, and Security

### Document Information

| Property | Value |
|----------|-------|
| Version | 1.0.0 |
| Last Updated | 2026-08-09 |
| Status | Production Ready |
| Domain | arkan-tsabit.github.io |
| Hosting | GitHub Pages |

---

## Table of Contents

1. [Maintenance Overview](#maintenance-overview)
2. [Maintenance Schedule](#maintenance-schedule)
3. [Daily Maintenance](#daily-maintenance)
4. [Weekly Maintenance](#weekly-maintenance)
5. [Monthly Maintenance](#monthly-maintenance)
6. [Quarterly Maintenance](#quarterly-maintenance)
7. [Annual Maintenance](#annual-maintenance)
8. [Emergency Maintenance](#emergency-maintenance)
9. [Backup Strategy](#backup-strategy)
10. [Disaster Recovery](#disaster-recovery)
11. [Cost Estimation](#cost-estimation)
12. [Cost Breakdown](#cost-breakdown)
13. [Cost Optimization](#cost-optimization)
14. [Budget Planning](#budget-planning)
15. [Security Overview](#security-overview)
16. [Security Headers](#security-headers)
17. [CORS Configuration](#cors-configuration)
18. [Rate Limiting](#rate-limiting)
19. [Input Validation](#input-validation)
20. [Secret Management](#secret-management)
21. [Security Checklist](#security-checklist)
22. [Incident Response](#incident-response)

---

## Maintenance Overview

### Maintenance Philosophy

The Arkan Tsabit Portfolio website follows a proactive maintenance approach to ensure high availability, security, and performance. Regular maintenance activities are scheduled to prevent issues before they occur.

### Maintenance Objectives

| Objective | Description |
|-----------|-------------|
| Availability | Maintain 99.9% uptime |
| Security | Keep all components secure |
| Performance | Optimize load times and response |
| Content | Keep content up-to-date |
| Reliability | Prevent and fix issues proactively |

### Maintenance Scope

```
+=============================================================================+
|                         MAINTENANCE SCOPE                                   |
|                                                                             |
|  +-----------------------------------------------------------------------+  |
|  |                    IN SCOPE                                             |  |
|  |  - Static Website (GitHub Pages)                                      |  |
|  |  - Cloudflare Workers API                                              |  |
|  |  - Cloudflare Vectorize Database                                       |  |
|  |  - Google Sheets Integration                                           |  |
|  |  - Content Updates                                                     |  |
|  |  - Security Patches                                                    |  |
|  |  - Performance Optimization                                            |  |
|  |  - Backup Management                                                   |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  +-----------------------------------------------------------------------+  |
|  |                    OUT OF SCOPE                                         |  |
|  |  - Third-party Services (GitHub, Cloudflare, Google)                  |  |
|  |  - Physical Infrastructure                                            |  |
|  |  - User Device Maintenance                                            |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

---

## Maintenance Schedule

### Maintenance Frequency

| Type | Frequency | Time Required | Impact |
|------|-----------|---------------|--------|
| Daily | Every day | 5 minutes | None |
| Weekly | Every week | 15 minutes | None |
| Monthly | Every month | 30 minutes | None |
| Quarterly | Every 3 months | 1 hour | Low |
| Annual | Every year | 2 hours | Low |
| Emergency | As needed | Varies | Variable |

### Maintenance Window

| Window | Day | Time | Duration |
|--------|-----|------|----------|
| Weekly | Sunday | 08:00 - 08:15 | 15 minutes |
| Monthly | First Sunday | 08:00 - 08:30 | 30 minutes |
| Quarterly | First Sunday of quarter | 08:00 - 09:00 | 1 hour |
| Annual | First Sunday of year | 08:00 - 10:00 | 2 hours |

---

## Daily Maintenance

### Daily Checklist

| No | Task | Status | Notes |
|----|------|--------|-------|
| 1 | Check website availability | ⬜ Pending | Visit https://arkantsabit123.github.io/arkan-tsabit.github.io/ |
| 2 | Check API health endpoint | ⬜ Pending | https://arkan-chatbot.arkan-chatbot.workers.dev/health |
| 3 | Check for error alerts | ⬜ Pending | Cloudflare dashboard, email |
| 4 | Check contact form submissions | ⬜ Pending | Google Sheets |
| 5 | Monitor suspicious activity | ⬜ Pending | Security logs |

### Daily Commands

```bash
# Check website availability
curl -I https://arkantsabit123.github.io/arkan-tsabit.github.io/
# Expected: 200 OK

# Check API health
curl https://arkan-chatbot.arkan-chatbot.workers.dev/health
# Expected: {"status":"healthy"}

# Check Cloudflare Worker logs
wrangler tail --format=json | grep -i error

# Check Google Sheets (manual)
# Open: https://docs.google.com/spreadsheets/d/1zcck8oaWyw5aWOpNl4JqstaLFYhjMvh_aNvrr0adqAg

# Check security alerts
# Cloudflare Dashboard -> Security -> Events
```

---

## Weekly Maintenance

### Weekly Checklist

| No | Task | Status | Notes |
|----|------|--------|-------|
| 1 | Review analytics (visitors, bounce rate) | ⬜ Pending | Google Analytics |
| 2 | Check API usage metrics | ⬜ Pending | Cloudflare Dashboard |
| 3 | Review error logs | ⬜ Pending | Cloudflare Dashboard |
| 4 | Validate backup integrity | ⬜ Pending | Check backup files |
| 5 | Update content if needed | ⬜ Pending | Projects, certifications |
| 6 | Check external links | ⬜ Pending | Verify links working |
| 7 | Review security logs | ⬜ Pending | Cloudflare Security |
| 8 | Check SSL certificate status | ⬜ Pending | GitHub Pages HTTPS |

### Weekly Commands

```bash
# Check Google Analytics
# Login to https://analytics.google.com
# Review: Users, Sessions, Bounce Rate, Pages per Session

# Check API usage
# Cloudflare Dashboard -> Workers & Pages -> arkan-chatbot -> Analytics
# Review: Requests, Response Time, Error Rate

# Review error logs
wrangler tail --format=json --status=error

# Check backup integrity
# Pull latest backup
git clone https://github.com/ArkanTsabit123/arkan-tsabit.github.io.git backup
# Verify files
ls -la backup/

# Check external links
npx link-checker https://arkantsabit123.github.io/arkan-tsabit.github.io/

# SSL certificate check
curl -I https://arkantsabit123.github.io/arkan-tsabit.github.io/ | grep -i "strict-transport-security"
```

---

## Monthly Maintenance

### Monthly Checklist

| No | Task | Status | Priority | Notes |
|----|------|--------|----------|-------|
| 1 | Performance audit (Lighthouse) | ⬜ Pending | High | Run Lighthouse, track scores |
| 2 | Update dependencies (Python) | ⬜ Pending | High | Check requirements.txt |
| 3 | Update dependencies (NPM) | ⬜ Pending | High | Check package.json |
| 4 | Security scan | ⬜ Pending | High | Run security tools |
| 5 | Content review | ⬜ Pending | Medium | Update outdated content |
| 6 | Check broken links | ⬜ Pending | Medium | Scan all pages |
| 7 | Review documentation | ⬜ Pending | Medium | Update if needed |
| 8 | Check storage usage | ⬜ Pending | Low | GitHub Pages, Vectorize |
| 9 | Review costs | ⬜ Pending | Low | Check monthly spend |
| 10 | Backup verification | ⬜ Pending | High | Test backup restoration |

### Monthly Commands

```bash
# Performance audit (Lighthouse)
npx lighthouse https://arkantsabit123.github.io/arkan-tsabit.github.io/ --view

# PageSpeed Insights
# Visit: https://pagespeed.web.dev/?url=https://arkantsabit123.github.io/arkan-tsabit.github.io/

# Check Python dependencies
pip list --outdated

# Update Python dependencies
pip install --upgrade -r requirements.txt

# Check NPM dependencies
npm outdated

# Update NPM dependencies
npm update

# Security scan
# Python Safety
pip install safety
safety check

# NPM audit
npm audit

# Check broken links
npx link-checker https://arkantsabit123.github.io/arkan-tsabit.github.io/ --recursive

# Check storage
du -sh ./
# Check GitHub Pages storage: Settings -> Pages

# Check costs
# Cloudflare Dashboard -> Billing
```

---

## Quarterly Maintenance

### Quarterly Checklist

| No | Task | Status | Priority | Notes |
|----|------|--------|----------|-------|
| 1 | Full security audit | ⬜ Pending | High | Comprehensive security review |
| 2 | Code review | ⬜ Pending | High | Review all code changes |
| 3 | Update documentation | ⬜ Pending | High | README, blueprint, changelog |
| 4 | Review SEO | ⬜ Pending | High | Check rankings, optimize |
| 5 | Test disaster recovery | ⬜ Pending | High | Test backup restoration |
| 6 | Review user feedback | ⬜ Pending | Medium | Contact form, chatbot logs |
| 7 | Plan new features | ⬜ Pending | Medium | Roadmap planning |
| 8 | Check GDPR compliance | ⬜ Pending | Medium | Privacy policy review |
| 9 | Knowledge base update | ⬜ Pending | Medium | Add new documents |
| 10 | Performance optimization | ⬜ Pending | Medium | Optimize assets |

### Quarterly Commands

```bash
# Full security audit
# OWASP ZAP scan
zap-cli quick-scan https://arkantsabit123.github.io/arkan-tsabit.github.io/

# SSL Labs test
# Visit: https://www.ssllabs.com/ssltest/analyze.html?d=arkan-tsabit.github.io

# Security Headers test
# Visit: https://securityheaders.com/?q=arkan-tsabit.github.io

# CSP Evaluator
# Visit: https://csp-evaluator.withgoogle.com/?url=arkan-tsabit.github.io

# Code review
git log --oneline --since="3 months ago"

# SEO audit
# Visit: https://search.google.com/search-console

# Backup restoration test
# Test restoring from backup

# Knowledge base update
python upload_vectors.py --update
```

---

## Annual Maintenance

### Annual Checklist

| No | Task | Status | Priority | Notes |
|----|------|--------|----------|-------|
| 1 | Domain renewal | ⬜ Pending | High | Cloudflare Registrar |
| 2 | Full security audit | ⬜ Pending | High | Comprehensive audit |
| 3 | Review and update policies | ⬜ Pending | High | Privacy, terms |
| 4 | Major dependency updates | ⬜ Pending | High | Version upgrades |
| 5 | Content refresh | ⬜ Pending | High | Update all content |
| 6 | Infrastructure review | ⬜ Pending | High | Evaluate current stack |
| 7 | Budget review | ⬜ Pending | High | Plan next year budget |
| 8 | SEO review and strategy | ⬜ Pending | High | Review rankings |
| 9 | Backup strategy review | ⬜ Pending | Medium | Validate backups |
| 10 | Disaster recovery test | ⬜ Pending | Medium | Full DR test |

### Annual Commands

```bash
# Domain renewal
# Cloudflare Registrar -> Dashboard
# Check domain expiry: arkantsabit.com
# Renew if needed

# Full security audit
# Combine all security tools:
# - OWASP ZAP
# - SSL Labs
# - Security Headers
# - CSP Evaluator
# - Snyk

# Dependency major updates
# Review major version updates
pip install --upgrade --upgrade-strategy eager -r requirements.txt

# Content review
# All pages: index, about, projects, certifications, achievements, contact

# Infrastructure review
# Evaluate current costs and services

# Budget planning
# Review last year costs, plan next year

# SEO audit
# Google Search Console -> Performance
# Check keyword positions
# Review top performing pages

# Backup validation
# Test full restore from backup
```

---

## Emergency Maintenance

### Emergency Types

| Emergency | Severity | Response Time |
|-----------|----------|---------------|
| Website Down | Critical | < 1 hour |
| API Down | Critical | < 1 hour |
| Security Breach | Critical | < 30 minutes |
| Data Loss | Critical | < 1 hour |
| Performance Degradation | High | < 4 hours |
| Content Issues | Medium | < 24 hours |
| Minor Bugs | Low | < 48 hours |

### Emergency Response Procedures

```markdown
# Emergency Response Procedure

## Step 1: Detection
- Monitor alerts and logs
- Identify issue type and severity
- Notify team

## Step 2: Assessment
- Determine scope and impact
- Identify affected systems
- Gather information

## Step 3: Response
- Implement immediate fix
- Isolate affected systems
- Apply workaround

## Step 4: Resolution
- Implement permanent fix
- Test fix
- Deploy to production

## Step 5: Review
- Document incident
- Analyze root cause
- Implement improvements
```

### Emergency Command Scripts

```bash
# Emergency: Website Down
# Check GitHub Pages status
curl -I https://arkantsabit123.github.io/arkan-tsabit.github.io/
# Check GitHub Pages service status
# https://www.githubstatus.com/

# Emergency: API Down
# Check Worker status
wrangler tail --format=json
# Redeploy worker
cd chatbot && wrangler deploy

# Emergency: Security Breach
# Revoke API tokens
# Cloudflare Dashboard -> API Tokens -> Revoke
# Rotate environment variables
# Deploy new .env file
# Monitor suspicious activity

# Emergency: Data Loss
# Restore from backup
# Check Google Sheets history
# Restore Vectorize from backup
```

---

## Backup Strategy

### Backup Schedule

| Backup Type | Frequency | Location | Retention |
|-------------|-----------|----------|-----------|
| Full Backup | Weekly | GitHub | Unlimited |
| Content Backup | Daily | Google Drive | 90 days |
| Knowledge Base | Weekly | Local | 30 days |
| Configuration | Weekly | GitHub | Unlimited |
| Environment | Monthly | Password Manager | Unlimited |

### Backup Commands

```bash
# Full backup (GitHub)
# Automatic on every push
git push origin main

# Content backup (Google Drive)
# Manual: Copy Google Sheets to Google Drive
# Cloudflare Vectorize backup
wrangler vectorize get arkan-knowledge-base --output backup.ndjson

# Knowledge base backup
cp chatbot/knowledge-upload.json backup/knowledge-upload-$(date +%Y%m%d).json

# Configuration backup
cp .env backup/.env-$(date +%Y%m%d)
cp wrangler.toml backup/wrangler.toml-$(date +%Y%m%d)

# Google Sheets backup
# Manual: File -> Download -> CSV
```

---

## Disaster Recovery

### Disaster Recovery Plan

| Scenario | Recovery Procedure | Time to Recover |
|----------|-------------------|-----------------|
| Website Down | Check GitHub Pages, redeploy | < 1 hour |
| API Down | Check Workers, redeploy | < 1 hour |
| Data Loss | Restore from backup | < 2 hours |
| Security Breach | Revoke tokens, restore | < 4 hours |
| Domain Issues | Check DNS settings | < 1 hour |
| Database Corruption | Restore Vectorize index | < 2 hours |

### Recovery Commands

```bash
# Recover website from GitHub
git clone https://github.com/ArkanTsabit123/arkan-tsabit.github.io.git recovery

# Redeploy Worker
cd chatbot
wrangler deploy

# Recover Vectorize index
wrangler vectorize insert arkan-knowledge-base --file backup.ndjson

# Recover environment
cp backup/.env-$(date +%Y%m%d) .env

# Restore Google Sheets
# Google Sheets -> File -> Import -> Upload backup CSV
```

---

## Cost Estimation

### Total Cost Summary

| Category | Monthly | Annual |
|----------|---------|--------|
| Hosting | $0.00 | $0.00 |
| Domain | $0.87 | $10.44 |
| Cloudflare Services | $0.00 | $0.00 |
| Third-Party Services | $0.00 | $0.00 |
| Total | $0.87 | $10.44 |

### Monthly Cost Table

| Service | Tier | Monthly Cost | Units | Cost per Unit |
|---------|------|--------------|-------|---------------|
| GitHub Pages | Free | $0.00 | Unlimited | $0.00 |
| Cloudflare Workers | Free | $0.00 | 100k requests | $0.00 |
| Cloudflare Vectorize | Free | $0.00 | 1M queries | $0.00 |
| Cloudflare Workers AI | Free | $0.00 | 10k requests | $0.00 |
| Google Sheets | Free | $0.00 | Unlimited | $0.00 |
| Google Analytics | Free | $0.00 | Unlimited | $0.00 |
| Cloudflare Registrar | Paid | $0.87 | 1 domain | $0.87 |
| Total | | $0.87 | | |

### Annual Cost Table

| Service | Annual Cost | Frequency |
|---------|-------------|-----------|
| GitHub Pages | $0.00 | Yearly |
| Cloudflare Workers | $0.00 | Yearly |
| Cloudflare Vectorize | $0.00 | Yearly |
| Cloudflare Workers AI | $0.00 | Yearly |
| Google Sheets | $0.00 | Yearly |
| Google Analytics | $0.00 | Yearly |
| Cloudflare Registrar | $10.44 | Yearly |
| Total | $10.44 | |

### Free Tier Limits

| Service | Free Tier Limits | Usage |
|---------|------------------|-------|
| GitHub Pages | Unlimited | 10MB storage |
| Cloudflare Workers | 100k requests/day | ~100 requests/day |
| Cloudflare Vectorize | 1M queries/month | ~1,000 queries/month |
| Cloudflare Workers AI | 10k requests/day | ~100 requests/day |
| Google Sheets | 5M cells | ~10 cells |
| Google Analytics | 10M hits/month | ~1,000 hits/month |

---

## Cost Optimization

### Free Tier Optimization

| Strategy | Implementation | Savings |
|----------|----------------|---------|
| Use Free Tiers | Leverage free limits | $100+ / month |
| Optimize Worker Usage | Reduce unnecessary requests | $0.00 (free) |
| Cache Static Assets | Browser and CDN caching | $0.00 (free) |
| Compress Data | GZIP compression | $0.00 (free) |
| Minify Code | CSS/JS minification | $0.00 (free) |

### Cost Saving Tips

| Tip | Implementation | Impact |
|-----|----------------|--------|
| 1. Use Free CDN | GitHub Pages CDN | $0.00 |
| 2. Optimize Images | Compress images | Faster load |
| 3. Enable Caching | Browser caching | Fewer requests |
| 4. Reduce API Calls | Batch requests | Fewer requests |
| 5. Use Static Files | JSON over database | No database costs |
| 6. Monitor Usage | Cloudflare dashboard | Prevent overages |

---

## Budget Planning

### Annual Budget Breakdown

| Category | Budget | Actual | Variance |
|----------|--------|--------|----------|
| Hosting | $0.00 | $0.00 | $0.00 |
| Domain | $15.00 | $10.44 | $4.56 |
| Cloudflare Services | $0.00 | $0.00 | $0.00 |
| Third-Party Services | $0.00 | $0.00 | $0.00 |
| Total | $15.00 | $10.44 | $4.56 |

### Cost Projections

| Year | Hosting | Domain | Total | Growth |
|------|---------|--------|-------|--------|
| Year 1 | $0.00 | $10.44 | $10.44 | - |
| Year 2 | $0.00 | $10.44 | $10.44 | 0% |
| Year 3 | $0.00 | $10.44 | $10.44 | 0% |

---

## Security Overview

### Security Philosophy

The Arkan Tsabit Portfolio website follows a defense-in-depth security approach with multiple layers of protection. The system is designed to be secure by default while maintaining simplicity and performance.

### Security Objectives

| Objective | Description |
|-----------|-------------|
| Confidentiality | Protect sensitive data from unauthorized access |
| Integrity | Ensure data accuracy and prevent tampering |
| Availability | Maintain system uptime and accessibility |
| Authenticity | Verify source of data and requests |
| Non-repudiation | Prevent denial of actions |

### Security Scope

```
+=============================================================================+
|                         SECURITY SCOPE                                      |
|                                                                             |
|  +-----------------------------------------------------------------------+  |
|  |                    IN SCOPE                                             |  |
|  |  - Static Website (GitHub Pages)                                      |  |
|  |  - Cloudflare Workers API                                              |  |
|  |  - Cloudflare Vectorize Database                                       |  |
|  |  - Google Sheets Integration                                           |  |
|  |  - Contact Form Handling                                               |  |
|  |  - API Rate Limiting                                                   |  |
|  |  - SSL/TLS Encryption                                                  |  |
|  |  - CORS Configuration                                                  |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  +-----------------------------------------------------------------------+  |
|  |                    OUT OF SCOPE                                         |  |
|  |  - User Device Security                                                |  |
|  |  - Network Infrastructure of Users                                    |  |
|  |  - Third-party Services (GitHub, Cloudflare, Google)                  |  |
|  |  - Physical Security                                                   |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

---

## Security Headers

### Security Headers Configuration

| Header | Value | Purpose |
|--------|-------|---------|
| Content-Security-Policy | `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://arkan-chatbot.arkan-chatbot.workers.dev;` | Prevent XSS and data injection |
| X-Content-Type-Options | `nosniff` | Prevent MIME type sniffing |
| X-Frame-Options | `DENY` | Prevent clickjacking |
| X-XSS-Protection | `1; mode=block` | Enable XSS filtering |
| Referrer-Policy | `strict-origin-when-cross-origin` | Control referrer information |
| Permissions-Policy | `geolocation=(), microphone=(), camera=()` | Restrict browser features |
| Strict-Transport-Security | `max-age=31536000; includeSubDomains; preload` | Enforce HTTPS |

### CSP Implementation

```html
<!-- Example CSP header for HTML pages -->
<meta http-equiv="Content-Security-Policy" 
  content="default-src 'self'; 
           script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; 
           style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; 
           font-src 'self' https://fonts.gstatic.com; 
           img-src 'self' data: https:; 
           connect-src 'self' https://arkan-chatbot.arkan-chatbot.workers.dev; 
           frame-ancestors 'none'; 
           base-uri 'self'; 
           form-action 'self';">
```

### HSTS Implementation

```html
<!-- Force HTTPS -->
<meta http-equiv="Strict-Transport-Security" 
  content="max-age=31536000; includeSubDomains; preload">
```

---

## CORS Configuration

### CORS Policy

```javascript
// Cloudflare Worker CORS Configuration
const corsHeaders = {
  'Access-Control-Allow-Origin': 'https://arkantsabit123.github.io/arkan-tsabit.github.io/',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Accept',
  'Access-Control-Expose-Headers': 'Content-Type, Accept',
  'Access-Control-Max-Age': '86400',
  'Access-Control-Allow-Credentials': 'false'
};
```

### Allowed Origins

| Origin | Status |
|--------|--------|
| https://arkantsabit123.github.io/arkan-tsabit.github.io/ | ✅ Allowed |
| https://arkantsabit.com | ✅ Allowed (future) |
| http://localhost:8000 | ✅ Allowed (development) |
| Other Origins | ❌ Blocked |

---

## Rate Limiting

### Rate Limit Configuration

| Limit | Value |
|-------|-------|
| Requests per IP | 30 per minute |
| Burst Limit | 5 requests per second |
| Window | 1 minute (sliding window) |

### Rate Limit Headers

```http
X-RateLimit-Limit: 30
X-RateLimit-Remaining: 15
X-RateLimit-Reset: 60
```

### Rate Limit Exceeded Response

```json
{
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please try again in 60 seconds.",
  "code": "RATE_LIMIT_EXCEEDED",
  "status": 429,
  "retry_after": 60
}
```

---

## Input Validation

### Validation Rules

| Input Type | Validation Rules |
|------------|------------------|
| Question | Required, min 1 char, max 500 chars, sanitized |
| Name (Contact) | Required, min 1 char, max 100 chars, sanitized |
| Email (Contact) | Required, valid email format, max 100 chars |
| Subject (Contact) | Required, min 1 char, max 200 chars, sanitized |
| Message (Contact) | Required, min 1 char, max 1000 chars, sanitized |

### Sanitization Functions

```javascript
// Input sanitization
function sanitizeInput(input) {
  let sanitized = input.trim();
  sanitized = sanitized.replace(/&/g, '&amp;')
                       .replace(/</g, '&lt;')
                       .replace(/>/g, '&gt;')
                       .replace(/"/g, '&quot;')
                       .replace(/'/g, '&#x27;');
  sanitized = sanitized.replace(/<script>/gi, '')
                       .replace(/<\/script>/gi, '');
  return sanitized;
}

// Email validation
function validateEmail(email) {
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return regex.test(email);
}
```

---

## Secret Management

### Environment Variables

```bash
# .env file (DO NOT COMMIT)
CLOUDFLARE_ACCOUNT_ID=1ac4476c492b63bf4eeb0fb1523aab34
CLOUDFLARE_API_TOKEN=your_api_token_here
VECTORIZE_INDEX_NAME=arkan-knowledge-base
EMBEDDING_MODEL=@cf/baai/bge-small-en-v1.5
LLM_MODEL=@cf/mistral/mistral-7b-instruct-v0.2-lora
```

### Secret Storage

| Secret | Storage Location | Access |
|--------|------------------|--------|
| Cloudflare API Token | .env file | Local development only |
| Vectorize Index Name | .env file | Local development only |
| Embedding Model | .env file | Local development only |
| Google Sheets URL | contact.html | Public (safe) |

### Secret Security Guidelines

| Guideline | Implementation |
|-----------|----------------|
| Never commit secrets | .env in .gitignore |
| Use environment variables | All secrets in .env |
| Rotate regularly | Scheduled rotation |
| Monitor access | Cloudflare API access logs |
| Limit permissions | Minimal required permissions |

---

## Security Checklist

| No | Task | Status | Priority |
|----|------|--------|----------|
| 1 | HTTPS enabled | ✅ Done | High |
| 2 | TLS 1.3 support | ✅ Done | High |
| 3 | Security headers implemented | ✅ Done | High |
| 4 | CSP configured | ✅ Done | High |
| 5 | CORS restricted | ✅ Done | High |
| 6 | Rate limiting enabled | ✅ Done | High |
| 7 | Input validation | ✅ Done | High |
| 8 | Output encoding | ✅ Done | High |
| 9 | XSS prevention | ✅ Done | High |
| 10 | No eval() in code | ✅ Done | High |
| 11 | No innerHTML | ✅ Done | High |
| 12 | No PII stored | ✅ Done | High |
| 13 | Data encryption in transit | ✅ Done | High |
| 14 | .env in .gitignore | ✅ Done | High |
| 15 | No hardcoded secrets | ✅ Done | High |
| 16 | Regular secret rotation | ⬜ Pending | Medium |
| 17 | Logging enabled | ✅ Done | High |

---

## Incident Response

### Incident Response Plan

```
+=============================================================================+
|                     INCIDENT RESPONSE PLAN                                   |
|                                                                             |
|  Phase 1: Detection                                                        |
|  +-----------------------------------------------------------------------+  |
|  |  - Monitor alerts and logs                                             |  |
|  |  - Identify security incidents                                         |  |
|  |  - Classify severity (Critical, High, Medium, Low)                    |  |
|  |  - Notify security team                                                |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 2: Analysis                                                         |
|  +-----------------------------------------------------------------------+  |
|  |  - Investigate incident                                                |  |
|  |  - Determine scope and impact                                         |  |
|  |  - Identify affected systems                                          |  |
|  |  - Gather evidence                                                    |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 3: Containment                                                       |
|  +-----------------------------------------------------------------------+  |
|  |  - Isolate affected systems                                            |  |
|  |  - Stop unauthorized access                                            |  |
|  |  - Rotate compromised credentials                                      |  |
|  |  - Disable vulnerable features                                        |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 4: Eradication                                                       |
|  +-----------------------------------------------------------------------+  |
|  |  - Remove cause of incident                                            |  |
|  |  - Patch vulnerabilities                                              |  |
|  |  - Update security controls                                           |  |
|  |  - Verify system integrity                                            |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 5: Recovery                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  - Restore affected systems                                            |  |
|  |  - Deploy fixes                                                       |  |
|  |  - Monitor for recurrence                                             |  |
|  |  - Resume normal operations                                           |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 6: Lessons Learned                                                    |
|  +-----------------------------------------------------------------------+  |
|  |  - Document incident                                                  |  |
|  |  - Analyze root cause                                                 |  |
|  |  - Implement improvements                                             |  |
|  |  - Update incident response plan                                      |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

### Incident Severity Levels

| Severity | Description | Response Time |
|----------|-------------|---------------|
| Critical | Data breach, system compromise | < 1 hour |
| High | Service disruption, unauthorized access | < 4 hours |
| Medium | Performance issues, minor security event | < 24 hours |
| Low | Suspicious activity, potential threat | < 48 hours |

### Contact Information

| Role | Contact |
|------|---------|
| Security Lead | arkantsabit025@gmail.com |
| Technical Lead | arkantsabit025@gmail.com |
| Emergency Contact | +62 81295709620 |

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer