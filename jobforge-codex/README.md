# JobForge — AI Career Agent (Codex Edition)

> AI-powered resume analysis, job search, ATS optimization, tailored cover letters, and form auto-fill with approval — built for OpenAI Codex CLI.

---

## What This Is

JobForge is a Codex CLI skill set (also compatible with any agent that supports `.agents/skills/`) that turns your raw resume into high-quality, tailored job applications — with you in full control at every step.

This is the **Codex Edition** — same skills, same workflows as the Claude Code plugin version, structured for Codex's `.agents/skills/` discovery system.

---

## Skills

| Ask the agent... | What it does |
|-----------------|-------------|
| "Set up JobForge" | One-time onboarding — resume, preferences, work history interview |
| "Score my resume" | 100-pt ATS score with breakdown and ranked fixes |
| "Find matching jobs" | Browser search → fit scoring → network connections → job folders |
| "Tailor my resume for [URL]" | Rewrite resume for a specific job posting |
| "Write a cover letter for [URL]" | Tailored, human-sounding cover letter |
| "Apply to [URL]" | Fill the form → get approval → submit |
| "Show my application tracker" | Pipeline view, response rate, follow-up reminders |

---

## Quick Start

**Step 1 — Add to your Codex setup:**

Option A — Add to your global Codex skills:
```
# Copy the .agents folder to your home directory
cp -r .agents ~/.agents
```

Option B — Project-specific (place in your working directory):
```
# Just work from within this folder, or copy .agents/ to your project root
```

Option C — Global Codex config path:
```
# Copy skills to ~/.codex/skills/
cp -r .agents/skills/* ~/.codex/skills/
```

**Step 2 — Run setup:**
```
codex "Set up JobForge"
```

**Step 3 — Find jobs:**
```
codex "Find matching jobs"
```

**Step 4 — Apply:**
```
codex "Tailor my resume for https://jobs.example.com/engineer"
codex "Write a cover letter for the last job"
codex "Apply to the last job"
```

---

## Discovery Paths

Codex auto-discovers skills from (highest to lowest priority):
1. `[current-directory]/.agents/skills/`
2. `[repo-root]/.agents/skills/`
3. `~/.codex/skills/`

Place this `.agents/` folder in whichever location fits your workflow.

---

## Data Storage

All data is stored locally in `.jobforge/` or `~/.jobforge/`. Nothing is sent anywhere except to the AI model's context window.

```
~/.jobforge/
  resume/              # Your resume file(s)
  preferences.md       # Job search preferences
  profile.md           # Detailed work history
  application-data.md  # Personal info + form answers
  linkedin-contacts.csv
  jobs/                # One folder per job
    [company]-[date]/
      posting.md
      resume.md
      cover-letter.md
      answers.md
      applied.md
  job-history.md
  ats-reports/
```

---

## Core Principles

1. **Never fabricate** — Only uses what's real in your resume and profile
2. **Human approval required** — Will never submit an application without your explicit "submit" confirmation
3. **Quality over quantity** — Fewer, better applications beat mass-applying
4. **Local-first** — All data stays on your machine

---

## Comparison: Codex vs Claude Code Editions

| | Codex Edition | Claude Code Edition |
|-|--------------|---------------------|
| Discovery path | `.agents/skills/` | `.claude-plugin/` |
| Skill format | `SKILL.md` with YAML frontmatter | `SKILL.md` with YAML frontmatter |
| Invocation | Natural language to Codex | `/jobforge:skillname` slash commands |
| Shared references | Same files | Same files |
| Features | Identical | Identical |

---

## Requirements

- OpenAI Codex CLI
- For job search + apply skills: browser MCP tools enabled (`mcp__browser__*` permissions)
- For setup + ats-score + tailor + track: no browser needed

---

## License

MIT
