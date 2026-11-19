import os
from playwright.sync_api import sync_playwright
import pypdf

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Adarsh Tiwari - QA Engineer & SDET Resume</title>
  <style>
    @page {
      size: A4;
      margin: 12mm 15mm 12mm 15mm;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
      font-size: 9.3pt;
      line-height: 1.38;
      color: #1e293b;
      background: #ffffff;
    }
    a {
      color: #0369a1;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }

    /* Header */
    .header {
      text-align: center;
      padding-bottom: 8px;
      border-bottom: 2px solid #0f172a;
      margin-bottom: 10px;
    }
    .name {
      font-size: 21pt;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #0f172a;
      text-transform: uppercase;
      margin-bottom: 3px;
    }
    .title {
      font-size: 11pt;
      font-weight: 700;
      color: #1e40af;
      margin-bottom: 6px;
      letter-spacing: 0.3px;
    }
    .contact-bar {
      font-size: 8.8pt;
      color: #334155;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .separator {
      color: #94a3b8;
    }

    /* Section Styling */
    .section {
      margin-bottom: 11px;
    }
    .section-title {
      font-size: 10.2pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: #0f172a;
      border-bottom: 1.5px solid #0f172a;
      padding-bottom: 2px;
      margin-bottom: 6px;
    }

    /* Text */
    .summary-text {
      font-size: 9.2pt;
      color: #334155;
      text-align: justify;
      line-height: 1.42;
    }

    /* Skills Table */
    .skills-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 9pt;
    }
    .skills-table td {
      padding: 2.2px 0;
      vertical-align: top;
    }
    .skill-cat {
      font-weight: 700;
      color: #0f172a;
      width: 24%;
    }
    .skill-val {
      color: #334155;
      width: 76%;
    }

    /* Experience Header */
    .job-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 3px;
    }
    .job-title {
      font-size: 10pt;
      font-weight: 700;
      color: #0f172a;
    }
    .company {
      font-weight: 700;
      color: #1e40af;
    }
    .job-meta {
      font-size: 8.8pt;
      font-weight: 600;
      color: #475569;
    }

    /* Bullets */
    ul {
      margin-left: 17px;
      margin-top: 3px;
    }
    li {
      font-size: 8.9pt;
      color: #334155;
      margin-bottom: 3.5px;
      line-height: 1.38;
      text-align: justify;
    }
    li strong {
      color: #0f172a;
      font-weight: 600;
    }

    /* Projects */
    .project-item {
      margin-bottom: 9px;
    }
    .project-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 2px;
    }
    .project-name {
      font-size: 9.6pt;
      font-weight: 700;
      color: #0f172a;
    }
    .project-tech {
      font-size: 8.4pt;
      font-weight: 600;
      color: #0369a1;
      font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
    }

    /* Education */
    .edu-grid {
      display: flex;
      justify-content: space-between;
      font-size: 9pt;
      margin-top: 2px;
    }
    .edu-item {
      width: 48%;
    }
    .edu-degree {
      font-weight: 700;
      color: #0f172a;
    }
    .edu-meta {
      font-size: 8.5pt;
      color: #475569;
      margin-top: 1px;
    }

    /* Page Break */
    .page-break {
      page-break-before: always;
    }
  </style>
</head>
<body>

  <!-- ==================== PAGE 1 ==================== -->

  <!-- HEADER -->
  <div class="header">
    <div class="name">Adarsh Tiwari</div>
    <div class="title">Software Development Engineer in Test (SDET) | QA Automation Engineer</div>
    <div class="contact-bar">
      <span>Jaunpur / Varanasi, Uttar Pradesh, India (Open to Relocation)</span>
      <span class="separator">|</span>
      <span>+91 7000426836</span>
      <span class="separator">|</span>
      <span><a href="mailto:tiwarishrey0@gmail.com">tiwarishrey0@gmail.com</a></span>
      <span class="separator">|</span>
      <span><a href="https://www.linkedin.com/in/adarsh-shrey-tiwari">linkedin.com/in/adarsh-shrey-tiwari</a></span>
      <span class="separator">|</span>
      <span><a href="https://github.com/Adarsh-tiwari1223">github.com/Adarsh-tiwari1223</a></span>
    </div>
  </div>

  <!-- PROFESSIONAL SUMMARY -->
  <div class="section">
    <div class="section-title">Professional Summary</div>
    <div class="summary-text">
      Experienced <strong>Software Development Engineer in Test (SDET) / QA Engineer</strong> with in-depth expertise across <strong>Manual Testing, REST API Testing, and Playwright Test Automation</strong> in enterprise-scale web applications. Proven track record in designing, building, and scaling automated testing frameworks using <strong>Python, Playwright, and PyTest</strong> implementing the <strong>Page Object Model (POM)</strong> architecture. Specialized in multi-tier verification covering complex business workflows, multi-role access controls (RBAC), API contract schemas, and transactional database integrity. Brings strong analytical problem-solving skills across enterprise <strong>HRMS &amp; Payroll</strong>, <strong>US IT Recruitment</strong>, and <strong>Travel Management</strong> platforms, backed by a Master of Computer Applications (MCA) degree.
    </div>
  </div>

  <!-- TECHNICAL COMPETENCIES -->
  <div class="section">
    <div class="section-title">Technical Competencies</div>
    <table class="skills-table">
      <tr>
        <td class="skill-cat">Test Automation:</td>
        <td class="skill-val">Playwright (Python), PyTest, Selenium WebDriver (Python), Page Object Model (POM), Data-Driven Frameworks, Reusable Scope-Aware Fixtures, Headless Execution</td>
      </tr>
      <tr>
        <td class="skill-cat">API &amp; Backend Testing:</td>
        <td class="skill-val">RESTful API Validation, Postman, Python Requests Library, Status Codes, JSON Schema Contracts, Request/Response Payload Assertions, Header &amp; Token Validation</td>
      </tr>
      <tr>
        <td class="skill-cat">Database &amp; Data Integrity:</td>
        <td class="skill-val">SQL Queries, Relational Database Auditing, Backend State Verification, Data Consistency Checks, Transaction Rollback Auditing</td>
      </tr>
      <tr>
        <td class="skill-cat">Testing Methodologies:</td>
        <td class="skill-val">Functional Testing, Regression Testing, Smoke &amp; Sanity Testing, Integration Testing, End-to-End (E2E), Exploratory Testing, UAT, Boundary Value Analysis, Negative Testing</td>
      </tr>
      <tr>
        <td class="skill-cat">Test Management &amp; CI/CD:</td>
        <td class="skill-val">Requirement Traceability, Test Scenario Creation, Test Case Design, Defect Lifecycle Management, Jira, GitHub Actions (CI/CD Pipelines), Docker, Git, Linux</td>
      </tr>
      <tr>
        <td class="skill-cat">AI-Assisted QA:</td>
        <td class="skill-val">AI-Powered Test Scenario Expansion, Edge-Case Identification, Synthetic Test Data Generation, Automation Scripting Assistance &amp; Optimization</td>
      </tr>
    </table>
  </div>

  <!-- PROFESSIONAL EXPERIENCE -->
  <div class="section">
    <div class="section-title">Professional Experience</div>
    
    <div class="job-header">
      <div>
        <span class="job-title">QA Engineer / SDET</span> &mdash; <span class="company">TEK Inspirations LLC (Originator Informatics Pvt. Ltd.)</span>
      </div>
      <div class="job-meta">Jul 2025 – Present | Varanasi, Uttar Pradesh</div>
    </div>
    
    <ul>
      <li>Led quality engineering and test execution across 3 flagship enterprise products: <strong>HR Lense (HRMS &amp; Payroll System)</strong>, <strong>US IT Recruitment Management System</strong>, and <strong>Travel Management System</strong>.</li>
      <li>Analyzed sprint user stories, Product Requirement Documents (PRDs), and business workflow architectures to design comprehensive test plans, test scenarios, and detailed test cases with full requirements coverage.</li>
      <li>Executed end-to-end testing cycles encompassing Functional, Regression, Smoke, Sanity, Integration, System, and User Acceptance Testing (UAT), ensuring zero Sev-1 defects escaped to client environments.</li>
      <li>Architected automated UI test suites using <strong>Python, Playwright, and PyTest</strong> following the <strong>Page Object Model (POM)</strong>, replacing manual regression overhead and accelerating regression cycle completion.</li>
      <li>Engineered custom, scope-aware <strong>PyTest fixtures</strong> for session authentication, browser context configuration, and test data setup, eliminating repetitive login actions across test modules.</li>
      <li>Conducted extensive REST API validation using <strong>Postman and Python Requests</strong>, asserting status codes, payload structures, JSON schemas, response latency, and authorization token lifecycles.</li>
      <li>Validated multi-tier <strong>Role-Based Access Control (RBAC)</strong> and approval hierarchies across Super Admin, HR Manager, Recruiter, and Employee roles, verifying data segregation and preventing permission leaks.</li>
      <li>Executed direct <strong>SQL database queries</strong> to validate backend state transitions, confirming that critical financial, attendance, and onboarding transactions committed accurately to relational tables.</li>
      <li>Documented, tracked, and verified defect lifecycles in <strong>Jira</strong> with complete diagnostic logs, reproduction steps, network requests, and screenshots; collaborated closely with developers during sprint triage.</li>
    </ul>
  </div>

  <!-- ==================== PAGE 2 ==================== -->
  <div class="page-break"></div>

  <!-- KEY ENTERPRISE PROJECTS -->
  <div class="section">
    <div class="section-title">Key Enterprise Projects</div>

    <!-- Project 1: HR Lense -->
    <div class="project-item">
      <div class="project-header">
        <span class="project-name">1. HR Lense &mdash; Enterprise HRMS &amp; Payroll Platform</span>
        <span class="project-tech">Python · Playwright · PyTest · REST APIs · SQL · POM · Requests</span>
      </div>
      <ul>
        <li>Validated mission-critical enterprise modules: Employee Onboarding, Attendance &amp; Shift Management, Leave Accrual &amp; Approvals, Payroll Generation, and Document Management.</li>
        <li>Engineered a specialized <strong>Python-based payroll validation utility</strong> that programmatically parses exported payroll calculations (gross salary, allowances, deductions, net pay) and validates them against backend API and database records, identifying calculation mismatches with 100% precision.</li>
        <li>Automated core regression paths using <strong>Playwright with Python</strong>, utilizing dynamic locators and event-driven assertions to achieve resilient, headless execution across multiple browsers.</li>
        <li>Executed multi-tier integration testing across interrelated workflows (e.g., leave deduction impacting salary generation), ensuring cross-module data consistency across the entire employee lifecycle.</li>
        <li>Wrote targeted SQL queries to verify database consistency across multi-table relationships, validating that payroll lockouts, status updates, and audit trails accurately reflect business rules.</li>
      </ul>
    </div>

    <!-- Project 2: US IT Recruitment -->
    <div class="project-item">
      <div class="project-header">
        <span class="project-name">2. US IT Recruitment Management System</span>
        <span class="project-tech">Playwright · Python · Postman · REST API Testing · RBAC · Jira</span>
      </div>
      <ul>
        <li>Validated the end-to-end staffing lifecycle: Client Requirement Acquisition, Job Posting, Candidate Sourcing, Client Submissions, Interview Scheduling, and Consultant Onboarding.</li>
        <li>Conducted rigorous boundary and negative testing on multi-tenant access controls, verifying that recruitment teams and external vendor portals maintain strict candidate data isolation.</li>
        <li>Performed REST API contract testing to guarantee data integrity between the applicant tracking interface and backend submission databases.</li>
        <li>Automated candidate onboarding workflows and status transition journeys using <strong>Playwright</strong> component fixtures, reducing manual pipeline verification effort.</li>
        <li>Identified and logged high-impact edge cases involving concurrent candidate submissions, interview rescheduling conflicts, and duplicate consultant profile creation.</li>
      </ul>
    </div>

    <!-- Project 3: Travel Management -->
    <div class="project-item">
      <div class="project-header">
        <span class="project-name">3. Travel Management System (Client Portal &amp; Administrative Console)</span>
        <span class="project-tech">Manual Testing · REST APIs · SQL · Chrome DevTools · Cross-Browser</span>
      </div>
      <ul>
        <li>Executed comprehensive testing across inquiry management, customized itinerary generation, travel package configuration, and booking reservation lifecycles.</li>
        <li>Validated real-time bi-directional data synchronization between the customer-facing booking portal and the internal administrative operations panel.</li>
        <li>Executed negative scenarios and edge cases around session timeouts, currency conversions, payment gateway mock responses, and booking cancellation state rollbacks.</li>
      </ul>
    </div>
  </div>

  <!-- AI-ASSISTED TESTING & ENGINEERING PRACTICES -->
  <div class="section">
    <div class="section-title">Modern QA Engineering &amp; AI-Assisted Practices</div>
    <ul>
      <li><strong>AI-Assisted Test Engineering:</strong> Leverages generative AI tools to systematically uncover non-obvious boundary conditions, generate complex synthetic test datasets, and optimize automation scripts.</li>
      <li><strong>Multi-Layer Quality Philosophy:</strong> Champions validation beyond UI DOM checks by verifying what the front-end renders, what the API returns, and what the database commits to disk.</li>
      <li><strong>Open-Source &amp; Automation Architecture:</strong> Active maintainer of the open-source <strong>HRlens_Playwright</strong> test suite and interactive developer portfolio at <em>github.com/Adarsh-tiwari1223</em>.</li>
    </ul>
  </div>

  <!-- EDUCATION -->
  <div class="section">
    <div class="section-title">Education</div>
    <div class="edu-grid">
      <div class="edu-item">
        <div class="edu-degree">Master of Computer Applications (MCA)</div>
        <div class="edu-meta">Kashi Institute of Technology | Graduated: 2025</div>
      </div>
      <div class="edu-item">
        <div class="edu-degree">Bachelor of Science (B.Sc.)</div>
        <div class="edu-meta">Allahabad State University | Graduated: 2022</div>
      </div>
    </div>
  </div>

</body>
</html>
"""

def generate(month_year="nov_2026"):
    output_html = "resume/Adarsh_Tiwari_Resume.html"
    output_pdf = f"resume/Adarsh_Tiwari_QA_{month_year}.pdf"
    
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Wrote HTML: {output_html}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(HTML_CONTENT, wait_until="networkidle")
        
        page.pdf(
            path=output_pdf,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        browser.close()
    
    reader = pypdf.PdfReader(output_pdf)
    print(f"SUCCESS: Generated {output_pdf} with EXACTLY {len(reader.pages)} page(s)!")
    for i, page in enumerate(reader.pages):
        print(f"  Page {i+1} characters: {len(page.extract_text())}")

if __name__ == "__main__":
    generate("nov_2026")
