# JobForge â€” AI Career Agent Plugin

> AI-powered resume analysis, job search, ATS optimization, tailored cover letters, and form auto-fill with approval.

---

## What This Is

JobForge is a Claude Code plugin (and Antigravity-compatible skill set) that turns your raw resume into high-quality, tailored job applications â€” with you in control at every step.

It mirrors the structure of the [Proficiently](https://proficiently.com) skill set, rebuilt from scratch as an open, extensible plugin.

---

## Skills

| Command | What It Does |
|---------|-------------|
| `/jobforge:setup` | One-time onboarding â€” resume, preferences, work history interview |
| `/jobforge:ats-score` | Score your resume (0â€“100) with detailed breakdown and fixes |
| `/jobforge:job-search` | Find matching jobs, scored for fit, with network connection flags |
| `/jobforge:tailor-resume` | Rewrite your resume for a specific job posting |
| `/jobforge:cover-letter` | Write a tailored, human-sounding cover letter |
| `/jobforge:apply` | Fill the application form + get approval before submitting |
| `/jobforge:track` | View application tracker, update statuses, get follow-up reminders |

---

## Quick Start

**Step 1:** Install the plugin in Claude Code or add the `.agents/` folder to your project.

**Step 2:** Run setup:
```
/jobforge:setup
```

**Step 3:** Find jobs:
```
/jobforge:job-search
```

**Step 4:** Tailor and apply:
```
/jobforge:tailor-resume https://jobs.example.com/engineer
/jobforge:cover-letter last
/jobforge:apply last
```

---

## Data Storage

All your data is stored locally in `.jobforge/` (current directory) or `~/.jobforge/` (home directory). Nothing is sent anywhere except to Claude's context window.

```
~/.jobforge/
  resume/              # Your resume file(s)
  preferences.md       # Job search preferences
  profile.md           # Detailed work history from interview
  application-data.md  # Personal info + standard form answers
  linkedin-contacts.csv
  jobs/                # One folder per job
    [company]-[date]/
      posting.md       # Job description
      resume.md        # Tailored resume
      cover-letter.md  # Cover letter
      answers.md       # Form Q&A
      applied.md       # Application log
  job-history.md       # Running log of all jobs seen
  ats-reports/         # Saved ATS score reports
```

---

## Core Principles

1. **Never fabricate** â€” Only uses what's real in your resume and profile
2. **Human approval required** â€” Will never submit an application without your explicit confirmation
3. **Quality over quantity** â€” Fewer, better applications beat mass-applying
4. **Local-first** â€” All data stays on your machine

---

## Requirements

- Claude Code (or Antigravity with browser MCP tools for job search and auto-apply)
- For job search + apply: browser MCP tools enabled (`mcp__browser__*` permissions)
- For setup + ats-score + tailor + track: no browser needed

---





For Codex Desktop specific setup, see [CODEX_SETUP_GUIDE.md](../CODEX_SETUP_GUIDE.md).

