<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Adarsh Tiwari – QA Engineer</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #080c10;
    --surface: #0d1117;
    --surface2: #111820;
    --border: #1e2d3d;
    --accent: #00d4ff;
    --accent2: #00ff88;
    --accent3: #ff6b35;
    --text: #c9d1d9;
    --text-dim: #6e7681;
    --text-bright: #f0f6fc;
    --mono: 'Space Mono', monospace;
    --display: 'Syne', sans-serif;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--mono);
    font-size: 13px;
    line-height: 1.7;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0, 212, 255, 0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0, 212, 255, 0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .wrap {
    position: relative;
    z-index: 1;
    max-width: 860px;
    margin: 0 auto;
    padding: 60px 24px 80px;
  }

  /* ── HERO ── */
  .hero {
    text-align: center;
    padding: 60px 0 50px;
    position: relative;
  }

  .hero::after {
    content: '';
    display: block;
    width: 1px;
    height: 60px;
    background: linear-gradient(to bottom, var(--accent), transparent);
    margin: 40px auto 0;
  }

  .hero-label {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 0.25em;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 20px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.1s forwards;
  }

  .hero-name {
    font-family: var(--display);
    font-size: clamp(42px, 8vw, 72px);
    font-weight: 800;
    color: var(--text-bright);
    letter-spacing: -0.02em;
    line-height: 1;
    margin-bottom: 18px;
    opacity: 0;
    animation: fadeUp 0.7s ease 0.25s forwards;
  }

  .hero-name span {
    color: var(--accent);
  }

  .hero-tagline {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--text-dim);
    letter-spacing: 0.1em;
    opacity: 0;
    animation: fadeUp 0.7s ease 0.4s forwards;
  }

  .hero-tagline strong {
    color: var(--accent2);
    font-weight: 400;
  }

  /* ── TYPING STRIP ── */
  .typing-strip {
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    background: var(--surface);
    padding: 14px 20px;
    margin: 0 0 50px;
    font-size: 12px;
    color: var(--accent2);
    display: flex;
    align-items: center;
    gap: 12px;
    opacity: 0;
    animation: fadeUp 0.7s ease 0.55s forwards;
  }

  .typing-strip::before {
    content: '▶';
    color: var(--accent);
    font-size: 10px;
    flex-shrink: 0;
  }

  .typing-text {
    overflow: hidden;
    white-space: nowrap;
    border-right: 2px solid var(--accent2);
    animation: typing 3.5s steps(60) 1.2s both, blink 0.75s step-end 1.2s infinite;
    max-width: 100%;
  }

  @keyframes typing {
    from { width: 0 }
    to { width: 100% }
  }
  @keyframes blink {
    50% { border-color: transparent }
  }

  /* ── SECTION ── */
  .section {
    margin-bottom: 50px;
    opacity: 0;
    animation: fadeUp 0.6s ease forwards;
  }

  .section:nth-child(3)  { animation-delay: 0.6s; }
  .section:nth-child(4)  { animation-delay: 0.7s; }
  .section:nth-child(5)  { animation-delay: 0.8s; }
  .section:nth-child(6)  { animation-delay: 0.9s; }
  .section:nth-child(7)  { animation-delay: 1.0s; }
  .section:nth-child(8)  { animation-delay: 1.1s; }
  .section:nth-child(9)  { animation-delay: 1.2s; }
  .section:nth-child(10) { animation-delay: 1.3s; }
  .section:nth-child(11) { animation-delay: 1.4s; }

  .section-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 20px;
  }

  .section-num {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--accent);
    letter-spacing: 0.1em;
    flex-shrink: 0;
  }

  .section-title {
    font-family: var(--display);
    font-size: 18px;
    font-weight: 700;
    color: var(--text-bright);
    letter-spacing: 0.02em;
    text-transform: uppercase;
  }

  .section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, var(--border), transparent);
  }

  /* ── PROSE ── */
  .prose {
    font-size: 13px;
    color: var(--text);
    line-height: 1.8;
  }

  .prose strong {
    color: var(--text-bright);
    font-weight: 700;
  }

  .prose em {
    color: var(--accent2);
    font-style: normal;
  }

  /* ── CARD GRID ── */
  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
  }

  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 16px 18px;
    position: relative;
    transition: border-color 0.2s, transform 0.2s;
    cursor: default;
  }

  .card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: var(--accent);
    opacity: 0;
    transition: opacity 0.2s;
  }

  .card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
  }
  .card:hover::before { opacity: 1; }

  .card-label {
    font-size: 10px;
    letter-spacing: 0.15em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin-bottom: 6px;
  }

  .card-value {
    font-family: var(--display);
    font-size: 14px;
    font-weight: 600;
    color: var(--text-bright);
  }

  /* ── TAG CLOUD ── */
  .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .tag {
    background: var(--surface2);
    border: 1px solid var(--border);
    padding: 5px 12px;
    font-size: 11px;
    color: var(--text);
    letter-spacing: 0.05em;
    transition: all 0.2s;
    cursor: default;
  }

  .tag:hover {
    background: rgba(0, 212, 255, 0.08);
    border-color: var(--accent);
    color: var(--accent);
  }

  .tag.accent { border-color: rgba(0, 212, 255, 0.4); color: var(--accent); }
  .tag.green  { border-color: rgba(0, 255, 136, 0.4); color: var(--accent2); }
  .tag.orange { border-color: rgba(255, 107, 53, 0.4); color: var(--accent3); }

  /* ── TABLE ── */
  .tech-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
  }

  .tech-table th {
    text-align: left;
    padding: 8px 14px;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-dim);
    border-bottom: 1px solid var(--border);
  }

  .tech-table td {
    padding: 10px 14px;
    border-bottom: 1px solid rgba(30, 45, 61, 0.5);
    color: var(--text);
    vertical-align: top;
  }

  .tech-table tr:hover td {
    background: rgba(0, 212, 255, 0.03);
  }

  .tech-table td:first-child {
    color: var(--text-dim);
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    white-space: nowrap;
    width: 140px;
  }

  .tech-table td:last-child {
    color: var(--accent2);
  }

  /* ── PROJECT BLOCK ── */
  .project {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 2px solid var(--accent);
    padding: 24px;
    margin-bottom: 16px;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s;
  }

  .project:hover { transform: translateY(-2px); }

  .project::after {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 100px; height: 100px;
    background: radial-gradient(circle, rgba(0, 212, 255, 0.06) 0%, transparent 70%);
    pointer-events: none;
  }

  .project-name {
    font-family: var(--display);
    font-size: 15px;
    font-weight: 700;
    color: var(--text-bright);
    margin-bottom: 10px;
    letter-spacing: 0.03em;
  }

  .project-desc {
    font-size: 12px;
    color: var(--text-dim);
    line-height: 1.7;
    margin-bottom: 14px;
  }

  .project-items {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  /* ── PRINCIPLES ── */
  .principles {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  @media (max-width: 500px) {
    .principles { grid-template-columns: 1fr; }
    .card-grid { grid-template-columns: 1fr 1fr; }
  }

  .principle {
    border: 1px solid var(--border);
    padding: 18px;
    position: relative;
    background: var(--surface);
  }

  .principle-icon {
    font-size: 20px;
    margin-bottom: 10px;
    display: block;
  }

  .principle-text {
    font-size: 12px;
    color: var(--text);
    line-height: 1.7;
  }

  .principle-text strong {
    color: var(--accent);
    display: block;
    margin-bottom: 4px;
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  /* ── FOCUS LIST ── */
  .focus-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .focus-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 14px;
    background: var(--surface);
    border: 1px solid var(--border);
    font-size: 12px;
    color: var(--text);
    transition: border-color 0.2s;
  }

  .focus-item:hover { border-color: var(--accent2); }

  .focus-item::before {
    content: '→';
    color: var(--accent2);
    font-size: 12px;
    flex-shrink: 0;
  }

  /* ── CONNECT ── */
  .connect-row {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }

  .connect-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 18px;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-family: var(--mono);
    font-size: 11px;
    text-decoration: none;
    letter-spacing: 0.08em;
    transition: all 0.2s;
    cursor: pointer;
  }

  .connect-btn:hover {
    border-color: var(--accent);
    color: var(--accent);
    background: rgba(0, 212, 255, 0.05);
  }

  .connect-btn .dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent);
    flex-shrink: 0;
  }

  /* ── FOOTER ── */
  .footer {
    text-align: center;
    margin-top: 60px;
    padding-top: 30px;
    border-top: 1px solid var(--border);
    font-size: 11px;
    color: var(--text-dim);
    letter-spacing: 0.1em;
  }

  .footer span { color: var(--accent2); }

  /* ── DIVIDER ── */
  .divider {
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border), transparent);
    margin: 12px 0 28px;
  }

  /* ── QUOTE ── */
  .quote {
    border-left: 3px solid var(--accent);
    padding: 14px 20px;
    background: var(--surface);
    font-size: 13px;
    color: var(--text);
    line-height: 1.8;
    font-style: italic;
    margin-top: 8px;
  }

  .quote strong { color: var(--accent2); font-style: normal; }

  /* ── ANIMATIONS ── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
  }
</style>
</head>
<body>
<div class="wrap">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-label">// quality assurance engineer</div>
    <div class="hero-name">Adarsh <span>Tiwari</span></div>
    <div class="hero-tagline">
      <strong>Manual Testing</strong> &nbsp;·&nbsp;
      <strong>Test Automation</strong> &nbsp;·&nbsp;
      <strong>Enterprise QA</strong>
    </div>
  </div>

  <!-- TYPING STRIP -->
  <div class="typing-strip">
    <div class="typing-text">Selenium · Python · PyTest · CRM &amp; HRMS · Workflow Validation · Defect Analysis</div>
  </div>

  <!-- SECTION 1: QA PROFILE -->
  <div class="section">
    <div class="section-header">
      <span class="section-num">01</span>
      <span class="section-title">QA Profile</span>
      <span class="section-line"></span>
    </div>
    <div class="prose">
      Quality Assurance Engineer focused on validating <strong>enterprise software systems</strong> through structured testing methodologies and disciplined execution.<br><br>
      My experience centers on <strong>functional validation, regression stability, and workflow testing</strong> across CRM and HRMS applications. I work closely with system behavior, test documentation, and defect reproducibility to ensure releases maintain <em>functional reliability and business integrity.</em>
    </div>
    <div class="divider"></div>
    <div class="tags">
      <span class="tag">Structured Test Design</span>
      <span class="tag">Accurate Defect Reporting</span>
      <span class="tag">Workflow-Driven Validation</span>
      <span class="tag">Traceable Documentation</span>
      <span class="tag">Maintainable Automation</span>
    </div>
  </div>

  <!-- SECTION 2: TESTING MINDSET -->
  <div class="section">
    <div class="section-header">
      <span class="section-num">02</span>
      <span class="section-title">Testing Mindset</span>
      <span class="section-line"></span>
    </div>
    <div class="quote">
      Quality Assurance is not simply about identifying bugs.<br>
      It is about <strong>understanding system behavior, validating business workflows, and ensuring software performs reliably under real operational scenarios.</strong>
    </div>
    <div class="divider"></div>
    <div class="principles">
      <div class="principle">
        <span class="principle-icon">⚙</span>
        <div class="principle-text">
          <strong>Business Workflows</strong>
          Validating end-to-end module behavior across real operational paths
        </div>
      </div>
      <div class="principle">
        <span class="principle-icon">🔒</span>
        <div class="principle-text">
          <strong>Access Control</strong>
          Role and permission-based access behavior under varied conditions
        </div>
      </div>
      <div class="principle">
        <span class="principle-icon">🖥</span>
        <div class="principle-text">
          <strong>UI Consistency</strong>
          Interaction logic and visual integrity across build cycles
        </div>
      </div>
      <div class="principle">
        <span class="principle-icon">🗄</span>
        <div class="principle-text">
          <strong>Data Integrity</strong>
          Ensuring clean, consistent data flow across all system processes
        </div>
      </div>
    </div>
  </div>

  <!-- SECTION 3: CORE COMPETENCIES -->
  <div class="section">
    <div class="section-header">
      <span class="section-num">03</span>
      <span class="section-title">Core QA Competencies</span>
      <span class="section-line"></span>
    </div>
    <div class="card-grid">
      <div class="card"><div class="card-label">Manual</div><div class="card-value">Functional Testing</div></div>
      <div class="card"><div class="card-label">Manual</div><div class="card-value">Regression Testing</div></div>
      <div class="card"><div class="card-label">Manual</div><div class="card-value">Smoke Testing</div></div>
      <div class="card"><div class="card-label">Manual</div><div class="card-value">UI Validation</div></div>
      <div class="card"><div class="card-label">Design</div><div class="card-value">Test Case Design</div></div>
      <div class="card"><div class="card-label">Analysis</div><div class="card-value">Requirement Analysis</div></div>
      <div class="card"><div class="card-label">Process</div><div class="card-value">Workflow Validation</div></div>
      <div class="card"><div class="card-label">Automation</div><div class="card-value">POM Framework</div></div>
    </div>
    <div class="divider"></div>
    <div class="prose">Automation focus: <strong>Page Object Model</strong> · <strong>PyTest fixtures &amp; hooks</strong> · <strong>data-driven testing</strong> · <strong>automated regression flows</strong></div>
  </div>

  <!-- SECTION 4: TOOLS -->
  <div class="section">
    <div class="section-header">
      <span class="section-num">04</span>
      <span class="section-title">Tools &amp; Technology</span>
      <span class="section-line"></span>
    </div>
    <table class="tech-table">
      <thead>
        <tr>
          <th>Category</th>
          <th>Technology</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Programming</td><td>Python</td></tr>
        <tr><td>Automation</td><td>Selenium WebDriver · PyTest</td></tr>
        <tr><td>API Testing</td><td>Postman</td></tr>
        <tr><td>Test Data</td><td>JSON · Faker</td></tr>
        <tr><td>Version Control</td><td>Git · GitHub</td></tr>
        <tr><td>Debugging</td><td>Chrome DevTools</td></tr>
        <tr><td>Defect Tracking</td><td>Jira · Spreadsheet Logs</td></tr>
      </tbody>
    </table>
  </div>

  <!-- SECTION 5: PROJECTS -->
  <div class="section">
    <div class="section-header">
      <span class="section-num">05</span>
      <span class="section-title">QA Project Work</span>
      <span class="section-line"></span>
    </div>

    <div class="project">
      <div class="project-name">Selenium · PyTest Automation Framework</div>
      <div class="project-desc">Developing a modular automation framework focused on maintainability and scalability. Reduces repetitive manual validation through structured regression automation.</div>
      <div class="project-items">
        <span class="tag accent">Page Object Model</span>
        <span class="tag accent">JSON Test Data</span>
        <span class="tag accent">Faker Data Gen</span>
        <span class="tag accent">Reusable Fixtures</span>
        <span class="tag accent">Assertion Validation</span>
      </div>
    </div>

    <div class="project">
      <div class="project-name">HRMS System Testing</div>
      <div class="project-desc">Full cycle QA across core HR modules — scenario creation, regression execution, workflow validation, and structured defect documentation.</div>
      <div class="project-items">
        <span class="tag green">Employee Management</span>
        <span class="tag green">Leave Management</span>
        <span class="tag green">Attendance Tracking</span>
        <span class="tag green">Document Workflow</span>
      </div>
    </div>

    <div class="project">
      <div class="project-name">CRM Workflow Testing</div>
      <div class="project-desc">Validated lead lifecycle, deal approval flows, and role-based access permissions. Maintained structured test cases, defect logs, and UI validation documentation.</div>
      <div class="project-items">
        <span class="tag orange">Lead Lifecycle</span>
        <span class="tag orange">Deal Approvals</span>
        <span class="tag orange">Role Hierarchy</span>
        <span class="tag orange">Access Restrictions</span>
      </div>
    </div>
  </div>

  <!-- SECTION 6: CURRENT FOCUS -->
  <div class="section">
    <div class="section-header">
      <span class="section-num">06</span>
      <span class="section-title">Current Focus</span>
      <span class="section-line"></span>
    </div>
    <div class="focus-list">
      <div class="focus-item">Selenium + PyTest framework design</div>
      <div class="focus-item">Python-based automation utilities</div>
      <div class="focus-item">Reusable QA documentation templates</div>
      <div class="focus-item">Scalable regression testing strategies</div>
    </div>
  </div>

  <!-- SECTION 7: PRINCIPLE -->
  <div class="section">
    <div class="section-header">
      <span class="section-num">07</span>
      <span class="section-title">Professional Principle</span>
      <span class="section-line"></span>
    </div>
    <div class="quote">
      Testing is the <strong>quality control layer between engineering and real users.</strong><br><br>
      Effective testing requires <strong>clarity, discipline, and structured thinking.</strong> A good QA engineer ensures system workflows behave as expected, data integrity remains intact, defects are discovered early, and releases remain stable.
    </div>
  </div>

  <!-- SECTION 8: CONNECT -->
  <div class="section">
    <div class="section-header">
      <span class="section-num">08</span>
      <span class="section-title">Connect</span>
      <span class="section-line"></span>
    </div>
    <div class="connect-row">
      <a class="connect-btn" href="https://www.linkedin.com/in/adarsh-tiwari-qa" target="_blank">
        <span class="dot"></span>LinkedIn — adarsh-tiwari-qa
      </a>
      <a class="connect-btn" href="mailto:tiwarishrey0@gmail.com">
        <span class="dot"></span>tiwarishrey0@gmail.com
      </a>
    </div>
  </div>

  <div class="footer">
    <span>Adarsh Tiwari</span> &nbsp;·&nbsp; Quality Assurance Engineer &nbsp;·&nbsp; Focused on building reliable systems through structured testing
  </div>

</div>
</body>
</html>
