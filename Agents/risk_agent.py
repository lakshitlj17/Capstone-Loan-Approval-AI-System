def risk_agent(data):
    income = data["income"]
    loan = data["loan_amount"]

    dti = loan / income if income > 0 else 1

    risk_level = "High" if dti > 0.5 else "Low"

    return {
        "dti": round(dti, 2),
        "risk_level": risk_level
    }