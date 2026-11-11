---
name: jobforge-track
description: >-
  View and manage the user's job application tracker — see all applications,
  current statuses, response rate, follow-up reminders, and outcome analytics.
  Use when the user asks to "track my applications", "show my application
  status", "application dashboard", "where do my applications stand", "follow
  up on applications", "update application status", "which companies responded",
  "how many interviews do I have", or "show my pipeline". Can also update a
  specific application's status or generate follow-up email templates.
argument-hint: "'update [company] [status]' to quickly update a status, or 'followup' to show overdue follow-ups"
---

# JobForge Track Skill

> **Priority hierarchy**: See `.agents/shared/references/priority-hierarchy.md`.

Your application dashboard. See where everything stands, update statuses, and get follow-up reminders.

## Quick Start

- Ask: **"Show my application tracker"**
- Ask: **"Update [company] to interview stage"**
- Ask: **"Which applications need a follow-up?"**

## Data Directory

Resolve using `.agents/shared/references/data-directory.md`.

---

## Workflow

### Step 0: Check Prerequisites

Resolve the data directory. If `DATA_DIR/job-history.md` doesn't exist and no `DATA_DIR/jobs/*/applied.md` files exist, tell the user:

> "No applications tracked yet. Apply to jobs and they'll appear here automatically."

---

### Step 1: Load Application Data

Read:
- `DATA_DIR/job-history.md` — running job log with statuses
- All `DATA_DIR/jobs/*/applied.md` files — individual application logs

Build a unified list of all applications with: company, role, date applied, current status, follow-up date.

---

### Step 2: Handle Quick Status Update

If the user said something like "update [company] to interview" or "mark [company] as rejected":
- Find the matching application
- Update its status in `applied.md` and `job-history.md`
- Confirm: "Updated [Company] → [new status]"

**Valid statuses:** `applied` | `viewed` | `phone_screen` | `interview` | `offer` | `rejected` | `withdrawn` | `ghosted`

---

### Step 3: Handle Follow-up Request

If the user asked specifically about follow-ups, show only applications where:
- Status is "applied" and it's been 7+ days since applying with no update
- Status is "phone_screen" or "interview" and it's been 5+ days since the last status change

Present as a prioritized follow-up list.

---

### Step 4: Present the Full Dashboard

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 APPLICATION TRACKER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY
  Total applications : [N]
  Active pipeline    : [N]
  Response rate      : [X]%
  Interviews         : [N]
  Offers             : [N]
  Avg response time  : [X] days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACTIVE PIPELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 INTERVIEW STAGE
  [Company] — [Role] — Interview on [date]

🔵 AWAITING RESPONSE
  [Company] — [Role] — Applied [date]  ⏰ Follow up [if 7+ days]
  [Company] — [Role] — Applied [date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLOSED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🟢 [Company] — Offer received [date]
  🔴 [Company] — Rejected [date]
  ⚪ [Company] — Withdrawn [date]
  💀 [Company] — Ghosted (no response after [N] days)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ FOLLOW-UP NEEDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [Company] — applied [N] days ago — suggest following up
  [Company] — applied [N] days ago — suggest following up
```

---

### Step 5: Offer Actions

After the dashboard, ask if the user wants to:
- Update a status: "Update [company] to [status]"
- Get a follow-up email template for a specific company
- Apply to a new job

**Follow-up email template** (if requested):
- Under 100 words
- References the specific role applied for
- Reaffirms interest with one specific detail about the company
- Politely asks for a status update
- Subject line: "Following up — [Role] Application"

---

## Status Definitions

| Status | Meaning |
|--------|---------|
| `applied` | Application submitted, waiting |
| `viewed` | Company viewed your application |
| `phone_screen` | Recruiter screen scheduled or done |
| `interview` | Technical / panel interview scheduled or done |
| `offer` | Offer received |
| `rejected` | Explicitly rejected |
| `withdrawn` | You withdrew |
| `ghosted` | No response after 3+ weeks |

---

## Response Format

1. **Summary Stats** — totals, response rate, active count
2. **Active Pipeline** — grouped by status, follow-up flags
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
