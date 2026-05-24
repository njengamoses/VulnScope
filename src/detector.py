def detect_vulnerabilities(targets):
    findings = []

    for t in targets:
        name = t.get("name", "").lower()
        description = t.get("description", "").lower()

        # RULE 1: login endpoints are risky
        if "login" in name or "login" in description:
            findings.append({
                "name": "Potential Authentication Issue",
                "severity": "high",
                "description": "Login-related endpoint may be exposed or weak"
            })

        # RULE 2: search/input fields → XSS risk simulation
        if "search" in name or "input" in description:
            findings.append({
                "name": "Possible XSS Surface",
                "severity": "medium",
                "description": "User input fields detected"
            })

        # RULE 3: missing headers simulation
        if "header" in name or "headers" in description:
            findings.append({
                "name": "Missing Security Headers",
                "severity": "low",
                "description": "Security headers not configured"
            })

    return findings
