---
name: jobforge-job-search
description: >-
  Search for jobs that match the user's resume and preferences. Use when the
  user asks to "find jobs", "search for jobs", "what jobs fit me", "job
  matches", "find me a job", "look for openings", "daily job search", or
  "search [keyword] jobs". Scores every result for fit using the user's
  preferences and dealbreakers. Flags when the user has LinkedIn connections
  at a company. Saves high-fit job postings to data folders for tailoring
  and applying. Accepts optional search keywords as argument.
argument-hint: "optional search keyword (e.g. 'senior engineer remote', 'product manager fintech')"
---

# JobForge Job Search Skill

> **Priority hierarchy**: See `.agents/shared/references/priority-hierarchy.md`.

Find jobs that match the user's profile. Score every result. Flag network connections. Save top postings.

## Quick Start

- Ask: **"Find matching jobs"** — searches using default terms from preferences
- Ask: **"Search for senior engineer jobs"** — searches with specific keywords

## File Structure

```
scripts/
  evaluate-jobs.md         # Job evaluation subagent prompt
assets/
  templates/
    job-history-init.md    # Template for new job-history.md
```

## Data Directory

Resolve using `.agents/shared/references/data-directory.md`. Resume and preferences are both required.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. `DATA_DIR/resume/` and `DATA_DIR/preferences.md` are both required.

---

### Step 1: Load Context

Read:
- `DATA_DIR/resume/*` — skills, experience, primary role
- `DATA_DIR/preferences.md` — target roles, location, salary, dealbreakers
- `DATA_DIR/job-history.md` — to avoid duplicate results (load if it exists)
- `DATA_DIR/linkedin-contacts.csv` — for network matching (load if it exists)

Extract search terms from:
1. User's argument/request (keywords they specified)
2. Target roles from `preferences.md`

---

### Step 2: Search for Jobs

Use browser tools to search job boards. Start with:
- **hiring.cafe** — broad aggregator, good signal-to-noise
- **wellfound.com** — for startup roles
- **LinkedIn Jobs** — search only (do not use Easy Apply from here)

For each search term, enter the query and apply filters: date posted (last 7 days), location, remote/onsite preference.

**Extracting results — IMPORTANT:**
Do NOT use `get_page_text` on listing pages — it overloads the context window.

Use `javascript_tool` to extract only structured listing rows:

```javascript
Array.from(document.querySelectorAll('[class*="job"],[class*="listing"],[class*="card"],[role="listitem"]'))
  .slice(0, 50)
  .map(el => el.innerText.trim())
  .filter(t => t.length > 20 && t.length < 500)
  .join('\n---\n')
```

If that selector doesn't match, take a screenshot to understand the structure, then write a targeted JS selector. Goal: title + company + location + salary only — not the full page.

**Never show aggregator URLs to the user.** Resolve direct employer URLs in Step 5.

---

### Step 3: Score Each Job

For each result, apply the fit scoring criteria in `.agents/shared/references/fit-scoring.md`.

Also check keyword overlap between job requirements and resume skills using `.agents/shared/references/ats-rules.md`.

---

### Step 4: Save to Job History

Append ALL jobs seen (not just good fits) to `DATA_DIR/job-history.md` to avoid duplicates in future searches:

```markdown
## [DATE] — Search: "[terms]"

| Job Title | Company | Location | Salary | Fit | Notes |
|-----------|---------|----------|--------|-----|-------|
| ... | ... | ... | ... | High/Med/Low/Skip | ... |
```

Create the file if it doesn't exist.

---

### Step 5: Resolve Employer URLs & Save Top Job Folders

For each **High-fit** job:
1. Click through to the actual employer careers page
2. Capture the direct employer job posting URL
3. Extract job description using `javascript_tool`:
   ```javascript
   document.querySelector('[class*="description"],[class*="content"],article,main')?.innerText
   ```
4. Save to `DATA_DIR/jobs/[company-slug]-[YYYYMMDD]/posting.md` with the direct URL at the top

For **Medium-fit** jobs: resolve direct URL only (don't save full posting).

If the direct link can't be resolved, note the company name so the user can find it themselves.

---

### Step 6: Check Network Connections

If `DATA_DIR/linkedin-contacts.csv` was loaded, cross-reference each company name against the CSV "Company" column using fuzzy matching ("Google" matches "Google LLC", "Alphabet/Google").

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
- **Salary**: $Xk–$Yk (or "Not listed")
- **Location**: [Remote / City, State]
- **Network**: You know [Name] ([Title]) at [Company]
- **Apply**: [direct employer URL]

---

### 🟡 MEDIUM FIT

#### 1. [Job Title] at [Company]
- **Why it's medium**: [what matches, what's missing]
- **Salary**: $Xk
- **Location**: [location]
- **Apply**: [direct employer URL]
```

Omit Network line if no connection. Omit Medium section if empty.

---

### Step 8: Offer Next Steps

```
Next steps:
  → "Tailor my resume for [company URL]" — optimize resume for a specific job
  → "Write a cover letter for [company URL]" — write a tailored letter
  → "Apply to [company URL]" — fill and submit the application
  → "Search for [different keywords]" — try a different search
```

**Do NOT tailor resumes, write cover letters, or fill applications in this skill.** Those are separate skills. Direct the user to ask for them explicitly.

---

### Step 9: Learn from Feedback

If the user gives feedback on results, update `DATA_DIR/preferences.md` immediately:
- "No agencies" → add to Dealbreakers
- "Only AI companies" → add to Nice-to-Haves
- "Minimum $200k total comp" → update Compensation section

---

## Response Format

1. **Top Matches** — High and Medium fits with company, role, salary, location, network, URL
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
