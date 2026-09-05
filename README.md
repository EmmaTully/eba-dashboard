# Electric Bike Academy — Growth Dashboard

Live client dashboard for [electricbikeacademy.com](https://electricbikeacademy.com), hosted on GitHub Pages.

## How it works
- `index.html` — static single-page dashboard (Chart.js). No build step.
- `data/metrics.json` — the single data source. While `"sample": true`, the UI shows a sample-data banner.
- `scripts/fetch_metrics.py` — nightly refresh script (GA4 Data API, Google Ads API, Search Console API). Stubs are in place; they activate as client access is granted.
- `automation/refresh-data.yml` — daily GitHub Action that runs the script and commits fresh data. (Parked here because the current GitHub token lacks `workflow` scope; move to `.github/workflows/` when activating live data — step 4 below.)

## Activating live data
1. Client grants access per `docs/ACCESS-CHECKLIST.md` (in the main workspace).
2. Add repo Actions secrets: `GOOGLE_SERVICE_ACCOUNT_JSON`, `GA4_PROPERTY_ID`, `GOOGLE_ADS_YAML`, `GOOGLE_ADS_CUSTOMER_ID`.
3. Fill in the three `fetch_*` functions in `scripts/fetch_metrics.py`.
4. `git mv automation/refresh-data.yml .github/workflows/` (after `gh auth refresh -s workflow`).

## Privacy note
GitHub Pages on a free plan requires a **public repo** — once real revenue/ads data flows in, either upgrade to keep the repo private with Pages, or move behind auth (Cloudflare Access / Vercel). Currently only sample data is published.
