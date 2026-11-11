"""
JobForge Multi-Platform High-Volume Job Search Engine
Aggregates and normalizes 100-1000+ jobs across:
- LinkedIn
- Indeed
- Naukri
- Unstop
- Apna
- Shine
- Foundit (Monster)
- Greenhouse / Lever / Workday direct boards
"""

import urllib.parse
import json
import re
from typing import List, Dict, Any

SUPPORTED_PLATFORMS = [
    "linkedin", "indeed", "naukri", "unstop", "apna", "shine", "foundit", "greenhouse", "lever"
]

def build_search_queries(keywords: str, location: str = "India", remote: bool = True) -> Dict[str, str]:
    """Generates direct multi-platform search URLs for high volume job harvesting."""
    q_enc = urllib.parse.quote(keywords)
    loc_enc = urllib.parse.quote(location)
    
    urls = {
        "linkedin": f"https://www.linkedin.com/jobs/search/?keywords={q_enc}&location={loc_enc}&f_TPR=r604800" + ("&f_WT=2" if remote else ""),
        "indeed": f"https://in.indeed.com/jobs?q={q_enc}&l={loc_enc}&fromage=7" + ("&sc=0kf%3Aattr%28DSQF7%29%3B" if remote else ""),
        "naukri": f"https://www.naukri.com/{keywords.lower().replace(' ', '-')}-jobs-in-{location.lower()}?k={q_enc}&l={loc_enc}",
        "unstop": f"https://unstop.com/jobs?searchTerm={q_enc}&quickApply=true",
        "apna": f"https://apna.co/jobs?search={q_enc}&location={loc_enc}",
        "shine": f"https://www.shine.com/job-search/{keywords.lower().replace(' ', '-')}-jobs",
        "foundit": f"https://www.foundit.in/srp/results?query={q_enc}&locations={loc_enc}",
        "hiring_cafe": f"https://hiring.cafe/?search={q_enc}"
    }
    return urls

def parse_job_card(platform: str, raw_element: Dict[str, Any]) -> Dict[str, Any]:
    """Normalizes job data from any platform into canonical JobForge format."""
    return {
        "platform": platform,
        "title": raw_element.get("title", "").strip(),
        "company": raw_element.get("company", "").strip(),
        "location": raw_element.get("location", "Remote/India").strip(),
        "salary": raw_element.get("salary", "Not Disclosed").strip(),
        "url": raw_element.get("url", "").strip(),
        "easy_apply": bool(raw_element.get("easy_apply", False)),
        "posted": raw_element.get("posted", "Recent"),
        "raw_description": raw_element.get("description", "")
    }

def deduplicate_jobs(jobs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Deduplicates jobs by company + title similarity across all platforms."""
    seen = set()
    unique_jobs = []
    for job in jobs:
        # Create a unique key normalized
        norm_title = re.sub(r'[^a-zA-Z0-9]', '', job['title'].lower())
        norm_company = re.sub(r'[^a-zA-Z0-9]', '', job['company'].lower())
        key = f"{norm_company}:{norm_title[:15]}"
        if key not in seen and job.get("url"):
            seen.add(key)
            unique_jobs.append(job)
    return unique_jobs
