from playwright.sync_api import sync_playwright

SVG_LOGO = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>

    <linearGradient id="primaryG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>

    <linearGradient id="accentG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="50%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="400" height="400" rx="36" fill="url(#bgG)"/>
  <rect x="1" y="1" width="398" height="398" rx="35" fill="none" stroke="#1e293b" stroke-width="2"/>

  <!-- Ambient Glow Ring -->
  <circle cx="200" cy="180" r="110" fill="#0284c7" opacity="0.12" filter="url(#glow)"/>
  <circle cx="200" cy="180" r="85" fill="#10b981" opacity="0.08" filter="url(#glow)"/>

  <!-- Outer Hexagonal Emblem -->
  <polygon points="200,80 286,130 286,230 200,280 114,230 114,130" 
           fill="#111827" stroke="url(#accentG)" stroke-width="3.5" filter="url(#glow)"/>

  <!-- Inner Hexagon Accent -->
  <polygon points="200,95 273,137 273,223 200,265 127,223 127,137" 
           fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="8 5"/>

  <!-- Stylized Geometric "AT" Monogram -->
  <!-- Letter A -->
  <path d="M 200,118 L 150,225 L 172,225 L 183,200 L 217,200 L 228,225 L 250,225 Z M 200,158 L 210,183 L 190,183 Z" 
        fill="url(#primaryG)"/>
  
  <!-- Crossbar / Circuit Node for T -->
  <rect x="140" y="142" width="120" height="12" rx="6" fill="url(#accentG)" filter="url(#glow)"/>
  <rect x="194" y="142" width="12" height="75" rx="6" fill="url(#accentG)"/>

  <!-- Tech Dots / Circuit Points -->
  <circle cx="140" cy="148" r="6" fill="#38bdf8"/>
  <circle cx="260" cy="148" r="6" fill="#10b981"/>
  <circle cx="200" cy="217" r="5" fill="#38bdf8"/>

  <!-- Typography -->
  <text x="200" y="325" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif" 
        font-weight="800" font-size="16.5" fill="#f8fafc" letter-spacing="3" text-anchor="middle">
    ADARSH TIWARI
  </text>
  <text x="200" y="348" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif" 
        font-weight="700" font-size="11" fill="#38bdf8" letter-spacing="4" text-anchor="middle">
    LABS
  </text>
  <text x="200" y="370" font-family="ui-monospace, Menlo, Consolas, monospace" 
        font-size="8.5" fill="#64748b" letter-spacing="2" text-anchor="middle">
    SDET &amp; AUTOMATION
  </text>
</svg>
"""

with open("linkedin/company_logo.svg", "w", encoding="utf-8") as f:
    f.write(SVG_LOGO)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 400, "height": 400})
    page.set_content(f'<body style="margin:0;background:transparent;">{SVG_LOGO}</body>')
    page.screenshot(path="linkedin/company_logo.png", omit_background=True)
    browser.close()

print("SUCCESS: Generated linkedin/company_logo.png (400x400) and linkedin/company_logo.svg")
