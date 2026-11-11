---
name: jobforge-job-search
description: >-
  Search 100+ jobs across multiple job platforms: LinkedIn, Indeed, Naukri,
  Apna, Shine, and HiringCafe. Use when the user asks to "find jobs", "search
  100 jobs", "search linkedin jobs", "search naukri jobs", "search indeed jobs",
  "search apna jobs", "search shine jobs", "multi-platform job search", "find me
  jobs in India / remote", or "bulk job search". Pulls 100+ openings, deduplicates,
  scores fit against resume, flags LinkedIn connections, and saves top postings.
argument-hint: "role, location, and optional target count (e.g. 'Software Engineer India 100+')"
---

# JobForge Multi-Platform Job Search Skill (100+ Target)

> **Priority hierarchy**: See .agents/shared/references/priority-hierarchy.md.
> **Platform Connectors**: See .agents/shared/references/job-platforms.md.

Search across 6 major platforms (**LinkedIn, Indeed, Naukri, Apna, Shine, HiringCafe**) and harvest 100+ job openings in a single run.

## Supported Portals & Query Rules

1. **LinkedIn Jobs**: https://www.linkedin.com/jobs/search/?keywords={QUERY}&location={LOCATION}
2. **Naukri**: https://www.naukri.com/{QUERY-SLUG}-jobs-in-{LOCATION-SLUG}?k={QUERY}&l={LOCATION}
3. **Indeed (India/Global)**: https://in.indeed.com/jobs?q={QUERY}&l={LOCATION}
4. **Apna**: https://apna.co/jobs?text={QUERY}&location={LOCATION}
5. **Shine**: https://www.shine.com/job-search/{QUERY-SLUG}-jobs?q={QUERY}&loc={LOCATION}
6. **HiringCafe**: https://hiring.cafe/?search={QUERY}

---

## Workflow: 100+ Job Aggregation Loop

### Step 1: Ingest Preferences & Search Query
- Target query keywords (e.g. "React Developer", "Data Analyst", "Backend Engineer")
- Location target (e.g. "India", "Bangalore", "Remote", "Delhi NCR")
- Minimum target count: default **100 jobs** (unless specified otherwise)

### Step 2: Multi-Platform Batched Scraping
Distribute queries across platforms using browser tools:
* **LinkedIn**: Scrape 25-50 jobs (pages 1 & 2)
* **Naukri**: Scrape 30-40 jobs (pages 1 & 2)
* **Indeed**: Scrape 20-30 jobs (pages 1 & 2)
* **Apna & Shine**: Scrape 20-30 jobs
* **HiringCafe**: Scrape 20-30 direct corporate postings

**Critical JS extraction pattern (No get_page_text blowout):**
Execute in console via javascript_tool:
`javascript
(() => {
  const selectors = [
    // LinkedIn
    '.job-search-card', '.base-card',
    // Naukri
    'article.jobTuple', 'div.srp-jobtuple-wrapper',
    // Indeed
    'div.job_seen_beacon', 'div.cardOutline',
    // Shine & Apna
    'div.jobCard', 'div[class*="JobCard"]',
    // Fallback generic
    '[class*="listing"], [class*="job-card"], [role="listitem"]'
  ];
  const items = Array.from(document.querySelectorAll(selectors.join(', ')));
  return items.slice(0, 50).map(el => {
    const a = el.querySelector('a[href*="/job"], a[href*="/viewjob"], a.title, a.base-card__full-link') || el.querySelector('a');
    return {
      title: (el.querySelector('h2, h3, a.title, [class*="title"]')?.innerText || '').trim(),
      company: (el.querySelector('[class*="company"], [class*="brand"], [class*="comp-name"]')?.innerText || '').trim(),
      location: (el.querySelector('[class*="location"], [class*="locWdth"]')?.innerText || '').trim(),
      link: a ? a.href : window.location.href
    };
  }).filter(j => j.title && j.title.length > 2);
})();
`

### Step 3: Deduplication & Clean
1. Key items by lowercase(title) + '@' + lowercase(company).
2. Filter out duplicates across sites.
3. Keep searching subsequent platforms until aggregate total reaches **100+ unique jobs**.

### Step 4: Fit Scoring & Ranking
Evaluate all 100+ items against user's preferences.md and esume/:
- **High Fit**: Meets role, core skills, no dealbreakers.
- **Medium Fit**: Adjacent role, good tech overlap.
- **Skip/Low**: Non-matching or violates dealbreaker.

### Step 5: Save & Present Results
1. Append all 100+ jobs into DATA_DIR/job-history.md with source portal tagged.
2. For the **Top 5 High Fit** jobs, resolve direct application URLs and save job folders.
3. Cross-reference with DATA_DIR/linkedin-contacts.csv for 1st-degree referral paths.
4. Output a clean breakdown:
   - Total Scanned: 100+ (by portal: LinkedIn, Naukri, Indeed, Apna, Shine)
   - Top Ranked Matches with direct apply links
   - Next steps to tailor resume or auto-apply.
