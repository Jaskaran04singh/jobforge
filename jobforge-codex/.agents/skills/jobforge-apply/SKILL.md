---
name: jobforge-apply
description: >-
  Fill out a job application form automatically and submit it only after
  explicit user approval. Use when the user asks to "apply to [job URL]",
  "fill the application form", "submit my application", "auto-apply",
  "apply to the last job", "complete the application", or "fill out the form
  for [company]". Supports Greenhouse, Lever, Workday, Ashby, and other
  ATS platforms. Always tailors the resume and generates answers for form
  questions before filling. Presents a full plan for user approval before
  touching the Submit button. Saves an application log after submitting.
argument-hint: "job URL, 'last' to use the most recent job, or 'current' for the active browser tab"
---

# JobForge Apply Skill

> **Priority hierarchy**: See `.agents/shared/references/priority-hierarchy.md`.
> **Non-negotiable**: NEVER submit a form without explicit user confirmation in the current session.

Fill job application forms intelligently — resume, cover letter, every field — then wait for the user to approve before clicking Submit.

## Quick Start

- Ask: **"Apply to [job URL]"**
- Ask: **"Apply to the last job"**
- Ask: **"Fill the application form that's open in my browser"**

## File Structure

```
scripts/
  fill-page.md    # Form-filling subagent prompt
```

## Data Directory

Resolve using `.agents/shared/references/data-directory.md`. Resume is required.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. Resume required. Load `DATA_DIR/application-data.md` if it exists.

---

### Step 1: Determine Target Job

**If a URL is provided:**
- Check if a matching job folder exists in `DATA_DIR/jobs/`
- If found: load `posting.md`, `resume.md`, `cover-letter.md` from that folder
- If not: fetch the posting and save to a new job folder

**If argument is "last" or no argument:**
- Find the most recently modified folder in `DATA_DIR/jobs/`
- Load its files
- Confirm: "Applying to [Role] at [Company]. Right?"

**If argument is "current":**
- Skip navigation — use the active browser tab
- Try to match the tab URL to a saved job folder

---

### Step 2: Build / Load Application Data

If `DATA_DIR/application-data.md` exists: read it, load all values.

If it does NOT exist:
1. Extract from resume: name, email, phone, LinkedIn, location
2. Present to user. Ask to confirm and fill gaps: work authorization, visa sponsorship
3. EEO defaults: all "Decline to self-identify"
4. Save to `DATA_DIR/application-data.md` (see format in jobforge-setup Step 5)

---

### Step 3: Navigate to Form and Scout

Use browser tools to navigate to the application form.
Detect ATS type using `.agents/shared/references/ats-patterns.md`.

- **Lever** — append `/apply` to job URL or click "APPLY FOR THIS JOB"
- **Greenhouse** — extract iframe tokens via JS, navigate to direct form URL
- **Workday** — click "Apply Now", choose "Apply Manually", handle auth gate if present (user must sign in themselves)
- **Ashby / Other** — navigate to URL, take screenshot if needed

**Scout the form** (read-only, do NOT fill during this step):
- Is there a resume upload field?
- Is there a cover letter upload or text field?
- Any unusual required fields?

Record these requirements — they determine what materials to generate in Step 4.

---

### Step 4: Generate Missing Materials

**Resume:** Always tailor before applying.
- If `DATA_DIR/jobs/[job-folder]/resume.md` exists → use it
- If not → run `jobforge-tailor-resume` skill inline. Present for quick review before continuing.

**Cover letter:** Only if the form has a cover letter field.
- If `DATA_DIR/jobs/[job-folder]/cover-letter.md` exists → use it
- If not → run `jobforge-cover-letter` skill inline. Present for quick review.
- If no cover letter field on the form → skip entirely.

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

**Lever / Greenhouse:** `read_page(tabId, filter="interactive")` to get all fields at once.

**Workday (multi-step wizard):**
- Scroll top-to-bottom, calling `read_page` at each viewport position
- Collect all field labels, types, and required status
- Scan each wizard page as you reach it in Step 7

For each field: record label, type, required status, element ref.

---

### Step 6: Propose Answers — Get ONE Approval

Generate a proposed answer for every field using this priority:
1. `application-data.md` — match field label (see Field Matching Reference below)
2. Reasonable defaults: legal name = name, signature = full name, arbitration = Accept
3. Custom answers from `application-data.md` (cached from previous applications)
4. Best guess from field label and job context
5. "Need your input" — only if truly ambiguous

Present ONE consolidated summary:

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
- [Only truly ambiguous required fields]

Manual upload required:
- Resume: [file path]  ← please upload while reviewing
- Cover letter: [file path]  ← if applicable

Type "approve" and I'll fill everything in. Or tell me what to change.
```

**Key rule:** One approval, then fill. Do NOT interrupt with per-field questions.
Cache any new answers in `DATA_DIR/application-data.md` under "Custom Answers" for future use.

---

### Step 7: Fill the Form

After user approves, fill everything in one pass. Delegate to `scripts/fill-page.md` with:
- ATS type, approved field→value mapping, tab ID, file paths

**For multi-page forms (Workday):**
1. Fill current page → click "Save and Continue"
2. If validation errors: read them, fix, retry
3. On new page: scan fields, match against approved answers, fill, advance
4. Repeat until reaching the review page

**File uploads:** Tell the user the file path and ask them to upload the PDF manually — this is a known browser limitation.

---

### Step 8: Review Before Submit — MANDATORY

When the review page is reached or all fields on a single-page form are filled:
1. Take a screenshot
2. Confirm everything looks correct
3. Ask explicitly:

```
The application is filled and ready.

[Screenshot summary]

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

```
Applied to [Role] at [Company] on [date].

Files saved to: DATA_DIR/jobs/[folder]/

What's next?
  → "Apply to [next-job-url]" — apply to another job
  → "Find more jobs" — run job search again
  → "Show my application tracker" — view all applications
```

---

## Field Matching Reference

| Label pattern | Data source |
|---------------|------------|
| `first name` | Personal.FirstName |
| `last name` | Personal.LastName |
| `full name` | FirstName + LastName |
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
| `arbitration`, `terms` | Accept |

Unrecognized fields: if required → ask user; if optional → skip. Cache user answers.

---

## Response Format

1. **Application Status** — what was filled, what was skipped, submission confirmation
2. **Files Saved** — paths to job folder files and application log
3. **Next Steps** — next job or tracker

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
