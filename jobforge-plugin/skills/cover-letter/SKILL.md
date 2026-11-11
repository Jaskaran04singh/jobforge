---
name: cover-letter
description: Write a tailored, human-sounding cover letter for a specific job posting using the user's real work history and achievements
argument-hint: "job URL, or 'last' to use the most recent job"
---

# JobForge Cover Letter Skill

> **Priority hierarchy**: See `shared/references/priority-hierarchy.md` for conflict resolution.

Write natural, persuasive cover letters that sound like a real professional wrote them.

## Quick Start

- `/jobforge:cover-letter` — Asks for a job URL
- `/jobforge:cover-letter https://...` — Write a cover letter for a specific job
- `/jobforge:cover-letter last` — Write for the most recently saved job

## File Structure

```
scripts/
  write-cover-letter.md    # Cover letter writing agent prompt
```

## Data Directory

Resolve the data directory using `shared/references/data-directory.md`. Resume is required; profile is strongly recommended.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. Resume required. Profile recommended but not blocking.

---

### Step 1: Get Job Details

**If `$ARGUMENTS` is "last" or empty:**
- Find the most recently modified folder in `DATA_DIR/jobs/`
- Load `posting.md` and `resume.md` from that folder
- Confirm: "Writing a cover letter for [Role] at [Company]. Right?"

**If `$ARGUMENTS` is a URL:**
- Check if a job folder already exists for this company in `DATA_DIR/jobs/`
- If yes: load existing `posting.md` and `resume.md`
- If no: use browser tools to fetch the posting. Save to `DATA_DIR/jobs/[company-slug]-[YYYYMMDD]/posting.md`

If the page can't be loaded, ask the user to paste the job description.

---

### Step 2: Gather Materials

Check the job folder for:
- `posting.md` — required
- `resume.md` — tailored resume for this role (use it if it exists; fall back to original resume + profile if not)
- `DATA_DIR/profile.md` — work history with detailed stories and metrics

The more context available, the better the letter. If the tailored resume doesn't exist, suggest running `/jobforge:tailor-resume` first, but proceed if the user wants the cover letter now.

---

### Step 3: Write the Cover Letter

Follow the full framework in `scripts/write-cover-letter.md`.

**Requirements:**
- 250–350 words
- Start with "Dear Hiring Manager,"
- End with "Regards, [Name]"
- Use ONLY hyphens, never em dashes
- Sound like a real professional wrote it
- Never fabricate or exaggerate any detail
- Connect 2–3 specific, measurable achievements to what this employer needs

**Structure (3 paragraphs):**

**Paragraph 1 — Hook + Why This Company**
- Start with something specific about the company (not generic praise)
- Reference a real detail from the JD, company product, mission, or recent news
- State the role you're applying for
- DO NOT start with: "I am excited to apply...", "I am writing to express...", "I have always been passionate about..."

**Paragraph 2 — Your Best 2–3 Matching Achievements**
- Pick 2–3 achievements from the resume/profile most relevant to this job
- Connect each one directly to a specific requirement in the posting
- Use numbers and outcomes where available
- Show why YOUR experience is exactly what THEY need right now

**Paragraph 3 — Forward-Looking Close**
- Express genuine interest in contributing to their specific goals
- Invite a conversation
- End with confidence, not groveling

**Writing rules — CRITICAL:**
- Short sentences. Plain words. No em dashes.
- No clichés: "passionate", "excited to apply", "team player", "hard worker", "think outside the box"
- Do not repeat the resume verbatim — the letter adds context, not copies content
- Do not use: "I believe I would be a great fit" unless you back it up immediately with evidence
- Do not list more than 2 things in a single sentence

---

### Step 4: Critique Before Presenting

Re-read every sentence before showing the letter:
- Does it sound like a human wrote it?
- Is every sentence under 25 words?
- Does paragraph 1 mention something specific to this company?
- Do paragraphs 2–3 connect directly to the job requirements?
- Is the total word count between 250–350?

If any sentence fails the human test, rewrite it.

---

### Step 5: Save and Present

Save to `DATA_DIR/jobs/[company-slug]-[date]/cover-letter.md`.

Present to user:

```
[Full cover letter text]

---
**Writing notes:**
- Achievements highlighted: [which ones, and why they fit this role]
- Company-specific hook: [what you referenced and where you found it]
- Word count: [N]

Saved to: DATA_DIR/jobs/[folder]/cover-letter.md
```

---

### Step 6: Iterate

Ask if the user wants to adjust:
- Tone (more formal, more casual, more technical)
- Which achievements to highlight
- Specific phrasing
- Length

Apply changes and re-save.

---

## Response Format

1. **Cover Letter** — full text, ready to copy-paste
2. **Writing Notes** — what achievements were highlighted and why, what company detail was used
3. **What's Next** — suggest `/jobforge:apply` to submit the full application

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
