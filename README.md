# Electric Bike Academy dashboard

Live client report for [electricbikeacademy.com](https://electricbikeacademy.com), hosted on GitHub Pages.

**URL:** https://emmatully.github.io/eba-dashboard/

The page is `noindex`. The repo is public, so anyone with the link can see the snapshot (visitors, purchases, ad spend). Do not put secrets here.

## Files

- `index.html` — Cohelm report UI. No build step.
- `data/metrics.json` — latest live snapshot.
- `.github/workflows/refresh-dashboard.yml` — pulls GA4, Google Ads, Search Console, and the first-party beacon every hour, then publishes changed data.

The refresh runs at 17 minutes past each hour. GitHub may start scheduled jobs a few minutes late.

Credentials and the private pull script are encrypted GitHub Actions secrets. Remote operations are read-only; the workflow only writes the resulting `metrics.json` to this repository.

If the local `eba-stats/pull.py` changes, update the `EBA_PULL_SCRIPT` repository secret before relying on the scheduled version.

Do not commit `pull.py`, FTP credentials, OAuth tokens, or Google API keys.
