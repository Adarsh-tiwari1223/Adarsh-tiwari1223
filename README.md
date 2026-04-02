```
╔══════════════════════════════════════════════════════════════════╗
║  ADARSH TIWARI  //  Quality Assurance Engineer                   ║
║  Selenium · PyTest · Python · CRM · HRMS · Workflow Systems      ║
║                                                                  ║
║  "I don't find bugs.                                             ║
║   I find assumptions that were never tested."                    ║
╚══════════════════════════════════════════════════════════════════╝
```

Most QA engineers validate that software **works**.  
I validate that it works **the way users actually behave** — not the way developers assumed they would.

That distinction is the entire job.

---

## What I Specialize In

Enterprise workflow systems — CRM pipelines, HRMS modules, role-based access matrices — where a skipped edge case doesn't just break a feature. It breaks a business process.

My testing starts before any test case is written.

I spend the first phase understanding the **domain model**, the **failure modes that matter**, and the **assumptions baked silently into the requirements**. By the time I'm writing test cases, I already know where the system will likely break.

---

## Current Build

```
PROJECT       :  Selenium + PyTest Automation Framework
Architecture  :  Page Object Model — locators, actions, and tests stay separate
Test Data     :  JSON fixtures + Faker for runtime generation
Fixtures      :  conftest.py with scope-aware session/function hooks
Reporting     :  pytest-html + structured failure logs
Target        :  Regression suite for HRMS workflows
Goal          :  Automation a junior engineer can maintain 6 months later
                 without asking me what any of it does
```

---

## Stack

```python
core = {
    "language"    : "Python 3.x",
    "automation"  : "Selenium WebDriver + PyTest",
    "pattern"     : "Page Object Model",
    "data"        : "JSON fixtures · Faker",
    "api_testing" : "Postman",
    "tracking"    : "Jira · Git · GitHub",
    "reporting"   : "pytest-html · structured defect logs",
}

next = [
    "API-layer tests via requests + PyTest",
    "GitHub Actions CI integration",
    "Parametrized data-driven test expansion",
]
```

---

## Where Bugs Actually Hide

Most test suites check the obvious paths. These are the rows most suites skip:

```
Test Type              What I'm actually checking
─────────────────────────────────────────────────────────────────────
Boundary inputs      → Does the system degrade gracefully or fail silently?
State transitions    → Can a Lead skip stages it shouldn't?
                       Can a closed Deal be reopened without audit?
Role boundaries      → Does the UI hide things — or does the API actually
                       block them? (These are not the same thing.)
Data integrity       → Does saving twice create two records?
                       Does cancel actually cancel?
Session behavior     → What happens to a form when the session expires
                       mid-fill?
Concurrent actions   → What happens when two users edit the same record?
```

The last three rows are where most production bugs live.  
Most test suites stop at row one.

---

## Domain Coverage

**CRM Systems**
- Lead lifecycle: creation → qualification → conversion → closure
- Multi-stage Deal approval flows with role-gated transitions
- Permission matrix: what each role can *see* vs. *do* vs. *cannot access*
- Workflow restriction validation: user-level rules, override logic, audit trails

**HRMS Systems**
- Employee management: onboarding data integrity, field validation, duplicate detection
- Leave management: balance calculations, approval chains, edge cases at period boundaries
- Attendance: clock-in/out sequences, break handling, data sync consistency
- Document workflows: upload → review → approval → archive, role access at each gate

---

## How I Write Defects

A defect report is a **reproducibility contract** between me and the developer.

```
TITLE        :  Precise. Not "Login fails" — write "Login fails when email
                contains uppercase characters, despite case-insensitive
                spec in AUTH-214"

ENVIRONMENT  :  Browser · OS · test account role · data state at failure time

STEPS        :  Numbered. Atomic. Reproducible in under 5 minutes by someone
                who has never seen the system before.

EXPECTED     :  What the spec says, with reference to the requirement

ACTUAL       :  Exactly what happened — screenshot + console log attached

SEVERITY     :  Tied to business impact, not personal frustration
```

Developers merge my bug reports without asking follow-up questions.  
That's the metric I care about.

---

## Roadmap

```
Q2 2025  →  POM framework complete — HRMS regression suite live
Q3 2025  →  API-layer tests alongside UI layer (requests + PyTest)
Q4 2025  →  GitHub Actions CI: test runs triggered on every PR
2026     →  End-to-end automated regression with zero manual repetition
```

---

## Open To

QA Engineer roles at **product companies** building enterprise software.  
Teams where QA is an engineering discipline — not a sign-off ceremony at the end of a sprint.

```
tiwarishrey0@gmail.com
linkedin.com/in/adarsh-tiwari-qa
```
