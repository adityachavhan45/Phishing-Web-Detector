import datetime

def log_event(url, score, result, reasons):
    with open("phishing_logs.txt", "a") as f:
        f.write(f"\n[{datetime.datetime.now()}]\n")
        f.write(f"URL: {url}\n")
        f.write(f"Score: {score}\n")
        f.write(f"Result: {result}\n")
        for r in reasons:
            f.write(f"- {r}\n")
