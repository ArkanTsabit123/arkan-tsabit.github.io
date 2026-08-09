# GUIDE.md

## User Experience and Contribution Guidelines

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

1. [User Flow Overview](#user-flow-overview)
2. [User Personas](#user-personas)
3. [User Journey Maps](#user-journey-maps)
4. [Core User Flows](#core-user-flows)
5. [Chatbot User Flow](#chatbot-user-flow)
6. [Contact Form User Flow](#contact-form-user-flow)
7. [Mobile User Flow](#mobile-user-flow)
8. [Conversion Funnel](#conversion-funnel)
9. [Contribution Guidelines](#contribution-guidelines)
10. [Code of Conduct](#code-of-conduct)
11. [Getting Started for Contributors](#getting-started-for-contributors)
12. [Development Workflow](#development-workflow)
13. [Code Style Guidelines](#code-style-guidelines)
14. [Commit Guidelines](#commit-guidelines)
15. [Pull Request Process](#pull-request-process)
16. [Testing Guidelines](#testing-guidelines)
17. [Issue Reporting](#issue-reporting)
18. [Feature Requests](#feature-requests)
19. [Review Process](#review-process)
20. [Release Process](#release-process)

---

## User Flow Overview

### Flow Philosophy

The Arkan Tsabit Portfolio website is designed to provide an intuitive, seamless user experience that guides visitors from entry to conversion. Each user flow is optimized for clarity, speed, and engagement.

### Flow Objectives

| Objective | Description |
|-----------|-------------|
| Discovery | Help users find what they're looking for |
| Engagement | Keep users interested and exploring |
| Conversion | Guide users to take desired actions |
| Retention | Encourage return visits |
| Satisfaction | Ensure positive user experience |

### User Flow Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Bounce Rate | < 40% | - |
| Pages per Session | > 3 | - |
| Session Duration | > 2 min | - |
| Conversion Rate | > 5% | - |
| Chatbot Engagement | > 10% | - |
| Return Visitors | > 30% | - |

---

## User Personas

### Persona 1: Recruiter

```
+=============================================================================+
|                     PERSONA 1: RECRUITER                                    |
|                                                                             |
|  Name: Sarah Johnson                                                        |
|  Age: 35                                                                   |
|  Role: Technical Recruiter                                                  |
|  Industry: Technology Recruitment                                          |
|                                                                             |
|  Goals:                                                                     |
|  - Find qualified data engineering candidates                              |
|  - Verify skills and certifications                                         |
|  - Assess project experience                                                |
|  - Contact promising candidates                                             |
|                                                                             |
|  Pain Points:                                                               |
|  - Time-consuming to review CVs                                            |
|  - Need to verify technical skills                                          |
|  - Want quick access to relevant information                               |
|                                                                             |
|  User Flow:                                                                 |
|  1. Arrives via LinkedIn link                                               |
|  2. Lands on Homepage                                                       |
|  3. Views certifications (quick scan)                                       |
|  4. Checks projects (deep dive)                                            |
|  5. Reviews experience                                                      |
|  6. Contacts via form or email                                              |
|                                                                             |
|  Devices: Desktop (80%), Mobile (20%)                                       |
|  Time of Day: 9 AM - 5 PM (business hours)                                 |
|                                                                             |
+=============================================================================+
```

### Persona 2: Hiring Manager

```
+=============================================================================+
|                     PERSONA 2: HIRING MANAGER                               |
|                                                                             |
|  Name: Michael Chen                                                         |
|  Age: 42                                                                   |
|  Role: Data Engineering Manager                                             |
|  Industry: E-commerce/Retail                                                |
|                                                                             |
|  Goals:                                                                     |
|  - Evaluate technical depth                                                 |
|  - Assess problem-solving skills                                            |
|  - Check production experience                                              |
|  - Determine cultural fit                                                   |
|                                                                             |
|  Pain Points:                                                               |
|  - Need to see real projects, not just CVs                                 |
|  - Want to understand technical stack                                       |
|  - Need to assess data quality and scale                                    |
|                                                                             |
|  User Flow:                                                                 |
|  1. Finds via Google search                                                 |
|  2. Lands on Projects page                                                  |
|  3. Views project details (architectures, metrics)                         |
|  4. Checks technical skills                                                 |
|  5. Reviews experience                                                      |
|  6. Uses chatbot for specific questions                                     |
|  7. Contacts via form                                                       |
|                                                                             |
|  Devices: Desktop (90%), Mobile (10%)                                       |
|  Time of Day: 8 AM - 6 PM (business hours)                                 |
|                                                                             |
+=============================================================================+
```

### Persona 3: Technical Peer

```
+=============================================================================+
|                     PERSONA 3: TECHNICAL PEER                               |
|                                                                             |
|  Name: David Park                                                           |
|  Age: 28                                                                   |
|  Role: Data Engineer                                                        |
|  Industry: Technology                                                       |
|                                                                             |
|  Goals:                                                                     |
|  - Learn from others' projects                                              |
|  - Discover new tools and technologies                                      |
|  - Connect with like-minded professionals                                   |
|  - Share knowledge and experience                                          |
|                                                                             |
|  Pain Points:                                                               |
|  - Bored with generic portfolio websites                                   |
|  - Want to see code and architecture                                        |
|  - Interested in problem-solving approaches                                |
|                                                                             |
|  User Flow:                                                                 |
|  1. Finds via GitHub/developer communities                                  |
|  2. Lands on Homepage                                                       |
|  3. Views projects (technical deep dive)                                   |
|  4. Checks tech stack                                                       |
|  5. Uses chatbot (technical questions)                                      |
|  6. Connects on GitHub or LinkedIn                                          |
|                                                                             |
|  Devices: Desktop (70%), Mobile (30%)                                       |
|  Time of Day: 6 PM - 11 PM (evening)                                       |
|                                                                             |
+=============================================================================+
```

### Persona 4: Student/Learner

```
+=============================================================================+
|                     PERSONA 4: STUDENT/LEARNER                              |
|                                                                             |
|  Name: Emily Rodriguez                                                      |
|  Age: 22                                                                   |
|  Role: Data Science Student                                                 |
|  Industry: Education                                                        |
|                                                                             |
|  Goals:                                                                     |
|  - Learn about data engineering                                             |
|  - Understand project workflows                                             |
|  - Get inspiration for own projects                                         |
|  - Find learning resources                                                  |
|                                                                             |
|  Pain Points:                                                               |
|  - Overwhelmed by complexity                                                |
|  - Need clear, accessible explanations                                     |
|  - Want to see real-world examples                                          |
|                                                                             |
|  User Flow:                                                                 |
|  1. Finds via educational resources                                         |
|  2. Lands on About page                                                     |
|  3. Reads bio and career transition story                                   |
|  4. Views projects (simplified)                                             |
|  5. Checks certifications                                                   |
|  6. Uses chatbot (learning questions)                                       |
|  7. Connects on LinkedIn                                                    |
|                                                                             |
|  Devices: Mobile (60%), Desktop (40%)                                       |
|  Time of Day: 7 PM - 12 AM (evening/night)                                 |
|                                                                             |
+=============================================================================+
```

### Persona 5: Potential Client

```
+=============================================================================+
|                     PERSONA 5: POTENTIAL CLIENT                             |
|                                                                             |
|  Name: Robert Williams                                                      |
|  Age: 45                                                                   |
|  Role: Business Owner/CTO                                                   |
|  Industry: Small Business/Startup                                           |
|                                                                             |
|  Goals:                                                                     |
|  - Find consultant/freelance data engineer                                  |
|  - Assess ability to solve business problems                               |
|  - Check experience with similar projects                                   |
|  - Evaluate reliability and professionalism                                |
|                                                                             |
|  Pain Points:                                                               |
|  - Need to trust vendor                                                    |
|  - Want to see relevant experience                                          |
|  - Need to understand communication style                                  |
|                                                                             |
|  User Flow:                                                                 |
|  1. Finds via recommendation/Google search                                  |
|  2. Lands on Homepage                                                       |
|  3. Reads about page (professional summary)                                 |
|  4. Reviews projects (business value)                                       |
|  5. Checks contact information                                              |
|  6. Contacts via form                                                       |
|                                                                             |
|  Devices: Desktop (80%), Mobile (20%)                                       |
|  Time of Day: 9 AM - 5 PM (business hours)                                 |
|                                                                             |
+=============================================================================+
```

---

## User Journey Maps

### Recruiter Journey Map

```
+=============================================================================+
|                     RECRUITER JOURNEY MAP                                   |
|                                                                             |
|  Phase 1: Discovery                                                         |
|  +-----------------------------------------------------------------------+  |
|  |  Actions:                                                              |  |
|  |  - Clicks LinkedIn link or job board link                             |  |
|  |  - Searches "Arkan Tsabit Data Engineer" on Google                    |  |
|  |                                                                       |  |
|  |  Touchpoints:                                                          |  |
|  |  - LinkedIn profile link                                              |  |
|  |  - Google search results                                              |  |
|  |                                                                       |  |
|  |  Pain Points:                                                          |  |
|  |  - Need quick access to relevant info                                 |  |
|  |  - Want to verify authenticity                                       |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 2: Entry                                                              |
|  +-----------------------------------------------------------------------+  |
|  |  Actions:                                                              |  |
|  |  - Lands on Homepage or About page                                    |  |
|  |  - Quick scan of hero section                                        |  |
|  |  - Views metrics: 10 certifications, 4 projects, 4 experience        |  |
|  |                                                                       |  |
|  |  Touchpoints:                                                          |  |
|  |  - Homepage hero section                                              |  |
|  |  - Metrics display                                                    |  |
|  |                                                                       |  |
|  |  Pain Points:                                                          |  |
|  |  - Need to find specific info quickly                                 |  |
|  |  - Information overload possible                                      |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 3: Exploration                                                        |
|  +-----------------------------------------------------------------------+  |
|  |  Actions:                                                              |  |
|  |  - Navigates to Certifications page                                   |  |
|  |  - Verifies 10 certifications                                         |  |
|  |  - Clicks "Verify" buttons                                            |  |
|  |  - Navigates to Projects page                                         |  |
|  |  - Reviews project details                                            |  |
|  |                                                                       |  |
|  |  Touchpoints:                                                          |  |
|  |  - Certifications page                                                |  |
|  |  - Projects page                                                      |  |
|  |                                                                       |  |
|  |  Pain Points:                                                          |  |
|  |  - Need to quickly verify information                                 |  |
|  |  - Want to see detailed projects                                      |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 4: Evaluation                                                         |
|  +-----------------------------------------------------------------------+  |
|  |  Actions:                                                              |  |
|  |  - Navigates to About page                                            |  |
|  |  - Reviews experience                                                 |  |
|  |  - Checks technical skills                                            |  |
|  |  - Uses chatbot for specific questions                                |  |
|  |                                                                       |  |
|  |  Touchpoints:                                                          |  |
|  |  - About page                                                         |  |
|  |  - Chatbot widget                                                     |  |
|  |                                                                       |  |
|  |  Pain Points:                                                          |  |
|  |  - Need to assess fit with company                                    |  |
|  |  - Want to understand career trajectory                               |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Phase 5: Conversion                                                         |
|  +-----------------------------------------------------------------------+  |
|  |  Actions:                                                              |  |
|  |  - Navigates to Contact page                                          |  |
|  |  - Fills contact form                                                  |  |
|  |  - Or sends email directly                                            |  |
|  |                                                                       |  |
|  |  Touchpoints:                                                          |  |
|  |  - Contact page                                                       |  |
|  |  - Contact form                                                       |  |
|  |                                                                       |  |
|  |  Pain Points:                                                          |  |
|  |  - Need response within 24-48 hours                                   |  |
|  |  - Want to know application status                                    |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

---

## Core User Flows

### Flow 1: Research and Discovery

```
+=============================================================================+
|                     FLOW 1: RESEARCH AND DISCOVERY                          |
|                                                                             |
|  Purpose: User wants to learn about Arkan's background and expertise       |
|                                                                             |
|  Start: Homepage                                                            |
|                                                                             |
|  Step 1: Homepage                                                           |
|  +-----------------------------------------------------------------------+  |
|  |  - Read hero section: "Data Engineer | Cloud Data Engineer"           |  |
|  |  - View metrics: 10 Certs, 4 Projects, 4 Experience                   |  |
|  |  - Scan skills preview                                                 |  |
|  |  - View featured project                                               |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 2: About Page                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  - Read professional bio                                               |  |
|  |  - Review career transition story                                      |  |
|  |  - Check work experience (4 roles)                                    |  |
|  |  - Explore technical skills (5 categories)                            |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 3: Certifications Page                                                 |
|  +-----------------------------------------------------------------------+  |
|  |  - View 10 certification cards                                         |  |
|  |  - Verify credentials via "Verify" buttons                            |  |
|  |  - Check provider logos (Oracle, IBM, Meta)                           |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 4: Projects Page                                                       |
|  +-----------------------------------------------------------------------+  |
|  |  - View 4 project cards                                                |  |
|  |  - Filter by technology if needed                                     |  |
|  |  - Click project details                                               |  |
|  |  - Explore architectures, metrics, tech stack                         |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 5: Achievements Page                                                   |
|  +-----------------------------------------------------------------------+  |
|  |  - View 3 achievements                                                |  |
|  |  - Read details of Oracle Race (Global Top 108)                       |  |
|  |  - Read details of Oracle Race (Indonesia Top 3)                      |  |
|  |  - Read Best Teacher Award details                                    |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  End: Contact Page                                                           |
|  +-----------------------------------------------------------------------+  |
|  |  - Reach out via contact form                                          |  |
|  |  - Connect via LinkedIn                                                |  |
|  |  - Send email                                                         |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

### Flow 2: Project Deep Dive

```
+=============================================================================+
|                     FLOW 2: PROJECT DEEP DIVE                               |
|                                                                             |
|  Purpose: User wants detailed information about specific projects          |
|                                                                             |
|  Start: Homepage                                                            |
|                                                                             |
|  Step 1: Homepage                                                           |
|  +-----------------------------------------------------------------------+  |
|  |  - View featured project (BatchETL)                                  |  |
|  |  - Click "View All Projects" button                                  |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 2: Projects Page                                                       |
|  +-----------------------------------------------------------------------+  |
|  |  - View all 4 project cards                                           |  |
|  |  - Read brief descriptions                                            |  |
|  |  - Check metrics: 2.96M rows, under 30 sec, 100% quality             |  |
|  |  - View tech stack badges                                             |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 3: Project Detail (Cards Expand)                                      |
|  +-----------------------------------------------------------------------+  |
|  |  - Read full project description                                      |  |
|  |  - View architecture diagrams                                         |  |
|  |  - See dashboard screenshots                                          |  |
|  |  - Check ERD/schema diagrams                                          |  |
|  |  - Review metrics in detail                                           |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 4: Technical Exploration                                              |
|  +-----------------------------------------------------------------------+  |
|  |  - Click GitHub repository link                                       |  |
|  |  - View code on GitHub                                                |  |
|  |  - Check README and documentation                                     |  |
|  |  - See commit history                                                 |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 5: Chatbot Question                                                    |
|  +-----------------------------------------------------------------------+  |
|  |  - Ask technical questions about project                             |  |
|  |  - Get detailed responses from AI                                     |  |
|  |  - Clarify technical choices                                          |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  End: Connect                                                                |
|  +-----------------------------------------------------------------------+  |
|  |  - Contact for collaboration                                          |  |
|  |  - Connect on GitHub                                                  |  |
|  |  - Connect on LinkedIn                                                |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

### Flow 3: Job Application

```
+=============================================================================+
|                     FLOW 3: JOB APPLICATION                                 |
|                                                                             |
|  Purpose: Recruiter or hiring manager wants to assess candidate            |
|                                                                             |
|  Start: LinkedIn/GitHub/Resume                                              |
|                                                                             |
|  Step 1: Entry                                                              |
|  +-----------------------------------------------------------------------+  |
|  |  - Clicks link from LinkedIn profile                                  |  |
|  |  - Clicks link from resume                                            |  |
|  |  - Google search: "Arkan Tsabit"                                     |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 2: Homepage                                                            |
|  +-----------------------------------------------------------------------+  |
|  |  - Scan hero section                                                  |  |
|  |  - View key metrics: 10 certs, 4 projects, 4 experience              |  |
|  |  - Read tagline                                                        |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 3: About Page                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  - Read professional bio                                              |  |
|  |  - Review work experience (newest to oldest)                          |  |
|  |    - BRI SD-WAN (Current)                                             |  |
|  |    - Satu Benih (2024-2025)                                           |  |
|  |    - Bejagoo (2023-2024)                                              |  |
|  |    - Airport (2022-2023)                                              |  |
|  |  - Check technical skills (5 categories)                              |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 4: Certifications Page                                                 |
|  +-----------------------------------------------------------------------+  |
|  |  - Verify 10 certifications                                          |  |
|  |  - Click "Verify" buttons for authenticity                            |  |
|  |  - Check dates and providers                                          |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 5: Projects Page                                                        |
|  +-----------------------------------------------------------------------+  |
|  |  - Review 4 projects in detail                                         |  |
|  |  - Check production experience                                         |  |
|  |  - Evaluate scale: 2.96M rows, 95%+ success rate                     |  |
|  |  - Assess tech stack alignment                                         |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 6: Contact                                                              |
|  +-----------------------------------------------------------------------+  |
|  |  - Fill contact form: Name, Email, Subject, Message                    |  |
|  |  - Send message about job opportunity                                  |  |
|  |  - Or email directly: arkantsabit025@gmail.com                         |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

---

## Chatbot User Flow

### Chatbot Interaction Flow

```
+=============================================================================+
|                     CHATBOT USER FLOW                                       |
|                                                                             |
|  Step 1: Discovery                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  User sees chatbot widget floating in bottom right corner            |  |
|  |  - Icon: Chat bubble with "Chat with Arkan's AI" text                |  |
|  |  - Hover: "Ask me anything"                                          |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 2: Open Chat                                                           |
|  +-----------------------------------------------------------------------+  |
|  |  User clicks chatbot icon                                              |  |
|  |  - Widget opens sliding from bottom                                    |  |
|  |  - Welcome message: "Hi! I'm Arkan's AI assistant"                   |  |
|  |  - Suggested questions displayed                                      |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 3: Question Input                                                      |
|  +-----------------------------------------------------------------------+  |
|  |  User types question in input box                                     |  |
|  |  - Example: "What projects has Arkan built?"                         |  |
|  |  - Character limit: 500 characters                                    |  |
|  |  - Auto-validation                                                    |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 4: Processing                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  - Loading indicator appears                                           |  |
|  |  - Typing animation: "..."                                            |  |
|  |  - API call to Cloudflare Worker                                      |  |
|  |  - Vector search in knowledge base                                    |  |
|  |  - LLM response generation                                            |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 5: Response                                                            |
|  +-----------------------------------------------------------------------+  |
|  |  - Response displayed in chat window                                   |  |
|  |  - Source: "llm" or "fallback"                                       |  |
|  |  - Context documents (optional)                                       |  |
|  |  - Auto-scroll to bottom                                               |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 6: Follow-up                                                           |
|  +-----------------------------------------------------------------------+  |
|  |  User continues conversation                                           |  |
|  |  - Ask follow-up questions                                            |  |
|  |  - Get more details                                                    |  |
|  |  - Click suggested questions                                           |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 7: Close Chat                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  User clicks close button or clicks outside                           |  |
|  |  - Chat window slides down                                            |  |
|  |  - Widget returns to icon                                             |  |
|  |  - Conversation history preserved (session)                          |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

### Chatbot Question Categories

| Category | Example Questions | Success Rate |
|----------|-------------------|--------------|
| Profile | "Who is Arkan Tsabit?" | 100% |
| Projects | "What projects has Arkan built?" | 100% |
| Certifications | "What certifications does Arkan have?" | 100% |
| Achievements | "What achievements does Arkan have?" | 100% |
| Experience | "What is Arkan's work experience?" | 100% |
| Skills | "What is Arkan's tech stack?" | 100% |
| Contact | "How can I contact Arkan?" | 100% |
| General | "Tell me about Arkan" | 100% |

### Suggested Questions

```json
{
  "profile": [
    "Who is Arkan Tsabit?",
    "What is Arkan's background?",
    "Tell me about Arkan's career"
  ],
  "projects": [
    "What projects has Arkan built?",
    "Tell me about the BatchETL Pipeline",
    "What technology stack does Arkan use?"
  ],
  "certifications": [
    "What certifications does Arkan have?",
    "What Oracle certifications does Arkan have?",
    "Are Arkan's certifications verified?"
  ],
  "achievements": [
    "What achievements does Arkan have?",
    "What is Oracle Race to Certification?",
    "Tell me about Arkan's awards"
  ],
  "contact": [
    "How can I contact Arkan?",
    "What is Arkan's email?",
    "Where can I find Arkan on LinkedIn?"
  ]
}
```

---

## Contact Form User Flow

### Contact Form Flow

```
+=============================================================================+
|                     CONTACT FORM USER FLOW                                  |
|                                                                             |
|  Step 1: Access Form                                                        |
|  +-----------------------------------------------------------------------+  |
|  |  User navigates to Contact page                                       |  |
|  |  - Clicks "Contact" in navigation                                     |  |
|  |  - Clicks "Contact Me" button on Homepage                             |  |
|  |  - Scrolls to contact section                                          |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 2: View Form                                                           |
|  +-----------------------------------------------------------------------+  |
|  |  User sees contact form                                               |  |
|  |  - Name field (required)                                              |  |
|  |  - Email field (required, valid format)                               |  |
|  |  - Subject field (required)                                           |  |
|  |  - Message field (required)                                           |  |
|  |  - Send button                                                        |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 3: Fill Form                                                           |
|  +-----------------------------------------------------------------------+  |
|  |  User fills form fields                                               |  |
|  |  - Name: "John Doe"                                                   |  |
|  |  - Email: "john@example.com"                                          |  |
|  |  - Subject: "Job Opportunity"                                         |  |
|  |  - Message: "I have a position for you..."                           |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 4: Validation                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  Form validation occurs                                                |  |
|  |  - Client-side validation                                              |  |
|  |  - Check required fields                                               |  |
|  |  - Validate email format                                               |  |
|  |  - Check message length                                                |  |
|  |  - Show errors if any                                                  |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 5: Submit                                                               |
|  +-----------------------------------------------------------------------+  |
|  |  User clicks "Send Message" button                                      |  |
|  |  - Loading indicator appears                                            |  |
|  |  - Form disabled during submission                                      |  |
|  |  - POST request to Google Apps Script                                   |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 6: Processing                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  Google Apps Script processes form                                    |  |
|  |  - Validates data                                                      |  |
|  |  - Appends to Google Sheets                                            |  |
|  |  - Adds date and time                                                 |  |
|  |  - Returns success/error response                                     |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 7: Feedback                                                            |
|  +-----------------------------------------------------------------------+  |
|  |  Response displayed to user                                           |  |
|  |  - Success: "Your message has been sent successfully!"               |  |
|  |  - Error: "Something went wrong. Please try again."                  |  |
|  |  - Form reset on success                                               |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 8: Follow-up                                                            |
|  +-----------------------------------------------------------------------+  |
|  |  User receives email confirmation (manual)                            |  |
|  |  - Response within 24-48 hours                                        |  |
|  |  - Thank you message                                                   |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

### Form Validation Rules

| Field | Validation | Error Message |
|-------|------------|---------------|
| Name | Required, min 1 char, max 100 chars | "Please enter your name" |
| Email | Required, valid format, max 100 chars | "Please enter a valid email address" |
| Subject | Required, min 1 char, max 200 chars | "Please enter a subject" |
| Message | Required, min 1 char, max 1000 chars | "Please enter a message" |

---

## Mobile User Flow

### Mobile Navigation Flow

```
+=============================================================================+
|                     MOBILE USER FLOW                                        |
|                                                                             |
|  Step 1: Entry                                                              |
|  +-----------------------------------------------------------------------+  |
|  |  - User opens website on mobile device                                |  |
|  |  - Responsive design adapts to screen size                            |  |
|  |  - Hamburger menu icon visible                                        |  |
|  |  - Smaller hero text and buttons                                      |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 2: Navigation                                                          |
|  +-----------------------------------------------------------------------+  |
|  |  - Click hamburger menu icon                                          |  |
|  |  - Menu slides from top or side                                       |  |
|  |  - Menu items: Home, About, Projects, Certifications, Achievements,  |  |
|  |    Contact                                                            |  |
|  |  - Tap to navigate                                                    |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 3: Content Browsing                                                    |
|  +-----------------------------------------------------------------------+  |
|  |  - Swipe to scroll vertically                                         |  |
|  |  - Tap to expand/collapse sections                                    |  |
|  |  - Tap to view images                                                |  |
|  |  - Pinch to zoom on images                                            |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 4: Form Submission                                                     |
|  +-----------------------------------------------------------------------+  |
|  |  - Tap form fields to open keyboard                                   |  |
|  |  - Use mobile keyboard to input                                      |  |
|  |  - Auto-suggest/autofill for email                                    |  |
|  |  - Tap send button                                                    |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 5: Chatbot Interaction                                                 |
|  +-----------------------------------------------------------------------+  |
|  |  - Tap chatbot icon (bottom right)                                    |  |
|  |  - Chat window opens (full screen on mobile)                          |  |
|  |  - Type question using mobile keyboard                                |  |
|  |  - Tap send button                                                    |  |
|  |  - Response displayed in chat                                         |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

---

## Conversion Funnel

### Funnel Stages

```
+=============================================================================+
|                     CONVERSION FUNNEL                                        |
|                                                                             |
|  Stage 1: Awareness                                                         |
|  +-----------------------------------------------------------------------+  |
|  |  - User discovers website                                              |  |
|  |  - Source: LinkedIn, GitHub, Google, Referral                         |  |
|  |  - Landing page: Homepage, About, Projects                            |  |
|  |  - Metric: Unique visitors                                             |  |
|  |  - Current: 1,000/month                                               |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Stage 2: Interest                                                            |
|  +-----------------------------------------------------------------------+  |
|  |  - User engages with content                                           |  |
|  |  - Actions: Scroll, click, hover                                      |  |
|  |  - Pages: Homepage, About, Projects                                   |  |
|  |  - Metric: Pages per session, time on site                            |  |
|  |  - Current: 3 pages/session, 2 min                                   |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Stage 3: Consideration                                                      |
|  +-----------------------------------------------------------------------+  |
|  |  - User explores specific content                                     |  |
|  |  - Actions: Project deep dive, verify certs, chatbot questions         |  |
|  |  - Pages: Projects, Certifications, Achievements                      |  |
|  |  - Metric: Engagement rate, chatbot usage                             |  |
|  |  - Current: 20% engagement, 10% chatbot usage                         |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Stage 4: Intent                                                              |
|  +-----------------------------------------------------------------------+  |
|  |  - User decides to take action                                        |  |
|  |  - Actions: Click "Contact Me", visit Contact page                    |  |
|  |  - Pages: Contact, About                                              |  |
|  |  - Metric: Contact page visits                                        |  |
|  |  - Current: 5% of visitors                                            |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Stage 5: Conversion                                                         |
|  +-----------------------------------------------------------------------+  |
|  |  - User completes desired action                                      |  |
|  |  - Actions: Submit form, send email, connect on LinkedIn              |  |
|  |  - Pages: Contact, external (LinkedIn, GitHub)                        |  |
|  |  - Metric: Conversion rate                                            |  |
|  |  - Current: 5% of contact page visitors                               |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

---

## Contribution Guidelines

### Welcome

Welcome to the Arkan Tsabit Portfolio contributing guide! This document provides comprehensive guidelines for contributing to the project. Whether you're fixing a bug, adding a feature, or improving documentation, your contributions are valuable.

### Contribution Types

| Type | Description |
|------|-------------|
| Bug Fixes | Fixing issues in the code |
| Features | Adding new functionality |
| Documentation | Improving docs and comments |
| Design | UI/UX improvements |
| Testing | Adding or improving tests |
| Performance | Optimizing code and assets |

### Quick Links

| Resource | URL |
|----------|-----|
| Repository | https://github.com/ArkanTsabit123/arkan-tsabit.github.io |
| Issues | https://github.com/ArkanTsabit123/arkan-tsabit.github.io/issues |
| Projects | https://github.com/ArkanTsabit123/arkan-tsabit.github.io/projects |
| Discussions | https://github.com/ArkanTsabit123/arkan-tsabit.github.io/discussions |
| Pull Requests | https://github.com/ArkanTsabit123/arkan-tsabit.github.io/pulls |

---

## Code of Conduct

### Our Pledge

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive Behavior Examples:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable Behavior Examples:**
- The use of sexualized language or imagery
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate

### Reporting

If you experience or witness unacceptable behavior, please report it by contacting:
- **Email**: arkantsabit025@gmail.com

---

## Getting Started for Contributors

### Prerequisites

| Requirement | Version | Installation |
|-------------|---------|--------------|
| Git | 2.x | https://git-scm.com/downloads |
| Python | 3.9+ | https://python.org/downloads |
| Node.js | 16.x+ | https://nodejs.org/download |
| Wrangler CLI | Latest | `npm install -g wrangler` |
| Text Editor | Any | VS Code recommended |

### Setup Development Environment

```bash
# 1. Fork the repository
# Click "Fork" button on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/arkan-tsabit.github.io.git
cd arkan-tsabit.github.io

# 3. Add upstream remote
git remote add upstream https://github.com/ArkanTsabit123/arkan-tsabit.github.io.git

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Install Node dependencies (if any)
npm install

# 6. Set up environment variables
cp .env.example .env
# Edit .env with your credentials

# 7. Start local development server
python -m http.server 8000

# 8. Open browser
# http://localhost:8000
```

---

## Development Workflow

### Basic Workflow

```
+=============================================================================+
|                     DEVELOPMENT WORKFLOW                                    |
|                                                                             |
|  Step 1: Find or Create Issue                                              |
|  +-----------------------------------------------------------------------+  |
|  |  - Search existing issues                                               |  |
|  |  - Create new issue if needed                                           |  |
|  |  - Assign yourself to the issue                                         |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 2: Create Branch                                                       |
|  +-----------------------------------------------------------------------+  |
|  |  - Create branch from main                                             |  |
|  |  - Branch naming: feature/description or fix/description              |  |
|  |  - Example: feature/add-new-project                                    |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 3: Make Changes                                                        |
|  +-----------------------------------------------------------------------+  |
|  |  - Write code                                                          |  |
|  |  - Follow coding standards                                             |  |
|  |  - Test changes locally                                                |  |
|  |  - Update documentation                                                |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 4: Commit Changes                                                      |
|  +-----------------------------------------------------------------------+  |
|  |  - Stage changes: git add .                                            |  |
|  |  - Commit with proper message: git commit -m "..."                    |  |
|  |  - Push to fork: git push origin branch-name                          |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 5: Create Pull Request                                                 |
|  +-----------------------------------------------------------------------+  |
|  |  - Open pull request to main branch                                   |  |
|  |  - Link to issue                                                       |  |
|  |  - Fill PR template                                                    |  |
|  |  - Request review                                                      |  |
|  +-----------------------------------------------------------------------+  |
|                                      |                                       |
|                                      v                                       |
|  Step 6: Review and Merge                                                    |
|  +-----------------------------------------------------------------------+  |
|  |  - Address review feedback                                             |  |
|  |  - Pass CI/CD checks                                                   |  |
|  |  - PR approved                                                         |  |
|  |  - Merge to main branch                                               |  |
|  +-----------------------------------------------------------------------+  |
|                                                                             |
+=============================================================================+
```

### Branch Naming Convention

| Branch Type | Format | Example |
|-------------|--------|---------|
| Feature | `feature/description` | `feature/add-chatbot` |
| Bug Fix | `fix/description` | `fix/nav-bar-error` |
| Documentation | `docs/description` | `docs/update-readme` |
| Performance | `perf/description` | `perf/optimize-images` |
| Security | `security/description` | `security/fix-cors` |
| Testing | `test/description` | `test/add-unit-tests` |

---

## Code Style Guidelines

### HTML Guidelines

```html
<!-- GOOD: Semantic HTML -->
<header>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about.html">About</a></li>
    </ul>
  </nav>
</header>

<main>
  <section>
    <h1>Welcome</h1>
    <p>Content goes here.</p>
  </section>
</main>

<footer>
  <p>&copy; 2026 Arkan Tsabit</p>
</footer>
```

### CSS Guidelines

```css
/* GOOD: CSS with variables and comments */
:root {
  --primary-color: #2563EB;
  --secondary-color: #6B7280;
  --background-color: #FFFFFF;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

/* GOOD: BEM naming */
.button {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
}

.button--primary {
  background-color: var(--primary-color);
  color: white;
}
```

### JavaScript Guidelines

```javascript
// GOOD: Clean, documented JavaScript
async function loadProjects(filter = 'all') {
  try {
    const response = await fetch('/data/projects.json');
    const data = await response.json();
    const filtered = filter === 'all' ? data : data.filter(p => p.technologies.includes(filter));
    renderProjects(filtered);
  } catch (error) {
    console.error('Failed to load projects:', error);
    showError('Failed to load projects');
  }
}
```

---

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types

| Type | Description | Example |
|------|-------------|---------|
| feat | New feature | `feat(chatbot): add vector search` |
| fix | Bug fix | `fix(nav): fix mobile menu toggle` |
| docs | Documentation | `docs(readme): update setup instructions` |
| style | Code style | `style(css): format with prettier` |
| refactor | Code refactoring | `refactor(api): simplify error handling` |
| perf | Performance | `perf(images): compress and optimize images` |
| test | Testing | `test(chatbot): add unit tests` |
| chore | Maintenance | `chore(deps): update dependencies` |
| security | Security | `security(env): rotate API tokens` |

---

## Pull Request Process

### PR Template

```markdown
## Description
[Description of the changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring
- [ ] Security fix
- [ ] Other

## Related Issues
Closes #[issue_number]

## Checklist
- [ ] I have read the contributing guidelines
- [ ] I have tested my changes locally
- [ ] I have updated documentation
- [ ] I have added tests for my changes
- [ ] All tests are passing
- [ ] My code follows the project's style guidelines
```

### PR Checklist

| Check | Description |
|-------|-------------|
| ✅ | Read contributing guidelines |
| ✅ | Tested changes locally |
| ✅ | Updated documentation |
| ✅ | Added tests (if needed) |
| ✅ | All tests passing |
| ✅ | Code style guidelines followed |
| ✅ | No merge conflicts |
| ✅ | PR description filled properly |
| ✅ | Linked to related issue |

---

## Testing Guidelines

### Running Tests

```bash
# Run chatbot test suite
cd chatbot
python test_all.py

# Run portfolio validation
python checker.py

# Run HTML validation
npx html-validator --file index.html

# Run CSS linting
npx stylelint "css/*.css"

# Run JavaScript linting
npx eslint "js/*.js"

# Run link checking
npx link-checker http://localhost:8000

# Run security scan
pip install safety
safety check
```

### Test Coverage

| Component | Current Coverage | Target |
|-----------|------------------|--------|
| Python | 34/34 tests | 100% |
| HTML | Manual | 100% |
| CSS | Manual | 100% |
| JavaScript | Manual | 100% |

---

## Issue Reporting

### Bug Report Template

```markdown
## Bug Description
[Clear and concise description of the bug]

## Steps to Reproduce
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Screenshots
[If applicable, add screenshots]

## Environment
- Browser: [Chrome/Firefox/Safari]
- Version: [e.g., 120]
- OS: [Windows/Mac/Linux]
- Device: [Desktop/Mobile]
```

### Feature Request Template

```markdown
## Feature Description
[Clear and concise description of the feature]

## Problem Solved
[What problem does this feature solve?]

## Proposed Solution
[How should this feature work?]

## Alternatives Considered
[Any alternative solutions considered]

## Additional Context
[Any other context or screenshots]
```

---

## Review Process

### Code Review Checklist

| Check | Description |
|-------|-------------|
| ✅ | Code follows style guidelines |
| ✅ | Code is properly documented |
| ✅ | Tests are added/updated |
| ✅ | Tests are passing |
| ✅ | No security vulnerabilities |
| ✅ | No performance regressions |
| ✅ | Accessibility standards met |
| ✅ | Browser compatibility verified |

### Review Response Guidelines

| Response | Description |
|----------|-------------|
| Approve | Ready to merge |
| Request Changes | Changes needed before merge |
| Comment | General feedback, no changes needed |
| Block | Major issue, cannot merge |

### Review Timeline

| Step | Time Limit |
|------|------------|
| Initial Review | 24-48 hours |
| Response to Feedback | 24-48 hours |
| Final Review | 24 hours |
| Merge | Within 24 hours of approval |

---

## Release Process

### Versioning

| Version | Format | Example |
|---------|--------|---------|
| Major | X.0.0 | 2.0.0 |
| Minor | X.Y.0 | 1.2.0 |
| Patch | X.Y.Z | 1.1.1 |

### Release Checklist

| No | Task | Status |
|----|------|--------|
| 1 | All tests passing | ⬜ |
| 2 | All PRs merged | ⬜ |
| 3 | Documentation updated | ⬜ |
| 4 | CHANGELOG.md updated | ⬜ |
| 5 | Version bumped | ⬜ |
| 6 | Deployed to production | ⬜ |
| 7 | Production verified | ⬜ |

### Release Types

| Type | Description | Frequency |
|------|-------------|-----------|
| Major | Breaking changes | Yearly |
| Minor | New features | Quarterly |
| Patch | Bug fixes | Monthly |

---

## Resources

### Development Resources

| Resource | URL |
|----------|-----|
| HTML5 | https://developer.mozilla.org/en-US/docs/Web/HTML |
| CSS3 | https://developer.mozilla.org/en-US/docs/Web/CSS |
| JavaScript | https://developer.mozilla.org/en-US/docs/Web/JavaScript |
| Python | https://docs.python.org/3/ |
| Cloudflare Workers | https://developers.cloudflare.com/workers/ |
| Cloudflare Vectorize | https://developers.cloudflare.com/vectorize/ |

### Getting Help

| Issue Type | Where to Ask |
|------------|--------------|
| Technical Questions | GitHub Discussions |
| Bug Reports | GitHub Issues |
| Feature Requests | GitHub Issues |
| General Questions | GitHub Discussions |
| Security Issues | Email (private) |

### Response Times

| Type | Response Time |
|------|---------------|
| General Questions | 24-48 hours |
| Bug Reports | 24-48 hours |
| Feature Requests | 48-72 hours |
| Security Issues | < 24 hours |
| PR Review | 24-48 hours |

---

Built by Arkan Tsabit | Data Engineer | Cloud Data Engineer