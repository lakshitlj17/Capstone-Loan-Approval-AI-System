def profile_agent(data):
    income = data["income"]
    employment = data["employment"]

    income_score = "High" if income > 50000 else "Low"
    employment_risk = "Low" if employment == "Full-time" else "Medium"

    return {
        "income_stability": income_score,
        "employment_risk": employment_risk
    }