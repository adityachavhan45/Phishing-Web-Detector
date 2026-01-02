import whois, dns.resolver
from datetime import datetime
from urllib.parse import urlparse

def analyze_domain(url):
    score = 0
    reasons = []
    domain = urlparse(url).netloc

    try:
        w = whois.whois(domain)
        created = w.creation_date
        if isinstance(created, list):
            created = created[0]
        age = (datetime.now() - created).days
        if age < 30:
            score += 2; reasons.append("Newly registered domain")
    except:
        score += 1; reasons.append("WHOIS info hidden")

    try:
        dns.resolver.resolve(domain, 'A')
    except:
        score += 2; reasons.append("Invalid DNS records")

    return score, reasons
