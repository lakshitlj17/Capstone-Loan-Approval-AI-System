def decision_agent(profile, risk):
    if risk["risk_level"] == "High":
        return "REJECTED"
    elif profile["income_stability"] == "Low":
        return "REVIEW"
    else:
        return "APPROVED"