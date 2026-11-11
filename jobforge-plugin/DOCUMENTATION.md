# 📖 JobForge — Complete Documentation & User Manual

Welcome to **JobForge**, an AI career automation suite built for **Codex Desktop** and **Claude Code**.

JobForge assists you through the full job hunt pipeline:
1. **Resume Intake & Work History Profiling**
2. **ATS Scoring & Gap Diagnostics**
3. **Automated Search & Company Fit Evaluation**
4. **Tailoring Resumes per Job Posting**
5. **Human-Grade Cover Letter Generation**
6. **LinkedIn Network Scanning for Warm Introductions**
7. **Form Pre-Filling & Controlled Auto-Apply**
8. **Application Pipeline Tracking**
9. **Headless Telegram Assistant Loop**

---

## 🛠️ Global Setup & Installation

### For Codex Desktop (Any Folder)
All skills are installed globally in:
`C:\Users\Jaskaran Singh\.codex\skills\`

Whenever you open **any folder or workspace** in Codex Desktop, Codex automatically recognizes all `jobforge-*` skills without extra configuration.

---

## 📚 Detailed Skill Documentation & Usage

---

### 1. 🏁 Setup & Onboarding (`jobforge-setup`)

**Purpose:**
Initializes your local storage profile. It parses your resume, asks about your preferences (roles, target salary, remote vs hybrid), and conducts a structured work history interview to capture quantifiable metrics.

* **Trigger in Codex Desktop:**
  * *"Set up JobForge for me"*
  * *"Onboard my resume"*
* **Inputs:**
  * Attach your resume file, paste the full file path, or paste raw text.
* **Outputs:**
  * Saves structured files under `~/.jobforge/`:
    * `resume/` (Original resume files)
    * `preferences.md` (Role, location, compensation filters)
    * `profile.md` (Deep career accomplishment database)
    * `application-data.md` (Contact details & standard EEO preferences)

---

### 2. 📊 ATS Score (`jobforge-ats-score`)

**Purpose:**
Scores your resume out of 100 points against modern Applicant Tracking System standards (Greenhouse, Lever, Workday) and pinpoints exactly what to fix.

* **Trigger in Codex Desktop:**
  * *"Score my resume against ATS"*
  * *"What is my ATS score?"*
  * *"Check my resume against [Job URL / Description]"*
* **Outputs:**
  * **Score:** 0–100 with category grade.
  * **Breakdown:** Keyword Match (25), Quantified Results (20), Structure (15), Format Safety (10), Action Verbs (10), Skills (10), Dates (5), Length (5).
  * **Critical Fixes:** Ranked list of high-impact adjustments.
  * **Missing Keywords:** Exact terms missing for your target role.

---

### 3. 🔍 Job Search (`jobforge-job-search`)

**Purpose:**
Finds active job postings that match your profile. Scores each job (High, Medium, Skip) and flags companies where you have LinkedIn connections.

* **Trigger in Codex Desktop:**
  * *"Find jobs matching my resume"*
  * *"Search for remote Senior Backend Engineer roles"*
* **Outputs:**
  * Curated list of matching openings.
  * Direct careers URLs (bypassing job board aggregators).
  * Auto-saves high-fit job postings to `~/.jobforge/jobs/[company]-[date]/posting.md`.

---

### 4. ✍️ Tailor Resume (`jobforge-tailor-resume`)

**Purpose:**
Customizes your resume for a specific role. Mirrors keywords and job terminology, highlights relevant achievements, rewrites weak bullets, and guarantees high human readability.

* **Trigger in Codex Desktop:**
  * *"Tailor my resume for [Job URL or Description]"*
  * *"Optimize my resume for the last job found"*
* **Safety Rule:**
  * **Zero Fabrication:** Never invents fake degrees, titles, or metrics.
* **Outputs:**
  * Complete tailored resume saved to `~/.jobforge/jobs/[company]-[date]/resume.md`.
  * Summary changelog explaining what changed and why.

---

### 5. ✉️ Cover Letter (`jobforge-cover-letter`)

**Purpose:**
Drafts a 250–350 word cover letter connecting your quantifiable achievements to the employer's needs.

* **Trigger in Codex Desktop:**
  * *"Write a cover letter for the last job"*
  * *"Draft a cover letter for [Company Name]"*
* **Outputs:**
  * Custom letter formatted with an engaging opening hook (no AI clichés).
  * Saved to `~/.jobforge/jobs/[company]-[date]/cover-letter.md`.

---

### 6. 🌐 Network Scan (`jobforge-network-scan`)

**Purpose:**
Cross-references your exported LinkedIn connections against company career pages to find jobs where you can request a warm referral.

* **Trigger in Codex Desktop:**
  * *"Scan my network for open jobs"*
  * *"Check companies from my last 50 LinkedIn contacts"*
* **Prerequisites:**
  * Place your exported `Connections.csv` from LinkedIn at `~/.jobforge/linkedin-contacts.csv`.
* **Outputs:**
  * Matches grouped by company and mutual contacts for warm intros.

---

### 7. 🚀 Apply (`jobforge-apply`)

**Purpose:**
Automates form filling on Greenhouse, Lever, and Workday with mandatory human-in-the-loop review.

* **Trigger in Codex Desktop:**
  * *"Help me apply to the last job"*
  * *"Apply to https://jobs.lever.co/..."*
* **How It Works:**
  1. Scans form inputs (name, email, work authorization, custom questions).
  2. Presents a **single approval summary** in chat.
  3. Pre-fills fields automatically.
  4. **Stops before submission** and asks for explicit confirmation ("type submit to confirm").

---

### 8. 📈 Application Tracker (`jobforge-track`)

**Purpose:**
Maintains your job application pipeline and alerts you when applications need follow-ups.

* **Trigger in Codex Desktop:**
  * *"Show my application tracker"*
  * *"Which applications need a follow-up?"*
  * *"Update Stripe status to interview"*
* **Outputs:**
  * Real-time metrics: Total Applied, Response Rate, Active Pipeline, Offers.
  * Follow-up warnings for applications over 7 days old.

---

### 9. 🤖 Telegram Assistant Loop (`jobforge-telegram`)

**Purpose:**
Allows you to control JobForge headlessly directly from Telegram while you are away from your desk.

* **Trigger in Codex Desktop:**
  * *"Run Telegram job assistant"*
* **Telegram Commands:**
  * Send any job link ➔ Prepares tailored resume & proposals.
  * `search [keywords]` ➔ Searches for openings.
  * `status` ➔ Shows current pipeline status.

---

## 🔒 Privacy & Local-First Philosophy
* All resume files, profiles, credentials, and job folders are stored locally on your machine at `~/.jobforge/`.
* No external databases or third-party trackers are used.
