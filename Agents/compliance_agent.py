import datetime

def compliance_agent(decision):
    return {
        "final_decision": decision,
        "timestamp": str(datetime.datetime.now()),
        "status": "Processed"
    }