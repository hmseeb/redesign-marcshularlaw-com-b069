# -*- coding: utf-8 -*-
"""Page content + generation entry point for the Marc Shular Law redesign."""
import os
from build import (SERVICES, sidebar, cta_section, page_hero, layout, write_page, lead_form,
                   ico, PHONE, PHONE_HREF, PHONE2, EMAIL, FAX, OFFICE1, OFFICE2,
                   BUSINESS, SOCIAL, YOUTUBE, APPSTORE, GOOGLEPLAY)

# ---------------------------------------------------------------- helpers
def blocks_to_html(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f"<p>{val}</p>")
        elif kind == "lead":
            out.append(f'<p class="lede">{val}</p>')
        elif kind == "h2":
            out.append(f"<h2>{val}</h2>")
        elif kind == "h3":
            out.append(f"<h3>{val}</h3>")
        elif kind == "callout":
            out.append(f'<div class="callout">{val}</div>')
        elif kind == "list":
            items = "".join(f"<li>{i}</li>" for i in val)
            out.append(f"<ul>{items}</ul>")
    return "\n".join(out)


def service_page(slug, title, desc, h1, lead, body_blocks, related, form_name="Free consultation",
                 extra="", current="services"):
    article = blocks_to_html(body_blocks)
    hero = page_hero([("Home", "/"), ("Practice Areas", "/family-law-practice/"), (h1, None)], h1, lead)
    body = f"""
    <section class="section">
      <div class="container">
        <div class="layout">
          <article class="prose">{article}</article>
          {sidebar(related)}
        </div>
      </div>
    </section>
    {cta_section(form_name, "Request a Free Consultation",
                 "Take control of your family law situation today. We offer a free consultation to help you at this time of change.")}
    {extra}
    """
    return {"path": slug, "title": title, "desc": desc, "current": current,
            "hero_html": hero, "body_html": body}


def service_grid(limit=None):
    items = SERVICES[:limit] if limit else SERVICES
    cards = []
    for i, (slug, label, blurb) in enumerate(items):
        cards.append(f"""
        <a class="card service-tile" href="/{slug}/">
          <div class="ic">{ico(['scale','users','child','heart','shield','globe','home','file','lock','check','gavel','bank','chart','briefcase','file','heart','file','scale','bank','gavel','shield'][i % 21])}</div>
          <h3>{label}</h3>
          <p>{blurb}</p>
          <span class="card-link">Learn more</span>
        </a>""")
    return '<div class="grid grid-3">%s</div>' % "".join(cards)


# ================================================================ HOME
def build_home():
    hero = f"""
    <section class="hero">
      <div class="hero-inner">
        <div class="hero-copy">
          <span class="hero-eyebrow">Family Law Attorney &middot; San Diego, CA</span>
          <h1>The attorney you trust when your <span class="accent">day in court arrives.</span></h1>
          <p class="hero-lead">Dedicated to providing the highest quality legal services in San Diego and surrounding areas. Certified Family Law Specialist Marc Shular offers a free consultation to help you through this time of change.</p>
          <div class="hero-actions">
            <a class="btn btn-gold btn-lg" href="{PHONE_HREF}">Call Now: {PHONE}</a>
            <a class="btn btn-outline-light btn-lg" href="/#consultation">Get a Free Consultation</a>
          </div>
          <div class="hero-stats">
            <div class="hero-stat"><div class="num">25+</div><div class="lbl">Years in Practice</div></div>
            <div class="hero-stat"><div class="num">34+</div><div class="lbl">Years Combined Experience</div></div>
            <div class="hero-stat"><div class="num">5.0</div><div class="lbl">Star Client Reviews</div></div>
            <div class="hero-stat"><div class="num">24/7</div><div class="lbl">Availability</div></div>
          </div>
        </div>
        <div class="hero-figure">
          <img src="/images/source/01-family-law-attorney-poway.jpg" alt="Marc Shular family law attorney serving Poway and San Diego, California" width="709" height="399">
          <div class="hero-badge">
            <span class="ic" aria-hidden="true">&#9733;</span>
            <span><b>Certified Family Law Specialist</b><span>CPA &amp; Special Master experience</span></span>
          </div>
        </div>
      </div>
    </section>
    """

    welcome = f"""
    <section class="section">
      <div class="container">
        <div class="split">
          <div class="split-media">
            <img src="/images/source/02-poway-family-law-attorney-300x199.jpg" alt="Marc Shular Law office handling divorce and family law matters in California" width="300" height="199">
          </div>
          <div class="split-copy">
            <span class="eyebrow">Welcome</span>
            <h2>Welcome to Marc Shular Family Law Firm</h2>
            <p>Marc Shular specializes in divorce and family law and is dedicated to providing the highest quality legal services to individuals in the San Diego area, Southern California area and beyond. Every effort is made to resolve your case in a prompt manner.</p>
            <p>Marc Shular is a law professional who specializes in handling all kinds of family matters. He offers a free consultation to help you at this time of change. With 34+ years of combined experience, our firm provides personal attention to every case &mdash; and we never refer our cases out.</p>
            <a class="btn btn-navy" href="/about/">Meet Marc Shular</a>
          </div>
        </div>
      </div>
    </section>
    """

    services = f"""
    <section class="section section-cream" id="services">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Practice Areas</span>
          <h2>Comprehensive Family Law Services</h2>
          <p>These are the types of practice Marc Shular specializes in. Select the category related to your case to learn more.</p>
        </div>
        {service_grid(9)}
        <p class="text-center mt-3"><a class="btn btn-outline" href="/family-law-practice/">View all family law services</a></p>
      </div>
    </section>
    """

    why = f"""
    <section class="section">
      <div class="container">
        <div class="split reverse">
          <div class="split-media">
            <img src="/images/source/00-about-marc-shular-2.jpg" alt="Portrait of Marc D. Shular, Certified Family Law Specialist in San Diego" width="709" height="399">
          </div>
          <div class="split-copy">
            <span class="eyebrow">Why Hire Us</span>
            <h2>Representation you can rely on</h2>
            <p>From your first consultation to your final hearing, we work to make sure your case has the best chance of success. Marc Shular is licensed to practice accounting as a Certified Public Accountant and has been appointed as a special master to help the Court resolve complicated property and equalization issues.</p>
            <ul class="checklist mt-2">
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
        </div>
      </div>
    </section>
    """

    matters = f"""
    <section class="section section-navy">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow" style="color:var(--gold-2)">How We Help</span>
          <h2>Family law matters we handle</h2>
          <p>Whatever your family's situation, our team brings knowledge and compassion to your unique case.</p>
        </div>
        <div class="grid grid-3">
          <div class="card"><h3>Divorce</h3><p>Divorce is usually handled by a divorce lawyer, but if your family lawyer has experience in the field he can help. We look out for your best interests &mdash; getting you your share of property, helping you maintain custody of your children, and working out alimony.</p></div>
          <div class="card"><h3>Legal Separation</h3><p>Sometimes you want time apart from your spouse without necessarily getting a divorce. We help make clear who is entitled to what and when, and make sure both parties stick to it.</p></div>
          <div class="card"><h3>Child Custody</h3><p>Custody matters can be very difficult. Engage the services of a family lawyer early &mdash; they will fight to ensure your wishes are honored where child custody is concerned.</p></div>
          <div class="card"><h3>Child Support</h3><p>Once you have a child with someone they are required to help bring up the child. We follow up with the other parent to make sure they meet their obligation.</p></div>
          <div class="card"><h3>Division of Property</h3><p>Property is a sensitive issue. We assess your situation, let you know what you can and cannot get, and argue on your behalf either before your family or in court.</p></div>
          <div class="card"><h3>Spousal Support</h3><p>Legally, your spouse may be required to continue to offer you the same kind of life through spousal support. We help make sure you get what you deserve.</p></div>
        </div>
      </div>
    </section>
    """

    apps = f"""
    <section class="section">
      <div class="container">
        <div class="split">
          <div class="split-copy">
            <span class="eyebrow">Download Our Apps Today</span>
            <h2>Marc Shular Family Lawyer, in your pocket</h2>
            <p>Stay connected with the firm on the go. Download our mobile app for quick access and answers to common family law questions.</p>
            <div class="footer-badges" style="margin-top:1.2rem">
              <a href="{APPSTORE}" target="_blank" rel="noopener" aria-label="Download on the App Store"><img src="/images/source/03-appstorefinal-e1497352455646.png" alt="Download Marc Shular Family Lawyer on the App Store" height="52"></a>
              <a href="{GOOGLEPLAY}" target="_blank" rel="noopener" aria-label="Get it on Google Play"><img src="/images/source/04-googleplayfinal-e1497352478301.png" alt="Get Marc Shular Family Lawyer on Google Play" height="52"></a>
            </div>
          </div>
          <div class="split-media">
            <div class="grid grid-2" style="gap:1.2rem">
              <div class="card"><div class="ic">{ico('chart')}</div><h3>Recognized</h3><p>Rated on Avvo and reviewed by clients across San Diego.</p></div>
              <div class="card"><div class="ic">{ico('users')}</div><h3>Trusted</h3><p>34+ years of combined family law experience.</p></div>
              <div class="card"><div class="ic">{ico('shield')}</div><h3>Certified</h3><p>Certified Family Law Specialist.</p></div>
              <div class="card"><div class="ic">{ico('phone')}</div><h3>Available</h3><p>24/7 availability for our clients.</p></div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    body = welcome + services + why + matters + apps + cta_section(
        "Free consultation",
        "Talk to a San Diego family law attorney today",
        "Give us a call, and let us help you move forward with confidence. Free consultation available.")
    hero_html = hero
    return {"path": "", "title": "Marc Shular Law | San Diego Family Law & Divorce Attorney",
            "desc": "Marc Shular Law is a San Diego family law firm offering divorce, child custody, child support and spousal support representation. Certified Family Law Specialist. Free consultation.",
            "current": "home", "hero_html": hero_html, "body_html": body}


# ================================================================ SERVICE PAGES
def build_service_pages():
    pages = []

    related_default = [(s, l) for s, l, _ in SERVICES]

    # 01 Family law practice hub
    fam_blocks = [
        ("lead", "You may have found yourself facing a divorce; in this situation you may need the help of a family law attorney. Marc Shular is a law professional who specializes in handling all kinds of family matters. He offers a free consultation to help you at this time of change."),
        ("h2", "Family Law Legal Services"),
        ("p", "The Law Office of Marc D. Shular provides experienced legal counsel for the full range of family law matters. Select the practice area related to your case below to learn more."),
        ("h2", "These are the types of practice Marc Shular specializes in"),
    ]
    fam_body = blocks_to_html(fam_blocks) + service_grid()
    pages.append({
        "path": "family-law-practice",
        "title": "Family Law San Diego | Family Law Attorney San Diego",
        "desc": "Marc Shular Law provides family law legal services in San Diego, including divorce, child custody, child support, spousal support and more. Free consultation.",
        "current": "services",
        "hero_html": page_hero([("Home", "/"), ("Practice Areas", None)], "Family Law Legal Services",
                               "Marc Shular is a law professional who specializes in handling all kinds of family matters."),
        "body_html": f"""
        <section class="section">
          <div class="container">
            <div class="layout">
              <article class="prose">{fam_body}</article>
              {sidebar(related_default)}
            </div>
          </div>
        </section>
        {cta_section("Free consultation", "Not sure which practice area applies to you?",
                     "Call us and we will help you identify the right path for your family law matter.")}
        """
    })

    # 02 Spousal Support
    pages.append(service_page(
        "spousal-support-san-diego",
        "San Diego Spousal Support Attorney | Spousal Support California",
        "Spousal support lawyer in San Diego, CA. Marc Shular Law helps you take control of your spousal support case with individualized, confidential attention.",
        "Spousal Support Lawyer in San Diego, CA",
        "Your spousal support case does not have to play out like everyone else's. Take control of your situation &mdash; never leaving anything to chance.",
        [
            ("p", "At The Law Office of Marc D. Shular, we understand that life is unpredictable. Your Spousal Support case does not have to play out in the same way. When you choose The Law Office of Marc D. Shular, you choose to take control of your Spousal Support situation, never leaving anything to chance. We have no greater mission than to help you."),
            ("p", "At The Law Office of Marc D. Shular you will never receive the run-around as many Spousal Support firms in the San Diego area do. No matter what the circumstances of your Spousal Support case may be, you will receive the individualized and confidential attention your case deserves."),
            ("p", "At The Law Office of Marc D. Shular, our Spousal Support team aims for clarity when dealing with your family matters. We will try to make sure that your Spousal Support case gets resolved as soon as possible. With our many years of experience, you can expect us to bring our knowledge to the table and apply it to your unique case. Trust our firm in the San Diego area."),
            ("callout", "<strong>Give us a call today!</strong> If your family is facing Spousal Support matters in the San Diego area courts, you deserve the professional care of a team like The Law Office of Marc D. Shular. With 25 years of practice, we have come to realize how important compassion and efficiency are in Spousal Support cases. Call us today at (858) 212-0052."),
            ("address", None),
        ],
        related_default))

    # 03 Family court
    pages.append(service_page(
        "san-diego-family-court-lawyer",
        "Family Court Lawyer in San Diego | Info Provided by Marc Shular Law",
        "San Diego family court lawyer with 25 years of experience. Strong advocacy, accurate predictions and clear expectations for your family court case.",
        "San Diego, CA Family Court Lawyer",
        "Do not settle for Family Court firms that tell you they will do what they can and hope for the best. We have the know-how to fight and win.",
        [
            ("p", "Do not settle for Family Court firms that tell you they will do what they can and hope for the best. With 25 years of experience handling Family Court cases, we will help make your case a success. The Law Office of Marc D. Shular has the know-how to fight and win. When you need strong advocacy, there is only one place to turn to in the San Diego, CA area, and that is The Law Office of Marc D. Shular."),
            ("p", "Over our 25 years history, The Law Office of Marc D. Shular has learned that the key to being a skilled attorney is making accurate predictions about the future. A big part of our job, as your Family Court representation is having open communication and setting clear and obtainable expectations to better plan for the future. When litigation is necessary to protect our client, The Law Office of Marc D. Shular is innovative with our strategies. We will take measured action as your Family Court advocate to assert your rights."),
            ("p", "You will enjoy working with The Law Office of Marc D. Shular in the San Diego, CA area as your Family Court case moves through the process. Over the 25 years we have been around, we have seen both sides of the coin regarding Family Court cases. In any Family Court case, it is important to protect your rights as early as possible."),
            ("callout", "<strong>Reach out to us today!</strong> If you are from the San Diego, CA area and your family is dealing with Family Court matters, do not hesitate to call us at The Law Office of Marc D. Shular, (858) 212-0052 for help and advice today."),
        ],
        related_default))

    # 04 Child support
    pages.append(service_page(
        "child-support-san-diego",
        "Child Support Lawyer San Diego | California Child Support Lawyers",
        "Child support lawyer in San Diego, CA. Marc Shular Law works toward good resolutions and professional representation for child support matters.",
        "Child Support Lawyer in San Diego, CA",
        "We know how difficult a lengthy child support case can be. Our focus is finding a good resolution between the two parties.",
        [
            ("p", "At The Law Office of Marc D. Shular we know how difficult a lengthy Child Support case can be. Many families in the San Diego area can be torn apart because these cases are so emotional that there just seems to be no way to reconcile. We focus on finding a good resolution between the two parties to minimize the potential fallout."),
            ("p", "Working with clients throughout the San Diego area, The Law Office of Marc D. Shular has represented both men and women who are going through the litigation process. No matter which aspect of the Child Support process you are facing, we will work with you to make sure we are moving together towards your goals. We can provide professional services for your Child Support matters."),
            ("p", "Give our team a call if you need a reliable Child Support lawyer in the San Diego area. At The Law Office of Marc D. Shular, we have many years of experience that we will apply to your case."),
            ("callout", "<strong>Call us now!</strong> A situation involving Child Support matters can be a delicate process, and the complexity of San Diego area law may create unnecessary strife in your family's life. You need the guidance of a professional team like The Law Office of Marc D. Shular. Call us today at (858) 212-0052."),
        ],
        related_default))

    # 05 Child custody
    pages.append(service_page(
        "child-custody-san-diego",
        "Child Custody California | San Diego Child Custody Attorney",
        "Child custody attorney in San Diego, CA. Move through the child custody process as seamlessly as possible with over 25 years of experience.",
        "Child Custody Attorney San Diego CA",
        "We are here to help clients who want to move through the Child Custody process as seamlessly as possible.",
        [
            ("p", "Law Office of Marc D. Shular is here to help clients who want to move through the Child Custody process as seamlessly as possible. We have over 25 years of experience helping individuals with their family matters. We are proud to say that we can successfully work with clients looking for a Child Custody attorney in San Diego."),
            ("p", "If you are looking for an experienced Child Custody lawyer in the San Diego area, then give us at Law Office of Marc D. Shular a call today. We welcome all clients throughout the San Diego area who are looking for a firm that can effectively represent them in their case."),
            ("p", "Throughout our over 25 years of fighting for the rights of our clients, we have gained insight on how to better conduct our Child Custody services. We put one hundred percent of our efforts towards getting our San Diego clients the fair and speedy trial that they deserve."),
            ("callout", "<strong>Let us be your guides!</strong> Law Office of Marc D. Shular wants to be your guide for your custody case in San Diego. We have the experience to help you, and we will put our over 25 years to work for you. Give us a call today at (858) 212-0052."),
        ],
        related_default))

    # 06 Military divorce
    pages.append(service_page(
        "military-divorce-san-diego",
        "Military Divorce Lawyers San Diego | San Diego Military Divorce Lawyers",
        "Military divorce services in San Diego, CA. Marc Shular Law ensures your paperwork is properly filled out, filed, managed and defended.",
        "Military Divorce Services in San Diego CA",
        "It is important to work with a qualified Military Divorce Services lawyer in San Diego to ensure your paperwork is properly handled.",
        [
            ("p", "Each case in San Diego that we at Law Office of Marc D. Shular handle is different from the last; because of this we tackle each one independently and make sure we devote equal time and effort to all. We know there are cases where the client is themselves looking for help with a Military Divorce Services matter, or is seeking our help for a family member or friend. This is why it's important to work with a qualified Military Divorce Services lawyer in San Diego to ensure that your paperwork is properly filled out, properly filed, correctly managed and defended."),
            ("p", "At Law Office of Marc D. Shular, we know that the issues you are facing in the San Diego area extend to your entire life like a dark stormy cloud. We know what it is like to face Military Divorce Services issues, and we have been helping others just like you beat these issues and improve their lives in the San Diego area. Also at Law Office of Marc D. Shular, we are up-to-date on relevant Military Divorce Services case law and advocacy strategies. After over 25 years of practicing law, we know how to achieve the best results for our clients. Every case contains many decisions that affect the ultimate outcome; Law Office of Marc D. Shular can help you make the right decision."),
            ("callout", "<strong>Give us a call today!</strong> At Law Office of Marc D. Shular, we hope that you will trust us even if you consider your Military Divorce Services case to be out of this world tough. Give us a call at (858) 212-0052 today and see why we have so many clients throughout San Diego."),
        ],
        related_default))

    # 07 International family
    pages.append(service_page(
        "international-family",
        "International Family | Info Provided by Marc Shular Law",
        "International family lawyer in San Diego, CA. Experienced counsel for family matters that cross state and international boundaries.",
        "International Family Lawyer San Diego CA",
        "Whether it is the last will and testament or divorce, we can provide an experienced lawyer to aid you.",
        [
            ("p", "In today's world, International Family law is comprised of several different areas of focus. Whether it is the last will and testament or divorce, The Law Office of Marc D. Shular can provide an experienced lawyer to aid you. For 25 years we have helped clients throughout the San Diego CA area by having the skill and compassion to delicately handle these uneasy matters. We know that dealing with International Family laws can be difficult and we do not want you to have to go through it alone."),
            ("p", "At The Law Office of Marc D. Shular we are more than happy to take on new clients and find ways that they can live happily with the greatest possible legal representation. Throughout the International Family process, The Law Office of Marc D. Shular can use our many years of experience to help you make the right decision. Discipline and diligence are the only ways to dispose of a lengthy International Family case successfully."),
            ("p", "If you are involved with a tough International Family case, you should contact The Law Office of Marc D. Shular to get the advice you need to make it through a difficult period of family transition. When necessary, we can assert or defend your interests in court. With 25 years of experience practicing law we understand that an important step in International Family law issues is to help our clients define and articulate their goals. At The Law Office of Marc D. Shular we can handle International Family matters that present a high degree of complexity, or conflict."),
            ("callout", "To schedule a consultation with a San Diego CA attorney, contact The Law Office of Marc D. Shular by calling us at (858) 212-0052 today."),
        ],
        related_default))

    # 08 Parenting time
    pages.append(service_page(
        "parenting-time-lawyer-san-diego-ca",
        "Parenting Time Lawyer San Diego, CA | Marc Shular Law",
        "Parenting time lawyer in San Diego, CA. We help you reach a successful outcome in your parenting time case with compassion and proficiency.",
        "Parenting Time Lawyer San Diego, CA",
        "No matter how difficult and emotionally-charged your Parenting Time case may be, we know what it takes for you to have a successful outcome.",
        [
            ("p", "No matter how difficult and emotionally-charged your Parenting Time case may be, we know what it takes for you to have a successful outcome. Over the course of 25 years here at The Law Office of Marc D. Shular we have helped countless clients throughout San Diego CA reach successful outcomes in their cases."),
            ("p", "At The Law Office of Marc D. Shular, our main concern is that you and your family are led through your Parenting Time case efficiently for the sake of your wellbeing. Resolving your Parenting Time issues in the San Diego CA area in a way where you are protected is of the utmost importance to us."),
            ("p", "At The Law Office of Marc D. Shular we take the time to listen to your story and get to know you on more than just a business to customer level. We know it is important to know your personal plights in the San Diego CA area because that will allow us to serve you better in court. We want to help you through your Parenting Time cases."),
            ("p", "Choosing a Parenting Time firm which not only competently handles any potential Parenting Time legal complexities and challenges in the San Diego CA area with superior knowledge and efficiency, and also treats each client compassionately and respectfully is of paramount importance. At The Law Office of Marc D. Shular, we have learned over the course of 25 years that our clients value proficiency in both areas."),
        ],
        related_default))

    # 09 Spousal maintenance
    pages.append(service_page(
        "spousal-maintenance-lawyer-san-diego-ca",
        "Spousal Maintenance Lawyer San Diego, CA | Marc Shular Law",
        "Spousal maintenance lawyer in San Diego, CA. Plan ahead and seek proper spousal maintenance advice before the situation escalates.",
        "Spousal Maintenance Lawyer in San Diego, CA",
        "Seek legal counsel on matters of Spousal Maintenance before the situation fully evolves or escalates.",
        [
            ("p", "Seek legal counsel on matters of Spousal Maintenance cases before the situation fully evolves or escalates into something worse. Sometimes a person in our San Diego, CA community does not see the writing on the wall. In such Spousal Maintenance cases, there are definite advantages to planning ahead and seeking proper Spousal Maintenance advice from The Law Office of Marc D. Shular."),
            ("p", "The Law Office of Marc D. Shular prides itself on being able to provide high-level legal counsel that does not sacrifice a personal touch. With 25 years experience working with clients in the San Diego, CA area, we know how to maneuver through these difficult scenarios while keeping your best interest as our focus. Let our team of professionals in the San Diego, CA area bring you the peace of mind you need and deserve."),
            ("p", "Here at The Law Office of Marc D. Shular, we fancy ourselves proactive and forward thinkers who are dedicated to solving your Spousal Maintenance case issues. We have many years of experience in dealing with these cases in the San Diego, CA area. We have significant experience devoting ourselves to these Spousal Maintenance cases. We will put our experience to work for you in the San Diego, CA area."),
            ("callout", "Part of our practice at The Law Office of Marc D. Shular is providing people in San Diego, CA with help for the rest of their life. We'll use our 25 years of experience in your Spousal Maintenance case to help you move on and meet your life goals."),
        ],
        related_default))

    # 10 Order for protection
    pages.append(service_page(
        "order-for-protection",
        "Order For Protection Attorney San Diego, CA | Marc Shular Law",
        "Order for Protection attorney in San Diego, CA. Quick, resolute action and confidential counsel for your order for protection case.",
        "Order For Protection Attorney in San Diego, CA",
        "The first element in an effective Order for Protection strategy is quick, resolute action.",
        [
            ("p", "The Law Office of Marc D. Shular has a long history of carefully looking over what our clients need from their attorney and trying to fulfill those needs as much as possible. We work with anyone in the San Diego, CA area who is looking for an experienced Order for Protection lawyer."),
            ("p", "At The Law Office of Marc D. Shular we walk clients in the San Diego, CA area through their cases. We have the experience you can trust, and with 25 years in practice, we know what it takes to be successful in a difficult Order for Protection case."),
            ("p", "Our legal team at The Law Office of Marc D. Shular understands the heavy toll that emotionally-charged family cases can exact. We know that every Order for Protection case is different and everyone has his or her version of success. If you are in the San Diego, CA area, we will create a legal strategy to help you in your case."),
            ("p", "The first element in an effective Order for Protection strategy is quick, resolute action. For that reason The Law Office of Marc D. Shular is waiting for you to contact them to take that first step toward a satisfactory resolution in your Order for Protection case. We know that some clients in the San Diego, CA area prefer to speak privately; so you can call us at (858) 212-0052. Be assured that your conversation is very important to us; and that your case and information will remain confidential with our legal counsel and services."),
        ],
        related_default))

    # 11 Child visitation
    pages.append(service_page(
        "child-visitation-attorney-san-diego-ca",
        "Child Visitation Attorney San Diego, CA | Marc Shular Law",
        "Child visitation attorney in San Diego, CA. Open dialogue and experienced representation to protect your rights in your visitation case.",
        "Child Visitation Attorney San Diego, CA",
        "We make it our goal to understand your situation and where you stand in your Child Visitation matter.",
        [
            ("p", "At The Law Office of Marc D. Shular, we always make sure our clients understand that we like to have open dialogue with our San Diego, CA clients and hope that they feel empowered as they work toward their goals. We always make it our goal to make sure we understand your situation and where you stand in your Child Visitation matter."),
            ("p", "Are you in the San Diego, CA area and looking for a lawyer to represent you in your Child Visitation case? The Law Office of Marc D. Shular has many years of experience working in these matters, and over the course of this time we have learned efficient legal representation that we can use to improve the chances of our San Diego, CA clients having a successful case."),
            ("p", "No matter how challenging it may seem to go up against an opposing lawyer in the San Diego, CA area to get a proper settlement for your Child Visitation case, The Law Office of Marc D. Shular is up for the challenge. We have seen and heard horror stories of individuals throughout San Diego, CA who have had terrible cases due to their lawyers either being unnerved or put off by some condition they did not expect."),
            ("callout", "Over our 25 years in practice we've seen a variety of family law issues that our clients have had to deal with, and all with their own unique circumstances. If you are looking for a Child Visitation lawyer to help you, we can make the process easier on you. Call us at (858) 212-0052 to get started today."),
        ],
        related_default))

    # 12 Divorce mediator
    pages.append(service_page(
        "divorce-mediator-san-diego-ca",
        "Divorce Mediator in San Diego, CA | Marc Shular Law",
        "Divorce mediator in San Diego, CA. A personal, supportive approach to mediation with proactive handling of filing deadlines and your goals.",
        "Divorce Mediator in San Diego, CA",
        "Our goal is not just to be a high-volume firm, but to provide a more personal touch to every case.",
        [
            ("p", "At The Law Office of Marc D. Shular, our goal is not just to be a high-volume firm, but to provide a more personal touch to every case. We know that Divorce Mediator laws can be difficult to maneuver, and the cases are extremely taxing. We want to provide our service to clients throughout the San Diego, CA area so that they have someone they can count on during these hard times. Do not go through Divorce Mediator cases alone. Let our San Diego, CA area firm guide you through this difficult time."),
            ("p", "We have seen after 25 years in practice the damage prolonged Divorce Mediator litigation can bring and try to avoid that experience for our clients. Legal separation is another option that The Law Office of Marc D. Shular uses and can lead to less stress for the clients within the San Diego, CA area. Your Divorce Mediator advocate will counsel you on the rights, benefits and drawback of this arrangement so you can make the right choice for yourself."),
            ("p", "The Law Office of Marc D. Shular is proactive in meeting filing deadlines and other elements of your case in the San Diego, CA area. At The Law Office of Marc D. Shular we drill to the bottom of your expectations and press your goals in your Divorce Mediator case."),
            ("callout", "The doors at The Law Office of Marc D. Shular are always open to you. We pride ourselves on providing a supportive, welcoming environment, as well as outstanding Divorce Mediator counsel. If you are unhappy with the way your current Divorce Mediator case is being handled in San Diego, CA, call The Law Office of Marc D. Shular in order to schedule your first consultation with us."),
        ],
        related_default))

    # 13 Equal timesharing
    pages.append(service_page(
        "equal-timesharing-attorney",
        "Equal Timesharing Attorney San Diego, CA | Marc Shular Law",
        "Equal timesharing attorney in San Diego, CA. Customized representation that makes your best interests the priority.",
        "Equal Timesharing Attorney in San Diego, CA",
        "We strive for a fast and favorable resolution to any Equal Timesharing legal proceedings you may be dealing with.",
        [
            ("p", "At The Law Office of Marc D. Shular, we have a proven track record of honoring the individual situation of each client in the San Diego, CA area. We strive for a fast and favorable resolution to any Equal Timesharing legal proceedings you may find yourself dealing with. Our 25 years of experience has taught us how to get you the results you want from your Equal Timesharing case."),
            ("p", "Every family has unique ways of dealing with Equal Timesharing cases, which is why every family will need a different approach. At The Law Office of Marc D. Shular, an established San Diego, CA law firm, we are dedicated to providing clients with customized representation that makes their best interests the priority. We put our 25 years working with clients in the area to work for you so you can feel safe knowing your Equal Timesharing case will get the best results possible."),
            ("p", "Choose The Law Office of Marc D. Shular and be assured you are receiving the highest standard of professional Equal Timesharing counsel. We promise to treat your individual Equal Timesharing case as our top priority. If you live in the San Diego, CA area and need an experienced Equal Timesharing attorney, choose the firm that has the knowledge and skill set your Equal Timesharing situation requires."),
            ("callout", "If you have been confronted in your life with an Equal Timesharing situation requiring legal advice or involvement, do not hesitate to seek guidance from The Law Office of Marc D. Shular and our knowledge of family law. You can call us here at The Law Office of Marc D. Shular in order to schedule your initial consultation."),
        ],
        related_default))

    # 14 Asset division
    pages.append(service_page(
        "asset-division-discovering-hidden-assets-san-diego",
        "Finding Hidden Assets after Divorce | Property Attorney San Diego",
        "Asset division and discovering hidden assets in San Diego. We identify, value and fairly divide marital assets and hidden accounts.",
        "Asset Division and Discovering Hidden Assets",
        "Law Office of Marc D. Shular wants to be your guide for your Asset Division and Discovering Hidden Assets case in San Diego.",
        [
            ("p", "Dividing marital property can be one of the most complicated parts of a divorce, especially when one spouse tries to conceal assets. Our team has the accounting and legal experience to identify retirement investments, real estate, hidden accounts, business valuations and other assets that belong in the marital estate."),
            ("p", "Mr. Shular is licensed to practice accounting as a Certified Public Accountant and has been appointed as a special master to help the Court resolve complicated issues such as division of community property or computation of an equalization payment."),
            ("callout", "<strong>Let us be your guides!</strong> Law Office of Marc D. Shular wants to be your guide for your Asset division and Discovering Hidden Assets Services case in San Diego. We have the experience to help you, and we will put our over 25 years to work for you. Give us a call today at (858) 212-0052."),
        ],
        related_default))

    # 15 Domestic violence San Diego
    pages.append(service_page(
        "domestic-violence-attorney-san-diego-ca",
        "Domestic Violence Attorney in San Diego | Marc Shular Law",
        "Domestic violence attorney in San Diego, CA. Compassionate, personalized representation with over 25 years of experience.",
        "Domestic Violence Attorney San Diego, CA",
        "The stakes are so high in Domestic Violence cases, they are seldom simple and straightforward.",
        [
            ("p", "Family Law is not just what we practice here at The Law Office of Marc D. Shular; it is who we are. Because of this, the San Diego, CA County community has an advocate in matters of Domestic Violence cases unlike any other. The stakes are so high in Domestic Violence cases, they are seldom simple and straightforward. Marc Shular has over 25 years as an experienced domestic violence attorney."),
            ("p", "Because The Law Office of Marc D. Shular puts the needs of our clients first, we are never intimidated during Domestic Violence disputes, nor does our San Diego, CA County firm back down in the face of opposition. We make every viable effort to see that the statutes of law and Domestic Violence case precedents are upheld, so justice can prevail."),
            ("p", "We believe each client comes with a unique set of circumstances and requires customized professional legal representation by recognizing these distinctive needs. We personalize our services within a sensitive environment with compassion and understanding."),
        ],
        related_default))

    # 16 Contested / uncontested
    pages.append(service_page(
        "contested-uncontested-divorce",
        "Contested and Uncontested Divorce in San Diego | Marc Shular Law",
        "Contested and uncontested divorce in San Diego, CA. Support whether your divorce is amicable or heavily disputed.",
        "Contested and Uncontested Divorce",
        "Let The Law Office of Marc D. Shular give you the legal support that you need and deserve.",
        [
            ("p", "Let The Law Office of Marc D. Shular, in the San Diego, CA area give you the legal support that you need and deserve. No matter how difficult your Uncontested Divorce matter might be, our many years of experience in the field allows us to put our knowledge to work for you and together we can come up with a plan that we can both get behind."),
            ("p", "At The Law Office of Marc D. Shular we know you live a busy life and do not have an abundance of free time to discuss your Uncontested Divorce case. For many Uncontested Divorce cases within the San Diego, CA area there is a variety of property types to value before they can be divided. We recognize the value of reducing stress by helping our clients work toward the more harmonious type of outcome whenever possible."),
            ("p", "At The Law Office of Marc D. Shular, we are the legal professionals who possess the knowledge that can be immensely beneficial to you, regardless of your Uncontested Divorce situation. In most Uncontested Divorce proceedings, knowledge is power to the powerless. Therefore, it is imperative to seek reasonable, dependable Uncontested Divorce counsel within the San Diego, CA area during the early stages of your concerns."),
            ("callout", "Give The Law Office of Marc D. Shular the chance to exceed your expectations. With regards to Uncontested Divorce disputes, you have everything to gain by contacting our law office. We are confident that after your initial consultation, you will immediately ascertain the benefits of choosing The Law Office of Marc D. Shular in San Diego, CA."),
        ],
        related_default))

    # 17 Prenuptial agreements
    pages.append(service_page(
        "prenuptial-agreements",
        "Prenuptial Agreement San Diego | Prenuptial Agreement California",
        "Prenuptial agreement attorney in San Diego, CA. Carefully drafted prenuptial and post-marital agreements that protect your interests.",
        "Prenuptial Agreement in San Diego CA",
        "Every prenuptial agreement is unique and the number and length of sessions may vary from case-to-case.",
        [
            ("p", "At Law Office of Marc D. Shular, we work hard to break false images of the profession and create an atmosphere of integrity and respect for our clients. We have built a strong record over our over 25 years history practicing Prenuptial Agreements law. Each prenuptial agreement is unique and the number and length of mediation sessions may vary from case-to-case. At Law Office of Marc D. Shular, we have a strong reputation within the San Diego legal community."),
            ("p", "At Law Office of Marc D. Shular, our Prenuptial Agreements representation ensures we will never settle for less than full compensation for you. While it is the decision of the client in San Diego whether to accept a settlement, we are fully prepared to take your case to trial. Dealing with insurance companies, negligent corporations, or individuals can be stressful for San Diego area clients; hiring Law Office of Marc D. Shular for your Prenuptial Agreements representation is the best way to fight back against what is often an inhuman system."),
            ("p", "At Law Office of Marc D. Shular, we take pride in being able to provide our unmatched services to our clients throughout the San Diego area. With the nature of Prenuptial Agreements cases, we know it can be difficult to handle these issues without proper legal representation. If you are looking for Prenuptial Agreements advice in the San Diego area, Law Office of Marc D. Shular can help."),
            ("callout", "<strong>Give us a call today!</strong> At Law Office of Marc D. Shular, we hope that you will trust us even if you consider your Prenuptial Agreements case to be out of this world tough. Give us a call at (858) 212-0052 today and see why we have so many clients throughout San Diego."),
        ],
        related_default))

    # 18 Legal separation & annulments (WORD FOR WORD)
    ls_blocks = [
        ("p", "Most Legal Separation situations are emotionally draining, but with over over 25 years of practice, The Law Office of Marc D. Shular has learned that marriages involving abuse make for the hardest divorce cases. This sense of commonality helps us with our Legal Separation services because we can get many different views of your case in San Diego."),
        ("p", "Many people within the San Diego area decide to have a Legal Separation matter happen later on in life for various reasons. In addition to addressing a client\u2019s legal rights, Law Office of Marc D. Shular understands that representation is about managing ones expectations during this process. Clients naturally have different emotions in Legal Separation cases, but it\u2019s our job to guide them towards concrete goals."),
        ("p", "In Legal Separation cases, your lawyer will be more than just a legal counselor. A lawyer form Law Office of Marc D. Shular understand that they need to get to know you on a personal level in order to better understand and advise you on your Legal Separation matter. With over 25 years of experience, we trust that our San Diego clients know we can provide them with knowledgeable and trustworthy counsel."),
        ("p", "Trust is a key factor when choosing a Legal Separation attorney in the San Diego area. When you decide to have the Law Office of Marc D. Shular work for you, or represent you in matters of Legal Separation proceedings, you have entered into a relationship of trust. It is a decision that our Legal Separation professionals do not take for granted. For over 25 years we have been building our reputation within the San Diego community. We have a commitment to excellence, and an unmatched standard of Legal Separation legal application."),
        ("callout", "<strong>Let us be your guides!</strong> Law Office of Marc D. Shular, 14282 Suite A Danielson Street, Poway, CA 92064, (858) 212-0052."),
        ("h2", "Call San Diego Annulment Attorney and Marriage Separation Law Firm Now For Free Legal Consultation"),
    ]
    pages.append({
        "path": "legal-separation-annulments-family-divorce-san-diego",
        "title": "Legal Separation San Diego | Legal Separation Attorney San Diego | Separation Agreement California",
        "desc": "Legal separation and annulment lawyer in San Diego. Trusted, knowledgeable counsel for legal separation, annulments and marriage separation agreements.",
        "current": "services",
        "hero_html": page_hero([("Home", "/"), ("Practice Areas", "/family-law-practice/"),
                                ("Annulments and Legal Separation", None)],
                               "Annulments and Legal Separation",
                               "Annulments and Legal Separation Lawyer in San Diego"),
        "body_html": f"""
        <section class="section">
          <div class="container">
            <div class="layout">
              <article class="prose">
                <h2>Annulments and Legal Separation Lawyer in San Diego</h2>
                {blocks_to_html(ls_blocks)}
              </article>
              {sidebar(related_default)}
            </div>
          </div>
        </section>
        {cta_section("Free consultation", "Speak with a San Diego legal separation attorney",
                     "For over 25 years we have been building our reputation within the San Diego community. Call us for a free consultation.")}
        """
    })

    # 19 High net worth divorce
    pages.append(service_page(
        "family-law-practice/high-net-worth-divorce-san-diego",
        "High Net worth Divorce Attorney San Diego | High Net Worth Divorce Lawyers",
        "High asset divorce attorney in San Diego. Sophisticated handling of complex, high-net-worth divorce and business valuations.",
        "High Asset Divorce Attorney in San Diego",
        "We are known for providing honest and effective legal representation throughout the San Diego area.",
        [
            ("p", "We are known for providing honest and effective legal representation throughout the San Diego area. We will devote our over 25 years of experience to your cause. Let one of our team members be your High Asset Divorce attorney in the San Diego area. The Law Office of Marc D. Shular wants you to be our next success story."),
            ("p", "The Law Office of Marc D. Shular is proactive in meeting filing deadlines and other elements of your case in the San Diego area. At The Law Office of Marc D. Shular we drill to the bottom of your expectations and press your goals in your High Asset Divorce case."),
            ("p", "Because The Law Office of Marc D. Shular puts the needs of our clients first, we are never intimidated during High Asset Divorce disputes, nor does our San Diego firm back down in the face of opposition. We make every viable effort to see that the statutes of law and High Asset Divorce case precedents are upheld, so justice can prevail."),
            ("callout", "<strong>Give us a call or stop by today!</strong> When it comes to High Asset Divorce matters in the San Diego area, we at The Law Office of Marc D. Shular want nothing but the best for your family. Do not let the complex process of San Diego area legal systems affect your family. Call us today at (858) 212-0052."),
            ("h2", "The Types Of Cases Our Divorce Law Firm Help High Income Individuals With"),
            ("list", ["Retirement investments like pensions, IRAs, 401ks, Stocks",
                      "Real estate investments", "Hidden accounts", "Motor vehicles",
                      "Collectibles", "Business valuations", "Prenuptial/post marriage agreements", "Debts"]),
            ("h2", "Free Customized Consultation With a San Diego High Net Worth & Asset Divorce Attorneys"),
        ],
        related_default))

    # 20 Divorce litigation & settlement
    pages.append(service_page(
        "divorce-litigation-settlement-san-diego",
        "Divorce Settlement Agreement San Diego | How to File For Divorce in California",
        "Divorce litigation and settlement in San Diego. Strong litigation and skillful settlement negotiation for divorce agreements.",
        "Divorce Settlement Agreement in San Diego, California",
        "We work hard to break false images of the profession and create an atmosphere of integrity and respect for our clients.",
        [
            ("p", "At Law Office of Marc D. Shular, we work hard to break false images of the profession and create an atmosphere of integrity and respect for our clients. We have built a strong record over our over 25 years history practicing Divorce Settlement Agreement law. Each mediation situation is unique and the number and length of mediation sessions may vary from case-to-case. At Law Office of Marc D. Shular, we have a strong reputation within the San Diego legal community."),
            ("p", "At Law Office of Marc D. Shular, we want to provide our San Diego clients with a Divorce Settlement Agreement lawyer that can help them maneuver through the web and get successful results. Throughout our over 25 years of experience, we have seen changes to Divorce Settlement Agreement rules and laws that have affected the way that the process changes. We can help our clients in San Diego adapt to these changes and make sure their Divorce Settlement Agreement process will not be affected."),
            ("p", "At Law Office of Marc D. Shular, we take pride in being able to provide our unmatched services to our clients throughout the San Diego area. With the nature of Divorce Settlement Agreement cases, we know it can be difficult to handle these issues without proper legal representation. If you are looking for Divorce Settlement Agreement advice in the San Diego area, Law Office of Marc D. Shular can help."),
            ("callout", "<strong>Let us be your guides!</strong> Law Office of Marc D. Shular wants to be your guide for your Divorce litigation and Settlement Services case in San Diego. We have the experience to help you, and we will put our over 25 years to work for you. Give us a call today at (858) 212-0052."),
        ],
        related_default))

    # 21 Domestic violence Santee
    pages.append(service_page(
        "domestic-violence-attorney-santee",
        "Domestic Violence Attorney Santee, CA | Marc Shular Law",
        "Domestic violence attorney in Santee, CA. Full-service family law firm with 25 years of relevant case experience.",
        "Domestic Violence Attorney Santee, CA",
        "We bring our experience and compassion to our Santee, CA clients to give them the representation they deserve.",
        [
            ("p", "At The Law Office of Marc D. Shular, we have 25 years of experience working on Domestic Violence cases with clients from all walks of life with all sorts of situations. We bring our experience and compassion to our Santee, CA clients to give them the representation they deserve for their Domestic Violence matter."),
            ("p", "The Law Office of Marc D. Shular, is a full-service family law firm with a focus on helping clients throughout the Santee, CA area. Our Domestic Violence lawyers provide clear and reliable legal guidance and representation based upon 25 years of relevant case experience. Our Santee, CA clients benefit from the knowledge, perspective and excellent professional reputations of our entire Domestic Violence team."),
            ("p", "For almost all Domestic Violence cases in the Santee, CA area, it is better to come to an amicable settlement than to fight through litigation. The Law Office of Marc D. Shular is trained to find a beneficial settlement agreement for our clients and use litigation selectively to pursue settlement goals. Our attorneys have also used alternative dispute resolution over the firm's 25 years of practice."),
            ("callout", "<strong>Give us a call today!</strong> The Santee, CA area court system can be an intimidating and convoluted place. If you and your family are dealing with Domestic Violence matters, look to our professionals at The Law Office of Marc D. Shular for a helping hand. Call The Law Office of Marc D. Shular at (858) 212-0052 for Domestic Violence guidance today."),
        ],
        related_default))

    return pages


# ================================================================ OTHER PAGES
def build_other_pages():
    pages = []
    related_default = [(s, l) for s, l, _ in SERVICES]

    # About
    about_body = f"""
    <section class="section">
      <div class="container">
        <div class="layout">
          <article class="prose">
            <p class="lede">Welcome to Marc Shular Law. Marc Shular specializes in divorce and family law and is dedicated to providing the highest quality legal services to individuals in the San Diego area, Southern California area and beyond. Every effort is made to resolve your case in a prompt manner.</p>
            <h2>Marc D. Shular, Certified Family Law Specialist</h2>
            <div class="split" style="gap:2rem;align-items:flex-start;margin:1.4rem 0">
              <div class="split-media" style="max-width:260px">
                <img src="/images/source/00-about-marc-shular-2.jpg" alt="Marc D. Shular, Certified Family Law Specialist and CPA at Marc Shular Law" width="709" height="399" style="border-radius:16px">
              </div>
              <div class="split-copy">
                <p>Mr. Shular is licensed to practice accounting as a Certified Public Accountant. In addition, Mr. Shular has been appointed to act as a special master to assist the Court resolve complicated issues. A special master is appointed when an issue such as division of community property or computation of an equalization payment, is too complicated and time consuming for the court to handle from the bench. In these situations, the Court will appoint a special master and defers judgment on the issue to a date at which the special master submits a written report.</p>
              </div>
            </div>
            <p>Mr. Shular did his undergraduate work at the New York University and graduated in 1986 with a Bachelor of Science in accounting. He then joined the public accountant firm of Arthur Andersen and Company in New York City as a Certified Public Accountant. Mr. Shular worked for Arthur Anderson and Company for a period of three years and then decided to give law school a try.</p>
            <p>He enrolled at California Western School of Law and worked for Denny Kershek while attending school. After graduation and passing the California State Bar Exam, Mr. Kershek and Mr. Shular formed the partnership.</p>
            <p>We are your number 1 resource for providing the best and most professional legal services related to family law. We will help you every step of the way to make sure that your case has the best chance of success.</p>
            <p>If you have any questions or concerns about divorce or family law in the State of California, do not hesitate to <a href="/contact-us/">contact us here</a>.</p>
          </article>
          {sidebar(related_default)}
        </div>
      </div>
    </section>
    {cta_section("Free consultation", "Meet with Marc Shular",
                 "Schedule your free consultation with a Certified Family Law Specialist today.")}
    """
    pages.append({
        "path": "about",
        "title": "About Marc Shular Law - The #1 Family Law Attorney in California",
        "desc": "Learn about Marc D. Shular, Certified Family Law Specialist and CPA, dedicated to providing the highest quality family law services in San Diego.",
        "current": "about",
        "hero_html": page_hero([("Home", "/"), ("About Marc Shular", None)], "About Marc Shular",
                               "Divorce and family law attorney serving the San Diego area, Southern California and beyond."),
        "body_html": about_body
    })

    # Videos
    def vcard(title, desc):
        return f"""<div class="video-card">
          <div class="thumb"><span class="play" aria-hidden="true"></span></div>
          <div class="vc-body"><h3>{title}</h3><p>{desc}</p>
          <p class="mt-2" style="margin-bottom:0"><a class="card-link" href="{YOUTUBE}" target="_blank" rel="noopener">Watch on YouTube</a></p></div>
        </div>"""
    videos_body = f"""
    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Videos</span>
          <h2>Learn about family law from Marc Shular</h2>
          <p>These videos and many more can be found on our <a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube Channel</a>.</p>
        </div>
        <div class="grid grid-3">
          {vcard("Our Place", "You may have found yourself facing a divorce; in this situation you may need the help of a family law attorney. Marc Shular is a law professional who specializes in handling all kinds of family matters. He offers a free consultation to help you at this time of change.")}
          {vcard("Why I became a lawyer", "Top rated family divorce lawyer in San Diego. Finding the right family divorce lawyer is very important. With over 25 years of experience, the right lawyer can determine your success for the best results.")}
          {vcard("Who are you going to CALL!", "Divorce is usually handled by a divorce lawyer but there is no reason why, if your family lawyer has experience in the field, he cannot help you. He will be looking out for your best interests by getting you your share of property, helping you maintain custody of your children, and working out your alimony.")}
        </div>
        <p class="text-center mt-3"><a class="btn btn-gold" href="{YOUTUBE}" target="_blank" rel="noopener">Visit our YouTube Channel</a></p>
      </div>
    </section>
    {cta_section("Free consultation", "Have questions after watching?",
                 "Call us for a free consultation and let us help you understand your options.")}
    """
    pages.append({
        "path": "published-videos",
        "title": "Video Page for Marc Shular Law | Watch Lawyer Videos to Learn",
        "desc": "Watch Marc Shular Law videos on family law, divorce, custody and more. Find more on our YouTube channel.",
        "current": "videos",
        "hero_html": page_hero([("Home", "/"), ("Videos", None)], "Videos",
                               "Watch and learn more about family law topics from Marc Shular."),
        "body_html": videos_body
    })

    # What to do before
    before_body = f"""
    <section class="section">
      <div class="container">
        <div class="layout">
          <article class="prose">
            <p class="lede">There are some important steps you should take before you get divorced, and before you even file for divorce.</p>
            <h2>What To Do Before Getting Divorced</h2>
            <p>First, you should set up a separate bank account. You want to gather joint financial documents and make copies of everything to bring to your lawyer. This includes account records, mortgages, phone bills, car notes, and anything else. It's also smart to obtain records of all online accounts. Some spouses might make it difficult to access documents if you've already filed for divorce, so it's important to do this preemptively.</p>
            <h3>Determine Custody For When You're Divorced</h3>
            <p>If you have children with your spouse, custody is probably at the front of your mind when getting divorced. Sharing custody is the most likely outcome, so review your work schedule, children's schedule, and your obligations before determining a custody situation.</p>
            <p>If you can come up with an amicable joint custody schedule before you get divorced, you'll be miles ahead of the game.</p>
            <h3>Purchases and Selling Before Divorced</h3>
            <p>Most judges will prohibit spouses from selling, buying, or otherwise disposing of any marital property once your divorce paperwork is filed. Courts do this to prevent spouses from draining the other's bank account, or dissipating the marital estate. So if you've been planning on selling rental property, buying a car, or anything of that nature, you'll be prevented from doing so.</p>
            <p>It's obviously not appropriate to drain bank accounts prior to filing for divorce (that can come back to haunt you), if you have legitimate sales or purchases that has been in the works, it's best to complete those transactions before filing.</p>
            <h3>Don't Act Like You're Single</h3>
            <p>In most jurisdictions, even if your marriage is over prior to being divorced, it's important not to live with another romantic partner. This is still considered adultery in most states. Additionally, a judge could consider money you've spent on a romantic partner as dissipating from the marital estate prior to being divorced, and could order you to reimburse your spouse for those expenditures.</p>
            <p>So, in order to figure out your financial goals when divorced, it's important to have an accurate assets and debts balance sheet. It might be necessary to hire an accountant for this. Include real property, cars, retirement accounts, bank accounts, other assets, mortgages, credit cards, and debts in this balance sheet. Determining your total assets can help you set a budget for how much to spend on an attorney, and will help give you an accurate picture of your financial goals.</p>
            <p>Finally, talk to an attorney about joint bank accounts and credit cards for when you're divorced. You don't want to be in a situation where your spouse can run up bills in your name or drain your bank accounts. Interview attorneys who are within your budget. Marc Shular has years of experience in these matters, and can help you with a balance sheet, with planning for the future, custody, and all other manner of divorce issues. Call today if you have any questions or concerns regarding your divorce.</p>
          </article>
          {sidebar(related_default)}
        </div>
      </div>
    </section>
    {cta_section("Free consultation", "Planning a divorce? Get advice first.",
                 "Talk to Marc Shular before you file. We can help you protect your interests from the start.")}
    """
    pages.append({
        "path": "what-to-do-before-being-divorced",
        "title": "What To Do Before Being Divorced - Marc Shular Law",
        "desc": "Important steps to take before you get divorced or file for divorce, from San Diego family law attorney Marc Shular.",
        "current": "about",
        "hero_html": page_hero([("Home", "/"), ("About Marc Shular", "/about/"), ("What To Do Before Being Divorced", None)],
                               "What To Do Before Being Divorced",
                               "Guidance on the steps to take before you file for divorce."),
        "body_html": before_body
    })

    # What to do after
    after_body = f"""
    <section class="section">
      <div class="container">
        <div class="layout">
          <article class="prose">
            <p class="lede">After being divorced, don't expect your ex to be reasonable &mdash; focus on yourself and your future.</p>
            <h2>What To Do After Being Divorced</h2>
            <p>After being divorced, don't expect your ex to be reasonable. Many divorces end amicably, but just as many end in ugliness. It's important to remember that you can only control your own actions, so don't keep your expectations too high. Focus on yourself. That being said, don't go trying to hook up with your ex. This can make things even worse (and often does), which could lead to a disruption of the child custody schedule, more alimony, or a host of other things. It's important to move on.</p>
            <h3>Go to Counseling</h3>
            <p>Not going to therapy or counseling is often a mistake. Being divorced is a traumatic event. Don't try to be hard as steel &mdash; if you didn't like your last therapist, find a new one. The important thing is to find someone you trust, so that you can work on yourself and heal the wounds gathered from being divorced.</p>
            <p>In the same boat as counseling and working on yourself, absolutely don't speak badly of your spouse on social media. This can also come to bite you. The whole world sees what goes on Facebook and Twitter and such, and those posts can come back to haunt you in more legal problems. It will do you no good to air out your dirty laundry, and can easily do a lot worse for your divorce case.</p>
            <h3>Don't Isolate Yourself</h3>
            <p>Reach out to your friends and family, even if they're married. Just because you no longer are, doesn't mean you should cut off all married couples from your life. Seeing the happiness other people has just might help spark a new outlook on marriage. Staying alone can lead to more misery, and misery can lead to depression. These are all things to talk about with your counselor after being divorced.</p>
            <h3>Have a Plan for Future Dates</h3>
            <p>Every married or once-married person must realize their role in their failed marriage. It's never a one-way street. For the next chapter in your life, make sure you realize your part in your first failed attempt, what led to being divorced, and you'll have a greater chance of not repeating the same mistakes, or ending up with the wrong person.</p>
            <p>Speak with your lawyer if you need help finding proper counseling or therapy. Marc Shular can help you rise above your woes, and ultimately you might have a new lease on life. Let Marc Shular Law aid you in turning a new page after being divorced, so that you can live a happy life again. Call today if you have any questions regarding divorce or post-divorce concerns.</p>
          </article>
          {sidebar(related_default)}
        </div>
      </div>
    </section>
    {cta_section("Free consultation", "Moving on after divorce? We can help.",
                 "Call Marc Shular Law today with any questions regarding divorce or post-divorce concerns.")}
    """
    pages.append({
        "path": "what-to-do-after-being-divorced",
        "title": "What To Do After Being Divorced | Marc Shular Law",
        "desc": "What to do after being divorced: counseling, support and planning for the future, from San Diego family law attorney Marc Shular.",
        "current": "about",
        "hero_html": page_hero([("Home", "/"), ("About Marc Shular", "/about/"), ("What To Do After Being Divorced", None)],
                               "What To Do After Being Divorced",
                               "Practical guidance for the chapter that follows your divorce."),
        "body_html": after_body
    })

    return pages


# ================================================================ CONTACT + LEGAL
def build_contact_and_legal():
    pages = []

    # Contact
    contact_body = f"""
    <section class="section">
      <div class="container">
        <div class="contact-grid">
          <div class="contact-card">
            <div class="ic">{ico('phone')}</div>
            <h3>By Phone</h3>
            <p><a href="{PHONE_HREF}">{PHONE}</a><br>Alternate: <a href="tel:+18582120052">{PHONE2}</a></p>
          </div>
          <div class="contact-card">
            <div class="ic">{ico('mail')}</div>
            <h3>By Email</h3>
            <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          </div>
          <div class="contact-card">
            <div class="ic">{ico('briefcase')}</div>
            <h3>By Fax</h3>
            <p>{FAX}</p>
          </div>
        </div>

        <h2 class="mt-3">Our Offices</h2>
        <div class="office-grid mt-2">
          <div class="office-card">
            <span class="tag">Main Office &middot; Poway Location</span>
            <h3>Poway, CA</h3>
            <address>14282 Danielson Street Suite A,<br>Poway, CA 92064</address>
          </div>
          <div class="office-card">
            <span class="tag">Rancho Santa Fe Location</span>
            <h3>Rancho Santa Fe, CA</h3>
            <address>16236 San Dieguito Rd Suite 5-16,<br>Rancho Santa Fe, CA 92091</address>
          </div>
        </div>
      </div>
    </section>
    {cta_section("Contact", "Send us a message",
                 "The use of this form does not establish an attorney-client relationship. Confidential or time-sensitive information should not be sent through this form.")}
    """
    pages.append({
        "path": "contact-us",
        "title": "Contact Marc Shular Law | San Diego Family Law Attorney",
        "desc": "Contact Marc Shular Law in Poway and Rancho Santa Fe, CA. Call (619) 743-9499 or email office@marcshularlaw.com for a free family law consultation.",
        "current": "contact",
        "hero_html": page_hero([("Home", "/"), ("Contact Us", None)], "Contact Us",
                               "Reach out by phone, email or the form below. Free consultation available."),
        "body_html": contact_body
    })

    # Privacy Policy (word for word from source)
    privacy = """
    <section class="section"><div class="container container-narrow"><div class="legal-body">
      <p>At Marc Shular Law, accessible from www.marcshularlaw.com, one of our main priorities is the privacy of our visitors. This Privacy Policy document contains types of information that is collected and recorded by Marc Shular Law and how we use it.</p>
      <p>If you have additional questions or require more information about our Privacy Policy, do not hesitate to contact us through email at contact@marcshularlaw.com</p>
      <h2>GDPR Information</h2>
      <p>Contacting Us: you can contact us at www.marcshularlaw.com/contact-us</p>
      <p>What information we collect from users: cookie information about your visit and your email if you complete any optin forms on our site.</p>
      <p>When we collect information from users: when you visit our website or sign up via an optin form.</p>
      <p>Protection of that information: all information is securely stored and only accessible to relevant staff members in the execution of their tasks.</p>
      <p>What we do with that information: we use cookies to enhance your visit, remember if you are logged in and to collect visit analytics.</p>
      <p>Data Protection Officer: Marc Shular</p>
      <h2>General Data Protection Regulation (GDPR)</h2>
      <p>We are a Data Controller of your information.</p>
      <p>Marc Shular Law legal basis for collecting and using the personal information described in this Privacy Policy depends on the Personal Information we collect and the specific context in which we collect the information:</p>
      <ul>
        <li>Marc Shular Law needs to perform a contract with you</li>
        <li>You have given Marc Shular Law permission to do so</li>
        <li>Processing your personal information is in Marc Shular Law legitimate interests</li>
        <li>Marc Shular Law needs to comply with the law</li>
      </ul>
      <p>Marc Shular Law will retain your personal information only for as long as is necessary for the purposes set out in this Privacy Policy. We will retain and use your information to the extent necessary to comply with our legal obligations, resolve disputes, and enforce our policies.</p>
      <p>If you are a resident of the European Economic Area (EEA), you have certain data protection rights. If you wish to be informed what Personal Information we hold about you and if you want it to be removed from our systems, please contact us.</p>
      <p>In certain circumstances, you have the following data protection rights:</p>
      <ul>
        <li>The right to access, update or to delete the information we have on you.</li>
        <li>The right of rectification.</li>
        <li>The right to object.</li>
        <li>The right of restriction.</li>
        <li>The right to data portability</li>
        <li>The right to withdraw consent</li>
      </ul>
      <h2>Log Files</h2>
      <p>Marc Shular Law follows a standard procedure of using log files. These files log visitors when they visit websites. All hosting companies do this and a part of hosting services' analytics. The information collected by log files include internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date and time stamp, referring/exit pages, and possibly the number of clicks. These are not linked to any information that is personally identifiable. The purpose of the information is for analyzing trends, administering the site, tracking users' movement on the website, and gathering demographic information.</p>
      <h2>Cookies and Web Beacons</h2>
      <p>Like any other website, Marc Shular Law uses 'cookies'. These cookies are used to store information including visitors' preferences, and the pages on the website that the visitor accessed or visited. The information is used to optimize the users' experience by customizing our web page content based on visitors' browser type and/or other information.</p>
      <h2>Privacy Policies</h2>
      <p>You may consult this list to find the Privacy Policy for each of the advertising partners of Marc Shular Law.</p>
      <p>Third-party ad servers or ad networks uses technologies like cookies, JavaScript, or Web Beacons that are used in their respective advertisements and links that appear on Marc Shular Law, which are sent directly to users' browser. They automatically receive your IP address when this occurs. These technologies are used to measure the effectiveness of their advertising campaigns and/or to personalize the advertising content that you see on websites that you visit.</p>
      <p>Note that Marc Shular Law has no access to or control over these cookies that are used by third-party advertisers.</p>
      <h2>Third Party Privacy Policies</h2>
      <p>Marc Shular Law's Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to consult the respective Privacy Policies of these third-party ad servers for more detailed information. It may include their practices and instructions about how to opt-out of certain options. You may find a complete list of these Privacy Policies and their links here: Privacy Policy Links.</p>
      <p>You can choose to disable cookies through your individual browser options. To know more detailed information about cookie management with specific web browsers, it can be found at the browsers' respective websites. What Are Cookies?</p>
      <h2>Children's Information</h2>
      <p>Another part of our priority is adding protection for children while using the internet. We encourage parents and guardians to observe, participate in, and/or monitor and guide their online activity.</p>
      <p>Marc Shular Law does not knowingly collect any Personal Identifiable Information from children under the age of 13. If you think that your child provided this kind of information on our website, we strongly encourage you to contact us immediately and we will do our best efforts to promptly remove such information from our records.</p>
      <h2>Online Privacy Policy Only</h2>
      <p>This privacy policy applies only to our online activities and is valid for visitors to our website with regards to the information that they shared and/or collect in Marc Shular Law. This policy is not applicable to any information collected offline or via channels other than this website.</p>
      <h2>Consent</h2>
      <p>By using our website, you hereby consent to our Privacy Policy and agree to its terms.</p>
    </div></div></section>
    """
    pages.append({
        "path": "privacy-policy",
        "title": "Privacy Policy | Marc Shular Law",
        "desc": "Privacy Policy for Marc Shular Law, including GDPR information, cookies, log files and children's information.",
        "current": "", "hero_html": page_hero([("Home", "/"), ("Privacy Policy", None)], "Privacy Policy"),
        "body_html": privacy
    })

    # Cookie Policy
    cookie = """
    <section class="section"><div class="container container-narrow"><div class="legal-body">
      <p>This is the Cookie Policy for Marc Shular Law, accessible from www.marcshularlaw.com</p>
      <h2>What Are Cookies</h2>
      <p>As is common practice with almost all professional websites this site uses cookies, which are tiny files that are downloaded to your computer, to improve your experience. This page describes what information they gather, how we use it and why we sometimes need to store these cookies. We will also share how you can prevent these cookies from being stored however this may downgrade or 'break' certain elements of the sites functionality.</p>
      <p>For more general information on cookies see the Wikipedia article on HTTP Cookies.</p>
      <h2>How We Use Cookies</h2>
      <p>We use cookies for a variety of reasons detailed below. Unfortunately in most cases there are no industry standard options for disabling cookies without completely disabling the functionality and features they add to this site. It is recommended that you leave on all cookies if you are not sure whether you need them or not in case they are used to provide a service that you use.</p>
      <h2>Disabling Cookies</h2>
      <p>You can prevent the setting of cookies by adjusting the settings on your browser (see your browser Help for how to do this). Be aware that disabling cookies will affect the functionality of this and many other websites that you visit. Disabling cookies will usually result in also disabling certain functionality and features of this site. Therefore it is recommended that you do not disable cookies.</p>
      <h2>The Cookies We Set</h2>
      <ul>
        <li>Site preferences cookies</li>
      </ul>
      <p>In order to provide you with a great experience on this site we provide the functionality to set your preferences for how this site runs when you use it. In order to remember your preferences we need to set cookies so that this information can be called whenever you interact with a page is affected by your preferences.</p>
      <h2>Third Party Cookies</h2>
      <p>In some special cases we also use cookies provided by trusted third parties. The following section details which third party cookies you might encounter through this site.</p>
      <h2>More Information</h2>
      <p>Hopefully that has clarified things for you and as was previously mentioned if there is something that you aren't sure whether you need or not it's usually safer to leave cookies enabled in case it does interact with one of the features you use on our site.</p>
      <p>However if you are still looking for more information then you can contact us through one of our preferred contact methods:</p>
      <ul>
        <li>Email: contact@marcshularlaw.com</li>
      </ul>
    </div></div></section>
    """
    pages.append({
        "path": "cookie-policy",
        "title": "Cookie Policy | Marc Shular Law",
        "desc": "Cookie Policy for Marc Shular Law explaining what cookies are, how we use them and how you can disable them.",
        "current": "", "hero_html": page_hero([("Home", "/"), ("Cookie Policy", None)], "Cookie Policy"),
        "body_html": cookie
    })

    # Terms & Conditions
    terms = """
    <section class="section"><div class="container container-narrow"><div class="legal-body">
      <h2>Introduction</h2>
      <p>These Website Standard Terms and Conditions written on this webpage shall manage your use of our website, Marc Shular Law accessible at www.marcshularlaw.com.</p>
      <p>These Terms will be applied fully and affect to your use of this Website. By using this Website, you agreed to accept all terms and conditions written in here. You must not use this Website if you disagree with any of these Website Standard Terms and Conditions.</p>
      <p>Minors or people below 18 years old are not allowed to use this Website.</p>
      <h2>Intellectual Property Rights</h2>
      <p>Other than the content you own, under these Terms, Marc Shular Law and/or its licensors own all the intellectual property rights and materials contained in this Website.</p>
      <p>You are granted limited license only for purposes of viewing the material contained on this Website.</p>
      <h2>Restrictions</h2>
      <p>You are specifically restricted from all of the following:</p>
      <ul>
        <li>publishing any Website material in any other media;</li>
        <li>selling, sublicensing and/or otherwise commercializing any Website material;</li>
        <li>publicly performing and/or showing any Website material;</li>
        <li>using this Website in any way that is or may be damaging to this Website;</li>
        <li>using this Website in any way that impacts user access to this Website;</li>
        <li>using this Website contrary to applicable laws and regulations, or in any way may cause harm to the Website, or to any person or business entity;</li>
        <li>engaging in any data mining, data harvesting, data extracting or any other similar activity in relation to this Website;</li>
        <li>using this Website to engage in any advertising or marketing.</li>
      </ul>
      <p>Certain areas of this Website are restricted from being access by you and Marc Shular Law may further restrict access by you to any areas of this Website, at any time, in absolute discretion. Any user ID and password you may have for this Website are confidential and you must maintain confidentiality as well.</p>
      <h2>Your Content</h2>
      <p>In these Website Standard Terms and Conditions, "Your Content" shall mean any audio, video text, images or other material you choose to display on this Website. By displaying Your Content, you grant Marc Shular Law a non-exclusive, worldwide irrevocable, sub licensable license to use, reproduce, adapt, publish, translate and distribute it in any and all media.</p>
      <p>Your Content must be your own and must not be invading any third-party's rights. Marc Shular Law reserves the right to remove any of Your Content from this Website at any time without notice.</p>
      <h2>No warranties</h2>
      <p>This Website is provided "as is," with all faults, and Marc Shular Law express no representations or warranties, of any kind related to this Website or the materials contained on this Website. Also, nothing contained on this Website shall be interpreted as advising you.</p>
      <h2>Limitation of liability</h2>
      <p>In no event shall Marc Shular Law, nor any of its officers, directors and employees, shall be held liable for anything arising out of or in any way connected with your use of this Website whether such liability is under contract. Marc Shular Law, including its officers, directors and employees shall not be held liable for any indirect, consequential or special liability arising out of or in any way related to your use of this Website.</p>
      <h2>Indemnification</h2>
      <p>You hereby indemnify to the fullest extent Marc Shular Law from and against any and/or all liabilities, costs, demands, causes of action, damages and expenses arising in any way related to your breach of any of the provisions of these Terms.</p>
      <h2>Severability</h2>
      <p>If any provision of these Terms is found to be invalid under any applicable law, such provisions shall be deleted without affecting the remaining provisions herein.</p>
      <h2>Variation of Terms</h2>
      <p>Marc Shular Law is permitted to revise these Terms at any time as it sees fit, and by using this Website you are expected to review these Terms on a regular basis.</p>
      <h2>Assignment</h2>
      <p>The Marc Shular Law is allowed to assign, transfer, and subcontract its rights and/or obligations under these Terms without any notification. However, you are not allowed to assign, transfer, or subcontract any of your rights and/or obligations under these Terms.</p>
      <h2>Entire Agreement</h2>
      <p>These Terms constitute the entire agreement between Marc Shular Law and you in relation to your use of this Website, and supersede all prior agreements and understandings.</p>
      <h2>Governing Law &amp; Jurisdiction</h2>
      <p>These Terms will be governed by and interpreted in accordance with the laws of 14282 Danielson Street Suite A, Poway, CA 92064, and you submit to the non-exclusive jurisdiction of the state and federal courts located there for the resolution of any disputes.</p>
    </div></div></section>
    """
    pages.append({
        "path": "terms-of-services",
        "title": "Terms and Conditions | Marc Shular Law",
        "desc": "Website Standard Terms and Conditions for Marc Shular Law, including intellectual property, restrictions and liability.",
        "current": "", "hero_html": page_hero([("Home", "/"), ("Terms & Conditions", None)], "Terms & Conditions"),
        "body_html": terms
    })

    # Data request
    data_request = f"""
    <section class="section"><div class="container container-narrow">
      <div class="legal-body">
        <p>Using the form below you can request all data that is stored about you in our application/website to be sent to you via email. After submitting your email address, we will collect all data based on your email address and IP address and send it to the email address you submitted.</p>
      </div>
      <div class="form-card mt-3">{lead_form("Data request", "Request your data", "Enter the email address associated with your data and we will send a copy to that address.")}</div>
    </div></section>
    """
    pages.append({
        "path": "data-request",
        "title": "Data Request | Marc Shular Law",
        "desc": "Request all data stored about you in our application/website to be sent to you via email.",
        "current": "", "hero_html": page_hero([("Home", "/"), ("Data Request", None)], "Data Request"),
        "body_html": data_request
    })

    # Data erasure
    data_erasure = f"""
    <section class="section"><div class="container container-narrow">
      <div class="legal-body">
        <p>Using the form below you can request all data that is stored about you in our application to be deleted from our database. Please note that we do not store any backups of this data so deletion is final and irreversible. As soon as your data is deleted, an email will be sent to your submitted email address. Please make sure you want to delete your information because there is no confirmation dialog after you send your email address.</p>
      </div>
      <div class="form-card mt-3">{lead_form("Data erasure", "Request data erasure", "Enter your email address to permanently delete the data we store about you.")}</div>
    </div></section>
    """
    pages.append({
        "path": "data-erasure",
        "title": "Data Erasure | Marc Shular Law",
        "desc": "Request all data stored about you in our application to be permanently deleted from our database.",
        "current": "", "hero_html": page_hero([("Home", "/"), ("Data Erasure", None)], "Data Erasure"),
        "body_html": data_erasure
    })

    return pages


def main():
    all_pages = [build_home()]
    all_pages += build_service_pages()
    all_pages += build_other_pages()
    all_pages += build_contact_and_legal()
    count = 0
    for p in all_pages:
        write_page(p["path"], layout(p))
        count += 1
    print("Wrote %d pages" % count)


if __name__ == "__main__":
    main()
