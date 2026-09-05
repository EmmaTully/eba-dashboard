#!/usr/bin/env python3
"""Refresh data/metrics.json from live APIs.

Runs nightly via GitHub Actions (.github/workflows/refresh-data.yml) once
credentials exist. Until then the dashboard shows sample data ("sample": true).

Required environment (GitHub Actions secrets):
  GOOGLE_SERVICE_ACCOUNT_JSON  service account with GA4 Data API + Search Console API access
  GA4_PROPERTY_ID              numeric GA4 property id for G-EPJGD8PC4C
  GOOGLE_ADS_YAML              google-ads.yaml contents (developer token, OAuth, login_customer_id)
  GOOGLE_ADS_CUSTOMER_ID       client account id (tag AW-1063475106)

pip install google-analytics-data google-api-python-client google-ads
"""
import json
import os
import sys
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "metrics.json")


def load_current() -> dict:
    with open(DATA) as f:
        return json.load(f)


def fetch_ga4(metrics: dict) -> bool:
    """Sessions, conversions, revenue, channel mix from the GA4 Data API."""
    if not os.environ.get("GA4_PROPERTY_ID"):
        return False
    # TODO once access granted:
    # from google.analytics.data_v1beta import BetaAnalyticsDataClient, RunReportRequest
    # client = BetaAnalyticsDataClient()  # uses GOOGLE_APPLICATION_CREDENTIALS
    # ... runReport for sessions/conversions/purchaseRevenue by date and by sessionDefaultChannelGroup
    # then update metrics["kpis"], metrics["traffic"], metrics["channels"]
    return False


def fetch_google_ads(metrics: dict) -> bool:
    """Spend, conversions, CPA from the Google Ads API (GAQL)."""
    if not os.environ.get("GOOGLE_ADS_CUSTOMER_ID"):
        return False
    # TODO once MCC link accepted:
    # from google.ads.googleads.client import GoogleAdsClient
    # query = "SELECT segments.week, metrics.cost_micros, metrics.conversions FROM customer ..."
    # then update metrics["ads"] and kpis adSpend/cpa/roas
    return False


def fetch_gsc(metrics: dict) -> bool:
    """Clicks/impressions from the Search Console API."""
    # TODO once GSC property verified:
    # from googleapiclient.discovery import build
    # service = build("searchconsole", "v1", credentials=creds)
    # service.searchanalytics().query(siteUrl="sc-domain:electricbikeacademy.com", ...)
    return False


def main() -> int:
    metrics = load_current()
    live = [fetch_ga4(metrics), fetch_google_ads(metrics), fetch_gsc(metrics)]
    if any(live):
        metrics["sample"] = False
    metrics["updated"] = datetime.now(timezone.utc).isoformat()
    end = datetime.now(timezone.utc).date()
    metrics["period"] = f"{(end - timedelta(days=30)):%b %-d} – {end:%b %-d, %Y}"
    with open(DATA, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"metrics.json updated (live sources: {sum(live)}/3)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
