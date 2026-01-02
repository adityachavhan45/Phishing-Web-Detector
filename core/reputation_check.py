def reputation_check(url):
    score = 0
    reasons = []

    known_bad = ["phish", "malware", "fraud"]
    if any(b in url.lower() for b in known_bad):
        score += 3
        reasons.append("Matched reputation blacklist pattern")

    return score, reasons
