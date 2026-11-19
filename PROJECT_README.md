# Career Command Center — Project Guide
*A complete, automated system for Adarsh Tiwari's professional profile, job search, and technical mentorship.*

---

## 🌟 What Is This Project?

This workspace (`My_Profile`) is a **personal career management system**. 

Instead of keeping resumes, job applications, LinkedIn drafts, and login notes scattered in different folders or emails, this project organizes everything into one centralized, automated command center.

It is designed to be **simple, organized, and reliable**—even for someone with zero programming background.

---

## 📁 What is Inside Each Folder? (Simple Guide)

### 1. `resume/` — Professional Resume Files
* **What it contains:** The official 2-page ATS-optimized resume for Adarsh Tiwari in PDF format (`Adarsh_Tiwari_QA_nov_2026.pdf`) and the original June backup (`Adarsh_Tiwari_QA_june_2026.pdf`).
* **Why it matters:** It is formatted cleanly without complex graphics or confusing tables so that company automated resume scanners (ATS) and human HR managers can read it without errors.

---

### 2. `naukari/` — 1-Click Naukri Automation
* **What it contains:** An automated helper script (`naukri_updater.py`) and two 1-click shortcut files (`run_update.bat` and `daily_refresh.bat`).
* **How it works:** 
  * Every morning between 9:00 AM and 10:30 AM, double-clicking **`daily_refresh.bat`** automatically re-saves your headline on Naukri.com.
  * This marks your profile as **"Active Today"**, putting you at the very top of recruiter searches across India without you needing to manually type or click anything.

---

### 3. `linkedin/` — Thought Leadership & Mentorship
* **What it contains:**
  * **`carousels/`**: A clean, 5-slide PDF guide explaining software testing architecture in a simple visual format.
  * **`posts/`**: Ready-to-publish educational articles designed to guide college students and junior testers entering the tech industry.
  * **`linkedin_publisher.py`**: An official tool that publishes posts safely using LinkedIn’s official developer system.

---

### 4. `instahyre/` — Product Startups & Unicorns
* **What it contains:** A complete profile setup guide for **Instahyre** (`profile_setup.md`).
* **What it does:** Instahyre is a "reverse hiring" platform used by top product companies (*Swiggy, Razorpay, CRED, Meesho*). Companies search for specific technical skills and reach out to you directly for interviews.

---

### 5. `cutshort/` — Direct Access to Engineering Managers
* **What it contains:** A 3-part elevator pitch and profile guide (`profile_setup.md`).
* **What it does:** Cutshort connects you directly to Engineering Managers and Tech Leads via WhatsApp and chat, skipping traditional HR screening delays.

---

### 6. `wellfound/` — Global & Remote Startups
* **What it contains:** Profile optimization guide for **Wellfound** (formerly AngelList Talent).
* **What it does:** Targets venture-funded tech companies and US/EU startups hiring remote software testing engineers in India.

---

### 7. `foundit_hirist/` — Enterprise Consultancies & MNCs
* **What it contains:** Keyword-dense setup guide for **Foundit** (formerly Monster) and **Hirist**.
* **What it does:** Generates high-volume interview inbound from large IT consultancies and multi-national corporations.

---

### 8. `github/` & `.github/` — Public Portfolio Page
* **What it contains:** The animated Demon Slayer × SDET profile page configuration that visitors see when opening [github.com/Adarsh-tiwari1223](https://github.com/Adarsh-tiwari1223).
* **Workflows:** Automatically updates a 3D commit city map and contribution snake animation daily.

---

## ⚡ The 2-Minute Daily Routine

To get the best results from this project every day:

1. **Morning (9:00 AM – 9:30 AM):** Double-click **`naukari/daily_refresh.bat`** to refresh your active ranking on Naukri.
2. **Review Inbound Messages:** Check your notifications on **Cutshort** and **Instahyre** for new interview invitations.
3. **LinkedIn Sharing:** Post technical tips or share slides from **`linkedin/`** to build your professional network and help students looking to learn QA automation.

---

## 🔒 Security & Privacy Note
All login cookies, passwords, and sensitive API tokens are protected by `.gitignore` and kept strictly on your local computer. They are never pushed or shared publicly.
