---
name: apply
description: Fill out a job application form on Greenhouse, Lever, Workday, Ashby, or other ATS platforms — with tailored resume, cover letter, smart form answers, and mandatory user approval before submitting
argument-hint: "job URL, 'last' to use the most recent job, or 'current' to fill the active browser tab"
---

# JobForge Apply Skill

> **Priority hierarchy**: See `shared/references/priority-hierarchy.md` for conflict resolution.
> **Non-negotiable rule**: NEVER submit a form without explicit user confirmation in the current session.

Fill job application forms intelligently — resume, cover letter, every field — then wait for the user to approve before clicking Submit.

## Quick Start

- `/jobforge:apply` — Asks for a job URL or uses the most recent job
- `/jobforge:apply https://...` — Apply to a specific job
- `/jobforge:apply last` — Apply using the most recently saved job folder
- `/jobforge:apply current` — Fill the application form already open in the browser

## File Structure

```
scripts/
  fill-page.md    # Form-filling subagent prompt
```

## Data Directory

Resolve the data directory using `shared/references/data-directory.md`. Resume is required.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. Resume required. Load `DATA_DIR/application-data.md` if it exists.

---

### Step 1: Determine Target Job

**If `$ARGUMENTS` is a URL:**
- Check if a matching job folder exists in `DATA_DIR/jobs/` (match by company slug or URL)
- If found: load `posting.md`, `resume.md`, `cover-letter.md` from that folder
- If not: use browser tools to fetch the posting and save to a new job folder

**If `$ARGUMENTS` is "last" or empty:**
- Find the most recently modified job folder in `DATA_DIR/jobs/`
- Load its `posting.md`, `resume.md`, `cover-letter.md`
- Confirm with user: "Applying to [Role] at [Company]. Right?"

**If `$ARGUMENTS` is "current":**
- Skip navigation — use the active browser tab as-is
- Try to match the tab's URL to a saved job folder to load context

Report what's loaded:
```
Applying to [Role] at [Company].
Resume: [loaded from job folder / original]
Cover letter: [loaded / will generate if needed]
```

---

### Step 2: Build / Load Application Data

If `DATA_DIR/application-data.md` exists: read it and load all values.

If it does NOT exist:
1. Extract from resume: name, email, phone, LinkedIn, location
2. Present to user. Ask them to confirm and fill gaps: work authorization, visa sponsorship, EEO preferences
3. Save to `DATA_DIR/application-data.md` (see format in setup skill Step 5)

---

### Step 3: Navigate to Form and Scout

Use browser tools to navigate to the application form.

Detect ATS type using `shared/references/ats-patterns.md`.

**Lever** — Append `/apply` to URL or click "APPLY FOR THIS JOB"
**Greenhouse** — Extract iframe tokens via JS, navigate to direct form URL
**Workday** — Click "Apply Now", choose "Apply Manually", handle auth gate if present
**Ashby / Other** — Navigate to URL, take screenshot if needed to identify form

**Scout the form** (read-only, do NOT fill during this step):
- Is there a resume upload field?
- Is there a cover letter upload or text field?
- Are there unusual required fields?

Record these requirements — they determine what materials to generate in Step 4.

---

### Step 4: Generate Missing Materials

**Resume:** Always tailor before applying.
- If `DATA_DIR/jobs/[job-folder]/resume.md` exists → use it. Skip.
- If not → run the tailor-resume skill inline (read `skills/tailor-resume/SKILL.md`). Present it briefly for user review before continuing.

**Cover letter:** Only if the form has a cover letter field.
- If `DATA_DIR/jobs/[job-folder]/cover-letter.md` exists → use it. Skip.
- If not → run the cover-letter skill inline (read `skills/cover-letter/SKILL.md`). Present briefly.
- If the form has no cover letter field → skip cover letter entirely.

Report what was prepared:
```
Prepared for [Role] at [Company]:
- Tailored resume: [generated / already existed]
- Cover letter: [generated / already existed / not required]

Ready to fill the form. Proceeding...
```

---

### Step 5: Scan All Fields

Scan the entire form to discover every field. Do NOT fill anything yet.

**Lever / Greenhouse (single-page):** `read_page(tabId, filter="interactive")` to get all fields at once.

**Workday (multi-step wizard):**
- Scroll top-to-bottom, calling `read_page` at each viewport position
- Collect all field labels, types, and required status
- Note: scan each wizard page as you reach it in Step 7

For each field found, record:
- Label, type (text/dropdown/radio/checkbox/file), required status, element ref

---

### Step 6: Propose Answers — Get ONE Approval

Generate a proposed answer for every field using this priority order:
1. `application-data.md` — match field label to stored data (see Field Matching Reference below)
2. Reasonable defaults for common fields (legal name = name, signature = full name, arbitration = Accept)
3. Custom answers section of `application-data.md` (cached from previous applications)
4. Best guess based on field label and job context
5. "Need your input" — only if truly ambiguous

Present ONE consolidated summary to the user:

```
Here's my plan for the [Company] application:

Auto-fill from your profile:
- First Name: [X]
- Last Name: [X]
- Email: [X]
- Phone: [X]
- LinkedIn: [X]
[...all standard fields...]

Proposed answers (please review):
- Legal First Name: [X] (same as first name)
- Electronic signature: [X]
- Arbitration agreement: Accept
- "How did you hear about us": Job Board
- [Any non-obvious fields with proposed answers]

Needs your input:
- [Only truly ambiguous fields — list them here]

Manual upload required:
- Resume: [file path]  ← please upload while reviewing
- Cover letter: [file path]  ← please upload while reviewing

Approve and I'll fill everything in. Or tell me what to change.
```

**Key rule:** One approval, then fill. Do NOT interrupt with per-field questions during form filling.

After approval (with any edits), cache any new answers in `DATA_DIR/application-data.md` under a "Custom Answers" section for future use.

---

### Step 7: Fill the Form

After user approves, fill everything in one pass. Delegate to `scripts/fill-page.md` with:
- ATS type
- Approved field→value mapping
- Tab ID
- File paths for uploads

**For multi-page forms (Workday):**
1. Fill current page → click "Save and Continue"
2. If validation errors: read them, fix fields, retry
3. On new page: scan fields, match against approved answers, fill, advance
4. Repeat until reaching the review/confirmation page

**File uploads:** MCP browser tools can upload images but not PDFs directly. Tell the user the file path and ask them to upload the PDF manually. (Include this in the Step 6 summary so they know in advance.)

---

### Step 8: Review Before Submit — MANDATORY

When the review page is reached or all fields on a single-page form are filled:
1. Take a screenshot
2. Confirm everything looks correct
3. **Ask explicitly for confirmation:**

```
The application is filled and ready.

[Screenshot summary of what was filled]

Type "submit" to submit the application, or tell me what to change first.
```

**Do NOT click Submit until the user types confirmation.**

---

### Step 9: Log the Application

After submission (or if user decides not to submit):

Create `DATA_DIR/jobs/[company-slug]-[date]/applied.md`:

```markdown
# Application Log

- **Role**: [Job Title]
- **Company**: [Company]
- **Date**: [YYYY-MM-DD]
- **ATS**: [Greenhouse/Lever/Workday/etc.]
- **Status**: Submitted / Draft (not submitted)
- **Notes**: [any notes]
```

Update `DATA_DIR/job-history.md` — find the entry for this job and add application status and date.

Present to user:
```
Applied to [Role] at [Company] on [date].

Files saved to: DATA_DIR/jobs/[folder]/

What's next?
  /jobforge:apply [URL]     — Apply to another job
  /jobforge:job-search      — Find more matching jobs
  /jobforge:track           — View your application tracker
```

---

## Field Matching Reference

| Label pattern | Data source |
|---------------|------------|
| `first name` | Personal.FirstName |
| `last name` | Personal.LastName |
| `full name` | Personal.FirstName + LastName |
| `email` | Personal.Email |
| `phone` | Personal.Phone |
| `city`, `location` | Personal.City |
| `country` | Personal.Country |
| `linkedin` | Profiles.LinkedIn |
| `github` | Profiles.GitHub |
| `portfolio`, `website` | Profiles.Portfolio |
| `resume`, `cv` | File upload |
| `cover letter` | File upload |
| `how did you hear` | "Job Board" |
| `previously worked here` | "No" |
| `work authorization` | StandardAnswers.WorkAuth |
| `sponsorship` | StandardAnswers.Sponsorship |
| `gender` | "Decline to self-identify" |
| `race`, `ethnicity` | "Decline to self-identify" |
| `veteran` | "I am not a veteran" |
| `disability` | "I don't wish to answer" |
| `legal first name` | Same as first name |
| `signature` | Full name |
| `arbitration` | Accept |
| `terms`, `acknowledgment` | Accept |

**Unrecognized fields:** If required → ask user. If optional → skip. Cache user answers for reuse.

---

## Response Format

1. **Application Status** — what was filled, what was skipped, submission confirmation
2. **Files Saved** — paths to job folder files and application log
3. **Next Steps** — next job to apply to, or job search

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
