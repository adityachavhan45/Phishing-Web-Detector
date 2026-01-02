import argparse
from core.url_analysis import analyze_url
from core.domain_analysis import analyze_domain
from core.content_analysis import analyze_content
from core.reputation_check import reputation_check
from core.logger import log_event

def main(url):
    total_score = 0
    reasons = []

    for func in [analyze_url, analyze_domain, analyze_content, reputation_check]:
        s, r = func(url)
        total_score += s
        reasons.extend(r)

    if total_score >= 10:
        result = "❌ CRITICAL PHISHING THREAT"
    elif total_score >= 5:
        result = "⚠️ SUSPICIOUS WEBSITE"
    else:
        result = "✅ LEGITIMATE WEBSITE"

    print("\nResult:", result)
    print("Risk Score:", total_score)
    print("Reasons:")
    for r in reasons:
        print("-", r)

    log_event(url, total_score, result, reasons)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Target website URL")
    args = parser.parse_args()
    main(args.url)
