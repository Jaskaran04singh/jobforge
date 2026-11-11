---
name: setup
description: One-time onboarding — upload resume, set job preferences, and do a work history interview so all other JobForge skills have full context
argument-hint: "'interview' to skip to the work history interview only"
---

# JobForge Setup Skill

> **Priority hierarchy**: See `shared/references/priority-hierarchy.md` for conflict resolution.

One-time onboarding. Run this before any other JobForge skill.

## Quick Start

- `/jobforge:setup` — Full onboarding (skips steps already completed)
- `/jobforge:setup interview` — Run only the work history interview (resume + prefs already done)

## File Structure

```
scripts/
  conduct-interview.md    # Work history interview guide
```

Profile template: `shared/templates/profile.md`

## Data Directory

Resolve the data directory using `shared/references/data-directory.md`. For setup, if no `.jobforge/` folder exists, create it at `~/.jobforge/` in Step 1.

---

## Workflow

### Step 0: Check What's Already Done

Resolve the data directory. Check which of these exist with real content (not just templates):
- `DATA_DIR/resume/` (has at least one file)
- `DATA_DIR/preferences.md`
- `DATA_DIR/profile.md`
- `DATA_DIR/application-data.md`

If `$ARGUMENTS` is "interview", skip directly to Step 4 (but verify resume exists first).

If everything exists and is populated, tell the user they're set up and list available skills. Otherwise run only the missing steps in order.

---

### Step 1: Resume Upload

Ask the user to provide their resume. Accept:
- A file path → copy it to `DATA_DIR/resume/`
- Pasted text → save as `DATA_DIR/resume/resume.md`

Confirm it was saved. Briefly summarize what you see: name, most recent role, number of roles, and total years of experience (estimate from dates).

---

### Step 2: Job Preferences

Ask in one natural, conversational question:

> "What kind of jobs are you looking for? Tell me about target roles, where you want to work (location/remote), salary expectations, and anything you'd want to filter out."

From their response, save `DATA_DIR/preferences.md`:

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
- [parsed from response]

## Dealbreakers
- [parsed from response — these trigger automatic Skip in job search]

## Nice-to-Haves
- [parsed from response]
```

If they leave something out, that's fine — save what you have. They can update at any time by editing the file or telling you a correction during any skill session.

---

### Step 3: LinkedIn Contacts (Optional)

If `DATA_DIR/linkedin-contacts.csv` doesn't exist, ask:

> "Want to import your LinkedIn contacts? This lets us flag when you know someone at a company that's hiring. You can skip this — it's optional."

If they want to proceed:

> **How to export LinkedIn connections:**
> 1. Go to linkedin.com/mypreferences/d/download-my-data
> 2. Select "Connections" only and request the download
> 3. LinkedIn emails a link (usually within minutes)
> 4. Download the ZIP, find `Connections.csv` inside
> 5. Share the file path or paste the CSV contents here

Save as `DATA_DIR/linkedin-contacts.csv`. Confirm: "Imported [N] contacts."

If they skip, move on.

---

### Step 4: Work History Interview

Read `scripts/conduct-interview.md` and follow its instructions to conduct a conversational interview. Cover every role on their resume, most recent first.

After the interview, save to `DATA_DIR/profile.md` using the template at `shared/templates/profile.md`.

---

### Step 5: Application Data

Extract from their resume: first name, last name, email, phone, city, country, LinkedIn, GitHub, portfolio.

Present what you found and ask the user to confirm and fill gaps:
- Work authorization (e.g. "US citizen", "Requires H1B")
- Visa sponsorship needed (Yes / No)
- EEO defaults (pre-fill all as "Decline to self-identify" unless user wants otherwise)

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
- Preferences: [brief summary — target roles + key criteria]
- LinkedIn Contacts: [N imported / skipped]
- Work History Profile: [N roles covered]
- Application Data: [name + email confirmed]

You can now use:
  /jobforge:job-search        — Find matching jobs
  /jobforge:ats-score         — Score your resume
  /jobforge:tailor-resume     — Tailor resume for a specific job
  /jobforge:cover-letter      — Write a cover letter
  /jobforge:apply             — Fill and submit an application
  /jobforge:track             — View your application tracker
```

---

## Response Format

1. **Setup Summary** — what was saved (resume, preferences, contacts, profile, application data)
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
