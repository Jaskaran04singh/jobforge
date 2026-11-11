---
name: tailor-resume
description: Tailor the user's resume for a specific job posting — rewrite bullets, inject keywords, reorder sections, and produce an ATS-optimized resume that still sounds human
argument-hint: "job URL or 'last' to use the most recent job"
---

# JobForge Tailor Resume Skill

> **Priority hierarchy**: See `shared/references/priority-hierarchy.md` for conflict resolution.

Create a tailored, ATS-optimized resume for a specific job. Every word stays true to what the user actually did.

## Quick Start

- `/jobforge:tailor-resume` — Asks for a job URL
- `/jobforge:tailor-resume https://...` — Tailor for a specific job posting
- `/jobforge:tailor-resume last` — Tailor for the most recently saved job

## File Structure

```
scripts/
  tailor-resume.md        # Resume tailoring agent prompt
```

## Data Directory

Resolve the data directory using `shared/references/data-directory.md`. Resume is required; profile is strongly recommended.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. Resume required. Profile strongly recommended — if missing, set a flag to verify all assumptions with the user at the end (see Step 3a).

---

### Step 1: Get Job Details

**If `$ARGUMENTS` is "last" or empty:**
- Find the most recently modified folder in `DATA_DIR/jobs/`
- Load `posting.md` from that folder
- Confirm with user: "Tailoring for [Role] at [Company]. Right?"

**If `$ARGUMENTS` is a URL:**
- Check if a job folder already exists for this URL/company slug in `DATA_DIR/jobs/`
- If yes: load existing `posting.md`
- If no: use browser tools to fetch the posting. Save to `DATA_DIR/jobs/[company-slug]-[YYYYMMDD]/posting.md`

If the page can't be loaded, ask the user to paste the job description directly.

**Extract from the posting:**
- Job title and seniority level
- Company name and what they do
- Key responsibilities (what the job actually involves)
- Requirements — must-have qualifications
- Preferred qualifications
- Keywords and terminology used
- Team context (who they report to, team size)

---

### Step 2: Analyze Match

Before writing, map the candidate's experience to the job:

1. **Level match** — Does the candidate's seniority match the role? Adjust language accordingly.
   - Executive role → emphasize strategy, P&L, board interaction, org-building
   - Director role → emphasize program ownership, team management, operational excellence
   - IC role → emphasize hands-on execution, technical depth, individual contributions

2. **Requirement mapping** — For each job requirement, find the strongest matching evidence:
   - Direct experience: "Led SEO strategy" → job asks for SEO
   - Analogous: "Scaled platform from 1M to 10M users" → job asks for growth experience
   - Transferable: "Managed 20-person team" → job asks for leadership

3. **Gap identification** — Note requirements with no clear match. Do NOT fabricate. Find adjacent experience that shows capability, or be honest about the gap.

4. **Keyword alignment** — Identify the job's exact terminology. Mirror it in the resume.

5. **Narrative** — Determine the 2–3 sentence story of why this person is the obvious choice.

---

### Step 3: Generate Tailored Resume

Follow the full tailoring guide in `scripts/tailor-resume.md`.

**Structure:**
- **Header**: Name, contact info, LinkedIn (same as original)
- **Summary**: 2–3 short sentences positioning the candidate specifically for THIS role and company
- **Experience**: All roles, bullets rewritten, reordered, and re-emphasized for this job
- **Skills**: Reorganized to lead with what the job asks for
- **Education**: Same as original

**Bullet point rules:**
- Lead each role with bullets most relevant to this target job
- Mirror the job posting's exact language where authentic
- Include metrics and quantified impact (from profile)
- Remove or de-emphasize bullets irrelevant to this role
- Add bullets from the profile that weren't on the original resume but ARE relevant here
- Every bullet starts with a strong action verb
- Format: what you did → how → what the impact was

**Writing rules — CRITICAL (target Flesch score above 90):**
- Write like a sharp professional. Short sentences. Plain words.
- One idea per sentence. Split anything with "and" connecting unrelated clauses.
- Never use em dashes. Use commas, periods, colons, or parentheses.
- No preamble clauses. Bad: "Leveraging deep expertise in X, led..." — Good: "Led..."
- No stacked adjectives. Pick one. Give an example.
- No filler: "demonstrating ability to", "with a track record of", "leveraging", "utilizing", "spanning"
- Summary: 2–3 SHORT sentences. Each under 20 words.

**Accuracy rules — CRITICAL:**
- ONLY use information explicitly in the resume or profile
- NEVER assume business model, revenue type, or company stage unless stated
- NEVER infer scope beyond what's written (don't add "P&L ownership" if resume says "revenue targets")
- NEVER add responsibilities, skills, or functional areas the user didn't mention
- If the resume is ambiguous, use conservative language or omit it
- Do NOT change job titles, dates, or company names

---

### Step 3b: Critique and Rewrite — MANDATORY Before Presenting

Before showing the resume, review every line and fix AI-sounding writing:

1. **Too much in one sentence?** Split it.
2. **Would a real person say this?** Read it aloud. If it sounds like a LinkedIn post, rewrite it.
3. **Any filler?** Cut phrases that add no information.
4. **Stacked buzzwords?** Pick one, give a concrete example.
5. **Summary under control?** Max 3 sentences. Each under 20 words. Max 2 items per sentence.

**Common AI patterns to kill:**
- "I combine X with Y, Z, and the W needed to..." → Split into separate statements
- "...demonstrating [abstract quality]" → Delete or replace with the actual result
- "...spanning [long list]" → Pick the most relevant 1–2 items
- "Led [action], [action], and [action] across [scope]" → One action per bullet
- Gerund clauses tacked on the end → Two sentences

**Test:** After rewriting, re-read the summary and first 3 bullets. If any sentence takes more than one breath to read aloud, shorten it.

---

### Step 4: Save and Present

Save to `DATA_DIR/jobs/[company-slug]-[date]/resume.md`.

Present to user:

```
Here's your tailored resume for [Role] at [Company].

**Key changes:**
- [What was reordered/emphasized and why]
- [What bullets were rewritten and why]
- [What was added from your work history]

**The narrative:** [2–3 sentence pitch for why you're the right person]

**ATS score:** [Before] → [After] (estimated)

Saved to: DATA_DIR/jobs/[folder]/resume.md
```

---

### Step 3a: Verify Assumptions (if no profile exists)

If no work history profile was available, present every assumption made:

```
Before we finalize — here are the assumptions I made. Please correct any that are wrong:

1. [Company] — I assumed [X]. Is that right?
2. [Role scope] — I described your scope as [Y]. Accurate?
3. [Business model] — I framed this as [Z]. Correct?
```

Wait for confirmation. Apply all corrections to the resume AND save them to `DATA_DIR/profile.md` so they persist.

---

### Step 5: Iterate

Ask if the user wants adjustments:
- Tone (more technical, more strategic, more concise)
- Emphasis (highlight certain roles or projects more)
- Length (condense to 1 page)
- Specific bullets to rephrase

Apply changes and re-save.

---

### Step 6: Update Profile (Always)

Every time the user corrects a factual detail, update `DATA_DIR/profile.md` immediately:
- Business model corrections
- Scope corrections
- Responsibility corrections
- Any other role/team/accomplishment clarification

This prevents the same mistakes on future resumes.

---

## Response Format

1. **Tailored Resume** — full resume text
2. **Tailoring Notes** — what changed and why, the narrative pitch, ATS score estimate
3. **What's Next** — suggest iterating on tone, or running `/jobforge:cover-letter`

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
