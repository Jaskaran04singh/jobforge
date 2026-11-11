---
name: track
description: View and update your job application tracker — see all applications, their current status, response rate, follow-up reminders, and outcome analytics
argument-hint: "optional: 'update [company] [status]' to quickly update a status"
---

# JobForge Track Skill

> **Priority hierarchy**: See `shared/references/priority-hierarchy.md` for conflict resolution.

Your application dashboard. See where everything stands, update statuses, and get follow-up reminders.

## Quick Start

- `/jobforge:track` — Show full application tracker
- `/jobforge:track update Acme interview` — Update Acme's status to "interview"
- `/jobforge:track followup` — Show all applications needing a follow-up

## Data Directory

Resolve the data directory using `shared/references/data-directory.md`.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. If `DATA_DIR/job-history.md` doesn't exist, tell the user:
> "No applications tracked yet. Apply to jobs with `/jobforge:apply` and they'll appear here."

---

### Step 1: Load Application Data

Read:
- `DATA_DIR/job-history.md` — running job log
- `DATA_DIR/jobs/*/applied.md` — application logs from each job folder

Build a unified list of all applications with: company, role, date applied, current status, follow-up date.

---

### Step 2: Handle Quick Update (if `$ARGUMENTS` contains "update")

Parse the argument: `update [company] [new-status]`

Valid statuses: `applied` | `viewed` | `phone_screen` | `interview` | `offer` | `rejected` | `withdrawn` | `ghosted`

Update the matching application's status in its `applied.md` and in `job-history.md`. Confirm:
```
Updated [Company] → [new status]
```

---

### Step 3: Handle Follow-up Request (if `$ARGUMENTS` is "followup")

Show only applications where:
- Status is "applied" and it's been 7+ days since applying with no update
- Status is "phone_screen" or "interview" and it's been 5+ days since the last status update

Present as a prioritized follow-up list (see output format below).

---

### Step 4: Present the Full Dashboard

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 APPLICATION TRACKER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY
  Total applications:  [N]
  Active pipeline:     [N]
  Response rate:       [X]%  (phone screens + interviews + offers / total)
  Interviews:          [N]
  Offers:              [N]
  Avg. response time:  [X] days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACTIVE PIPELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 INTERVIEW STAGE
  [Company] — [Role] — Interview on [date or "scheduled"]
  [Company] — [Role] — Phone screen [date]

🔵 APPLIED — AWAITING RESPONSE
  [Company] — [Role] — Applied [date]  ⏰ Follow up [if 7+ days ago]
  [Company] — [Role] — Applied [date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLOSED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🟢 [Company] — Offer received [date]
  🔴 [Company] — Rejected [date]
  ⚪ [Company] — Withdrawn [date]
  💀 [Company] — Ghosted (no response after [N] days)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ FOLLOW-UP NEEDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [Company] — applied [N] days ago — suggest following up now
  [Company] — applied [N] days ago — suggest following up now
```

---

### Step 5: Offer Actions

After presenting the dashboard, offer:

```
What would you like to do?
  /jobforge:track update [company] [status]  — Update a status
  /jobforge:apply [URL]                      — Apply to a new job
  /jobforge:job-search                       — Find more jobs
```

If the user asks for a follow-up email template for a specific company, generate a brief, professional follow-up:
- Under 100 words
- References the specific role applied for
- Reaffirms interest with one specific detail about the company
- Asks politely for a status update

---

## Status Definitions

| Status | Meaning |
|--------|---------|
| `applied` | Application submitted, waiting for response |
| `viewed` | Company viewed your application (from notification) |
| `phone_screen` | Recruiter screen scheduled or completed |
| `interview` | Technical / panel interview scheduled or completed |
| `offer` | Offer received |
| `rejected` | Explicitly rejected |
| `withdrawn` | You withdrew the application |
| `ghosted` | No response after 3+ weeks |

---

## Response Format

1. **Summary Stats** — totals, response rate, active count
2. **Active Pipeline** — grouped by status, with follow-up flags
3. **Closed** — offers, rejections, withdrawals, ghosted
4. **Follow-up List** — prioritized by urgency
5. **Actions** — what to do next

---

## Permissions Required

```json
{
  "permissions": {
    "allow": [
      "Read(~/.jobforge/**)",
      "Write(~/.jobforge/**)",
      "Edit(~/.jobforge/**)"
    ]
  }
}
```
