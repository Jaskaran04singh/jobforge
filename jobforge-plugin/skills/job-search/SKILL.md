---
name: job-search
description: Search for jobs matching the user's resume and preferences. Scores each job for fit, flags network connections, and saves top matches to job folders for tailoring and applying.
argument-hint: "optional keyword to search (e.g. 'senior engineer remote')"
---

# JobForge Job Search Skill

> **Priority hierarchy**: See `shared/references/priority-hierarchy.md` for conflict resolution.

Find jobs that match the user's profile and preferences. Score every result. Surface network connections.

## Quick Start

- `/jobforge:job-search` — Run search using default terms from preferences
- `/jobforge:job-search senior product manager` — Search with specific keywords

## File Structure

```
scripts/
  evaluate-jobs.md         # Job evaluation subagent prompt
assets/
  templates/
    job-entry.md           # Template for a single job-history entry
    job-history-init.md    # Template for new job-history.md file
    matching-rules.md      # Matching rule reference
```

## Data Directory

Resolve the data directory using `shared/references/data-directory.md`. Resume and preferences are both required.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. Resume and `preferences.md` are both required. Load all files listed in Step 1.

---

### Step 1: Load Context

Read:
- `DATA_DIR/resume/*` — candidate profile and skills
- `DATA_DIR/preferences.md` — target roles, location, salary, dealbreakers
- `DATA_DIR/job-history.md` — to avoid showing duplicate jobs (if file exists)
- `DATA_DIR/linkedin-contacts.csv` — for network matching (if file exists)

Extract search terms from:
1. `$ARGUMENTS` if provided
2. Target roles from `preferences.md`

---

### Step 2: Search for Jobs

Use browser tools to search job boards. Start with:
- **hiring.cafe** — broad aggregator, good signal-to-noise
- **LinkedIn Jobs** (search only, do not use Easy Apply from here)
- **wellfound.com** (for startups)

For each search term, enter the query and apply relevant filters (date posted: last 7 days, location/remote, experience level).

**Extracting results — IMPORTANT:**
Do NOT use `get_page_text` on job listing pages. It blows out the context window.

Instead use `javascript_tool` to pull only structured listing data:

```javascript
Array.from(document.querySelectorAll('[class*="job"], [class*="listing"], [class*="card"], [role="listitem"]'))
  .slice(0, 50)
  .map(el => el.innerText.trim())
  .filter(t => t.length > 20 && t.length < 500)
  .join('\n---\n')
```

If that doesn't work, take a screenshot to understand page structure, then write a targeted JS selector. Goal: title + company + location + salary only.

**Note:** Never show hiring.cafe links to the user. Resolve direct employer URLs in Step 5.

---

### Step 3: Score Each Job

For each result, apply the fit scoring criteria in `shared/references/fit-scoring.md`.

Also check the ats-rules keyword match from `shared/references/ats-rules.md` — does the job's required skills overlap with the resume?

---

### Step 4: Save to Job History

Append ALL jobs seen (not just good fits) to `DATA_DIR/job-history.md` to avoid duplicates in future searches:

```markdown
## [DATE] — Search: "[terms]"

| Job Title | Company | Location | Salary | Fit | Notes |
|-----------|---------|----------|--------|-----|-------|
| ... | ... | ... | ... | High/Med/Low/Skip | ... |
```

If `job-history.md` doesn't exist, create it using `assets/templates/job-history-init.md`.

---

### Step 5: Resolve Employer URLs & Save Top Job Folders

For each **High-fit** job:
1. Click through to the actual employer careers page (not the aggregator link)
2. Capture the direct employer job posting URL
3. Extract job description using `javascript_tool`:
   ```javascript
   document.querySelector('[class*="description"], [class*="content"], article, main')?.innerText
   ```
   Do NOT use `get_page_text` — employer pages have huge footers that bloat context.
4. Save to `DATA_DIR/jobs/[company-slug]-[YYYYMMDD]/posting.md` with the direct URL at the top

For **Medium-fit** jobs: resolve the employer URL only (don't save full posting yet).

If you can't resolve a direct link, note the company name so the user can find it themselves. Never show aggregator URLs to the user.

---

### Step 6: Check Network Connections

If `DATA_DIR/linkedin-contacts.csv` was loaded, cross-reference each result's company name against the "Company" column using fuzzy matching ("Google" matches "Google LLC", "Alphabet/Google").

If there's a match, note the contact's name and title for the results output.

---

### Step 7: Present Results

Show only new High and Medium fit jobs not already in the user's job history.

```markdown
## Job Search Results — [DATE]
Search: "[terms used]"

---

### 🟢 HIGH FIT

#### 1. [Job Title] at [Company]
- **Why it fits**: [2–3 specific reasons based on resume + preferences]
- **Salary**: $Xk–$Yk
- **Location**: [Remote / City]
- **Network**: You know [Name] ([Title]) at [Company]  ← omit if no match
- **Apply**: [direct employer URL]

---

### 🟡 MEDIUM FIT

#### 1. [Job Title] at [Company]
- **Why it's medium**: [what matches, what's missing]
- **Salary**: $Xk
- **Location**: [location]
- **Apply**: [direct employer URL]
```

Omit the Network line if there's no connection. Omit Medium section if empty.

---

### Step 8: Offer Next Steps

```
Next steps:
  /jobforge:tailor-resume [URL]    — Tailor your resume for a specific job
  /jobforge:cover-letter [URL]     — Write a cover letter
  /jobforge:apply [URL]            — Fill and submit the full application
  /jobforge:job-search [keywords]  — Search with different terms
```

**IMPORTANT:** Do NOT tailor resumes, write cover letters, or fill applications yourself in this skill. Those are separate skills. If the user asks, direct them to the right command.

---

### Step 9: Learn from Feedback

If the user gives feedback on results, update `DATA_DIR/preferences.md`:
- "No agencies" → add to Dealbreakers
- "Only AI companies" → add to Nice-to-Haves
- "Minimum $200k total comp" → update Compensation

---

## Response Format

1. **Top Matches** — High and Medium fit jobs with company, role, fit rating, salary, location, network connections, and direct URL
2. **Next Steps** — what to run next

---

## Permissions Required

```json
{
  "permissions": {
    "allow": [
      "Read(~/.jobforge/**)",
      "Write(~/.jobforge/**)",
      "Edit(~/.jobforge/**)",
      "mcp__browser__*"
    ]
  }
}
```
