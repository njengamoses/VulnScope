import argparse
from src.parser import load_vulnerabilities
from src.detector import detect_vulnerabilities
from src.formatter import format_vulnerabilities

def main():
    parser = argparse.ArgumentParser(description="VulnScope CLI Tool")

    parser.add_argument("--file", required=True)
    parser.add_argument("--severity")
    parser.add_argument("--output")

    args = parser.parse_args()

    # Step 1: load input data
    data = load_vulnerabilities(args.file)

    if not data:
        print("No input data found")
        return

    # Step 2: DETECTION (this is your new “engine”)
    findings = detect_vulnerabilities(data)

    if not findings:
        print("No vulnerabilities detected")
        return

    # Step 3: filter (optional)
    if args.severity:
        findings = [
            f for f in findings
            if f["severity"].lower() == args.severity.lower()
        ]

    # Step 4: report
    format_vulnerabilities(findings)

    # Step 5: export (optional reuse from before if you want later)

if __name__ == "__main__":
    main()
