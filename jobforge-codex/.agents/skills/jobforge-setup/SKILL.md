---
name: jobforge-setup
description: >-
  JobForge onboarding skill. Use when the user wants to get started with
  JobForge, upload or provide their resume for the first time, set job
  search preferences (target roles, salary, location), import LinkedIn
  contacts, or run a work history interview to build their career profile.
  Trigger phrases: "set up jobforge", "get started", "upload my resume",
  "first time setup", "job preferences", "work history interview",
  "onboard", "configure jobforge".
argument-hint: "'interview' to skip directly to the work history interview"
---

# JobForge Setup Skill

> **Priority hierarchy**: See `.agents/shared/references/priority-hierarchy.md`.

One-time onboarding. Run this before all other JobForge skills.

## Quick Start

- Ask the agent: **"Set up JobForge"** — Full onboarding (skips steps already done)
- Ask the agent: **"Run the work history interview"** — Interview only (resume + prefs already done)

## File Structure

```
scripts/
  conduct-interview.md    # Work history interview guide
```

Profile template: `.agents/shared/templates/profile.md`

## Data Directory

Resolve using `.agents/shared/references/data-directory.md`.
For setup: if no `.jobforge/` folder exists, create `~/.jobforge/` in Step 1.

---

## Workflow

### Step 0: Check What's Already Done

Resolve the data directory. Check which exist with real content (not just templates):
- `DATA_DIR/resume/` — has at least one file
- `DATA_DIR/preferences.md`
- `DATA_DIR/profile.md`
- `DATA_DIR/application-data.md`

If argument is "interview", jump to Step 4 (verify resume exists first).
If everything is already done, say so and list available skills. Otherwise run only missing steps.

---

### Step 1: Resume Upload

Ask the user to provide their resume. Accept:
- File path → copy to `DATA_DIR/resume/`
- Pasted text → save as `DATA_DIR/resume/resume.md`

Confirm it was saved. Briefly summarize: name, most recent role, number of roles, estimated years experience.

---

### Step 2: Job Preferences

Ask in one natural, conversational question:

> "What kind of jobs are you looking for? Tell me about target roles, where you want to work, salary expectations, and anything you'd want to filter out."

Save `DATA_DIR/preferences.md`:

```markdown
# Job Preferences

## Target Roles
- [parsed from response]

## Location & Remote
[parsed from response]

## Compensation
- Minimum: $[X]
- Target: $[Y]

## Must-Haves
- [parsed]

## Dealbreakers
- [parsed — these trigger automatic Skip in job search]

## Nice-to-Haves
- [parsed]
```

---

### Step 3: LinkedIn Contacts (Optional)

If `DATA_DIR/linkedin-contacts.csv` doesn't exist, ask:

> "Want to import your LinkedIn contacts? This flags when you know someone at a company that's hiring. Completely optional."

If yes, give export instructions:
> 1. Go to linkedin.com/mypreferences/d/download-my-data
> 2. Select "Connections" only → request download
> 3. LinkedIn emails a link (usually within minutes)
> 4. Download ZIP → find `Connections.csv` inside → share the path

Save as `DATA_DIR/linkedin-contacts.csv`. Confirm: "Imported [N] contacts."

---

### Step 4: Work History Interview

Read `scripts/conduct-interview.md` and follow its instructions. Cover every role, most recent first.

After the interview, save to `DATA_DIR/profile.md` using the template at `.agents/shared/templates/profile.md`.

---

### Step 5: Application Data

Extract from resume: first name, last name, email, phone, city, country, LinkedIn, GitHub, portfolio.

Present findings. Ask user to confirm and fill gaps (work authorization, visa sponsorship).
EEO defaults: all set to "Decline to self-identify" unless user specifies otherwise.

Save to `DATA_DIR/application-data.md`:

```markdown
# Application Data

## Personal Information
- First Name: ...
- Last Name: ...
- Email: ...
- Phone: ...
- City: ...
- Country: ...

## Online Profiles
- LinkedIn: ...
- GitHub: ...
- Portfolio: ...

## Standard Answers
- How did you hear about us: Job Board
- Previously worked at this company: No
- Authorized to work: [Yes/No]
- Requires visa sponsorship: [Yes/No]

## EEO / Voluntary Disclosures
- Gender: Decline to self-identify
- Race/Ethnicity: Decline to self-identify
- Veteran status: I am not a veteran
- Disability: I don't wish to answer
```

---

### Step 6: Summary

```
You're all set! Here's what we saved:

- Resume: [filename] in DATA_DIR/resume/
- Preferences: [brief summary]
- LinkedIn Contacts: [N imported / skipped]
- Work History Profile: [N roles]
- Application Data: [name + email confirmed]

You can now ask me to:
  → Find matching jobs
  → Score your resume (ATS score)
  → Tailor your resume for a specific job
  → Write a cover letter
  → Apply to a job (fill + approve)
  → View your application tracker
```

---

## Response Format

1. **Setup Summary** — what was saved with brief details
2. **What's Next** — list of available skills

---

## Permissions Required

```json
{
  "permissions": {
    "allow": [
      "Read(~/.jobforge/**)",
      "Write(~/.jobforge/**)",
      "Edit(~/.jobforge/**)"
    ]
  }
}
```
