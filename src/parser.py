import json

def load_vulnerabilities(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: File not found")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return []
