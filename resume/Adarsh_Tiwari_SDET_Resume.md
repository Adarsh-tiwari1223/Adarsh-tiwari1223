# ADARSH TIWARI
**Software Development Engineer in Test (SDET)**  
📍 India · Open to Remote / Bangalore / Gurgaon / Hyderabad / Noida  
📞 [Phone Number] · ✉️ [tiwarishrey0@gmail.com](mailto:tiwarishrey0@gmail.com)  
🔗 [LinkedIn: adarsh-shrey-tiwari](https://www.linkedin.com/in/adarsh-shrey-tiwari) · 🐙 [GitHub: Adarsh-tiwari1223](https://github.com/Adarsh-tiwari1223)

---

## PROFESSIONAL SUMMARY
Results-driven **Software Development Engineer in Test (SDET)** with expertise in architecting robust, scalable test automation frameworks for web applications and microservices using **Python, Playwright, and PyTest**. Proven track record in designing multi-layer validation architectures combining **UI automation, REST API contract validation, and SQL database state auditing**. Experienced in integrating automated regression pipelines into **GitHub Actions** and **Docker** to achieve deterministic, rapid CI/CD test feedback.

---

## TECHNICAL SKILLS

- **Languages:** Python (3.11+), SQL, Bash
- **Automation Frameworks:** Playwright, PyTest, Selenium WebDriver, Requests
- **Architecture & Design:** Page Object Model (POM), Scope-Aware Fixtures, Data-Driven Testing (DDT), Modular Test Design
- **API & Contract Testing:** REST API Automation, JSON Schema Validation, Postman, RBAC Boundary Verification
- **Databases & Validation:** SQL, RDBMS Backend Auditing, Transactional Integrity & State Transition Checks
- **DevOps & CI/CD:** GitHub Actions, Docker, Git, Linux / Bash Scripting
- **QA Methodologies:** Root Cause Analysis (RCA), Boundary Value Analysis, Negative Testing, Cross-Browser Testing, Exploratory Testing
- **Tools & Reporting:** Jira, PyTest-HTML, Allure, Structured Logging, Trace Viewer

---

## FLAGSHIP PROJECT & EXPERIENCE

### Software Development Engineer in Test (SDET) | HRlens Application
*Project Repository: [github.com/Adarsh-tiwari1223/HRlens_Playwright](https://github.com/Adarsh-tiwari1223/HRlens_Playwright)*

- Architected an end-to-end test automation framework using **Python, Playwright, and PyTest** implementing the **Page Object Model (POM)** for enterprise HR workflow testing.
- Automated **100+ UI scenarios** spanning Employee Lifecycle, Attendance & Time Tracking, Leave Management, Recruitment, and Role-Based Permissions.
- Formulated custom, scope-aware **PyTest fixtures** to manage browser contexts and session state injection, reducing test suite execution runtime by **~50%**.
- Integrated **REST API contract testing** with Python Requests to validate HTTP status codes, schema compliance, and authorization tokens prior to UI execution.
- Executed direct **SQL database queries** to verify backend persistence and prevent silent transactional rollback defects from escaping to production.
- Built a **GitHub Actions CI/CD pipeline** to trigger automated regression suites upon every pull request, automatically capturing execution artifacts, HTML reports, and Playwright video traces.
- Spearheaded **Root Cause Analysis (RCA)** for production defect leaks, reducing bug recurrence by documenting reproducible test scenarios and edge cases in Jira.

---

## TESTING ARCHITECTURE & METHODOLOGY

```text
               TRIGGER (GitHub Actions / Developer PR)
                                  │
                 ┌────────────────┴────────────────┐
                 ↓                                 ↓
            UI LAYER                           API LAYER
     Playwright + Fixtures                 Requests REST API
     • Page Object Model                   • Schema & Contract Check
     • Event-driven Waits                  • RBAC Authorization Token
                 │                                 │
                 └────────────────┬────────────────┘
                                  ↓
                        BUSINESS WORKFLOW LAYER
                       State Transition Mapping
                                  ↓
                        SQL / DATABASE AUDITING
                       Backend Integrity Checks
                                  ↓
                     FINAL DETERMINISTIC ASSERTION
                     Artifacts, Logs & Trace Output
```

---

## EDUCATION

**Bachelor of Technology (B.Tech)**  
*Computer Science & Engineering*

---

## KEY ACHIEVEMENTS & PHILOSOPHY
- **Zero-Tolerance for Flaky Tests:** Built resilient test synchronization using Playwright's locator assertions and auto-wait mechanisms without arbitrary sleep delays.
- **Security & Authorization Focus:** Developed comprehensive test suites verifying boundary access restrictions between Admin, Manager, and Employee roles.
- **Open-Source Contribution:** Authored the open-source **HRlens_Playwright** test suite and modern animated GitHub developer portfolio.
