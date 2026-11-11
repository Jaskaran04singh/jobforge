---
name: jobforge-apply
description: >-
  Fill out and submit single or batch job applications (10 to 100+ applications)
  across LinkedIn Easy Apply, Naukri 1-Click Apply, Unstop Quick Apply, Apna,
  Indeed, and direct ATS forms (Greenhouse, Lever, Workday). Use when user asks to
  "batch apply", "apply to 50 jobs", "apply to all matches", "auto apply to Naukri
  and LinkedIn jobs", "mass apply with approval", or "apply to [job URL]".
  Supports approval manifest before batch submission, intelligent form filling,
  and daily rate limiting to keep accounts completely safe.
argument-hint: "'batch 50', 'all', or specific job URL"
---

# JobForge Batch & Multi-Platform Auto-Apply Skill

> **Priority hierarchy**: See `.agents/shared/references/priority-hierarchy.md`.
> **Non-negotiable**: Requires user confirmation of the application manifest before submitting any batch.

Intelligently fills and submits applications at scale across:
- **LinkedIn Easy Apply**
- **Naukri Quick Apply**
- **Unstop 1-Click Apply**
- **Apna Fast Apply**
- **Indeed Apply**
- **Greenhouse / Lever / Workday direct ATS forms**

---

## Batch Application Workflow

### Step 1: Queue Inspection & Manifest Generation
1. Identify target jobs from:
   - Specific search batch or manifest (`~/.jobforge/search-batches/`)
   - Unapplied High-Fit jobs in `~/.jobforge/job-history.md`
   - Explicit URL provided by user
2. Generate an **Application Manifest** containing:
   - Target jobs count (e.g. 25, 50, 100)
   - Breakdown by platform (e.g. 20 LinkedIn, 15 Naukri, 10 Unstop, 5 Greenhouse)
   - Default answers for standard questions (notice period, current CTC, expected CTC, work authorization)

### Step 2: User Approval Manifest
Present the batch manifest to the user for one single approval:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 BATCH APPLICATION MANIFEST (Total: [N] Jobs)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Platforms: LinkedIn ([n]), Naukri ([n]), Unstop ([n]), Direct ATS ([n])

Pre-filled Data:
- Experience: [Years]
- Notice Period: [Days]
- Expected CTC / Salary: [Amount]
- Standard EEO: Decline to self-identify

Are you ready to submit this batch? (Reply "Confirm Batch [N]" to start)
```

### Step 3: Execution Engine with Rate-Limiting & Anti-Ban Pacing
Once confirmed, launch `scripts/engines/batch_apply_engine.py`:
1. **Safety Controls:**
   - 10–20 seconds pacing delay between submissions.
   - Max daily cap (default: 50 per day to avoid portal spam flags).
2. **Platform Handling:**
   - **LinkedIn Easy Apply:** Fills multi-step modal, uploads tailored resume, clicks Review -> Submit.
   - **Naukri Apply:** Matches questionnaire (notice period, CTC, skills), clicks 1-Click Apply.
   - **Unstop / Apna:** Fills profile links, github, and submits direct candidate form.
   - **Greenhouse / Lever:** Fills external web form and uploads resume.

### Step 4: Batch Summary & Live Logging
1. Record each successful submission in `~/.jobforge/jobs/[company]-[date]/applied.md`.
2. Update global status in `~/.jobforge/job-history.md`.
3. Present live progress report:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 BATCH APPLICATION COMPLETED!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Successfully Applied: [Count]
⏭️ Skipped / Manual Action Needed: [Count]
❌ Failed / Expired: [Count]

All details logged in ~/.jobforge/job-history.md!
```
