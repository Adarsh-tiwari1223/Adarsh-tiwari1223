# Adarsh Tiwari

### Software Development Engineer in Test (SDET)
**Python · Playwright · PyTest · REST APIs · SQL · CI/CD · Docker**

```
╔══════════════════════════════════════════════════════════════════╗
║  "I don't just find bugs.                                        ║
║   I find assumptions that were never tested."                    ║
╚══════════════════════════════════════════════════════════════════╝
```

Most test suites validate that software works on the happy path. I build resilient automation architectures that stress-test how enterprise systems behave under real-world concurrency, state transitions, and strict API/DB contract boundaries.

---

## 🛠️ Technical Stack & Tools

* **Languages:** Python 3.11+, SQL
* **UI Automation:** Playwright, PyTest, Selenium WebDriver
* **API Testing:** Requests, Postman, REST API, JSON Schema Validation
* **DevOps & Infrastructure:** Docker, GitHub Actions, Linux, Git
* **Architecture & Patterns:** Page Object Model (POM), Scope-Aware Fixtures, Multi-Layer Assertions, RCA
* **Reporting & Observability:** Pytest-HTML, Allure, Structured Logging, Jira Defect Tracing

---

## 🚀 Flagship Automation Repositories

* **[playwright-pytest-enterprise-framework](https://github.com/your-username/playwright-pytest-enterprise-framework)**  
  Modular, production-ready E2E automation framework featuring Page Object Model, reusable PyTest fixtures, cross-browser execution, and multi-layer validation (UI + API + SQL DB). Integrated with Docker and GitHub Actions CI/CD.

* **[rest-api-automation-pytest](https://github.com/your-username/rest-api-automation-pytest)**  
  RESTful API testing suite built with Python and Requests, validating endpoint contracts, payload schemas, auth headers, and backend database state consistency.

---

## ⚙️ Production Test Architecture Blueprint

```
FRAMEWORK      :  Playwright + PyTest Multi-Layer Suite
Design Pattern :  Page Object Model (POM) with isolated locators & actions
Fixtures       :  conftest.py with session/function scope-aware dependency injection
Multi-Layer    :  API setup/teardown + UI state verification + SQL DB assertions
Container      :  Dockerized headless test runner for environment parity
CI Pipeline    :  GitHub Actions executing smoke & regression suites on every PR
```

---

## 🔍 Engineering Rigor: Where Bugs Actually Hide

```
Test Dimension       What My Automation Actually Validates
─────────────────────────────────────────────────────────────────────────────
Boundary Inputs    → Does the system degrade gracefully or fail silently?
State Machines     → Can an entity skip approval stages via direct URL manipulation?
Role Isolation     → Does the UI hide buttons — or does the API reject unauthorized payloads?
Data Integrity     → Do atomic transactions rollback completely on DB execution errors?
Idempotency        → Does double-clicking submit create duplicate DB records?
Session Boundary   → How does the state engine behave when auth tokens expire mid-flow?
Race Conditions    → What happens when concurrent requests modify the same entity?
```

---

## 💼 Domain & Enterprise Workflow Expertise

* **Enterprise CRM Workflows:** Lead lifecycles, deal approval hierarchies, dynamic pipeline stages, and strict multi-tier Role-Based Access Control (RBAC).
* **HRMS & Operations Systems:** Employee onboarding data integrity, complex leave balance calculation state machines, and attendance record synchronization.

---

## 🎯 Defect Engineering Contract

```
TITLE        :  Precise. "AUTH-402: Login allows lowercase bypass on uppercase-enforced
                usernames, violating RFC-5322 compliance"

ENVIRONMENT  :  Headless Chromium · Ubuntu 22.04 · Staging v2.4.1 · Auth Token State

REPRODUCTION :  Atomic steps reproducible in under 2 minutes by any engineer.

PAYLOAD/LOGS :  Exact cURL command, API response code, and DB state mismatch.

IMPACT       :  Tied to security and business process failure, not visual inconvenience.
```

---

## 📬 Connect

* **Location:** India (Open to Remote, Bangalore, Gurgaon/Delhi NCR, Hyderabad, Noida)
* **LinkedIn:** [linkedin.com/in/adarsh-shrey-tiwari](https://www.linkedin.com/in/adarsh-shrey-tiwari)
* **Email:** tiwarishrey0@gmail.com
