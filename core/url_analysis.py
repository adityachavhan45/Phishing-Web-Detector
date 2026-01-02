import re
from urllib.parse import urlparse

def analyze_url(url):
    score = 0
    reasons = []

    if re.search(r'(\d{1,3}\.){3}\d{1,3}', url):
        score += 2; reasons.append("IP address used in URL")

    if len(url) > 75:
        score += 1; reasons.append("Very long URL")

    if urlparse(url).scheme != "https":
        score += 2; reasons.append("No HTTPS")

    if '@' in url or url.count('//') > 1 or '-' in url:
        score += 1; reasons.append("Suspicious URL symbols")

    keywords = ["login","verify","secure","update","account","bank"]
    if any(k in url.lower() for k in keywords):
        score += 1; reasons.append("Phishing keywords in URL")

    return score, reasons
