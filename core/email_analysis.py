def analyze_email(email_text):
    score = 0
    reasons = []

    urgent_words = ["urgent", "verify now", "action required", "account locked"]
    if any(w in email_text.lower() for w in urgent_words):
        score += 2; reasons.append("Urgent social engineering language")

    if "http" in email_text:
        score += 1; reasons.append("Suspicious link inside email")

    return score, reasons
