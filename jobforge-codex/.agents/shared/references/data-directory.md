# Data Directory Resolution

All user data lives in a `.jobforge/` folder. Follow these steps every time a skill starts.

## Resolution Algorithm

1. Check the current working directory for `.jobforge/` — use it if found.
2. Check `~/.jobforge/` — use it if found.
3. If neither exists:
   - **setup skill**: Fresh install. Create `~/.jobforge/` in Step 1.
   - **All other skills**: Stop and tell the user:
     > "Run `/jobforge:setup` first to get started. It only takes a few minutes."

## Ephemeral Session Warning

If the working directory looks like a temp/session path (e.g. `/tmp/`, `/sessions/`, or a system path), tell the user:

> "Please open a persistent folder before running JobForge skills so your data is saved between sessions."

Do NOT proceed without a confirmed persistent folder.

## DATA_DIR Folder Tree

All paths in skill instructions use `DATA_DIR` to refer to whichever `.jobforge/` directory was found or created.

```
DATA_DIR/
  resume/                  # Original resume file(s) uploaded by user
  preferences.md           # Job preferences: roles, salary, location, filters
  profile.md               # Detailed work history from setup interview
  application-data.md      # Personal info + standard form answers
  linkedin-contacts.csv    # LinkedIn connections export (optional)
  jobs/                    # One sub-folder per job
    [company-slug]-[date]/
      posting.md           # Parsed job description
      resume.md            # Tailored resume for this job
      cover-letter.md      # Tailored cover letter
      answers.md           # Form Q&A for this job
      applied.md           # Application log (created after applying)
  job-history.md           # Running log of all jobs seen/applied to
  ats-reports/             # Saved ATS score reports
```
