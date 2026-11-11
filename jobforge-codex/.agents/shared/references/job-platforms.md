# Job Search Platform Connectors & Multi-Source Rules

JobForge aggregates from global and Indian job portals. Supported platforms, selectors, query URL formats, and pagination strategies:

## Supported Platforms

### 1. LinkedIn Jobs (linkedin.com/jobs/search)
- **Query URL**: https://www.linkedin.com/jobs/search/?keywords={QUERY}&location={LOCATION}&f_TPR=r604800 (posted last week)
- **Pagination**: &start={PAGE * 25}
- **Card Selector**: .job-search-card, .base-card, div.base-search-card
- **Fields**: Title (.base-search-card__title), Company (.base-search-card__subtitle), Location (.job-search-card__location), Link (.base-card__full-link)

### 2. Indeed (indeed.com / in.indeed.com)
- **Query URL**: https://in.indeed.com/jobs?q={QUERY}&l={LOCATION}&fromage=7
- **Pagination**: &start={PAGE * 10}
- **Card Selector**: div.job_seen_beacon, td.resultContent, div.cardOutline
- **Fields**: Title (h2.jobTitle span), Company ([data-testid="company-name"]), Location ([data-testid="text-location"]), Link (h2.jobTitle a)

### 3. Naukri.com (
aukri.com)
- **Query URL**: https://www.naukri.com/{QUERY-SLUG}-jobs-in-{LOCATION-SLUG}?k={QUERY}&l={LOCATION}&experience={MIN_EXP}&dayRange=7
- **Pagination**: &pageNo={PAGE} (20 jobs per page)
- **Card Selector**: rticle.jobTuple, div.srp-jobtuple-wrapper
- **Fields**: Title (.title), Company (.comp-name), Location (span.locWdth), Exp (span.expwdth), Salary (span.sal), Link (.title)

### 4. Apna (pna.co)
- **Query URL**: https://apna.co/jobs?text={QUERY}&location={LOCATION}
- **Card Selector**: div[class*="JobCard"], div[class*="job-card"]
- **Fields**: Title, Company, Location, Salary, Direct URL

### 5. Shine.com (shine.com)
- **Query URL**: https://www.shine.com/job-search/{QUERY-SLUG}-jobs?q={QUERY}&loc={LOCATION}
- **Pagination**: &page={PAGE}
- **Card Selector**: div.jobCard, div.parent_jobCard
- **Fields**: Title (h2[itemprop="name"] a), Company (span.jobCard_brandName), Location (div.jobCard_location), Link (h2[itemprop="name"] a)

### 6. HiringCafe (hiring.cafe)
- **Query URL**: https://hiring.cafe/?search={QUERY}
- **Card Selector**: div[class*="job-card"], div[class*="listing"]
- **Strengths**: Direct corporate board links (no agency junk)

---

## 100+ Jobs Aggregation Engine Protocol

To hit 100+ results reliably across sessions:
1. **Multi-Source Distribution**: Query at least 3 distinct platforms concurrently (e.g. 40 LinkedIn + 30 Naukri + 30 Indeed + 20 Apna/Shine).
2. **Pagination Strategy**: Extract up to 2-3 pages per platform using direct URL offset parameters (start=0, start=25, start=50 or pageNo=1,2,3).
3. **Structured JS Scraper**: Extract rows using lightweight DOM queries to prevent context window explosion.
4. **Deduplication**: Clean company name and job title, keying by lowercase(title + company).
5. **Ranking**: Sort by match fit (High ➔ Medium ➔ Low).
