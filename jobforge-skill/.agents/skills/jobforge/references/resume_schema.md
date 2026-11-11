# Resume Schema Reference

When parsing a resume, extract and structure it into this exact JSON format.
Return this structure internally to use across all workflows.

```json
{
  "contact": {
    "name": "",
    "email": "",
    "phone": "",
    "location": "",
    "linkedin": "",
    "github": "",
    "portfolio": ""
  },
  "summary": "",
  "skills": {
    "technical": [],
    "soft": [],
    "tools": [],
    "languages": []
  },
  "experience": [
    {
      "company": "",
      "title": "",
      "location": "",
      "start_date": "",
      "end_date": "",
      "is_current": false,
      "bullets": [],
      "keywords_found": []
    }
  ],
  "education": [
    {
      "institution": "",
      "degree": "",
      "field": "",
      "graduation_year": null,
      "gpa": null,
      "honors": ""
    }
  ],
  "projects": [
    {
      "name": "",
      "description": "",
      "technologies": [],
      "url": ""
    }
  ],
  "certifications": [
    {
      "name": "",
      "issuer": "",
      "year": null,
      "url": ""
    }
  ],
  "achievements": [],
  "total_years_experience": null,
  "primary_role": "",
  "industry": ""
}
```

## Parsing Rules

1. **Don't invent data** — if a field is not present, leave it empty/null
2. **Normalize dates** — convert all date formats to `YYYY-MM` or `YYYY`
3. **Extract keywords** — for each experience entry, list technical keywords found in bullets
4. **Identify primary role** — determine the user's main job title/track (e.g., "Backend Engineer", "Product Manager")
5. **Calculate experience** — total years = sum of all job durations (handle overlaps if obvious)
6. **Separate skills types:**
   - Technical: Python, SQL, React, etc.
   - Soft: Leadership, Communication, etc.
   - Tools: Jira, Figma, AWS Console, etc.
   - Languages: English, Spanish, etc.
