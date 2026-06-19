"""
Configuration and prompts for Claude-powered agents.
"""
import os
import json
from anthropic import Anthropic

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
claude_client = Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None # pyright: ignore[reportGeneralTypeIssues]

DEFAULT_MODEL = "global.anthropic.claude-opus-4-5-20251101-v1:0"

DEFAULT_DTI_THRESHOLD = 0.5
DEFAULT_INCOME_THRESHOLD = 50000
DEFAULT_CREDIT_SCORE_THRESHOLD = 650

PROFILE_ANALYSIS_PROMPT = """You are a loan application profile analyst. Analyze the applicant profile.

Applicant Information:
- Age: {age}
- Annual Income: ${income:,.2f}
- Employment Type: {employment}
- Credit Score: {credit_score}

Provide JSON with:
1. "income_stability": "High" or "Low"
2. "employment_risk": "Low", "Medium", or "High"
3. "credit_profile": "Excellent", "Good", "Fair", or "Poor"
4. "application_completeness": "Complete" or "Incomplete"
5. "profile_score": 0-100
6. "reasoning": Brief explanation

Respond ONLY with valid JSON."""

RISK_ANALYSIS_PROMPT = """You are a financial risk analyst. Assess financial risk.

Applicant Data:
- Annual Income: ${income:,.2f}
- Loan Amount: ${loan_amount:,.2f}
- Employment Risk: {employment_risk}
- Credit Profile: {credit_profile}

Provide JSON with:
1. "dti": Debt-to-income ratio
2. "lti": Loan-to-income ratio
3. "risk_score": 0-100
4. "risk_level": "Low", "Medium", or "High"
5. "anomalies_detected": List of unusual patterns
6. "reasoning": Brief explanation

Respond ONLY with valid JSON."""

DECISION_PROMPT = """You are a loan decision engine. Make a decision.

Profile:
- Income Stability: {income_stability}
- Employment Risk: {employment_risk}
- Credit Profile: {credit_profile}
- Completeness: {application_completeness}
- Profile Score: {profile_score}

Risk:
- DTI: {dti}
- Risk Score: {risk_score}
- Risk Level: {risk_level}
- Anomalies: {anomalies}

Provide JSON with:
1. "decision": "APPROVED", "REJECTED", or "REVIEW"
2. "confidence": 0-100
3. "decision_factors": Top 3 factors with weights
4. "reasoning": Detailed explanation
5. "risk_summary": Brief summary

Respond ONLY with valid JSON."""

COMPLIANCE_PROMPT = """You are a compliance officer finalizing a decision.

Decision:
- Final Decision: {decision}
- Confidence: {confidence}%
- Reasoning: {reasoning}

Generate JSON with:
1. "case_id": Unique case ID (LOAN-XXXXX format)
2. "final_decision": The decision
3. "compliance_status": Status
4. "audit_trail_entry": Summary
5. "notification_required": true/false
6. "next_steps": Recommended steps

Respond ONLY with valid JSON."""

def get_claude_response(prompt: str, system_message: str = None) -> dict: # pyright: ignore[reportArgumentType]
    """Get response from Claude API with JSON parsing."""
    if not claude_client:
        raise ValueError("ANTHROPIC_API_KEY not set")

    messages = [{"role": "user", "content": prompt}]
    response = claude_client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=1024,
        system=system_message or "You are helpful. Respond with JSON only.",
        messages=messages # pyright: ignore[reportArgumentType]
    )

    response_text = response.content[0].text # pyright: ignore[reportAttributeAccessIssue]

    # Remove markdown code blocks if present
    if response_text.startswith("```json"):
        response_text = response_text[7:]
    elif response_text.startswith("```"):
        response_text = response_text[3:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]
    response_text = response_text.strip()

    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON: {response_text}")

def get_fallback_response(response_type: str, **kwargs) -> dict:
    """Fallback responses when Claude API unavailable."""
    if response_type == "profile":
        return {
            "income_stability": "High" if kwargs.get("income", 0) > DEFAULT_INCOME_THRESHOLD else "Low",
            "employment_risk": "Low" if kwargs.get("employment") == "Full-time" else "Medium",
            "credit_profile": "Good" if kwargs.get("credit_score", 600) > DEFAULT_CREDIT_SCORE_THRESHOLD else "Fair",
            "application_completeness": "Complete",
            "profile_score": 65,
            "reasoning": "Fallback: Basic rule-based assessment"
        }
    elif response_type == "risk":
        income = kwargs.get("income", 1)
        loan = kwargs.get("loan_amount", 0)
        dti = loan / income if income > 0 else 1.0
        return {
            "dti": round(dti, 2),
            "lti": round(loan / 100000, 2),
            "risk_score": 60,
            "risk_level": "High" if dti > DEFAULT_DTI_THRESHOLD else "Low",
            "anomalies_detected": [],
            "reasoning": "Fallback: DTI-based calculation"
        }
    elif response_type == "decision":
        return {
            "decision": kwargs.get("default_decision", "REVIEW"),
            "confidence": 50,
            "decision_factors": [
                {"factor": "Risk Score", "weight": 0.4},
                {"factor": "Credit Profile", "weight": 0.3},
                {"factor": "Income Stability", "weight": 0.3}
            ],
            "reasoning": "Fallback: Manual review recommended",
            "risk_summary": "Unable to assess - review needed"
        }
    elif response_type == "compliance":
        import uuid
        return {
            "case_id": f"LOAN-{uuid.uuid4().hex[:8].upper()}",
            "final_decision": kwargs.get("decision", "PENDING"),
            "compliance_status": "Requires Manual Review",
            "audit_trail_entry": f"Processed on {kwargs.get('timestamp', 'unknown')}",
            "notification_required": True,
            "next_steps": "Manual review by loan officer"
        }
    return {}
