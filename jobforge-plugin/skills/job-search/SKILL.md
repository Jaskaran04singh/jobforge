---
name: jobforge-job-search
description: >-
  Search 100 to 1000+ jobs across multiple major job portals simultaneously:
  LinkedIn, Indeed, Naukri, Unstop, Apna, Shine, Foundit, and direct ATS boards
  (Greenhouse, Lever, Workday). Use when user asks to "find 100 jobs", "search
  everywhere", "find jobs on LinkedIn and Naukri", "search Unstop and Apna",
  "mass job search", "find high volume jobs", or "scan all portals for [role]".
  Scores every job against candidate preferences, deduplicates cross-platform
  listings, and saves verified openings into the application pipeline.
argument-hint: "keywords and optional count (e.g. 'frontend developer remote 100' or 'naukri linkedin python')"
---

# JobForge High-Volume Multi-Platform Job Search

> **Priority hierarchy**: See `.agents/shared/references/priority-hierarchy.md`.

Search and harvest 100 to 1000+ targeted job postings across all major domestic and global platforms:
- **LinkedIn**
- **Indeed**
- **Naukri.com**
- **Unstop** (College / Freshers / Tech)
- **Apna.co** (Rapid hiring & local/remote tech)
- **Shine.com**
- **Foundit (Monster)**
- **Hiring.cafe / Direct ATS** (Greenhouse, Lever, Workday)

## Quick Start
- *"Search 100 jobs for Full Stack Developer across LinkedIn, Naukri, and Unstop"*
- *"Find all remote Python jobs on Indeed, Apna, and Shine"*
- *"Scan all platforms for 200 software engineering roles"*

---

## High-Volume Search Workflow

### Step 1: Query Formulation & Multi-Platform Dispatch
1. Parse user keywords, target locations, and desired volume (default: 50–100, max: 1000).
2. Execute `scripts/engines/multi_platform_search.py` to generate targeted search feeds for:
   - LinkedIn, Naukri, Indeed, Unstop, Apna, Shine, Foundit.
3. Open or scrape search streams in parallel:
   - **For ATS / Hiring.cafe:** Query direct employer postings.
   - **For Naukri / Indeed / Shine:** Extract job cards with title, company, experience bracket, salary, and direct URL.
   - **For Unstop / Apna:** Extract quick-apply opportunities and direct recruiter postings.

### Step 2: Extraction & Deduplication
1. Collect raw listings using browser JavaScript selectors:
   ```javascript
   Array.from(document.querySelectorAll('[class*="job"],[class*="card"],[data-job-id]'))
     .map(el => ({
        title: el.querySelector('h2,h3,[class*="title"]')?.innerText,
        company: el.querySelector('[class*="company"]')?.innerText,
        location: el.querySelector('[class*="location"]')?.innerText,
        url: el.querySelector('a')?.href
     }))
   ```
2. Feed all raw results through `deduplicate_jobs()` to eliminate identical positions posted across multiple portals.

### Step 3: Fast-Batch Fit Scoring
Score all harvested jobs (100–1000) into buckets:
- **🟢 High Fit (80–100% Match):** Match role, salary, skills, and pass dealbreakers.
- **🟡 Medium Fit (60–79% Match):** Good alignment, learnable skill gaps.
- **⛔ Skip:** Mismatched location, blacklist companies, or hard dealbreakers.

### Step 4: Batch Pipeline Export
1. Save the aggregated master manifest to:
   `~/.jobforge/search-batches/[YYYYMMDD]-[keywords]-manifest.json`
2. Append all unique jobs into `~/.jobforge/job-history.md`.
3. Auto-create job folders in `~/.jobforge/jobs/` for the top **High-Fit** positions so they are immediately queued for batch-applying.

---

## Response Format
Present results grouped by platform with a high-level summary table:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 MULTI-PLATFORM HARVEST RESULTS ([Total Found] Jobs)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LinkedIn : [Count] | Naukri : [Count] | Unstop : [Count]
Indeed   : [Count] | Apna   : [Count] | Shine  : [Count]
Direct   : [Count]

🟢 TOP HIGH-FIT MATCHES (Ready to Apply)
1. [Role] at [Company] — [Platform] — [Salary] — [Apply URL]
2. [Role] at [Company] — [Platform] — [Salary] — [Apply URL]
...

Next Action:
Say "Batch apply to top 20 high-fit jobs" or "Apply to all LinkedIn Easy Apply jobs"
```
