
def handler(result: object):

    department = result["answers"]["department"]["choice"]
    urgency = urgency_formatter(result["answers"]["urgency"])
    risk = risk_formatter(result["answers"]["churn_risk"])
    intent = result["answers"]["intent"]["choice"]
    
    print(f"\nWhich department should handle this ? : {department}")
    print(f"How urgent the request is ? : {urgency}")
    print(f"How much risk ? : {risk}")
    print(f"What is the intent ? : {intent}")
    print("\n")

def urgency_formatter(urgency: object):
    probabilities = urgency["probabilities"]

    highest = max(probabilities, key=probabilities.get)

    levels = {
        "0": "very urgent",
        "1": "as soon as possible",
        "2": "not urgent"
    }

    confidence = probabilities[highest] * 100
    return f"{levels[highest]} ({confidence:.2f}% confidence)"

def risk_formatter(risk: object):
    risk_score = risk["noul"]
    risk_percentage = risk_score * 100

    if risk_score >= 0.8:
        level = "High"
    elif risk_score >= 0.5:
        level = "Medium"
    else:
        level = "Low"

    return f"{level} ({risk_percentage:.2f}%)"