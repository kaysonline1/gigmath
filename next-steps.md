# What Kasen must do (all free)
1. **GitHub account** (github.com, free). Create a public repo `gigmath`, upload the contents of /workspace/business/site2/, then go to Settings → Pages → Source: "GitHub Actions". The workflows in .github/workflows (deploy, weekly lychee link check, 6-hourly uptime curl) **only run once they're in a repo**; none are active now. (Cloudflare Pages also works and is free.)
2. **Replace placeholders:** `URL` in build.py and SITE_URL in uptime.yml, then re-run `python3 build.py`. Also CONTACT-EMAIL-PLACEHOLDER in about.html (via build.py).
3. **Check the 2026 IRS mileage rate** at irs.gov (the tools use $0.725, from a third-party page).
4. **Affiliates (apply; none approved yet):** FreshBooks via PartnerStack; Everlance via Impact; Gigaverse (gigaverse.ai/affiliate-program); optionally Amazon Associates. Once approved, swap each `#AFFILIATE-PLACEHOLDER` link for your real link. Never add a link before approval.
5. **Gumroad or Lemon Squeezy** (free to start, fee per sale): build the Pro Kit spreadsheet, list it, and put the product URL in place of `#GUMROAD-OR-LEMONSQUEEZY-PLACEHOLDER` in pro.html.
6. **GoatCounter** (free for personal use) or Cloudflare Web Analytics: uncomment the snippet in the `<head>` (in build.py) and add your code.
7. Google Search Console + Bing Webmaster: verify the site and submit sitemap.xml.
8. Taxes: affiliate and product income is self-employment income. Programs may ask for a W-9 / 1099.

## Honest earnings expectations
No one can promise income, and I made up no numbers. What the sources actually say:
- Commissions only come after approval and real conversions: FreshBooks pays $10 per trial and up to $200 per paid plan (freshbooks.com/affiliate-program). Everlance pays about $2 per app install (linkclicky, 2024).
- Gigaverse's own page gives its math: about $22–30 per referred subscriber per year, and says "Twenty of those is a few hundred dollars, not a living" (gigaverse.ai/affiliate-program).
- New sites usually take months to rank in search. Expect $0 for the first stretch. Use Search Console impressions as the early sign it's working.
