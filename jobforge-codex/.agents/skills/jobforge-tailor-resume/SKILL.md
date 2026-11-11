---
name: jobforge-tailor-resume
description: >-
  Tailor and rewrite the user's resume for a specific job posting to maximize
  ATS keyword match and recruiter impact. Use when the user asks to "tailor
  my resume", "optimize my resume for this job", "rewrite my resume for
  [company]", "customize resume for [role]", "make my resume fit this job",
  "adapt resume", or shares a job URL and asks to apply or prepare materials.
  Rewrites bullet points, injects missing keywords naturally, reorders sections,
  and produces an ATS-optimized resume that still sounds human. Never fabricates
  experience. Saves tailored resume to the job's data folder.
argument-hint: "job URL, or 'last' to use the most recently saved job"
---

# JobForge Tailor Resume Skill

> **Priority hierarchy**: See `.agents/shared/references/priority-hierarchy.md`.

Rewrite the user's resume for a specific job. Every word stays true to what they actually did.

## Quick Start

- Ask: **"Tailor my resume for [job URL]"**
- Ask: **"Optimize my resume for the last job"**
- Ask: **"Customize my resume for [company]"**

## File Structure

```
scripts/
  tailor-resume.md    # Resume tailoring agent prompt
```

## Data Directory

Resolve using `.agents/shared/references/data-directory.md`. Resume is required; profile is strongly recommended.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. Resume required. Profile strongly recommended.
If no profile exists, set a flag to verify all assumptions with the user at the end (see Step 3a).

---

### Step 1: Get Job Details

**If argument is "last" or no URL provided:**
- Find the most recently modified folder in `DATA_DIR/jobs/`
- Load `posting.md` from that folder
- Confirm: "Tailoring for [Role] at [Company]. Right?"

**If a URL is provided:**
- Check if a job folder already exists for this URL/company slug in `DATA_DIR/jobs/`
- If yes: load existing `posting.md`
- If no: use browser tools to fetch the posting and save to `DATA_DIR/jobs/[company-slug]-[YYYYMMDD]/posting.md`

If the page can't be loaded, ask the user to paste the job description directly.

**Extract from posting:**
- Job title and seniority level (IC vs manager)
- Company name and what they do
- Key responsibilities
- Required qualifications and nice-to-haves
- Keywords and terminology used
- Team context

---

### Step 2: Analyze Match

Before writing, map the candidate's experience to the job:

1. **Level match** — Adjust language for the seniority level:
   - Executive → strategy, P&L, org-building, board interaction
   - Director → program ownership, team management, operational excellence
   - IC → hands-on execution, technical depth, individual contributions

2. **Requirement mapping** — For each job requirement, find the strongest evidence:
   - Direct: "Led SEO strategy" → job asks for SEO
   - Analogous: "Scaled to 10M users" → job asks for growth experience
   - Transferable: "Managed 20-person team" → job asks for leadership

3. **Gap identification** — Note requirements with no clear match. Do NOT fabricate. Find adjacent experience or be honest about the gap.

4. **Keyword alignment** — Identify the job's exact terminology to mirror in the resume.

5. **Narrative** — Determine the 2–3 sentence story of why this person is the obvious choice.

---

### Step 3: Generate Tailored Resume

**Structure:**
- **Header**: Name, contact info, LinkedIn (same as original)
- **Summary**: 2–3 short sentences positioning the candidate specifically for THIS role and company
- **Experience**: All roles, bullets rewritten, reordered, and re-emphasized for this job
- **Skills**: Reorganized to lead with what the job asks for first
- **Education**: Same as original

**Bullet point rules:**
- Lead each role with bullets most relevant to the target job
- Mirror the job posting's exact language where authentic
- Include metrics and quantified impact (from profile)
- Remove or de-emphasize bullets irrelevant to this role
- Add bullets from the profile that weren't on the original resume but ARE relevant here
- Every bullet starts with a strong action verb
- Format: what you did → how → what the impact was

**Writing rules — CRITICAL (Flesch score above 90):**
- Short sentences. Plain words. One idea per sentence.
- Never use em dashes. Use commas, periods, colons, or parentheses.
- No preamble clauses. Bad: "Leveraging deep expertise in X, led..." → Good: "Led..."
- No stacked adjectives. Pick one. Give an example.
- No filler: "demonstrating ability to", "with a track record of", "leveraging", "utilizing", "spanning"
- Summary: max 3 SHORT sentences. Each under 20 words.

**Accuracy rules — CRITICAL:**
- ONLY use information explicitly in the resume or profile
- NEVER assume business model, revenue type, or company stage unless stated
- NEVER infer scope beyond what's written
- NEVER add responsibilities, skills, or functional areas the user didn't mention
- Do NOT change job titles, dates, or company names

---

### Step 3b: Critique and Rewrite — MANDATORY Before Presenting

Review every line and fix AI-sounding writing. For each sentence ask:

1. Too much in one sentence? → Split it.
2. Would a real person say this? → If it sounds like LinkedIn, rewrite it.
3. Any filler? → Cut phrases that add no information.
4. Stacked buzzwords? → Pick one, give a concrete example.
5. Summary under control? → Max 3 sentences. Each under 20 words.

**Common AI patterns to kill:**
- "I combine X with Y, Z, and the W needed to..." → Split into separate statements
- "...demonstrating [abstract quality]" → Delete or replace with the actual result
- "Led [action], [action], and [action] across [scope]" → One action per bullet
- Gerund clauses tacked on the end → Two sentences

**Test:** After rewriting, re-read the summary and first 3 bullets. Any sentence that takes more than one breath to say aloud is too long. Shorten it.

---

### Step 4: Save and Present

Save to `DATA_DIR/jobs/[company-slug]-[date]/resume.md`.

```
Here's your tailored resume for [Role] at [Company].

Key changes:
- [What was reordered/emphasized and why]
- [What bullets were rewritten and why]
- [What was added from your work history]

The narrative: [2–3 sentence pitch for why you're the right person]

ATS score: [Before] → [After] (estimated)

Saved to: DATA_DIR/jobs/[folder]/resume.md
```

---

### Step 3a: Verify Assumptions (if no profile)

If no work history profile was available, present every assumption made:

```
Before we finalize — here are the assumptions I made:

1. [Company] — I assumed [X]. Is that right?
2. [Role scope] — I described your scope as [Y]. Accurate?
```

Wait for confirmation. Apply all corrections to the resume AND save them to `DATA_DIR/profile.md`.

---

### Step 5: Iterate

Ask if the user wants adjustments:
- Tone (more technical, more strategic, more concise)
- Emphasis (highlight certain roles or projects more)
- Length (condense to 1 page, expand details)
- Specific bullets to rephrase

Apply changes and re-save.

---

### Step 6: Update Profile (Always)

Every time the user corrects a factual detail, update `DATA_DIR/profile.md` immediately.
This prevents the same mistakes on future resumes.

---

## Response Format

1. **Tailored Resume** — full text
2. **Tailoring Notes** — what changed, why, and the narrative pitch
3. **What's Next** — suggest writing a cover letter or applying

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
