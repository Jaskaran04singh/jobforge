# ATS Scoring Rules

Used by both the `ats-score` skill and inline by `tailor-resume`.

## Score Categories (Total: 100 points)

### 1. Keyword Match — 25 pts
Compare resume keywords against the target job description (or standard role keywords if no JD provided).
- 90–100% matched → 25 pts
- 70–89% → 18 pts
- 50–69% → 12 pts
- 30–49% → 6 pts
- <30% → 0 pts

### 2. Quantified Achievements — 20 pts
Count bullet points containing numbers, %, $, or measurable outcomes.
Regex pattern: `\d+[%+x]?|\$[\d,]+|[0-9]+[KkMm]`
- 10+ quantified bullets → 20 pts
- 6–9 → 15 pts
- 3–5 → 10 pts
- 1–2 → 5 pts
- 0 → 0 pts

### 3. Section Structure — 15 pts
Required sections (3 pts each): Contact Info, Summary/Objective, Experience, Education, Skills.
Deduct 3 pts per missing required section.

### 4. Formatting Safety — 10 pts
- 10 pts: Clean text, no tables, no columns, no graphics
- 7 pts: Minor layout issues
- 5 pts: Tables or columns present (ATS may misparse)
- 2 pts: Heavy graphics, icons, or chart elements

### 5. Action Verbs — 10 pts
Ratio of bullet points starting with strong action verbs.
Strong verbs: Built, Led, Designed, Implemented, Increased, Reduced, Managed, Launched,
Developed, Architected, Spearheaded, Optimized, Delivered, Automated, Created, Established,
Drove, Achieved, Improved, Generated, Scaled, Negotiated, Shipped, Owned, Directed.
Weak verbs to flag: "Responsible for", "Helped with", "Assisted in", "Worked on", "Participated in".
Score = (strong_verb_bullets / total_bullets) × 10.

### 6. Skills Section — 10 pts
- 10 pts: Explicit skills section, 10+ relevant skills
- 7 pts: Skills section with 5–9 skills
- 4 pts: Skills section with <5 skills
- 0 pts: No dedicated skills section

### 7. Date Consistency — 5 pts
- 5 pts: All dates present and in consistent format
- 3 pts: Minor inconsistencies
- 0 pts: Missing dates or unexplained gaps >12 months

### 8. Length — 5 pts
- 0–3 yrs exp → 1 page = 5 pts
- 4–10 yrs exp → 2 pages = 5 pts
- 10+ yrs exp → 2–3 pages = 5 pts
- Significantly over = deduct 3 pts

## Grade Scale

| Score | Grade | Meaning |
|-------|-------|---------|
| 90–100 | 🟢 Excellent | Will pass most ATS filters |
| 75–89 | 🟡 Good | Minor improvements recommended |
| 60–74 | 🟠 Fair | Significant gaps — optimize before applying |
| 45–59 | 🔴 Weak | Major rework needed |
| 0–44 | ⛔ Critical | Likely auto-rejected |

## Common ATS Killers (Always Check)

- Contact info only in header/footer (ATS may miss it)
- Skills buried inside job bullets — not in a dedicated section
- Dates in unusual formats ("Spring 2022", "Q1 2023")
- Job titles that don't match standard industry terminology
- Generic summary ("Hardworking professional with passion for excellence")
- Bullet points that are full paragraphs (>3 lines)
- Using "I" statements anywhere
- Tables or text boxes (invisible to most ATS parsers)
