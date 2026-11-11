# 🚀 JobForge — Universal AI Career Agent & 100+ Job Aggregator

> **AI-powered career assistant for OpenAI Codex Desktop, Claude Code, and Google Antigravity.**
> Intelligently searches 100+ jobs across major portals, optimizes resumes for ATS filters, drafts human-grade cover letters, and helps you apply with explicit approval.

---

## 🌟 What's New in v1.1.0

- **🌐 100+ Multi-Platform Aggregation Engine**:
  - Concurrently searches **LinkedIn Jobs, Indeed (Global & India), Naukri.com, Apna.co, Shine.com, and HiringCafe**.
  - Multi-page automated scraping (start=0, 25, 50 / pageNo=1, 2, 3).
  - Automatic deduplication using normalized 	itle + company signatures.
  - Smart fit-scoring against your resume and preferences.
- **🤖 Triple AI Ecosystem Compatibility**:
  - **OpenAI Codex Desktop**: Global configuration under ~/.codex/skills/ with natural language triggers.
  - **Claude Code**: Packaged under jobforge-plugin/ with slash command support (/job-search, etc.).
  - **Google Antigravity**: Packaged under jobforge-skill/ with interactive workflows.
- **🔒 Local-First Privacy**:
  - All data (resumes, work history profiles, credentials, application logs) remains on your local machine at ~/.jobforge/.

---

## 📁 Repository Structure

| Directory | Target Platform | Description |
| :--- | :--- | :--- |
| **jobforge-codex/** | **OpenAI Codex Desktop** | Natural language skills + global \AGENTS.md\ context |
| **jobforge-plugin/** | **Claude Code** | Modular plugin with slash command triggers |
| **jobforge-skill/** | **Google Antigravity** | Unified interactive skill with progressive disclosure |
| **jobforge-saas/** | **Full Web SaaS** | Dockerized FastAPI backend & Next.js frontend scaffolding |
| **DOCUMENTATION.md** | **All Platforms** | Comprehensive guide & prompt triggers for every skill |

---

## 🛠️ The 9 Skills at a Glance

| Skill | Codex Trigger | Claude Slash Command | Description |
| :--- | :--- | :--- | :--- |
| **Setup** | *"Set up JobForge with my resume"* | \/jobforge:setup\ | Resume intake, job preferences & work history interview |
| **ATS Scorer** | *"Check my ATS score"* | \/jobforge:ats-score\ | 100-point ATS scorer with ranked fixes and missing keywords |
| **Job Search** | *"Search 100+ jobs across LinkedIn and Naukri"* | \/jobforge:job-search\ | Multi-platform aggregator (LinkedIn, Indeed, Naukri, Apna, Shine, HiringCafe) |
| **Tailor Resume** | *"Tailor my resume for [job link]"* | \/jobforge:tailor-resume\ | Zero-hallucination keyword optimization and bullet rewrites |
| **Cover Letter** | *"Write a cover letter for [company]"* | \/jobforge:cover-letter\ | 250–350 word letter connecting measurable achievements to the role |
| **Network Scan** | *"Scan my network for jobs"* | \/jobforge:network-scan\ | Cross-references LinkedIn connections with company career boards |
| **Apply** | *"Help me apply to the last job"* | \/jobforge:apply\ | Automated form filling with mandatory review before submit |
| **Tracker** | *"Show my application tracker"* | \/jobforge:track\ | Live pipeline dashboard with 7-day follow-up reminders |
| **Telegram** | *"Run Telegram job assistant"* | \/jobforge:jobsearch-telegram\ | Headless background assistant to manage applications via chat |

---

## 🚀 Quick Start Guide

### 1. Codex Desktop
Open Codex Desktop and ask:
> *"Set up JobForge for me. Here is my resume: [paste text or file path]"*

### 2. Claude Code
In your project directory, run:
`ash
/jobforge:setup
`

### 3. Read the Full Documentation
See [DOCUMENTATION.md](./DOCUMENTATION.md) for detailed inputs, workflows, and response formats.

---



