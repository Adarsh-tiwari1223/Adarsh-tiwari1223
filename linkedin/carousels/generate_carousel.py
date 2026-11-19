import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

CAROUSEL_DIR = Path(__file__).resolve().parent
HTML_PATH = CAROUSEL_DIR / "carousel_light.html"
PDF_PATH = CAROUSEL_DIR / "Playwright_3_Tier_Architecture_Carousel.pdf"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Playwright 3-Tier Architecture</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: #F1F5F9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #0F172A;
      -webkit-font-smoothing: antialiased;
    }

    @page {
      size: 1080px 1350px;
      margin: 0;
    }

    .slide {
      width: 1080px;
      height: 1350px;
      background: #FFFFFF;
      padding: 80px 75px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      page-break-after: always;
      break-after: page;
      position: relative;
    }

    /* Top accent line */
    .slide::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 8px;
      background: linear-gradient(90deg, #2563EB 0%, #7C3AED 50%, #059669 100%);
    }

    /* Header */
    .header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 24px;
      border-bottom: 2px solid #F1F5F9;
    }

    .tag-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #EFF6FF;
      border: 1px solid #BFDBFE;
      color: #1D4ED8;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 6px;
    }

    .slide-num {
      color: #64748B;
      font-size: 16px;
      font-weight: 700;
    }

    /* Content Area */
    .content-area {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      margin: 20px 0;
    }

    h1 {
      font-size: 42px;
      font-weight: 800;
      line-height: 1.25;
      color: #0F172A;
      margin-bottom: 16px;
      letter-spacing: -0.5px;
    }

    .subtitle {
      font-size: 20px;
      color: #475569;
      line-height: 1.5;
      margin-bottom: 30px;
      font-weight: 400;
    }

    /* Cards */
    .card {
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 14px;
      padding: 24px 28px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }

    .card-title {
      font-size: 19px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
    }

    .card-red {
      background: #FEF2F2;
      border-color: #FECACA;
    }
    .card-red .card-title { color: #DC2626; }

    .card-green {
      background: #F0FDF4;
      border-color: #BBF7D0;
    }
    .card-green .card-title { color: #16A34A; }

    .card-blue {
      background: #F8FAFC;
      border-color: #CBD5E1;
      border-left: 6px solid #2563EB;
    }

    .card-purple {
      background: #F8FAFC;
      border-color: #CBD5E1;
      border-left: 6px solid #7C3AED;
    }

    .card-emerald {
      background: #F8FAFC;
      border-color: #CBD5E1;
      border-left: 6px solid #059669;
    }

    /* Code Window (Mac-style terminal) */
    .code-window {
      background: #0F172A;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
      margin-top: 10px;
    }

    .code-header {
      background: #1E293B;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .code-dot {
      width: 11px;
      height: 11px;
      border-radius: 50%;
    }
    .dot-red { background: #EF4444; }
    .dot-yellow { background: #F59E0B; }
    .dot-green { background: #10B981; }

    .code-filename {
      color: #94A3B8;
      font-size: 13px;
      font-family: Consolas, monospace;
      margin-left: 8px;
    }

    .code-body {
      padding: 16px 20px;
      font-family: Consolas, Monaco, "Courier New", monospace;
      font-size: 14.5px;
      line-height: 1.6;
      color: #F8FAFC;
    }

    .kw { color: #F43F5E; font-weight: bold; }
    .fn { color: #38BDF8; }
    .str { color: #34D399; }
    .cls { color: #FBBF24; font-weight: bold; }
    .comment { color: #64748B; font-style: italic; }

    /* Footer */
    .footer-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 20px;
      border-top: 2px solid #F1F5F9;
      color: #64748B;
      font-size: 15px;
      font-weight: 600;
    }

    .author-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #334155;
    }

    .swipe-pill {
      color: #2563EB;
      font-size: 15px;
      font-weight: 700;
    }
  </style>
</head>
<body>

  <!-- SLIDE 1 -->
  <div class="slide">
    <div class="header-bar">
      <span class="tag-badge">Playwright + Pytest Architecture</span>
      <span class="slide-num">01 / 05</span>
    </div>

    <div class="content-area">
      <h1>
        Stop mixing locators, workflows and assertions in one file.
      </h1>
      <p class="subtitle">
        Why textbook Page Object Model breaks in real projects—and how separating concerns creates an automation suite you can actually trust.
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
        <div class="card card-red">
          <div class="card-title">❌ The Usual Approach (Coupled Code)</div>
          <ul style="color: #475569; font-size: 16.5px; line-height: 1.9; padding-left: 20px;">
            <li>Locators + actions + logic in one class</li>
            <li>Assertions scattered inside page helpers</li>
            <li>1 frontend button change breaks 15 tests</li>
            <li>Can't reuse methods for negative tests</li>
          </ul>
        </div>

        <div class="card card-green">
          <div class="card-title">✅ The 3-Layer Architecture</div>
          <ul style="color: #475569; font-size: 16.5px; line-height: 1.9; padding-left: 20px;">
            <li><strong>Pages Layer:</strong> Pure UI & selectors only</li>
            <li><strong>Workflows Layer:</strong> Business journeys</li>
            <li><strong>Tests Layer:</strong> Scenarios & assertions</li>
            <li>Isolated changes, zero flakiness</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <div class="author-badge">
        <strong>Adarsh Tiwari</strong> · SDET & QA Automation
      </div>
      <div class="swipe-pill">Swipe Next →</div>
    </div>
  </div>

  <!-- SLIDE 2 -->
  <div class="slide">
    <div class="header-bar">
      <span class="tag-badge">The Root Problem</span>
      <span class="slide-num">02 / 05</span>
    </div>

    <div class="content-area">
      <h1>
        What happens when Page Objects do too much
      </h1>
      <p class="subtitle">
        Tutorials usually show simple 5-line examples. In production apps with hundreds of tests, here is where it breaks:
      </p>

      <div style="display: flex; flex-direction: column; gap: 20px;">
        <div class="card" style="border-left: 6px solid #EF4444;">
          <div class="card-title" style="color: #DC2626;">1. High Coupling Between UI and Business Logic</div>
          <p style="color: #475569; font-size: 16px; line-height: 1.6;">
            When a button selector changes, you edit the page class. When product updates a business rule, you edit the <strong>exact same file</strong>. Every change introduces unintended side-effects across unrelated tests.
          </p>
        </div>

        <div class="card" style="border-left: 6px solid #F59E0B;">
          <div class="card-title" style="color: #D97706;">2. The Embedded Assertion Trap</div>
          <p style="color: #475569; font-size: 16px; line-height: 1.6;">
            If you embed assertions inside helper methods like <code>login_page.login()</code>, you can never reuse that method to test <em>invalid credentials</em> without duplicating code.
          </p>
        </div>

        <div class="card" style="border-left: 6px solid #6366F1;">
          <div class="card-title" style="color: #4F46E5;">3. Multi-Page Journeys Become Chaotic</div>
          <p style="color: #475569; font-size: 16px; line-height: 1.6;">
            Real flows (like onboarding an employee, generating payroll, and verifying an email) cross 3 or 4 pages. Forcing cross-page logic into a single page object breaks all modularity.
          </p>
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <div class="author-badge">
        <strong>Golden Rule:</strong> Pages interact. Workflows orchestrate. Tests validate.
      </div>
      <div class="swipe-pill">Swipe Next →</div>
    </div>
  </div>

  <!-- SLIDE 3 -->
  <div class="slide">
    <div class="header-bar">
      <span class="tag-badge">The Architecture</span>
      <span class="slide-num">03 / 05</span>
    </div>

    <div class="content-area">
      <h1>
        The 3-Layer Structure
      </h1>
      <p class="subtitle">
        Giving each layer exactly one responsibility so changes stay isolated:
      </p>

      <div style="display: flex; flex-direction: column; gap: 18px;">
        <div class="card card-blue">
          <div class="card-title" style="color: #1D4ED8;">
            Layer 1: Pages Layer (UI & Locators)
          </div>
          <p style="color: #334155; font-size: 16px; margin-bottom: 6px;">
            <strong>Responsibility:</strong> Locators and raw actions (<code>click</code>, <code>fill</code>, <code>select_option</code>).
          </p>
          <p style="color: #64748B; font-size: 15px;">
            If a frontend ID or CSS class changes, you update only this file. Workflows and tests don't change.
          </p>
        </div>

        <div class="card card-purple">
          <div class="card-title" style="color: #7C3AED;">
            Layer 2: Workflows Layer (Business Logic)
          </div>
          <p style="color: #334155; font-size: 16px; margin-bottom: 6px;">
            <strong>Responsibility:</strong> Reusable user journeys (<code>login_as_admin()</code>, <code>onboard_employee()</code>).
          </p>
          <p style="color: #64748B; font-size: 15px;">
            If business steps change, update the workflow. Your page locators stay untouched.
          </p>
        </div>

        <div class="card card-emerald">
          <div class="card-title" style="color: #059669;">
            Layer 3: Tests Layer (Validation)
          </div>
          <p style="color: #334155; font-size: 16px; margin-bottom: 6px;">
            <strong>Responsibility:</strong> Test scenarios, test data fixtures, and assertions (<code>assert ...is_visible()</code>).
          </p>
          <p style="color: #64748B; font-size: 15px;">
            Tests stay clean, readable, and focused purely on verifying the expected business outcome.
          </p>
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <div class="author-badge">
        <strong>Flow:</strong> Tests call Workflows → Workflows use Pages → Pages drive Browser
      </div>
      <div class="swipe-pill">Swipe Next →</div>
    </div>
  </div>

  <!-- SLIDE 4 -->
  <div class="slide">
    <div class="header-bar">
      <span class="tag-badge">Code Implementation</span>
      <span class="slide-num">04 / 05</span>
    </div>

    <div class="content-area">
      <h1>
        What the code looks like in Python
      </h1>
      <p class="subtitle" style="margin-bottom: 16px;">
        Notice how clean each class stays when it has only one job:
      </p>

      <!-- Code 1 -->
      <div class="code-window" style="margin-bottom: 14px;">
        <div class="code-header">
          <span class="code-dot dot-red"></span>
          <span class="code-dot dot-yellow"></span>
          <span class="code-dot dot-green"></span>
          <span class="code-filename">pages/login_page.py (Pure UI)</span>
        </div>
        <div class="code-body">
<span class="kw">class</span> <span class="cls">LoginPage</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, page):
        self.page = page
        self.username = page.locator(<span class="str">"input[name='username']"</span>)
        self.password = page.locator(<span class="str">"input[name='password']"</span>)
        self.submit_btn = page.locator(<span class="str">"button[type='submit']"</span>)

    <span class="kw">def</span> <span class="fn">enter_credentials</span>(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.submit_btn.click()</div>
      </div>

      <!-- Code 2 -->
      <div class="code-window" style="margin-bottom: 14px;">
        <div class="code-header">
          <span class="code-dot dot-red"></span>
          <span class="code-dot dot-yellow"></span>
          <span class="code-dot dot-green"></span>
          <span class="code-filename">workflows/auth_workflow.py (Business Logic)</span>
        </div>
        <div class="code-body">
<span class="kw">class</span> <span class="cls">AuthWorkflow</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, page):
        self.login_page = LoginPage(page)

    <span class="kw">def</span> <span class="fn">login_as_user</span>(self, user):
        self.login_page.page.goto(<span class="str">"/auth/login"</span>)
        self.login_page.enter_credentials(user.name, user.pwd)</div>
      </div>

      <!-- Code 3 -->
      <div class="code-window">
        <div class="code-header">
          <span class="code-dot dot-red"></span>
          <span class="code-dot dot-yellow"></span>
          <span class="code-dot dot-green"></span>
          <span class="code-filename">tests/test_auth.py (Scenario & Validation)</span>
        </div>
        <div class="code-body">
<span class="kw">def</span> <span class="fn">test_valid_admin_login</span>(page, admin_user):
    AuthWorkflow(page).login_as_user(admin_user)
    <span class="kw">assert</span> page.locator(<span class="str">"[data-testid='dashboard-welcome']"</span>).is_visible()</div>
      </div>
    </div>

    <div class="footer-bar">
      <div class="author-badge">
        <strong>Result:</strong> Zero assertions in pages. Zero selectors in tests.
      </div>
      <div class="swipe-pill">Swipe Next →</div>
    </div>
  </div>

  <!-- SLIDE 5 -->
  <div class="slide">
    <div class="header-bar">
      <span class="tag-badge">Directory Structure & Takeaway</span>
      <span class="slide-num">05 / 05</span>
    </div>

    <div class="content-area">
      <h1>
        Project Tree & Guidance for Students
      </h1>
      <p class="subtitle" style="margin-bottom: 20px;">
        A framework structure that scales cleanly as tests grow into hundreds:
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
        <div class="code-window" style="margin-top: 0;">
          <div class="code-header">
            <span class="code-dot dot-red"></span>
            <span class="code-dot dot-yellow"></span>
            <span class="code-dot dot-green"></span>
            <span class="code-filename">framework_structure/</span>
          </div>
          <div class="code-body" style="font-size: 14px; line-height: 1.6;">
my_playwright_suite/
├── <span class="kw">pages/</span>          <span class="comment"># UI Locators</span>
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── employee_page.py
├── <span class="kw">workflows/</span>      <span class="comment"># User Journeys</span>
│   ├── auth_workflow.py
│   └── payroll_workflow.py
├── <span class="kw">tests/</span>          <span class="comment"># Pytest Scenarios</span>
│   ├── test_auth.py
│   └── test_payroll.py
├── <span class="kw">fixtures/</span>       <span class="comment"># Browser & Auth setup</span>
└── <span class="kw">test_data/</span>      <span class="comment"># Dynamic Payloads</span></div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 16px;">
          <div class="card" style="border-left: 6px solid #2563EB;">
            <div class="card-title" style="color: #1D4ED8; font-size: 17px; margin-bottom: 6px;">
              For MCA & Engineering Students
            </div>
            <p style="color: #475569; font-size: 15px; line-height: 1.55;">
              In SDET technical interviews, hiring managers don't just ask if you know Playwright syntax. They want to see if you can design an automation architecture that a whole engineering team can maintain.
            </p>
          </div>

          <div class="card" style="border-left: 6px solid #059669;">
            <div class="card-title" style="color: #059669; font-size: 17px; margin-bottom: 6px;">
              Setting up your framework?
            </div>
            <p style="color: #475569; font-size: 15px; line-height: 1.55;">
              I have this Playwright + Pytest structure with GitHub Actions CI/CD in a clean sample repo. Feel free to connect or drop a message if you want to explore the setup.
            </p>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <div class="author-badge">
        <strong>Adarsh Tiwari</strong> · QA Engineer & SDET
      </div>
      <div class="swipe-pill" style="color: #059669;">Connect on LinkedIn 💬</div>
    </div>
  </div>

</body>
</html>
"""

async def generate_carousel():
    HTML_PATH.write_text(HTML_CONTENT, encoding="utf-8")
    print(f"[1/3] Wrote HTML to {HTML_PATH}")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})
        await page.goto(f"file:///{HTML_PATH.as_posix()}", wait_until="load")

        # Export high-res PDF
        await page.pdf(
            path=str(PDF_PATH),
            width="1080px",
            height="1350px",
            print_background=True,
            margin={"top": "0px", "bottom": "0px", "left": "0px", "right": "0px"}
        )
        print(f"[2/3] Generated PDF Carousel: {PDF_PATH}")

        # Also take PNG screenshots of each slide
        slides = await page.query_selector_all(".slide")
        for idx, slide in enumerate(slides, start=1):
            slide_img_path = CAROUSEL_DIR / f"slide_{idx}.png"
            await slide.screenshot(path=str(slide_img_path))
            print(f"      Exported slide {idx} image: {slide_img_path.name}")

        await browser.close()
    print("[3/3] Carousel build complete!")

if __name__ == "__main__":
    asyncio.run(generate_carousel())
