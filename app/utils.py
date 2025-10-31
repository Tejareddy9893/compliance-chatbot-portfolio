import pandas as pd
import json

def get_answer(query):
    sources = ["data/hipaa_faq.csv", "data/soc2_controls.csv"]
    best_match = None
    best_score = 0

    # Search CSVs
    for source in sources:
        df = pd.read_csv(source)
        for _, row in df.iterrows():
            text = " ".join(str(cell).lower() for cell in row)
            score = sum(word.lower() in text for word in query.split())
            if score > best_score:
                best_score = score
                best_match = row[1]

    # Search JSON
    with open("data/risk_scenarios.json") as f:
        risks = json.load(f)
        for risk in risks:
            text = " ".join(risk.values()).lower()
            score = sum(word.lower() in text for word in query.split())
            if score > best_score:
                best_score = score
                best_match = f"Scenario: {risk['scenario']}\nImpact: {risk['impact']}\nMitigation: {risk['mitigation']}"

    if best_match:
        return best_match
    return "Sorry, I couldn't find an answer for that."