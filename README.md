# QuiltingCompare.com

Quilt batting price comparison site — tracks Hobbs, Warm & Natural, Pellon, Quilters Dream, and Bosal Katahdin across Linda's Electric Quilters, Amazon, and Walmart.

## Site Structure

```
index.html          — Home page
cotton.html         — 100% Cotton batting comparison
wool.html           — Wool & wool blend batting comparison
cotton-poly.html    — Cotton-poly blend batting comparison
polyester.html      — 100% Polyester batting comparison
specialty.html      — Specialty batting (silk, fusible, etc.)
blog.html           — Blog listing
faq.html            — Frequently asked questions
about.html          — About page
404.html            — Custom 404 page
css/style.css       — All styles (bujo-inspired, mint palette)
```

## Deployment (GitHub Pages)

1. Push this repo to GitHub
2. Go to Settings → Pages
3. Set Source to: Deploy from branch → main → / (root)
4. Your site will be live at: `https://[username].github.io/[repo-name]/`
5. Add custom domain `quiltingcompare.com` in the Pages settings
6. Add DNS records at Porkbun pointing to GitHub's IP addresses

## GitHub Pages DNS (Porkbun)
Add these A records at Porkbun for quiltingcompare.com:
- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

Add CNAME record:
- www → [username].github.io

## Before Launch Checklist

- [ ] Replace `YOURTAG-20` in all price links with your Amazon Associates tag
- [ ] Replace Linda's search URLs with direct affiliate product URLs (once approved)
- [ ] Replace Walmart search URLs with Impact affiliate URLs (once approved)
- [ ] Replace newsletter form placeholder with actual Flodesk embed code
- [ ] Add real blog article pages (currently all link to blog.html)
- [ ] Set up 5 AM ET daily price update automation
- [ ] Set up Pinterest posting automation
- [ ] Set up Wednesday Flodesk newsletter automation
- [ ] Verify all prices are current

## Affiliate Link Format

### Amazon Associates
```
https://www.amazon.com/dp/ASIN?tag=YOURTAG-20
```

### Walmart (Impact)
```
https://www.walmart.com/ip/PRODUCTID?affiliates=[your-impact-id]
```

### Linda's (direct)
- Contact Linda's directly at lindas.com for their affiliate program terms

## Notes

- `.nojekyll` file prevents GitHub Pages from processing the site with Jekyll
- All CSS is in one file — no build tools required
- Mobile-first: works on 2 bars of cell signal
- Dot grid background is pure CSS (no images)
- Spiral binding and side tabs are CSS-only (zero load penalty)
- Google Font (Caveat + Inter) loads from Google CDN

## Color Palette

| Name | Hex |
|------|-----|
| Mint | #B8D8D1 |
| Mint Dark | #7BB8AE |
| Mint Light | #E4F3F0 |
| Gold | #C9A84C |
| Gold Light | #F5EDD2 |
| Text Dark | #2C3E35 |

---

A Potomac Falls Publishing project · Loudoun County, Virginia
