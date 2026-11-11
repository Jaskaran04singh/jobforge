---
name: job-search
description: Search 100+ jobs across multiple portals (LinkedIn, Indeed, Naukri, Apna, Shine, HiringCafe) with smart filtering and network matching
argument-hint: "keyword, location, and optional count (e.g. 'Software Engineer India 100+')"
---

# Multi-Platform Job Search (100+ Aggregator)

> **Platform references**: See shared/references/job-platforms.md.
> **Fit criteria**: See shared/references/fit-scoring.md.

Search across LinkedIn, Indeed, Naukri, Apna, Shine, and HiringCafe in parallel to aggregate **100+ matching jobs** per run.

## Supported Portals
- **LinkedIn Jobs** (Direct / Easy Apply)
- **Naukri.com** (India's premier portal)
- **Indeed** (Global & India)
- **Apna.co** (Tier 1/2/3 & startup roles)
- **Shine.com** (National job database)
- **HiringCafe** (Direct corporate career pages)

## Aggregation Strategy
1. Queries multiple platforms with paginated parameters (start=0, 25, pageNo=1, 2).
2. Scrapes clean structured metadata using JavaScript DOM extraction.
3. Automatically deduplicates listings across platforms.
4. Ranks listings by fit (High, Medium, Low) and saves full 100+ batch to ~/.jobforge/job-history.md.
5. Surfaces top 5-10 High Fit openings with direct links and LinkedIn referral contacts.
