<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,100:0d1117&height=1&section=header"/>

</div>

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ADARSH TIWARI  //  Quality Assurance Engineer                  ║
║   Selenium · PyTest · CRM · HRMS · Workflow Systems              ║
║                                                                  ║
║   "I don't find bugs. I find assumptions that were never tested." ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## What I Actually Do

Most QA engineers **validate that software works**.  
I validate that software works **the way users actually behave** — not the way developers assumed they would.

That distinction is the entire job.

I specialize in **enterprise workflow systems** — CRM pipelines, HRMS modules, role-based access matrices — where a single skipped edge case doesn't just break a feature, it breaks a business process.

My testing starts before any test case is written: understanding the **domain model**, the **failure modes that matter**, and the **assumptions baked into the requirements**. By the time I'm writing test cases, I already know where the system will break.

---

## What I'm Building Right Now

```
Selenium + PyTest Automation Framework
──────────────────────────────────────
Architecture  →  Page Object Model (strict separation of locators, actions, tests)
Test Data     →  JSON fixtures + Faker for dynamic generation
Fixtures      →  conftest.py with scope-aware session/function setup
Reporting     →  HTML reports via pytest-html + structured failure logs
Status        →  Active development — regression suite for HRMS flows
```

The goal isn't just automation. It's **automation that a junior engineer can maintain six months from now** without asking me what any of it does.

---

## Testing Philosophy — in practice, not in posters

**Before writing a single test case, I ask:**

- What is the system *supposed* to do? (requirements)
- What do users *actually* do? (observed behavior patterns)
- Where do those two things diverge? (the real risk surface)

**The cases that actually find bugs:**

| Type | What I'm really checking |
|------|--------------------------|
| Boundary inputs | Does the system degrade gracefully or explode silently? |
| State transitions | Can a Lead skip stages it shouldn't? Can a closed Deal reopen? |
| Role boundaries | Does the UI hide things, or does the *API* actually block them? |
| Data integrity | Does saving twice create two records? Does cancel *actually* cancel? |
| Session behavior | What happens to a form when the session expires mid-fill? |

The last two rows are where most bugs live. Most test suites stop at row one.

---

## Domain Coverage

**CRM Systems**
- Lead lifecycle: creation → qualification → conversion → closure
- Multi-stage Deal approval flows with role-gated transitions
- Permission matrix testing: what each role can *see* vs. *do* vs. *cannot access*
- Workflow restriction validation: user-level rules, override logic, audit trails

**HRMS Systems**
- Employee management: onboarding data integrity, field validation, duplicate detection
- Leave management: balance calculations, approval chains, edge cases at period boundaries  
- Attendance: clock-in/out sequences, break handling, data sync consistency
- Document workflows: upload → review → approval → archive, with role access at each gate

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

learning = [
    "Advanced PyTest fixtures and parametrize patterns",
    "CI/CD pipeline integration (GitHub Actions)",
    "API-layer test coverage to complement UI automation",
]
```

---

## How I Write Defects

A defect report is a **reproducibility contract** between me and the developer.

```
TITLE         : Precise. No vague "Login fails" — write "Login fails when 
                email contains uppercase characters despite case-insensitive 
                spec in AUTH-214"

ENVIRONMENT   : Browser, OS, test account role, data state at time of failure

STEPS         : Numbered. Atomic. Someone who's never seen the system can 
                reproduce this in under 5 minutes.

EXPECTED      : What the spec says, with reference

ACTUAL        : Exactly what happened, with screenshot and console log

SEVERITY      : Tied to business impact, not personal frustration
```

Developers merge my bug reports without asking follow-up questions.  
That's the metric I care about.

---

## Roadmap — 2025

```
Q2  →  Complete POM framework for HRMS regression suite
Q3  →  Add API-level tests (requests + PyTest) alongside UI layer  
Q4  →  GitHub Actions CI integration: test runs on every PR
```

---

## Currently Open To

QA Engineer roles in **product companies** working on enterprise software.  
Preferably teams where QA is treated as an engineering discipline, not a bottleneck.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-adarsh--tiwari--qa-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/adarsh-tiwari-qa)&nbsp;
[![Email](https://img.shields.io/badge/Email-tiwarishrey0%40gmail.com-EA4335?style=flat-square&logo=gmail)](mailto:tiwarishrey0@gmail.com)

---

<sub>Last updated: 2025 · Building in public · Framework code dropping soon</sub>
