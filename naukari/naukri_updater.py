#!/usr/bin/env python3
"""
Naukri.com Automated Profile Updater & Rank Booster
Tailored for Adarsh Tiwari (QA Engineer / SDET)

Uses Playwright with a persistent browser session so you log in once (human OTP/auth),
and the script handles the automated typing, updating, and resume PDF uploads.
"""

import os
import sys
import time
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

# Project Paths
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
RESUME_PDF = PROJECT_ROOT / "resume" / "Adarsh_Tiwari_QA_nov_2026.pdf"
SESSION_DIR = BASE_DIR / ".naukri_browser_session"

# Profile Content Constants
RESUME_HEADLINE = (
    "QA Engineer / SDET with hands-on experience in Playwright (Python), PyTest, "
    "Manual & REST API Testing | Postman, SQL, POM Framework | TEK Inspirations | "
    "MCA 2025 | Immediate / 30 Days Notice | Open to Relocation"
)

PROFILE_SUMMARY = (
    "QA Engineer / SDET with hands-on experience in Manual Testing, REST API Testing, "
    "and Playwright Test Automation using Python across enterprise HRMS, Payroll, and US IT Staffing domains.\n\n"
    "Core Technical Skills:\n"
    "• Test Automation: Building automation suites using Python, Playwright, and PyTest adhering to Page Object Model (POM) and modular test architecture.\n"
    "• API & Contract Testing: Testing RESTful APIs using Postman and Python Requests, validating status codes, JSON schema structures, authorization headers, and response payloads.\n"
    "• Database Validation: Writing direct SQL queries to verify backend transactional state and guarantee data consistency between UI workflows and database tables.\n"
    "• Test Design & Management: Requirement analysis, end-to-end test scenario creation, comprehensive test case design, defect tracking in Jira, and release validation across full SDLC & STLC lifecycles.\n\n"
    "Domain & Project Experience:\n"
    "• HR Lense (HRMS & Payroll): Tested employee lifecycle, attendance, leave approval hierarchies, and built a Python utility to audit payroll CSV exports against backend API responses.\n"
    "• US IT Recruitment System: End-to-end candidate tracking, job submissions, consultant management, and role-based access control (RBAC) validation.\n"
    "• Travel Management System: Lead tracking, booking workflows, travel packages, and admin-client portal data synchronization.\n\n"
    "Education: MCA (2025, Kashi Institute of Technology) | B.Sc (2022, Allahabad State University)\n"
    "Location: Jaunpur / Varanasi, UP | Open to Relocation (Bangalore, Gurgaon/Delhi NCR, Hyderabad, Noida, Pune, Remote)"
)

KEY_SKILLS = [
    "Playwright", "Python", "PyTest", "Manual Testing", "API Testing", "Postman",
    "REST APIs", "SQL", "Page Object Model (POM)", "Functional Testing",
    "Regression Testing", "Test Scenario Creation", "Test Case Design",
    "Defect Lifecycle", "Jira", "SDLC", "STLC", "Integration Testing",
    "End-to-End Testing", "Cross-Browser Testing", "Git", "GitHub"
]

def check_login(page):
    """Check if the user is genuinely logged into Naukri."""
    try:
        title = page.title().lower()
        if "access denied" in title or "login" in title:
            return False
        current_url = page.url.lower()
        if "nlogin" in current_url or "login" in current_url:
            return False
        
        # Check for confirmed authenticated elements on Naukri profile
        for sel in [
            ".user-name",
            ".profile-percent",
            "a[href*='logout']",
            "div.resumeHeadline",
            "span:has-text('Resume headline')",
            "span:has-text('Resume Headline')",
            "div:has-text('Profile summary')",
            "div:has-text('Profile Summary')",
            "text='Key skills'"
        ]:
            if page.locator(sel).first.is_visible(timeout=1000):
                return True
    except Exception:
        pass
    return False

def ensure_authenticated(context, page):
    """Ensure user is logged in, automatically detecting when login is completed in the browser."""
    print("\n[1/5] Navigating to Naukri Profile...")
    page.goto("https://www.naukri.com/mnjuser/profile", wait_until="domcontentloaded")
    time.sleep(3)

    if not check_login(page):
        print("\n" + "="*70)
        print("⚠️  AUTHENTICATION REQUIRED")
        print("Please log into your Naukri account in the opened Chrome browser window.")
        print("The script is waiting and will AUTOMATICALLY detect when you finish logging in!")
        print("="*70 + "\n")
        
        # Poll every 3 seconds for up to 5 minutes (300s)
        max_attempts = 100
        for i in range(max_attempts):
            time.sleep(3)
            current_url = page.url.lower()
            if "profile" in current_url and not ("login" in current_url or "nlogin" in current_url):
                print(f"\n✔ Login detected! URL: {current_url}")
                time.sleep(3)
                break
            if check_login(page):
                print("\n✔ Authenticated session detected!")
                time.sleep(2)
                break
            if (i + 1) % 10 == 0:
                print(f"Waiting for your login in the browser window... ({(i+1)*3}s elapsed)")
        else:
            print("❌ Login timed out after 5 minutes.")
            sys.exit(1)

    print("✔ Successfully authenticated on Naukri!")

def upload_resume_pdf(page):
    """Upload updated ATS resume PDF."""
    print("\n[2/5] Uploading Updated Resume PDF...")
    if not RESUME_PDF.exists():
        print(f"❌ Resume file not found at: {RESUME_PDF}")
        return False

    try:
        # Locate the resume file input
        file_input = page.locator("input[type='file'][id*='attach'], input[type='file']")
        if file_input.count() > 0:
            print(f"Found upload input. Attaching: {RESUME_PDF.name}...")
            file_input.first.set_input_files(str(RESUME_PDF))
            time.sleep(4)
            print("✔ Resume PDF uploaded successfully!")
            return True
        else:
            # Check for update resume button
            update_btn = page.locator("text='Update resume', text='Upload resume'")
            if update_btn.is_visible(timeout=3000):
                with page.expect_file_chooser() as fc_info:
                    update_btn.first.click()
                file_chooser = fc_info.value
                file_chooser.set_files(str(RESUME_PDF))
                time.sleep(4)
                print("✔ Resume PDF uploaded via file chooser!")
                return True
    except Exception as e:
        print(f"⚠️ Note on resume upload: {e}")
    return False

def update_resume_headline(page):
    """Update Naukri Resume Headline (250 chars max)."""
    print("\n[3/5] Updating Resume Headline...")
    try:
        # Ensure we are scrolled to the top where Headline lives
        page.evaluate("window.scrollTo(0, 0)")
        time.sleep(1)

        edit_btn = None
        selectors = [
            "//div[contains(@class, 'resumeHeadline')]//span[contains(text(), 'Edit') or contains(@class, 'edit')]",
            "//span[contains(text(), 'Resume headline') or contains(text(), 'Resume Headline')]/following-sibling::span[contains(text(), 'Edit') or contains(@class, 'edit')]",
            "//span[contains(text(), 'Resume headline') or contains(text(), 'Resume Headline')]/..//span[contains(text(), 'Edit') or contains(@class, 'edit')]",
            "div.resumeHeadline .edit",
            "div.resumeHeadline span:has-text('Edit')",
            "div.resumeHeadline [class*='edit']",
            "text='Resume headline' >> .. >> text='Edit'"
        ]
        for sel in selectors:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=2000):
                    edit_btn = loc
                    break
            except Exception:
                continue

        if edit_btn:
            print("Found Resume Headline Edit button. Clicking...")
            edit_btn.click()
            time.sleep(1.5)
            
            textarea = page.locator("textarea#resumeHeadlineTxt, div.resumeHeadline textarea, form textarea, textarea").first
            textarea.wait_for(state="visible", timeout=5000)
            textarea.fill("")
            textarea.fill(RESUME_HEADLINE)
            time.sleep(1)
            
            # Explicitly target the Save button (NOT generic button[type='submit'])
            save_btn = None
            save_candidates = [
                page.get_by_role("button", name="Save"),
                page.locator("button:text-is('Save')"),
                page.locator("button:has-text('Save')"),
                page.locator(".btn-dark-ot:has-text('Save')"),
                page.locator(".action button:has-text('Save')"),
                page.locator("form button:has-text('Save')")
            ]
            for candidate in save_candidates:
                try:
                    if candidate.first.is_visible(timeout=2000):
                        save_btn = candidate.first
                        break
                except Exception:
                    continue

            if save_btn:
                save_btn.click()
                time.sleep(3)
                print(f"✔ Resume Headline updated successfully! ({len(RESUME_HEADLINE)} chars)")
                return True
            else:
                print("⚠️ Could not find visible Save button for Resume Headline.")
        else:
            print("⚠️ Could not find 'Edit' button for Resume Headline.")
    except Exception as e:
        print(f"⚠️ Error updating Resume Headline: {e}")
    return False

def update_profile_summary(page):
    """Update Naukri Profile Summary section."""
    print("\n[4/5] Updating Profile Summary...")
    try:
        page.keyboard.press("Escape")
        time.sleep(0.5)

        # Scroll down to load all cards
        for _ in range(4):
            page.evaluate("window.scrollBy(0, 800)")
            time.sleep(0.5)

        # Find the Profile Summary card (excluding Quick links)
        cards = page.locator("div.card")
        target_card = None
        for i in range(cards.count()):
            c = cards.nth(i)
            txt = c.inner_text()
            if "profile summary" in txt.lower() and "quick links" not in txt.lower():
                target_card = c
                break

        if target_card:
            target_card.scroll_into_view_if_needed()
            time.sleep(1)
            edit_btn = target_card.locator("span.edit.icon, span:has-text('editOneTheme'), .edit").first
            if edit_btn.is_visible(timeout=3000):
                print("Found Profile Summary Edit button. Clicking...")
                edit_btn.click()
                time.sleep(1.5)

                textarea = page.locator("div.profileSummary textarea, form textarea, textarea").first
                textarea.wait_for(state="visible", timeout=5000)
                textarea.fill("")
                textarea.fill(PROFILE_SUMMARY)
                time.sleep(1)

                # Find the Save button specifically inside the active form/lightbox (exclude 'Save photo')
                save_btn = None
                save_selectors = [
                    "form button:text-is('Save')",
                    ".lightbox button:text-is('Save')",
                    ".drawer button:text-is('Save')",
                    "button:text-is('Save')",
                    "button.btn-dark-ot:text-is('Save')",
                    "form .btn-save"
                ]
                for sel in save_selectors:
                    try:
                        candidates = page.locator(sel)
                        for k in range(candidates.count()):
                            c = candidates.nth(k)
                            txt = c.inner_text().strip().lower()
                            if txt == "save" and "photo" not in txt and c.is_visible(timeout=1000):
                                save_btn = c
                                break
                        if save_btn:
                            break
                    except Exception:
                        continue

                if save_btn:
                    save_btn.click()
                    time.sleep(3)
                    print("✔ Profile Summary updated successfully!")
                    return True
                else:
                    print("⚠️ Could not find visible Save button for Profile Summary.")
            else:
                print("⚠️ Could not find 'Edit' button in Profile summary card.")
        else:
            print("⚠️ Profile summary card not found.")
    except Exception as e:
        print(f"⚠️ Error updating Profile Summary: {e}")
    return False

def daily_refresh(page):
    """Trigger the 10-second Daily Rank Booster by re-saving headline or resume."""
    print("\n=== Running Naukri Daily Profile Refresh ===")
    ensure_authenticated(None, page)
    
    # Simple re-save of the resume headline to trigger the 'Active Today' badge
    success = update_resume_headline(page)
    if not success:
        success = upload_resume_pdf(page)
        
    if success:
        print("\n🎉 SUCCESS: Your profile timestamp is now refreshed!")
        print("Your profile will now rank as 'Active Today' in recruiter Resdex searches.")
    else:
        print("\n⚠️ Refresh encountered an issue. Check the browser window.")

def full_update(page):
    """Run full profile overhaul (Resume PDF, Headline, Summary)."""
    print("\n=== Running Full Naukri Profile Overhaul ===")
    ensure_authenticated(None, page)
    
    upload_resume_pdf(page)
    update_resume_headline(page)
    update_profile_summary(page)
    
    print("\n" + "="*70)
    print("✅ NAUKRI PROFILE OVERHAUL COMPLETE!")
    print("Review the browser window to verify all sections.")
    print("="*70 + "\n")
    time.sleep(5)

def main():
    parser = argparse.ArgumentParser(description="Naukri.com Automated Profile Manager for Adarsh Tiwari")
    parser.add_argument(
        "action", 
        choices=["update", "refresh", "login"], 
        help="Action to perform: 'update' (full update), 'refresh' (daily rank boost), 'login' (save session)"
    )
    args = parser.parse_args()

    SESSION_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Starting Naukri Automation (Action: {args.action})...")
    with sync_playwright() as p:
        # Launch persistent browser context so login session is preserved across runs
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(SESSION_DIR),
            headless=False,
            channel="chrome",  # Uses local Chrome if available, otherwise falls back
            viewport={"width": 1280, "height": 800},
            args=["--disable-blink-features=AutomationControlled"]  # Prevents bot detection
        )
        
        page = context.pages[0] if context.pages else context.new_page()

        try:
            if args.action == "login":
                ensure_authenticated(context, page)
                print("Session saved! You can now run 'python naukari/naukri_updater.py update' or 'refresh'.")
            elif args.action == "update":
                full_update(page)
            elif args.action == "refresh":
                daily_refresh(page)
        finally:
            print("Closing browser session...")
            context.close()

if __name__ == "__main__":
    main()
