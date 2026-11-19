# 🐙 GitHub Profile Architecture & Maintenance Guide

This folder documents the architecture, automation workflows, and maintenance of your GitHub profile (`https://github.com/Adarsh-tiwari1223`).

---

## 🏛️ Profile Architecture

Your profile uses a **pure SVG + CSS/SMIL animation** structure with GitHub Actions automation:

| File | Purpose | Key Elements |
| :--- | :--- | :--- |
| `hero.svg` | Hero Banner & Identity | Terminal bootloader, glowing name gradient, role cycler, Demon Slayer `滅` crest, animated Nichirin katana slash. |
| `breathing-forms.svg` | Testing Methodology | 4 Slaying Forms: UI (Playwright), API (Requests), DB (SQL), and CI/CD (GitHub Actions). |
| `stack.svg` | Technical Arsenal | Orbiting planetary tech core + 4 categorized chip cards. |
| `hashira-id.svg` | ID Pass & Architecture | Wooden/Gold Hashira credential pass with holographic sheen + live interactive testing pipeline. |
| `connect.svg` | Contact & Socials | Kasugai Crow dispatch cards (LinkedIn, Email, GitHub). |
| `profile-3d-contrib/` | 3D Contribution City | Night skyline commit towers generated via GitHub Actions. |
| `README.md` (root) | Master Layout | Wires all components, HRlens project showcase, visitor counter. |

---

## ⚙️ Enabling GitHub Actions Workflows

To ensure your 3D contribution city and contribution snake update automatically:

1. Go to your repo on GitHub: `https://github.com/Adarsh-tiwari1223/Adarsh-tiwari1223`
2. Click **Settings** ➔ **Actions** ➔ **General**.
3. Under **Workflow permissions**, select **Read and write permissions**.
4. Click **Save**.
5. Go to the **Actions** tab on GitHub:
   - Select **3D contribution city 🌃** ➔ Click **Run workflow**.
   - Select **Generate Demon Slayer Contribution Snake 🐍** ➔ Click **Run workflow**.

---

## 💡 Pro-Tip: Cache-Busting
GitHub caches images aggressively via its Camo proxy. If you ever update an SVG file and don't see changes on GitHub, simply bump the version tag in root `README.md`:
```markdown
<img src="./hero.svg?v=2" ... />
```
Commit the SVG first, and the README second.
