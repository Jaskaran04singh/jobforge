# Work History Interview Guide

This script guides the agent through the work history interview in `/jobforge:setup`.

## Goal

Build a rich `profile.md` that captures real stories, real metrics, and the full context behind each job. This profile is what makes every other skill produce high-quality output.

## Rules

- Keep it conversational. This is a human interview, not a form.
- Follow up on vague answers ("Do you remember roughly what the numbers were?").
- Never interrogate. If they don't know, move on.
- Spend more time on recent and impactful roles. Older roles can be brief.
- Do NOT write the profile during the interview — take mental notes and write it all at the end.

---

## Interview Flow

### Opening

> "Let's build your work history profile. I'll ask you about each role on your resume — this helps me write much better resumes and cover letters later. It usually takes 10–15 minutes. Ready to start?"

---

### For Each Role (Most Recent First)

Ask these in a natural, flowing way — not as a numbered list.

**Question 1 — Context**
> "Tell me about [Company]. What did they do, and what was your role really about day-to-day?"

Listen for: company size, stage, business model, what their actual job involved vs the title.

**Question 2 — Accomplishments**
> "What were your biggest wins there? I'm looking for specific things — something you built, improved, led, or shipped. Numbers are great if you have them."

Follow up if vague:
- "What impact did that have?"
- "Do you have a rough number for that?"
- "How did you measure success?"

**Question 3 — Depth**
> "Anything else worth capturing — challenges you overcame, people you managed, why you moved on?"

---

### Closing

> "That was really helpful. I have a good picture of your background now. Give me a moment to write up the profile."

Write `DATA_DIR/profile.md` using the template at `shared/templates/profile.md`.

Then show the user the finished profile and ask:
> "Does this capture everything accurately? Anything I got wrong or should add?"

Apply all corrections immediately and re-save.
