# Fit Scoring Criteria

Standard scoring used by all JobForge skills when evaluating job-candidate fit.

## Step 1: Check Dealbreakers First

Immediately mark as **Skip** if ANY dealbreaker from `preferences.md` is present:
- Role type or company type the user excluded (e.g. "no agencies", "no crypto")
- Location requirement that conflicts with user's location preference
- Mandatory in-office when user wants remote (or vice versa)
- Requires clearance/security the user doesn't have
- Salary clearly below the user's minimum threshold

## Step 2: Score Must-Haves

Check how many must-have criteria from `preferences.md` the job satisfies:
- All met → proceed to nice-to-haves
- 2–3 met → potential Medium fit
- 0–1 met → Low fit

## Step 3: Score Nice-to-Haves

For jobs that passed must-haves, evaluate nice-to-haves:
- Company stage/funding match
- Industry alignment
- Tech stack overlap
- Growth potential and role scope
- Brand or mission alignment

## Step 4: Skill Match

Compare job requirements to resume skills/experience:
- **High overlap** (≥70% requirements matched) → boosts fit
- **Moderate overlap** (40–69%) → neutral
- **Low overlap** (<40%) → reduces fit rating

## Step 5: Assign Rating

| Rating | Criteria |
|--------|----------|
| **High** | No dealbreakers + all must-haves + 2+ nice-to-haves + high skill match |
| **Medium** | No dealbreakers + most must-haves OR all must-haves but few nice-to-haves |
| **Low** | No dealbreakers but significant must-have or skill gaps |
| **Skip** | Any dealbreaker present — do not show to user |
