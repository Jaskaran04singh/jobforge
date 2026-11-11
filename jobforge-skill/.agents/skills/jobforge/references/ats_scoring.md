# ATS Scoring Rules Reference

## Score Calculation (Total: 100 points)

### 1. Keyword Match — 25 points
- Identify the user's target role (from resume's `primary_role` or ask)
- Compare resume keywords vs standard keywords for that role
- Score: `(matched_keywords / total_expected_keywords) * 25`
- **Deduct 5 points** if critical keywords (from a specific job) are missing

### 2. Quantified Achievements — 20 points
- Count bullet points that contain numbers, percentages, or measurable outcomes
- Score formula:
  - 0 quantified bullets = 0 pts
  - 1–2 = 5 pts
  - 3–5 = 10 pts
  - 6–9 = 15 pts
  - 10+ = 20 pts
- Examples of good quantified bullets:
  - ✅ "Reduced API response time by 40% through caching"
  - ✅ "Managed a team of 8 engineers across 3 projects"
  - ❌ "Responsible for improving system performance"

### 3. Section Structure — 15 points
- Required sections (3 pts each): Contact, Summary/Objective, Experience, Education, Skills = 15 pts max
- **Deduct 3 pts** for each missing required section
- Bonus sections (no extra points, but noted): Projects, Certifications, Achievements

### 4. File Format / Formatting Safety — 10 points
- 10 pts if resume is clean text (no tables, no text boxes, no headers/footers with critical info)
- 7 pts if minor formatting issues detected
- 5 pts if tables or columns detected (ATS often can't parse these)
- 3 pts if heavy formatting (graphics, icons, charts) detected
- Note: Since we work with text, infer formatting issues from structure

### 5. Action Verbs — 10 points
- Count bullet points starting with strong action verbs
- Score: `(action_verb_bullets / total_bullets) * 10`
- Strong verbs: Built, Led, Designed, Implemented, Increased, Reduced, Managed, Launched, Developed, Architected, Spearheaded, Optimized, Delivered, Automated, etc.
- Weak verbs to flag: Responsible for, Helped with, Assisted in, Worked on

### 6. Skills Section — 10 points
- 10 pts: Explicit skills section with 10+ relevant technical skills listed
- 7 pts: Skills section present with 5–9 skills
- 5 pts: Skills section present but sparse (<5 skills)
- 0 pts: No skills section

### 7. Date Consistency — 5 points
- 5 pts: All dates consistent and parseable (e.g., "Jan 2022 – Mar 2024" or "2022–2024")
- 3 pts: Minor inconsistencies
- 0 pts: Missing dates, unexplained gaps >12 months

### 8. Length Appropriateness — 5 points
- 0–3 years experience → 1 page = 5 pts, 2 pages = 2 pts
- 4–10 years experience → 2 pages = 5 pts, 1 page = 3 pts, 3 pages = 2 pts
- 10+ years experience → 2–3 pages = 5 pts
- Estimate length from word count: ~400–500 words ≈ 1 page

---

## ATS Score Interpretation

| Score | Grade | Interpretation |
|-------|-------|---------------|
| 90–100 | 🟢 Excellent | Likely to pass most ATS filters |
| 75–89 | 🟡 Good | Minor improvements recommended |
| 60–74 | 🟠 Fair | Significant gaps, optimize before applying |
| 45–59 | 🔴 Weak | Major rework needed |
| 0–44 | ⛔ Critical | Resume likely auto-rejected |

---

## Common ATS Killers (Always Check)

- Using "I" statements in bullets (unprofessional)
- Contact info only in header/footer (ATS may miss it)
- Skills buried inside job descriptions (extract to dedicated skills section)
- Dates in unusual formats ("Spring 2022", "Q1 2023")
- Job titles that don't match standard industry titles
- Generic summary ("Hardworking professional with passion for excellence")
- Bullet points that are full paragraphs (>3 lines)
- No summary/professional profile section
