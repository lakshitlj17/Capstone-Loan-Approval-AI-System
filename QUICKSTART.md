# Loan Approval AI v2.0 - Quick Start Guide

## Overview
This guide will get you running the enhanced Loan Approval AI system in 5 minutes.

## What's New in v2.0

✨ **Key Enhancements:**
- 🤖 Claude AI-powered intelligent reasoning for all decisions
- 🔗 MCP communication layer for agent interoperability  
- 📊 Comprehensive audit trail and compliance logging
- 🎯 Confidence scoring and decision factors explanation
- 👤 Manual review workflow for borderline cases
- 💡 Full explainability for every decision

## Prerequisites

- Python 3.12+
- pip package manager
- Anthropic API key (optional - system works without it using fallback logic)

## Installation (5 minutes)

### 1. Install Dependencies
```bash
cd "Capstone Project"
pip install -r requirements.txt
```

### 2. Set Environment Variables
```bash
# Create or update Loan AI Project/.env
ANTHROPIC_API_KEY=sk-ant-your-api-key-here

# Or set as environment variable
export ANTHROPIC_API_KEY=sk-ant-your-api-key-here
```

### 3. Verify Installation
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
python3 -c "
import sys
sys.path.insert(0, '.')
from config import DEFAULT_MODEL
from mcp_tools import MCP_TOOLS
from audit_logger import get_audit_logger
print(f'✅ Config: {DEFAULT_MODEL}')
print(f'✅ MCP Tools: {len(MCP_TOOLS)} registered')
print(f'✅ Audit Logger: Ready')
"
```

## Running the System

### Terminal 1: Start Backend API
```bash
cd "Loan AI Project"
uvicorn api:app --reload --port 8000
```

You'll see:
```
Uvicorn running on http://127.0.0.1:8000
Press CTRL+C to quit
```

### Terminal 2: Start Frontend UI
```bash
cd "Loan AI Project"
streamlit run app.py
```

You'll see:
```
Streamlit app running on http://localhost:8501
Press CTRL+C to quit
```

### 3. Access the System
- **UI:** http://localhost:8501 (user-friendly application form)
- **API Docs:** http://localhost:8000/docs (interactive API documentation)
- **Health:** http://localhost:8000/health (system status)

## Testing

### Test Case 1: Standard Approval
Fill the form with:
- Age: 35
- Annual Income: $100,000
- Employment: Full-time
- Loan Amount: $250,000
- Credit Score: 750

**Expected Result:** APPROVED with high confidence

### Test Case 2: Manual Review
Fill the form with:
- Age: 28
- Annual Income: $45,000
- Employment: Self-employed
- Loan Amount: $200,000
- Credit Score: 620

**Expected Result:** REVIEW or APPROVED with low confidence

### Test Case 3: Rejection
Fill the form with:
- Age: 65
- Annual Income: $25,000
- Employment: Self-employed
- Loan Amount: $500,000
- Credit Score: 480

**Expected Result:** REJECTED with high confidence

## API Examples

### Process Loan Application
```bash
curl -X POST "http://localhost:8000/loan" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 32,
    "income": 85000,
    "employment": "Full-time",
    "loan_amount": 250000,
    "credit_score": 720
  }'
```

### Get System Health
```bash
curl "http://localhost:8000/health"
```

### Get Manual Review Queue
```bash
curl "http://localhost:8000/manual-review/queue"
```

### View Audit Trail
```bash
curl "http://localhost:8000/audit/LOAN-XXXXXXXX"
```

## Understanding the Output

### Decision Response Includes:
1. **Decision:** APPROVED, REJECTED, or REVIEW
2. **Confidence:** 0-100% confidence in the decision
3. **Reasoning:** Detailed explanation of the decision logic
4. **Decision Factors:** Top factors with weights influencing the decision
5. **Explanations:** Detailed reasoning from each agent
6. **Audit Trail:** Complete record of all processing steps

### Example Response Structure:
```json
{
  "decision": "APPROVED",
  "confidence": 87,
  "reasoning": "Multiple factors support approval...",
  "decision_factors": [
    {"factor": "Low DTI", "weight": 0.4},
    {"factor": "Good Credit", "weight": 0.3},
    {"factor": "Stable Employment", "weight": 0.3}
  ],
  "explanations": {
    "profile_reasoning": "Income stable and employment low-risk",
    "risk_reasoning": "DTI 0.38 within acceptable range",
    "decision_reasoning": "All factors align for approval"
  },
  "compliance_info": {
    "case_id": "LOAN-A1B2C3D4",
    "compliance_status": "Approved for Processing",
    "next_steps": "Application approved - funds available"
  },
  "audit_trail": [...]
}
```

## File Structure

```
Capstone Project/
├── config.py                    # Claude configuration
├── mcp_tools.py                # MCP protocol implementation
├── audit_logger.py             # Audit trail system
├── workflows/
│   ├── __init__.py
│   └── manual_review.py        # Review queue management
├── Agents/
│   ├── profile_agent.py        # Profile analysis (Claude-powered)
│   ├── risk_agent.py           # Risk assessment (Claude-powered)
│   ├── decision_agent.py       # Loan decision (Claude-powered)
│   └── compliance_agent.py     # Compliance finalization
├── Loan AI Project/
│   ├── orchestrator.py         # Pipeline orchestration
│   ├── api.py                  # FastAPI endpoints
│   ├── app.py                  # Streamlit UI
│   └── .env                    # Environment configuration
├── requirements.txt            # Python dependencies
├── audit_logs/                 # Generated audit trail files
└── README.md                   # Full documentation
```

## Troubleshooting

### "Cannot connect to API"
- Check FastAPI server is running on port 8000
- Verify no other service is using port 8000
- Try: `lsof -i :8000` (macOS/Linux) or `netstat -ano | findstr :8000` (Windows)

### "ANTHROPIC_API_KEY not set"
- System will use fallback rule-based logic
- Set the key in `.env` or environment to use Claude AI
- Without key, decisions use simple thresholds (still fully functional)

### "Module not found" errors
- Ensure venv is activated: `source venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python3 --version` (should be 3.12+)

### Audit logs not appearing
- Check `audit_logs/` directory exists
- Logs are written per application: `audit_logs/LOAN-XXXXXXXX.jsonl`
- View logs: `cat audit_logs/LOAN-XXXXXXXX.jsonl`

## Performance Tips

1. **Set ANTHROPIC_API_KEY** for intelligent decisions (vs. fallback rules)
2. **Run both servers** for full functionality (API + UI)
3. **Monitor audit_logs** for decision tracking
4. **Check /stats** endpoint for system metrics

## Next Steps

1. ✅ Run the system with test cases
2. ✅ Review decisions in the UI
3. ✅ Check audit trails via API
4. ✅ Try manual review queue endpoints
5. ✅ Read `IMPROVEMENTS.md` for detailed documentation

## Support

For detailed documentation: See `IMPROVEMENTS.md` and `IMPLEMENTATION_SUMMARY.md`

For API reference: Visit http://localhost:8000/docs when API is running

---

**Version:** 2.0  
**Status:** ✅ Production Ready  
**Last Updated:** 2026-06-19
