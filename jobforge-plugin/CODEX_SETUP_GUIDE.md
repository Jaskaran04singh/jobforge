# 📖 Codex Desktop Setup & User Guide for JobForge

This guide explains how to use **JobForge** inside **Codex Desktop** for automated job searches, ATS resume scoring, tailoring, and job applications.

---

## 🛠️ Global Availability

JobForge is installed in your user directory:
- **Skills Directory:** `C:\Users\Jaskaran Singh\.codex\skills\`
- **Standing Context:** `C:\Users\Jaskaran Singh\.codex\AGENTS.md`
- **User Data Storage:** `C:\Users\Jaskaran Singh\.jobforge\`

Because of this setup, **Codex Desktop recognizes all JobForge capabilities in ANY folder or project** you open.

---

## 🚀 Step-by-Step Usage Guide

### 1. Initial Profile Setup (First Time Only)
Tell Codex to set up your profile and provide your resume:
> **Prompt:**  
> `Set up JobForge for me. Here is my resume: [paste text or file path]`

Codex will:
1. Parse your work experience, skills, and contact details.
2. Store your profile in `~/.jobforge/profile.md`.
3. Ask for your target roles, salary expectations, and location/remote preferences.

---

### 2. Check ATS Score
Evaluate your resume against Applicant Tracking System standards:
> **Prompt:**  
> `Score my resume against ATS criteria`  
> *(or `Check my ATS score against [Job URL / Description]`)*

Codex will:
- Return a 0–100 score with category breakdowns.
- Highlight missing keywords for your target role.
- Provide a prioritized list of bullet points to improve.

---

### 3. Search 100+ Jobs Across Multiple Portals
Search across LinkedIn, Indeed, Naukri, Apna, Shine, and HiringCafe in one step:
> **Prompt:**  
> `Find 100+ jobs for React Developer in India`  
> *(or `Search 100 jobs matching my resume across LinkedIn and Naukri`)*

Codex will:
- Query multiple platforms simultaneously.
- Aggregate and deduplicate openings.
- Rank jobs by fit (High / Medium / Skip).
- Provide direct application links.

---

### 4. Tailor Resume for a Specific Role
Customize your resume for a job posting without any fabrication:
> **Prompt:**  
> `Tailor my resume for this job: [Paste URL or Description]`  
> *(or `Optimize my resume for the last job found`)*

Codex will:
- Reorder and reframe achievements to highlight relevant experience.
- Naturally integrate required keywords from the job description.
- Save the tailored version to `~/.jobforge/jobs/[company]-[date]/resume.md`.

---

### 5. Generate a Cover Letter
Create a concise, human-grade cover letter connecting your achievements to the company's needs:
> **Prompt:**  
> `Write a cover letter for the last job`  
> *(or `Draft a cover letter for [Company Name]`)*

Codex will:
- Write a 250–350 word letter with a company-specific hook.
- Avoid generic AI buzzwords.
- Save to `~/.jobforge/jobs/[company]-[date]/cover-letter.md`.

---

### 6. Scan Network Connections
Find roles at companies where you have 1st-degree connections:
> **Prompt:**  
> `Scan my network for open jobs`

*(Requires your exported LinkedIn connections at `~/.jobforge/linkedin-contacts.csv`)*

---

### 7. Form Pre-Filling & Application
Fill application forms on Greenhouse, Lever, or Workday:
> **Prompt:**  
> `Help me apply to the last job`

Codex will:
1. Scan the form and present a single summary of proposed answers.
2. Pre-fill the fields upon your approval.
3. Pause before final submission and ask: *"Type 'submit' to finish."* (Never submits without explicit confirmation).

---

### 8. Application Pipeline Tracker
View and update your job applications:
> **Prompt:**  
> `Show my application tracker`  
> *(or `Update Google status to interview`)*

Codex will:
- Display your active pipeline (Applied, Interview, Offer, Rejected).
- Highlight applications that haven't responded in 7+ days for follow-up.

---

## ⚡ Quick Prompt Reference

| Goal | What to say in Codex Desktop |
| :--- | :--- |
| **Setup Profile** | `Set up JobForge for me. Here is my resume: [paste text]` |
| **ATS Score** | `Score my resume against ATS criteria` |
| **Search 100+ Jobs** | `Search 100+ jobs for [Role] in [Location] across LinkedIn and Naukri` |
| **Tailor Resume** | `Tailor my resume for [Job URL / Description]` |
| **Cover Letter** | `Write a cover letter for the last job` |
| **Network Scan** | `Scan my network for hiring companies` |
| **Apply** | `Help me apply to the last job` |
| **Track Pipeline** | `Show my application tracker` |

---

## 🔒 Privacy & Local Storage
All your resumes, personal data, and job application history stay strictly on your local machine at:
`C:\Users\Jaskaran Singh\.jobforge`
