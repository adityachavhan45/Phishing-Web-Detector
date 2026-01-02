import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def analyze_content(url):
    score = 0
    reasons = []

    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        if soup.find("input", {"type": "password"}):
            score += 2; reasons.append("Password field detected")

        links = soup.find_all("a", href=True)
        domain = urlparse(url).netloc
        external = sum(1 for l in links if domain not in l['href'])

        if external > len(links) / 2:
            score += 1; reasons.append("High external link ratio")

        scripts = soup.find_all("script")
        if any("window.location" in s.text for s in scripts):
            score += 2; reasons.append("JavaScript redirection found")

    except:
        score += 1; reasons.append("Unable to analyze page content")

    return score, reasons
