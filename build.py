#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static-site generator for the Marc Shular Law redesign.

Produces plain HTML pages (vanilla HTML/CSS/JS) sharing a single header,
footer, navigation and LeadrVision-integrated lead form.

Run:  python3 build.py
"""
import os, html, textwrap

ROOT = os.path.dirname(os.path.abspath(__file__))

BUSINESS = "Marc Shular Law"
PHONE = "(619) 743-9499"
PHONE_HREF = "tel:+16197439499"
PHONE2 = "(858) 212-0052"
PHONE2_HREF = "tel:+18582120052"
FAX = "(858) 435-2198"
EMAIL = "office@marcshularlaw.com"
OFFICE1 = "14282 Danielson Street Suite A, Poway, CA 92064"
OFFICE2 = "16236 San Dieguito Rd Suite 5-16, Rancho Santa Fe, CA 92091"

SOCIAL = {
    "facebook": "https://www.facebook.com/Marc-Shular-Law-286803841654239",
    "linkedin": "https://www.linkedin.com/in/marcshular/",
    "yelp": "https://www.yelp.com/biz/marc-shular-law-poway-2",
    "avvo": "https://www.avvo.com/attorneys/92064-ca-marc-shular-239467.html",
}
YOUTUBE = "https://www.youtube.com/channel/UCZ3dPSbpDxVY-DU-Ehckcdg"
APPSTORE = "https://itunes.apple.com/us/app/marc-shular-family-lawyer/id1244938858?ls=1&mt=8"
GOOGLEPLAY = "https://play.google.com/store/apps/details?id=com.bf.app086b5e"

# --------------------------------------------------------------------------
# Practice areas (slug, nav label, short card blurb)
# --------------------------------------------------------------------------
SERVICES = [
    ("spousal-support-san-diego", "Spousal Support",
     "Pursue or defend fair spousal support orders with a team focused on clarity and results."),
    ("san-diego-family-court-lawyer", "Family Court",
     "Confident, prepared representation for every stage of a San Diego family court matter."),
    ("child-support-san-diego", "Child Support",
     "Reliable counsel to establish, modify or enforce child support with minimal conflict."),
    ("child-custody-san-diego", "Child Custody",
     "Protect your relationship with your children through a custody plan built around their best interests."),
    ("military-divorce-san-diego", "Military Divorce",
     "Specialized guidance for service members and families navigating military divorce rules."),
    ("international-family", "International Family",
     "Handling family matters that cross state and international boundaries with care."),
    ("parenting-time-lawyer-san-diego-ca", "Parenting Time",
     "Build a workable parenting time schedule that protects your role as a parent."),
    ("spousal-maintenance-lawyer-san-diego-ca", "Spousal Maintenance",
     "Plan ahead and resolve spousal maintenance questions before they escalate."),
    ("order-for-protection", "Order For Protection",
     "Fast, resolute action to obtain or respond to an order for protection."),
    ("child-visitation-attorney-san-diego-ca", "Child Visitation",
     "Advocate for meaningful visitation and open, empowered communication."),
    ("divorce-mediator-san-diego-ca", "Divorce Mediation",
     "A more personal, less combative path through divorce with experienced mediation."),
    ("equal-timesharing-attorney", "Equal Timesharing",
     "Customized representation for clients seeking equal timesharing arrangements."),
    ("asset-division-discovering-hidden-assets-san-diego", "Asset Division & Hidden Assets",
     "Identify, value and fairly divide marital assets, including hidden accounts."),
    ("domestic-violence-attorney-san-diego-ca", "Domestic Violence",
     "Compassionate, personalized representation in sensitive domestic violence matters."),
    ("contested-uncontested-divorce", "Contested & Uncontested Divorce",
     "Support whether your divorce is amicable or heavily disputed."),
    ("prenuptial-agreements", "Prenuptial Agreements",
     "Protect your interests with carefully drafted prenuptial and post-marital agreements."),
    ("legal-separation-annulments-family-divorce-san-diego", "Legal Separation & Annulments",
     "Navigate legal separation and annulment with a trusted, knowledgeable counselor."),
    ("family-law-practice/high-net-worth-divorce-san-diego", "High Net Worth Divorce",
     "Sophisticated handling of complex, high-asset divorce and business valuations."),
    ("divorce-litigation-settlement-san-diego", "Divorce Litigation & Settlement",
     "Strong litigation and skillful settlement negotiation for divorce agreements."),
    ("domestic-violence-attorney-santee", "Domestic Violence (Santee)",
     "Full-service family law representation for domestic violence matters in Santee."),
]

# header dropdown items (label, href)
DROPDOWN = [("Family Law Overview", "/family-law-practice/")] + \
           [(label, "/" + slug + "/") for slug, label, _ in SERVICES]

# --------------------------------------------------------------------------
# Integrated SVG icons
# --------------------------------------------------------------------------
def ico(name, cls="ic"):
    paths = {
        "scale": '<path d="M12 3v18M6 21h12M5 7h14M12 7l-4 7a4 4 0 008 0z"/><path d="M12 7l4 7a4 4 0 01-8 0" />',
        "shield": '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
        "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
        "users": '<path d="M16 19v-1a4 4 0 00-4-4H7a4 4 0 00-4 4v1"/><circle cx="9.5" cy="8" r="3.2"/><path d="M17 11a3 3 0 100-6"/><path d="M21 19v-1a4 4 0 00-3-3.8"/>',
        "child": '<circle cx="12" cy="7" r="3"/><path d="M6 21v-2a6 6 0 0112 0v2"/><path d="M9 13h6"/>',
        "heart": '<path d="M12 20s-7-4.3-7-9.3A4.2 4.2 0 0112 8a4.2 4.2 0 017 2.7C19 15.7 12 20 12 20z"/>',
        "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
        "file": '<path d="M14 3H7a2 2 0 00-2 2v14a2 2 0 002 2h10a2 2 0 002-2V8z"/><path d="M14 3v5h5"/>',
        "phone": '<path d="M4 4h4l2 5-2.5 1.5a11 11 0 006 6L15 14l5 2v4a15 15 0 01-16-16z"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        "pin": '<path d="M12 21s-7-6-7-11a7 7 0 0114 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/>',
        "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 012-2h4a2 2 0 012 2v2M3 12h18"/>',
        "bank": '<path d="M3 10l9-6 9 6"/><path d="M5 10v9M19 10v9M9 10v9M15 10v9M3 21h18"/>',
        "gavel": '<path d="M14 4l6 6-3 3-6-6z"/><path d="M11 7l-7 7 3 3 7-7"/><path d="M14 20h7"/>',
        "lock": '<rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V8a4 4 0 018 0v2"/>',
        "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
        "check": '<path d="M4 12l5 5L20 6"/>',
    }
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" ' \
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % paths.get(name, "")

# --------------------------------------------------------------------------
# Lead form (posts to LeadrVision)
# --------------------------------------------------------------------------
LEADR_ACTION = "https://vision.leadrai.com/api/forms/1517d1ee9d02445afd74c973203413ae"

def lead_form(form_name="Free consultation", title="Request a Free Consultation",
              sub="Tell us about your situation and we will respond promptly. All inquiries are confidential."):
    return textwrap.dedent(f"""
    <form class="lead-form" method="POST" action="{LEADR_ACTION}" novalidate>
      <input type="hidden" name="_form" value="{html.escape(form_name)}">
      <input type="hidden" name="_page" value="">
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none">

      <div class="form-status" role="status" aria-live="polite">
        <span class="tick" aria-hidden="true">&#10003;</span>
        <span>Thanks, your message was sent. We will be in touch shortly.</span>
      </div>
      <div class="form-error" role="alert">Sorry, something went wrong. Please call us at {PHONE}.</div>

      <h3>{html.escape(title)}</h3>
      <p class="form-sub">{html.escape(sub)}</p>

      <div class="field-row">
        <div class="field">
          <label for="lf-name-{form_name[:3]}">Full name</label>
          <input id="lf-name-{form_name[:3]}" type="text" name="name" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="lf-phone-{form_name[:3]}">Phone</label>
          <input id="lf-phone-{form_name[:3]}" type="tel" name="phone" autocomplete="tel">
        </div>
      </div>
      <div class="field">
        <label for="lf-email-{form_name[:3]}">Email</label>
        <input id="lf-email-{form_name[:3]}" type="email" name="email" autocomplete="email" required>
      </div>
      <div class="field">
        <label for="lf-service-{form_name[:3]}">Service needed</label>
        <select id="lf-service-{form_name[:3]}" name="Service needed">
          <option value="">Click to make your choice&hellip;</option>
          <option>Family Law</option>
          <option>Divorce</option>
          <option>Legal Separation</option>
          <option>Child Custody</option>
          <option>Child Support</option>
          <option>Spousal Support</option>
          <option>Division of Property</option>
          <option>Premarital Agreement</option>
          <option>Post Marital Agreement</option>
        </select>
      </div>
      <div class="field">
        <label for="lf-msg-{form_name[:3]}">How can we help?</label>
        <textarea id="lf-msg-{form_name[:3]}" name="Message" placeholder="Briefly describe your situation"></textarea>
      </div>

      <button class="btn btn-gold btn-lg btn-block" type="submit">Send my request</button>
      <p class="form-note">The use of the Internet or this form for communication with the firm or any individual member of the firm does not establish an attorney-client relationship. Confidential or time-sensitive information should not be sent through this form.</p>
    </form>
    """)


def cta_section(form_name="Free consultation", title="Request a Free Consultation",
                copy="Take control of your family law situation. Choose a team that never leaves anything to chance.",
                bullets=None):
    bullets = bullets or [
        "Personal attention to every case",
        "We do not refer our cases out",
        "24/7 availability",
        "Certified Family Law Specialist",
    ]
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""
    <section class="cta-band" id="consultation">
      <div class="container">
        <div class="cta-grid">
          <div class="cta-copy">
            <span class="eyebrow" style="color:var(--gold-2)">Free Consultation</span>
            <h2>{html.escape(title)}</h2>
            <p>{html.escape(copy)}</p>
            <ul class="cta-list">{lis}</ul>
            <p class="mt-2" style="margin-bottom:0">
              <a class="btn btn-outline-light" href="{PHONE_HREF}">Call Now: {PHONE}</a>
            </p>
          </div>
          <div class="form-card">{lead_form(form_name)}</div>
        </div>
      </div>
    </section>
    """

# --------------------------------------------------------------------------
# Sidebar used on service / article pages
# --------------------------------------------------------------------------
def sidebar(related=None, active=None):
    related = related or []
    links = "".join(
        f'<li><a href="/{t[0]}/">{html.escape(t[1])}</a></li>' for t in related[:8]
    )
    related_block = ""
    if links:
        related_block = f"""
        <div class="side-card">
          <h3>Related Practice Areas</h3>
          <ul class="side-links">{links}</ul>
        </div>"""
    return f"""
    <aside class="sidebar">
      <div class="side-card navy">
        <img class="avatar" src="/images/source/00-about-marc-shular-2.jpg" alt="Marc D. Shular, Certified Family Law Specialist at Marc Shular Law" loading="lazy" width="96" height="96">
        <h3 style="text-align:center;margin-bottom:0.1em">Marc D. Shular</h3>
        <p style="text-align:center;color:#aeb9cc;font-size:0.85rem;margin-bottom:0.6rem">Certified Family Law Specialist</p>
        <p style="text-align:center;color:#c9d4e5;font-size:0.9rem;margin-bottom:0.4rem">Call for a free consultation</p>
        <a class="side-phone" style="text-align:center" href="{PHONE_HREF}">{PHONE}</a>
        <a class="btn btn-gold btn-block" href="/contact-us/">Get started</a>
      </div>
      <div class="side-card">
        <h3>Why Hire Us</h3>
        <ul class="checklist">
          <li>Personal Attention to All Cases</li>
          <li>We Do Not Refer Our Cases Out</li>
          <li>24/7 Availability</li>
          <li>34+ Years of Combined Experience</li>
          <li>Top San Diego Attorneys</li>
          <li>Quality Representation</li>
          <li>5 Star Reviews</li>
          <li>Award Winning Team</li>
          <li>Certified Family Law Specialist</li>
        </ul>
      </div>
      {related_block}
    </aside>
    """

# --------------------------------------------------------------------------
# Shared chrome
# --------------------------------------------------------------------------
def nav_html(current):
    def li(href, label, key):
        cls = ' class="current"' if key == current else ''
        return f'<li{cls}><a href="{href}">{label}</a></li>'
    dropdown_items = "".join(
        f'<a href="{href}">{html.escape(lbl)}</a>' for lbl, href in DROPDOWN
    )
    services_open = ' class="current"' if current == "services" else ''
    return f"""
    <header class="site-header">
      <div class="topbar">
        <div class="container">
          <span class="tb-group">
            <span class="tb-item">{ico('pin')}<span>{OFFICE1}</span></span>
          </span>
          <span class="tb-group">
            <span class="tb-item">{ico('phone')}<a href="{PHONE_HREF}">{PHONE}</a></span>
            <span class="tb-item">{ico('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></span>
          </span>
        </div>
      </div>
      <nav class="nav" aria-label="Primary">
        <a class="brand" href="/" aria-label="{BUSINESS} home">
          <span class="brand-mark" aria-hidden="true">MS</span>
          <span class="brand-text">
            <span class="brand-name">{BUSINESS}</span>
            <span class="brand-sub">Family Law Attorney</span>
          </span>
        </a>

        <button class="nav-toggle" aria-label="Toggle navigation" aria-controls="primary-nav" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>

        <ul class="nav-links" id="primary-nav">
          {li('/', 'Home', 'home')}
          <li{services_open}>
            <button type="button" aria-haspopup="true" aria-expanded="false">Practice Areas <span class="caret" aria-hidden="true"></span></button>
            <div class="dropdown">{dropdown_items}</div>
          </li>
          {li('/about/', 'About Marc Shular', 'about')}
          {li('/published-videos/', 'Videos', 'videos')}
          {li('/contact-us/', 'Contact Us', 'contact')}
          <li class="nav-cta-mobile" style="border:none;padding-top:0.8rem">
            <a class="btn btn-gold btn-block" href="{PHONE_HREF}">Call {PHONE}</a>
          </li>
        </ul>

        <div class="nav-cta">
          <a class="btn btn-gold" href="/#consultation">Free Consultation</a>
        </div>
      </nav>
    </header>
    """


def footer_html():
    svc_links = "".join(
        f'<li><a href="/{s}/">{html.escape(l)}</a></li>' for s, l, _ in SERVICES[:10]
    )
    return f"""
    <footer class="site-footer">
      <div class="container">
        <div class="footer-main">
          <div class="footer-brand">
            <a class="brand" href="/" aria-label="{BUSINESS} home">
              <span class="brand-mark" aria-hidden="true">MS</span>
              <span class="brand-text">
                <span class="brand-name">{BUSINESS}</span>
                <span class="brand-sub">Family Law Attorney</span>
              </span>
            </a>
            <p>Dedicated to providing the highest quality family law services in San Diego and surrounding areas. Certified Family Law Specialist. Free consultation.</p>
            <div class="footer-social">
              <a href="{SOCIAL['facebook']}" aria-label="Facebook" target="_blank" rel="noopener">FB</a>
              <a href="{SOCIAL['linkedin']}" aria-label="LinkedIn" target="_blank" rel="noopener">IN</a>
              <a href="{SOCIAL['yelp']}" aria-label="Yelp" target="_blank" rel="noopener">YP</a>
              <a href="{SOCIAL['avvo']}" aria-label="Avvo" target="_blank" rel="noopener">AV</a>
            </div>
            <div class="footer-badges">
              <a href="{SOCIAL['avvo']}" target="_blank" rel="noopener" aria-label="Marc Shular Avvo profile"><img src="/images/source/05-avvo.png" alt="Marc Shular Avvo attorney rating badge" height="34"></a>
              <a href="http://www.dmca.com/Protection/Status.aspx?ID=c44c2dee-6700-46f3-b9c8-3306e69c875e" target="_blank" rel="noopener" aria-label="DMCA protection status"><img src="/images/source/06-dmca-logo-std-btn160w.png" alt="DMCA.com protection status badge" height="34"></a>
            </div>
          </div>

          <div>
            <h4>Explore</h4>
            <ul class="footer-links">
              <li><a href="/">Home</a></li>
              <li><a href="/family-law-practice/">Family Law</a></li>
              <li><a href="/about/">About Marc Shular</a></li>
              <li><a href="/published-videos/">Videos</a></li>
              <li><a href="/what-to-do-before-being-divorced/">Before Divorce</a></li>
              <li><a href="/what-to-do-after-being-divorced/">After Divorce</a></li>
              <li><a href="/contact-us/">Contact Us</a></li>
            </ul>
          </div>

          <div>
            <h4>Practice Areas</h4>
            <ul class="footer-links">
              {svc_links}
              <li><a href="/family-law-practice/"><strong>View all services &rarr;</strong></a></li>
            </ul>
          </div>

          <div>
            <h4>Contact</h4>
            <ul class="footer-contact">
              <li>{ico('phone')}<a href="{PHONE_HREF}">{PHONE}</a></li>
              <li>{ico('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
              <li>{ico('pin')}<span>{OFFICE1}</span></li>
              <li>{ico('pin')}<span>{OFFICE2}</span></li>
            </ul>
          </div>
        </div>

        <p class="disclaimer">Disclaimer: The use of the Internet or this form for communication with the firm or any individual member of the firm does not establish an attorney-client relationship. Confidential or time-sensitive information should not be sent through this form. This website is a redesign and the information provided is for general purposes only.</p>

        <div class="footer-bottom">
          <span>&copy; <span id="year">2017</span> {BUSINESS}. All rights reserved.</span>
          <nav class="footer-legal" aria-label="Legal">
            <a href="/privacy-policy/">Privacy Policy</a>
            <a href="/cookie-policy/">Cookie Policy</a>
            <a href="/terms-of-services/">Terms &amp; Conditions</a>
            <a href="/data-request/">Data Request</a>
            <a href="/data-erasure/">Data Erasure</a>
          </nav>
        </div>
      </div>
    </footer>
    """


def layout(page):
    """page dict: path, title, desc, current, hero_html, body_html"""
    canonical = "/" + page["path"] if page["path"] else "/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page['title'])}</title>
  <meta name="description" content="{html.escape(page['desc'])}">
  <meta name="theme-color" content="#0e2038">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{html.escape(page['title'])}">
  <meta property="og:description" content="{html.escape(page['desc'])}">
  <meta property="og:site_name" content="{BUSINESS}">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {nav_html(page['current'])}
  <main id="main">
{page['hero_html']}
{page['body_html']}
  </main>
  {footer_html()}
  <script src="/assets/js/main.js" defer></script>
  <script>document.getElementById('year').textContent=new Date().getFullYear();</script>
</body>
</html>
"""


def page_hero(crumbs, h1, lead=None):
    trail = ' <span>/</span> '.join(
        (f'<a href="{href}">{html.escape(txt)}</a>' if href else html.escape(txt))
        for txt, href in crumbs
    )
    lead_html = f"<p>{html.escape(lead)}</p>" if lead else ""
    return f"""
    <section class="page-hero">
      <div class="container">
        <div class="breadcrumbs">{trail}</div>
        <h1>{html.escape(h1)}</h1>
        {lead_html}
      </div>
    </section>"""


def write_page(path, content):
    if path == "" or path == "index.html":
        dest = os.path.join(ROOT, "index.html")
    else:
        dest = os.path.join(ROOT, path, "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(content)
    return dest
