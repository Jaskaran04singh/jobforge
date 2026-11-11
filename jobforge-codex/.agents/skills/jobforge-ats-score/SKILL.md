---
name: jobforge-ats-score
description: >-
  Score a resume against ATS (Applicant Tracking System) criteria and produce
  a detailed improvement report. Use when the user asks to "score my resume",
  "check my ATS score", "analyze my resume", "how good is my resume", "what's
  wrong with my resume", "get resume feedback", "resume health check", or
  "optimize my resume". Optionally scores against a specific job posting URL
  or job description pasted by the user. Returns a 0-100 score with per-category
  breakdown, ranked list of fixes, and missing keywords.
argument-hint: "optional job URL or paste a job description to score against a specific role"
---

# JobForge ATS Score Skill

> **Priority hierarchy**: See `.agents/shared/references/priority-hierarchy.md`.

Score a resume on 8 ATS criteria and produce a ranked, actionable improvement report.

## Quick Start

- Ask: **"Score my resume"** — scores against your target role from preferences
- Ask: **"Score my resume against [job URL]"** — scores against a specific posting
- Ask: **"What's wrong with my resume?"** — same as above

## Data Directory

Resolve using `.agents/shared/references/data-directory.md`. Resume is required.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. Resume in `DATA_DIR/resume/` is required.
Load `DATA_DIR/preferences.md` if it exists (used for target role keywords).

If a job URL was provided, fetch and parse it. If a job description was pasted, use it directly.

---

### Step 1: Load Resume

Read the resume from `DATA_DIR/resume/`. If multiple files exist, ask the user which to score.

---

### Step 2: Score the Resume

Apply all scoring rules from `.agents/shared/references/ats-rules.md`.

- **With job description** → use its keywords for the keyword match category
- **Without job description** → use standard keywords for the user's target role (from `preferences.md` or the resume's primary role)

Calculate all 8 categories. Sum to get the total score. Assign a grade.

---

### Step 3: Present Report

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 ATS SCORE: [X]/100   [emoji] [grade]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BREAKDOWN
  Keyword Match        [X]/25   [████░░░░░░]
  Quantified Results   [X]/20   [██░░░░░░░░]
  Section Structure    [X]/15   [███████░░░]
  Formatting Safety    [X]/10   [██████████]
  Action Verbs         [X]/10   [████░░░░░░]
  Skills Section       [X]/10   [███████░░░]
  Date Consistency     [X]/5    [█████░░░░░]
  Length               [X]/5    [██████████]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ STRENGTHS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [strength 1]
- [strength 2]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  CRITICAL FIXES  (biggest impact first)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Issue — specific, actionable fix]
2. [Issue — specific, actionable fix]
3. [Issue — specific, actionable fix]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔑 MISSING KEYWORDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[keyword1], [keyword2], [keyword3] ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 NEXT STEP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Recommend: tailor for a specific job / fix top issues first / apply now]
```

---

### Step 4: Save Report

Save the full report to `DATA_DIR/ats-reports/[YYYYMMDD]-[role-slug].md`.

Tell the user the saved path.

---

### Step 5: Offer Next Steps

After showing the report, suggest:
- "Ask me to tailor your resume for a specific job" → runs `jobforge-tailor-resume`
- "Ask me to find matching jobs" → runs `jobforge-job-search`
- "Fix the issues and ask me to re-score" → runs this skill again

---

## Response Format

1. **ATS Score** — total with grade emoji
2. **Breakdown** — 8 categories with visual bars
3. **Strengths** — what's working
4. **Critical Fixes** — ordered by point impact, specific advice per fix
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
