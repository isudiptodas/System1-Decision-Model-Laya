from laya import Router
import json
from predictHandler import handler

router = Router() 

# Representing an AI film-making company that has departments : sound-team, editing-team, prompt-team, social-media-team 
state = input("Enter your query : ")
questions = {
    "department": {
        "type": "choice",
        "instructions": "Which department should handle this ?",
        "criteria": {
            "sound-team": "background sound mismatch, sound copyright issue, lip sync match error, song selection",
            "editing-team": "color grading, video editing, video formatting, video compressing",
            "prompt-team": "story board making, prompt generation, video generation,",
            "social-media-team": "posting on social media, release updates for new company offers",
            "others": "Any other general query"
        },
    },
    "urgency": {
        "type": "score",
        "instructions": "How urgent is this ?",
        "criteria": ["very urgent", "as soon as possible", "not urgent"],
    },
    "churn_risk": {
        "type": "noul",
        "instructions": "Is the user threatening of damaging the company's reputation or public image ?",
    },
    "intent": {
        "type": "choice",
        "instructions": "Based on the request what intent the user signifies ?",
        "criteria": {
            "complain": "the user is angry and wants to register a complain",
            "information-request": "the user wants to understand or have any query regarding company services or company"
        }
    },
}

result = router.predict(state, questions)
formatted = json.dumps(result["answers"], indent=2)

handler(result=result)
print(formatted)
