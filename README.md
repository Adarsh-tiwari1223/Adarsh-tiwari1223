# Adarsh Tiwari

### Software Development Engineer in Test (SDET)

**Python · Playwright · PyTest · REST APIs · SQL · GitHub Actions · Docker**

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_GITHUB_USERNAME&show_icons=true&hide_border=true&rank_icon=github" height="165">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_GITHUB_USERNAME&layout=compact&hide_border=true" height="165">
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=YOUR_GITHUB_USERNAME&hide_border=true" />
</p>

---

## 👨‍💻 About Me

I am an **SDET focused on web application and API test automation**, with hands-on experience building and maintaining automated test suites using **Python, Playwright, and PyTest**.

My testing approach goes beyond validating the happy path. I focus on **business workflows, role-based access, state transitions, API contracts, database consistency, and regression coverage**.

> **I don't just find bugs. I find assumptions that were never tested.**

---

## 🛠️ Technical Stack

| Area                     | Technologies                                     |
| ------------------------ | ------------------------------------------------ |
| **Languages**            | Python 3.11+, SQL                                |
| **UI Automation**        | Playwright, PyTest, Selenium                     |
| **API Testing**          | REST API, Requests, Postman, JSON validation     |
| **Database**             | SQL, Backend/Data validation                     |
| **CI/CD**                | GitHub Actions                                   |
| **Containers**           | Docker                                           |
| **Version Control**      | Git, GitHub                                      |
| **Testing Architecture** | Page Object Model, Fixtures, Reusable Components |
| **Reporting**            | Pytest HTML, Allure, Structured Logging          |
| **Defect Management**    | Jira, RCA, Defect Tracking                       |
| **OS/Environment**       | Linux, Windows                                   |

---

# 🚀 Featured Project

## HRlens — HR Management System

**HRlens** is an enterprise HR management platform where I work across **manual testing and automation testing**, validating complex employee and administrative workflows.

### QA & Automation

* Python + PyTest + Playwright
* Page Object Model architecture
* Reusable and scope-aware PyTest fixtures
* UI functional and regression automation
* API validation
* SQL/database verification
* Role-Based Access Control testing
* End-to-end business workflow testing
* Cross-role workflow validation
* CI/CD test execution
* Defect investigation and RCA

### Major Workflow Areas

```text
Employee Management
        ↓
Attendance & Working Hours
        ↓
Leave Management
        ↓
Recruitment
        ↓
Documents
        ↓
Assets
        ↓
Role & Permission Management
        ↓
Administrative Workflows
```

### Automation Validation Model

```text
             TEST SCENARIO
                   │
          ┌────────┴────────┐
          ↓                 ↓
        UI TEST           API TEST
          │                 │
          └────────┬────────┘
                   ↓
             DATABASE CHECK
                   │
                   ↓
             BUSINESS RULE
               VALIDATION
                   │
                   ↓
             FINAL ASSERTION
```

---

# 🔍 What I Test

My automation focuses on areas where defects commonly escape basic functional testing.

```text
Boundary Conditions
        ↓
State Transitions
        ↓
Role & Permission Isolation
        ↓
API Contract Validation
        ↓
Database Consistency
        ↓
Duplicate Submission / Idempotency
        ↓
Session & Authentication States
        ↓
End-to-End Business Workflows
```

### Example

```text
User Action
    ↓
UI State
    ↓
API Request
    ↓
Backend Processing
    ↓
Database State
    ↓
Business Rule
    ↓
Expected Result
```

This allows defects to be identified at the **system level**, rather than only at the UI layer.

---

# 🧪 Testing Approach

### Manual Testing

* Functional Testing
* Regression Testing
* Integration Testing
* System Testing
* Exploratory Testing
* Negative Testing
* Boundary Value Testing
* Role-Based Access Testing
* End-to-End Workflow Testing

### Automation Testing

* Playwright E2E automation
* PyTest test framework
* Page Object Model
* Fixture-based test setup
* Parameterized testing
* API + UI integration
* Database assertions
* Screenshot and trace capture
* CI-based regression execution

---

# ⚙️ CI/CD Automation

My automation is designed to run as part of the development workflow.

```text
Developer Push / Pull Request
              ↓
        GitHub Actions
              ↓
       Install Dependencies
              ↓
        Start Test Environment
              ↓
       Execute PyTest Suite
              ↓
      Playwright Test Execution
              ↓
        Generate Reports
              ↓
        Pass / Fail Pipeline
```

### Example Pipeline

```yaml
name: Playwright Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Install Playwright
        run: playwright install --with-deps chromium

      - name: Run tests
        run: pytest -v

      - name: Upload reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: |
            reports/
            screenshots/
```

---

# 📊 GitHub Activity

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=YOUR_GITHUB_USERNAME&hide_border=true" />
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YOUR_GITHUB_USERNAME&no-frame=true&no-bg=true&margin-w=5" />
</p>

---

# 📌 Engineering Principles

```text
Automation should reduce repetitive effort.
Assertions should validate business behavior.
Tests should be independent and maintainable.
Failures should provide actionable evidence.
CI should detect regressions early.
A passing UI does not always mean a healthy system.
```

---

# 📈 Current Focus

```text
Advanced Playwright Automation
        +
API Automation
        +
SQL / Backend Validation
        +
CI/CD
        +
Docker
        +
Test Architecture
        +
SDET Engineering Practices
```

---

# 📬 Connect

**Location:** India
**Open to:** Remote · Bangalore · Gurgaon/Delhi NCR · Hyderabad · Noida

**LinkedIn:**
https://www.linkedin.com/in/adarsh-shrey-tiwari

**Email:**
[tiwarishrey0@gmail.com](mailto:tiwarishrey0@gmail.com)

---

### ⭐ If you are interested in QA Automation, SDET, Playwright, PyTest or CI/CD, feel free to explore my repositories.
