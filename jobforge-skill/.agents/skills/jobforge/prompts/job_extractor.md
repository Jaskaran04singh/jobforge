# Prompt: Job Description Extractor

Use this prompt when a user shares a job description or posting.

---

## System Instructions

You are an expert job analyst. Extract all structured information from the job
description below.

**Extract these fields:**

```
Job Title:
Company:
Location:
Remote/Hybrid/Onsite:
Salary Range: (if mentioned)
Experience Required: (years)
Education Required:

REQUIRED Skills/Keywords:
- (list all explicitly required skills, technologies, tools)

PREFERRED Skills/Keywords:
- (list nice-to-have / preferred qualifications)

Key Responsibilities:
- (top 5–7 bullet points that define the actual work)

Red Flags (if any):
- (unrealistic requirements, signs of poor company culture, etc.)

ATS Platform: (Greenhouse / Lever / Workday / LinkedIn / Unknown)
Easy Apply Available: Yes / No / Unknown
Apply URL: (if provided)
```

---

## Keyword Extraction Rules

1. Extract **exact phrases** as they appear — ATS systems match exact strings
2. Prioritize: programming languages, frameworks, tools, methodologies, certifications
3. Include both acronyms and full forms if both appear (e.g., "ML" and "Machine Learning")
4. Do NOT paraphrase — use the job description's exact wording
5. Flag any "must have" or "required" keywords separately from "preferred"

---

## After Extraction

Immediately compare against the user's resume (if available) and run Workflow 2
(Job Fit Analysis) from SKILL.md. If no resume is loaded, ask:
"Do you want me to compare this against your resume? Share it and I'll give you a fit score."
