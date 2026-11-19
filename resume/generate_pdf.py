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
      margin: 8mm 11mm 8mm 11mm;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 8.5pt;
      line-height: 1.28;
      color: #1e293b;
      background: #ffffff;
    }
    a {
      color: #0284c7;
      text-decoration: none;
    }
    
    /* Header */
    .header {
      text-align: center;
      padding-bottom: 4px;
      border-bottom: 2px solid #0f172a;
      margin-bottom: 5px;
    }
    .name {
      font-size: 18pt;
      font-weight: 800;
      letter-spacing: -0.3px;
      color: #0f172a;
      text-transform: uppercase;
      margin-bottom: 1px;
    }
    .title {
      font-size: 9.8pt;
      font-weight: 700;
      color: #2563eb;
      margin-bottom: 3px;
      letter-spacing: 0.2px;
    }
    .contact-bar {
      font-size: 8pt;
      color: #475569;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 8px;
    }
    .contact-item {
      display: inline-flex;
      align-items: center;
    }
    .separator {
      color: #94a3b8;
    }

    /* Section */
    .section {
      margin-bottom: 5px;
    }
    .section-title {
      font-size: 9.2pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: #0f172a;
      border-bottom: 1.2px solid #cbd5e1;
      padding-bottom: 1px;
      margin-bottom: 3px;
    }

    /* Summary */
    .summary-text {
      font-size: 8.2pt;
      color: #334155;
      text-align: justify;
      line-height: 1.3;
    }

    /* Skills Grid */
    .skills-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.1pt;
    }
    .skills-table td {
      padding: 1px 0;
      vertical-align: top;
    }
    .skill-cat {
      font-weight: 700;
      color: #0f172a;
      width: 20%;
    }
    .skill-val {
      color: #334155;
      width: 80%;
    }

    /* Experience */
    .job-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 1px;
    }
    .job-title {
      font-size: 8.8pt;
      font-weight: 700;
      color: #0f172a;
    }
    .company {
      font-weight: 700;
      color: #2563eb;
    }
    .job-meta {
      font-size: 8pt;
      font-weight: 600;
      color: #64748b;
    }

    /* Bullets */
    ul {
      margin-left: 14px;
      margin-top: 1px;
    }
    li {
      font-size: 8.1pt;
      color: #334155;
      margin-bottom: 1.5px;
      line-height: 1.28;
      text-align: justify;
    }
    li strong {
      color: #0f172a;
      font-weight: 600;
    }

    /* Projects */
    .project-item {
      margin-bottom: 3px;
    }
    .project-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
    }
    .project-name {
      font-size: 8.5pt;
      font-weight: 700;
      color: #0f172a;
    }
    .project-tech {
      font-size: 7.6pt;
      font-weight: 600;
      color: #0284c7;
      font-family: ui-monospace, Menlo, Consolas, monospace;
    }

    /* Education */
    .edu-grid {
      display: flex;
      justify-content: space-between;
      font-size: 8.1pt;
    }
    .edu-item {
      width: 48%;
    }
    .edu-degree {
      font-weight: 700;
      color: #0f172a;
    }
    .edu-meta {
      font-size: 7.8pt;
      color: #64748b;
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <div class="name">Adarsh Tiwari</div>
    <div class="title">QA Engineer | Automation &amp; API Testing Specialist | SDET</div>
    <div class="contact-bar">
      <span class="contact-item">📍 Jaunpur / Varanasi, UP (Open to Relocation)</span>
      <span class="separator">•</span>
      <span class="contact-item">📞 +91 7000426836</span>
      <span class="separator">•</span>
      <span class="contact-item">✉️ <a href="mailto:tiwarishrey0@gmail.com">tiwarishrey0@gmail.com</a></span>
      <span class="separator">•</span>
      <span class="contact-item">🔗 <a href="https://www.linkedin.com/in/adarsh-shrey-tiwari">linkedin.com/in/adarsh-shrey-tiwari</a></span>
      <span class="separator">•</span>
      <span class="contact-item">🐙 <a href="https://github.com/Adarsh-tiwari1223">github.com/Adarsh-tiwari1223</a></span>
    </div>
  </div>

  <!-- PROFESSIONAL SUMMARY -->
  <div class="section">
    <div class="section-title">Professional Summary</div>
    <div class="summary-text">
      Detail-oriented <strong>QA Engineer / SDET</strong> with proven expertise in <strong>Manual, REST API, and Playwright Test Automation</strong> across enterprise <strong>HRMS, Payroll, US IT Staffing, and Travel Management</strong> platforms. Proven track record in designing maintainable automation suites using <strong>Python, Playwright, and PyTest</strong> adhering to the <strong>Page Object Model (POM)</strong>. Expertise in validating complex business workflows, multi-tier Role-Based Access Control (RBAC), REST API contracts, and SQL database consistency. Skilled in utilizing <strong>AI-assisted testing tools</strong> to accelerate test design, edge-case discovery, and synthetic test data generation.
    </div>
  </div>

  <!-- TECHNICAL SKILLS -->
  <div class="section">
    <div class="section-title">Technical Skills</div>
    <table class="skills-table">
      <tr>
        <td class="skill-cat">Test Automation:</td>
        <td class="skill-val">Playwright (Python), PyTest, Selenium (Python), Page Object Model (POM), Data-Driven Testing, Reusable Fixtures</td>
      </tr>
      <tr>
        <td class="skill-cat">API &amp; Backend:</td>
        <td class="skill-val">REST APIs, Postman, Python Requests Library, Request/Response Payload Validation, JSON Schema, SQL Queries</td>
      </tr>
      <tr>
        <td class="skill-cat">QA Methodologies:</td>
        <td class="skill-val">Functional, Regression, Smoke, Sanity, Integration, System, End-to-End (E2E), Exploratory, UAT, Boundary Value, RBAC</td>
      </tr>
      <tr>
        <td class="skill-cat">AI-Assisted QA:</td>
        <td class="skill-val">AI-Powered Test Case Generation, Edge-Case Identification, Synthetic Test Data Generation, Scripting Assistance</td>
      </tr>
      <tr>
        <td class="skill-cat">Tools &amp; DevOps:</td>
        <td class="skill-val">Git, GitHub, GitHub Actions (CI/CD), Docker, Jira, Chrome DevTools, VS Code, Linux, Windows, Excel / Google Sheets</td>
      </tr>
    </table>
  </div>

  <!-- EXPERIENCE -->
  <div class="section">
    <div class="section-title">Professional Experience</div>
    
    <div class="job-header">
      <div>
        <span class="job-title">QA Engineer</span> — <span class="company">TEK Inspirations LLC (Originator Informatics Pvt. Ltd.)</span>
      </div>
      <div class="job-meta">Jul 2025 – Present | Varanasi, UP</div>
    </div>
    
    <ul>
      <li>Lead end-to-end testing across 3 core platforms: <strong>HR Lense (HRMS &amp; Payroll)</strong>, <strong>US IT Recruitment Management</strong>, and <strong>Travel Management System</strong>.</li>
      <li>Author detailed test scenarios and test cases from user stories, PRDs, and workflow analysis, ensuring 100% requirements traceability across SDLC/STLC.</li>
      <li>Execute rigorous Functional, Regression, Smoke, Sanity, Integration, Exploratory, and UAT test cycles, preventing defect leaks into production.</li>
      <li>Automate critical user journeys using <strong>Python, Playwright, and PyTest</strong> with the <strong>Page Object Model (POM)</strong>, reducing regression testing effort.</li>
      <li>Conduct in-depth REST API testing using <strong>Postman and Python Requests</strong>, validating HTTP status codes, response schemas, and RBAC token boundaries.</li>
      <li>Validate multi-tier <strong>Role-Based Access Control (RBAC)</strong>, approval hierarchies, and cross-module permissions across Admin, Manager, and Employee tiers.</li>
      <li>Perform backend data validation using <strong>SQL queries</strong> to ensure frontend transactions (payroll, attendance, onboarding) commit accurately to the database.</li>
      <li>Log, track, and verify defects in <strong>Jira</strong> with clear reproduction steps and logs; collaborate with developers and BAs in Agile/Scrum ceremonies.</li>
    </ul>
  </div>

  <!-- KEY PROJECTS -->
  <div class="section">
    <div class="section-title">Key Projects</div>

    <!-- HR Lense -->
    <div class="project-item">
      <div class="project-header">
        <span class="project-name">HR Lense — Enterprise HRMS &amp; Payroll System</span>
        <span class="project-tech">Python · Playwright · PyTest · Postman · SQL · POM</span>
      </div>
      <ul>
        <li>Validated core modules: Employee Onboarding, Attendance &amp; Shifts, Leave Approvals, Payroll Processing, and Document Verification.</li>
        <li>Engineered a custom <strong>Python-based payroll verification utility</strong> that compares exported payroll calculations with backend API responses, catching calculation mismatches with 100% accuracy.</li>
        <li>Validated intricate tax deduction algorithms, attendance-to-salary mapping, and multi-level approval hierarchies.</li>
      </ul>
    </div>

    <!-- US IT Recruitment -->
    <div class="project-item">
      <div class="project-header">
        <span class="project-name">US IT Recruitment Management System</span>
        <span class="project-tech">Playwright · Python · REST APIs · RBAC Testing</span>
      </div>
      <ul>
        <li>Validated full staffing lifecycle: Lead Generation, Job Posting, Candidate Sourcing, Interview Scheduling, Submissions, and Consultant Onboarding.</li>
        <li>Conducted boundary and RBAC testing ensuring strict data isolation between recruiting teams and external vendor portals.</li>
        <li>Automated core candidate onboarding and submission pipelines using <strong>Playwright</strong> component fixtures.</li>
      </ul>
    </div>

    <!-- Travel Management -->
    <div class="project-item">
      <div class="project-header">
        <span class="project-name">Travel Management System (Client Portal &amp; Admin Panel)</span>
        <span class="project-tech">Manual Testing · API Testing · SQL · Chrome DevTools</span>
      </div>
      <ul>
        <li>Tested end-to-end inquiry pipelines, booking workflows, customized itinerary creation, and travel package pricing tiers.</li>
        <li>Validated bi-directional data synchronization between client portal and admin panel, testing edge cases around timeouts and payments.</li>
      </ul>
    </div>
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

def generate():
    output_html = "resume/Adarsh_Tiwari_Resume.html"
    output_pdf = "resume/Adarsh_Tiwari_QA_june_2026.pdf"
    
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
    print(f"VERIFICATION: Output PDF generated with EXACTLY {len(reader.pages)} page(s)!")

if __name__ == "__main__":
    generate()
