import json, os, datetime
from guides_extra import EXTRA_GUIDES
SITE="GigMath"; URL="https://kaysonline1.github.io/gigmath"
NAV=[("/index.html","Home"),("/tools/index.html","Tools"),("/guides/index.html","Guides"),("/free-download.html","Free Log"),("/pro.html","Pro Kit"),("/about.html","About")]
GA='''<!-- ANALYTICS (free). Option A GoatCounter: create free account at goatcounter.com, pick a code, then uncomment:
<script data-goatcounter="https://YOURCODE.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
Option B Cloudflare Web Analytics (free): dash.cloudflare.com > Analytics > Web Analytics > add site, paste the beacon snippet here. -->'''
def page(path,title,desc,body,faqs=None):
    pre="../"*path.count("/")
    nav="".join(f'<a href="{pre}{h[1:]}">{t}</a>' for h,t in NAV)
    faq_html=""
    schema=""
    if faqs:
        faq_html="<h2>Common questions</h2>"+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)
        ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
        schema='<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+"</script>"
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="google-site-verification" content="KAWCMBSbq604hMIWI6Tml4BGcNKZZ-RXAt_9gTeH3hY" />
<title>{title} | {SITE}</title><meta name="description" content="{desc}"><link rel="canonical" href="{URL}/{path}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{URL}/{path}">
{schema}
<link rel="stylesheet" href="{pre}assets/style.css">{GA}</head><body>
<header><div class="wrap"><a class="logo" href="{pre}index.html">Gig<b>Math</b></a><nav>{nav}</nav></div></header>
<main class="wrap">{body}{faq_html}</main>
<footer><div class="wrap"><p><a href="{pre}privacy.html">Privacy</a> · <a href="{pre}terms.html">Terms</a> · <a href="{pre}disclosure.html">Affiliate Disclosure</a> · <a href="{pre}about.html">About/Contact</a></p>
<p class="small">Estimates for education only, not tax, legal, or financial advice. © {datetime.date.today().year} {SITE}, Phoenix, AZ.</p></div></footer>
<script src="{pre}assets/calc.js"></script><script src="{pre}assets/ui.js"></script></body></html>'''
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True); open(path,"w").write(html)
def f(id,label,val,step="any"): return f'<label>{label}<input type="number" id="{id}" value="{val}" step="{step}"></label>'
AFF='<div class="aff"><b>Recommended:</b> {name} — <a href="#AFFILIATE-PLACEHOLDER" rel="sponsored nofollow">{cta}</a> <span class="small">[PLACEHOLDER: apply to {prog}; replace link only after approval]</span></div>'
TOOLS=[
("gig-driver-profit-calculator","Gig Driver Profit Per Hour Calculator","Find your real DoorDash, Uber, Instacart, or Lyft profit per hour and per mile after gas and car wear.","gig",
 f("pay","Platform pay ($)",150)+f("tips","Tips ($)",50)+f("fees","Fees/other deductions ($)",0)+f("miles","Miles driven",100)+f("mpg","Vehicle MPG",25)+f("gas","Gas price ($/gal)",4)+f("wear","Wear & tear ($/mile)",0.10)+f("other","Other costs ($)",0)+f("hours","Online hours (incl. waiting)",8),
 AFF.format(name="Everlance mileage tracker",cta="Track miles automatically",prog="Everlance affiliate program via Impact (free)")),
("mileage-deduction-calculator","Mileage Tax Deduction Calculator (2026)","Estimate your 2026 IRS standard mileage deduction and approximate tax savings for 1099 gig and freelance driving.","mile",
 f("miles","Business miles",10000)+f("rate","IRS business rate ($/mile). 2026: 0.725 through June 30, 0.76 from July 1",0.76)+f("tolls","Business tolls & parking ($)",50)+f("taxRate","Combined tax rate (decimal, e.g. 0.25)",0.25),
 AFF.format(name="Everlance",cta="Log every deductible mile",prog="Everlance affiliate program via Impact (free)")),
("self-employment-tax-calculator","1099 Self-Employment Tax & Quarterly Estimate Calculator","Estimate 2026 self-employment tax (15.3% on 92.35% of profit), income tax set-aside, and quarterly estimated payments.","se",
 f("profit","Net self-employment profit ($)",30000)+f("w2","W-2 wages this year ($)",0)+f("incomePct","Your income tax rate estimate (%)",12),
 AFF.format(name="FreshBooks (accounting for freelancers)",cta="Try FreshBooks free",prog="FreshBooks via PartnerStack (free)")),
("freelance-hourly-rate-calculator","Freelance Hourly Rate Calculator","Work out the hourly and day rate you need as a freelancer to hit your take-home income goal after taxes and expenses.","rate",
 f("income","Desired take-home income ($/yr)",60000)+f("expenses","Business expenses ($/yr)",6000)+f("hoursWeek","Billable hours per week",25)+f("weeks","Working weeks per year",46)+f("taxPct","Tax set-aside (%)",25),
 AFF.format(name="FreshBooks",cta="Send invoices & track time",prog="FreshBooks via PartnerStack (free)")),
("earnings-goal-calculator","Side Hustle Earnings Goal Calculator","How many hours do you need to drive or freelance to hit a weekly or monthly money goal?","goal",
 f("goal","Money goal ($)",1000)+f("perHour","Your real net $/hour",25)+f("daysWeek","Days you can work",5),
 AFF.format(name="Gigaverse app (gig tax & mileage)",cta="See the app",prog="Gigaverse affiliate program (free, gigaverse.ai/affiliate-program)")),
]
for slug,title,desc,kind,inputs,aff in TOOLS:
    body=f'''<h1>{title}</h1><p class="lead">{desc}</p><div class="tool" data-tool="{kind}"><div class="grid">{inputs}</div>
<button class="btn" type="button" onclick="runTool()">Calculate</button><div id="out" class="out" aria-live="polite"></div></div>{aff}
<h2>How it works</h2><p>All math runs in your browser; nothing you type is sent anywhere. Figures are estimates — tax rules change yearly, so confirm with <a href="https://www.irs.gov/businesses/small-businesses-self-employed/self-employed-individuals-tax-center" rel="noopener">IRS.gov</a> or a tax professional.</p>
<p>Want to track this every week? <a href="../free-download.html">Get the free printable mileage &amp; earnings log</a>.</p>'''
    page(f"tools/{slug}.html",title,desc,body)
# invoice tool
inv='''<h1>Free Invoice Generator for Freelancers</h1><p class="lead">Create a clean invoice, then print or save as PDF. No signup, no data leaves your browser.</p>
<div class="tool" data-tool="invoice"><div class="grid"><label>From (your name)<input id="from" value="Kasen Example"></label><label>Bill to<input id="to" value="Client LLC"></label>
<label>Invoice #<input id="num" value="1001"></label><label>Tax (%)<input type="number" id="taxPct" value="8"></label><label>Discount ($)<input type="number" id="discount" value="50"></label></div>
<table id="items"><thead><tr><th>Description</th><th>Qty</th><th>Rate</th></tr></thead><tbody>
<tr><td><input value="Design work"></td><td><input type="number" value="2"></td><td><input type="number" value="100"></td></tr>
<tr><td><input value="Revisions"></td><td><input type="number" value="3"></td><td><input type="number" value="50"></td></tr></tbody></table>
<button class="btn" type="button" onclick="addRow()">+ Line</button> <button class="btn" type="button" onclick="runTool()">Calculate</button> <button class="btn alt" type="button" onclick="window.print()">Print / Save PDF</button>
<div id="out" class="out"></div></div>'''+AFF.format(name="FreshBooks",cta="Automate invoices & reminders",prog="FreshBooks via PartnerStack (free)")
page("tools/invoice-generator.html","Free Invoice Generator","Free printable invoice generator for freelancers and gig workers. No signup, works offline in your browser.",inv)
ALLT=[(s,t,d) for s,t,d,*_ in TOOLS]+[("invoice-generator","Free Invoice Generator","Make and print a professional invoice in seconds.")]
cards="".join(f'<a class="card" href="tools/{s}.html"><h3>{t}</h3><p>{d}</p></a>' for s,t,d in ALLT)
GUIDES=[("how-much-do-gig-drivers-really-make","How Much Do Gig Drivers Really Make After Expenses?","Learn how to calculate true gig driver earnings after gas, wear and tear, and taxes, with a worked example.",
"""<p>The number in your delivery app is <b>gross pay</b>. Your real income is what's left after fuel, vehicle wear, fees, and taxes — and after counting <i>all</i> the hours you were online, including waiting.</p>
<h2>The formula</h2><p>Net profit = pay + tips − fees − fuel − wear − other costs. Fuel = miles ÷ MPG × gas price. Per hour = net ÷ online hours.</p>
<h2>Worked example</h2><p>$150 pay + $50 tips, 100 miles at 25 MPG and $4 gas ($16 fuel), $0.10/mile wear ($10): net $174 over 8 hours = <b>$21.75/hour</b>, $1.74/mile — before taxes.</p>
<h2>Don't forget taxes</h2><p>As a 1099 contractor you owe self-employment tax (15.3% on 92.35% of net profit) once net earnings reach $400, per the IRS. Use our <a href="../tools/self-employment-tax-calculator.html">self-employment tax calculator</a>.</p>
<p>Run your own numbers with the <a href="../tools/gig-driver-profit-calculator.html">gig driver profit calculator</a>.</p>"""),
("mileage-deduction-guide-2026","Mileage Deduction for Gig Workers: 2026 Guide","How the IRS standard mileage deduction works for DoorDash, Uber and freelance drivers in 2026, and how to keep a compliant log.",
"""<p>If you drive for work as an independent contractor, the standard mileage deduction is often the largest write-off you have.</p>
<h2>Standard mileage vs. actual expenses</h2><p>You can deduct business miles × the IRS standard rate (plus business tolls and parking), <i>or</i> actual vehicle expenses for that car. For 2026 the IRS business rate is 72.5 cents per mile from January 1 through June 30 (Notice 2026-10) and 76 cents per mile from July 1 through December 31 (Announcement 2026-11). Check <a href="https://www.irs.gov/tax-professionals/standard-mileage-rates" rel="noopener">irs.gov/standard-mileage-rates</a> before you file.</p>
<h2>Keep a log</h2><p>The IRS expects a record of date, miles, destination and business purpose. Our <a href="../free-download.html">free printable log</a> covers all of it.</p>
<h2>Example</h2><p>1,000 business miles in the first half of 2026 × $0.725 = $725. The same 1,000 miles in the second half × $0.76 = $760. Tolls and parking for those trips are added on top. <a href="../tools/mileage-deduction-calculator.html">Try the calculator</a> with the rate for the miles you are counting.</p>"""),
("how-to-set-your-freelance-rate","How to Set Your Freelance Hourly Rate (Without Guessing)","A step-by-step method to price freelance work based on income goals, expenses, taxes, and billable hours.",
"""<p>New freelancers often copy their old hourly wage. That ignores taxes, unpaid admin time, and expenses an employer used to cover.</p>
<h2>The method</h2><ol><li>Pick your take-home goal.</li><li>Add yearly business expenses (software, equipment, insurance).</li><li>Gross up for taxes: (income + expenses) ÷ (1 − tax rate).</li><li>Divide by realistic <b>billable</b> hours (often 20–30/week).</li></ol>
<h2>Example</h2><p>$60,000 goal + $6,000 expenses at a 25% set-aside = $88,000 needed. 25 hrs × 46 weeks = 1,150 hours → <b>about $76.52/hour</b>.</p>
<p>Use the <a href="../tools/freelance-hourly-rate-calculator.html">freelance rate calculator</a>, then bill clients with our <a href="../tools/invoice-generator.html">free invoice generator</a>.</p>"""),
("quarterly-estimated-taxes-for-gig-workers","Quarterly Estimated Taxes for Gig Workers, Explained","Who must pay quarterly estimated taxes, typical due dates, and how to estimate how much to set aside.",
"""<p>No employer withholds tax from 1099 income, so the IRS generally expects you to pay during the year using Form 1040-ES if you expect to owe $1,000 or more.</p>
<h2>Usual due dates</h2><p>Typically mid-April, mid-June, mid-September and mid-January — confirm the exact dates for the year at <a href="https://www.irs.gov/forms-pubs/about-form-1040-es" rel="noopener">IRS Form 1040-ES</a>.</p>
<h2>How much?</h2><p>Estimate self-employment tax + income tax on profit, then divide by four. Our <a href="../tools/self-employment-tax-calculator.html">calculator</a> does it: $30,000 profit at 12% ≈ $1,896 per quarter.</p>""")]
GUIDES.extend(EXTRA_GUIDES)
for item in GUIDES:
    s,t,d,b=item[:4]
    faqs=item[4] if len(item)>4 else None
    page(f"guides/{s}.html",t,d,f'<article><h1>{t}</h1><p class="small">Educational guide · not tax advice. Confirm current figures at IRS.gov.</p>{b}</article>',faqs)
gl="".join(f'<a class="card" href="{s}.html"><h3>{t}</h3><p>{d}</p></a>' for s,t,d,*_ in GUIDES)
page("guides/index.html","Guides for Gig Workers & Freelancers","Plain-English guides on gig driver earnings, 2026 mileage rates, delivery write-offs, 1099 forms, and quarterly taxes.",f'<h1>Guides</h1><p class="lead">Practical guides for US gig drivers and 1099 freelancers. Tax figures are taken from IRS pages and are not advice.</p><div class="cards">{gl}</div>')
page("tools/index.html","Free Gig & Freelance Money Tools","Free calculators for gig drivers and freelancers: profit per hour, mileage deduction, self-employment tax, hourly rate, invoices.",f'<h1>All Tools</h1><div class="cards">{cards.replace("tools/","")}</div>')
page("index.html","Free Calculators for Gig Drivers & Freelancers","Know your real hourly pay. Free gig driver profit, mileage deduction, 1099 self-employment tax, freelance rate and invoice tools.",
f'''<section class="hero"><h1>Know what you <em>really</em> earn.</h1><p class="lead">Free, private calculators for gig drivers, delivery couriers and freelancers. No signup. Everything runs in your browser.</p>
<a class="btn" href="tools/gig-driver-profit-calculator.html">Calculate my real hourly pay</a> <a class="btn alt" href="free-download.html">Free mileage log (PDF)</a></section>
<h2>Tools</h2><div class="cards">{cards}</div><h2>Latest guides</h2><div class="cards">{gl.replace('href="','href="guides/')}</div>''')
page("free-download.html","Free Printable Mileage & Earnings Log (PDF)","Download a free printable gig driver mileage and earnings log that captures what the IRS expects.",
'<h1>Free Mileage &amp; Earnings Log</h1><p class="lead">A printable 1-page weekly log: date, start/end odometer, business purpose, pay, tips, hours, and a weekly totals box.</p><p><a class="btn" href="downloads/gigmath-mileage-earnings-log.pdf" download>Download the PDF (free)</a></p><p>Want spreadsheets that do the math for you? See the <a href="pro.html">Pro Kit</a>.</p>')
page("pro.html","GigMath Pro Tax-Year Kit","Coming soon: a spreadsheet kit for gig workers with a mileage log, weekly earnings, expenses, and a quarterly tax estimator.",
'''<h1>GigMath Pro Tax-Year Kit</h1><p class="lead">Coming soon. A spreadsheet for a full tax year: mileage log with totals, weekly earnings, an expense tracker, and a quarterly estimated-tax worksheet with formulas.</p>
<div class="aff"><b>Status: Coming soon.</b> Not for sale yet. <!-- PLACEHOLDER: list the product on Gumroad or Lemon Squeezy, then replace the button link with that product URL. Do not add a public download link. --></div>
<p><a class="btn" href="#GUMROAD-OR-LEMONSQUEEZY-PLACEHOLDER">Get the Pro Kit — coming soon</a></p><p class="small">One-time purchase when it launches. No subscription.</p>''')
page("about.html","About & Contact","About GigMath, a free tool site for gig workers and freelancers, based in Phoenix, Arizona.",
'<h1>About GigMath</h1><p>GigMath is run by Kasen Clements in Phoenix, AZ. I built these free tools because gig apps show gross pay, not what you actually keep.</p><h2>Contact</h2><p>Email: <a href="mailto:CONTACT-EMAIL-PLACEHOLDER">CONTACT-EMAIL-PLACEHOLDER</a> (replace with a free address before launch).</p>')
page("privacy.html","Privacy Policy","GigMath privacy policy.",'<h1>Privacy Policy</h1><p>Calculator inputs never leave your device. We may use privacy-friendly, cookie-free analytics (GoatCounter or Cloudflare Web Analytics) that count page views without personal profiles. Affiliate links may let partner sites set their own cookies when you click; their policies apply. We do not sell data. Contact: see About page. Last updated: '+str(datetime.date.today())+'.</p>')
page("terms.html","Terms of Use","GigMath terms of use.",'<h1>Terms of Use</h1><p>Tools and articles are provided "as is" for general education and are not tax, legal, or financial advice. Results are estimates and may be wrong; verify with official sources or a qualified professional. We are not liable for decisions made using this site. Arizona law governs.</p>')
page("disclosure.html","Affiliate Disclosure","GigMath affiliate disclosure.",'<h1>Affiliate Disclosure</h1><p>Some links on this site may be affiliate links. If you click and sign up or buy, GigMath may earn a commission at no extra cost to you. This follows FTC endorsement guidelines. We only recommend products we believe are relevant to gig workers and freelancers.</p>')
pages=["index.html","tools/index.html","guides/index.html","free-download.html","pro.html","about.html","privacy.html","terms.html","disclosure.html"]+[f"tools/{s}.html" for s,*_ in ALLT]+[f"guides/{s}.html" for s,*_ in GUIDES]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{URL}/{p}</loc></url>\n" for p in pages)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nDisallow: /downloads/pro/\nSitemap: {URL}/sitemap.xml\n")
