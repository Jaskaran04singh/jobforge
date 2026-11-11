# ATS Platform Patterns

Used by the `apply` skill to detect which ATS a job posting uses.

## Detection Rules (check URL and page content)

| ATS | URL Patterns | Page Signals |
|-----|-------------|--------------|
| **Greenhouse** | `boards.greenhouse.io`, `grnh.se`, `app.greenhouse.io` | `grnhse_iframe`, `Greenhouse` in page source |
| **Lever** | `jobs.lever.co`, `lever.co/[company]/jobs` | Lever branding, `lever-job-posting` class |
| **Workday** | `*.myworkdayjobs.com`, `wd1.myworkdaysite.com` | Workday logo, "Apply with Workday" |
| **Ashby** | `jobs.ashbyhq.com` | Ashby branding |
| **iCIMS** | `*.icims.com`, `careers.*.com/icims` | iCIMS branding |
| **Taleo** | `*.taleo.net`, `tbe.taleo.net` | Taleo/Oracle branding |
| **SmartRecruiters** | `jobs.smartrecruiters.com` | SmartRecruiters UI |
| **LinkedIn Easy Apply** | `linkedin.com/jobs` | "Easy Apply" button present |
| **Workable** | `apply.workable.com` | Workable branding |
| **BambooHR** | `*.bamboohr.com/jobs` | BambooHR branding |

## ATS-Specific Notes

### Greenhouse
- Navigate to posting URL — form is in an iframe (`grnhse_iframe`)
- Extract iframe tokens via JS: `document.getElementById('grnhse_iframe').src`
- Navigate to direct form URL: `https://job-boards.greenhouse.io/embed/job_app?for={boardToken}&token={jobToken}`
- `form_input` with value works directly for all field types

### Lever
- Append `/apply` to job posting URL to reach the form directly
- Or navigate to posting and click "APPLY FOR THIS JOB"
- `form_input` works for all field types including dropdowns

### Workday
- Navigate to posting, click "Apply Now"
- If Autofill/Manual options appear → click "Apply Manually"
- If auth gate appears → tell user to sign in, wait for "continue"
- Multi-step wizard: scan each page by scrolling (read_page only shows viewport)
- Radio buttons: use `find` tool or click at coordinates (not in read_page output)
- Dropdowns: click button → locate option in popup panel → click option

### Unknown ATS
- Take a screenshot, describe what you see
- Attempt to identify form fields
- If unrecognizable, tell the user and ask for guidance
