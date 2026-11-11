---
name: ats-score
description: Score a resume against ATS criteria and get a detailed improvement report with missing keywords, weak sections, and specific fixes
argument-hint: "optional job URL or job description to score against a specific role"
---

# JobForge ATS Score Skill

> **Priority hierarchy**: See `shared/references/priority-hierarchy.md` for conflict resolution.

Analyze a resume against ATS criteria and produce an actionable improvement report.

## Quick Start

- `/jobforge:ats-score` — Score your resume against general criteria for your target role
- `/jobforge:ats-score https://...` — Score against a specific job posting

## Data Directory

Resolve the data directory using `shared/references/data-directory.md`. Resume is required.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. Resume in `DATA_DIR/resume/` is required. Load `DATA_DIR/preferences.md` if it exists.

If `$ARGUMENTS` is a URL, fetch the job posting (browser or ask user to paste). Extract keywords and requirements.

---

### Step 1: Load Resume

Read the resume from `DATA_DIR/resume/`. If multiple files exist, ask the user which one to score.

---

### Step 2: Score the Resume

Apply all scoring rules from `shared/references/ats-rules.md`.

If a job description was provided, use its keywords for the keyword match category.
If not, use standard keywords for the user's target role (from `preferences.md` or resume's primary role).

---

### Step 3: Present Report

```
📊 ATS SCORE: [X]/100  [grade emoji] [grade label]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORE BREAKDOWN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keyword Match        [X]/25   [█████░░░░░]
Quantified Results   [X]/20   [████░░░░░░]
Section Structure    [X]/15   [███████░░░]
Formatting Safety    [X]/10   [██████████]
Action Verbs         [X]/10   [████░░░░░░]
Skills Section       [X]/10   [███████░░░]
Date Consistency     [X]/5    [█████░░░░░]
Length               [X]/5    [██████████]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ STRENGTHS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [strength 1]
- [strength 2]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  CRITICAL FIXES (biggest impact first)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Issue — specific, actionable fix]
2. [Issue — specific, actionable fix]
3. [Issue — specific, actionable fix]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔑 MISSING KEYWORDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
[keyword1], [keyword2], [keyword3], ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 NEXT STEP
━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Recommend: tailor for a specific job / fix top issues first / apply now if score is good]
```

---

### Step 4: Save Report

Save the full report to `DATA_DIR/ats-reports/[date]-[role-slug].md`.

Tell the user the file path.

---

### Step 5: Offer Next Steps

After showing the report, suggest:
- `/jobforge:tailor-resume [job URL]` — Optimize resume for a specific job
- `/jobforge:job-search` — Find matching jobs
- Fix the top issues manually and re-run this skill

---

## Response Format

1. **ATS Score** — total score with grade
2. **Score Breakdown** — per-category scores with visual bars
3. **Strengths** — what's working well
4. **Critical Fixes** — ordered by impact, with specific advice
5. **Missing Keywords** — exact terms to add
6. **Next Steps** — what to do now

---

## Permissions Required

```json
{
  "permissions": {
    "allow": [
      "Read(~/.jobforge/**)",
      "Write(~/.jobforge/**)"
    ]
  }
}
```
