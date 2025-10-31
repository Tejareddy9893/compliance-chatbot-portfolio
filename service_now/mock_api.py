def create_ticket(issue_summary, category="Compliance"):
    return {
        "ticket_id": "SNOW123456",
        "status": "Created",
        "summary": issue_summary,
        "category": category,
        "link": "https://servicenow.example.com/ticket/SNOW123456"
    }

def search_kb(query):
    if "HIPAA" in query:
        return "HIPAA KB Article: https://servicenow.example.com/kb/hipaa"
    elif "SOC2" in query:
        return "SOC2 KB Article: https://servicenow.example.com/kb/soc2"
    else:
        return "No matching KB article found."