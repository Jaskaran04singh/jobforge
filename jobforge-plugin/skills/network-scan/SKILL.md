---
name: network-scan
description: Scan your LinkedIn contacts' companies for matching job openings
argument-hint: "number of contacts (default 25) or 'all'"
---

# Network Scan Skill

> **Priority hierarchy**: See `shared/references/priority-hierarchy.md` for conflict resolution.

Proactively check whether companies where you know someone are hiring for roles that match you. First run builds a cache of company careers page URLs. Subsequent runs reuse the cache, making weekly checks fast.

## Quick Start

- `/jobforge:network-scan` — Scan companies from your 25 most recent contacts
- `/jobforge:network-scan 50` — Check the 50 most recent contacts
- `/jobforge:network-scan all` — Check all contacts

## Workflow

Follow the procedure in `shared/references/fit-scoring.md` and use your stored contacts in `~/.jobforge/linkedin-contacts.csv`.
Resolve company careers pages, scan open roles, evaluate fit, and present high-match openings with warm intro paths.
