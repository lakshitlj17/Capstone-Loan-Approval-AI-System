# 💰 Loan Approval AI System

An intelligent loan application processor using multi-agent AI pipeline. The system analyzes loan applications through parallel agents for profile analysis, risk assessment, decision-making, and compliance checking.

## 🏗️ Architecture

### Components

**Frontend (Streamlit)**
- Modern, responsive UI for loan application submission
- Real-time analysis display with visual decision indicators
- Support for applicant details: age, income, employment type, loan amount

**Backend (FastAPI)**
- RESTful API for loan processing
- `/loan` - POST endpoint to process applications
- Integrates with multi-agent orchestration

**Multi-Agent Pipeline (LangGraph)**
1. **Profile Agent** - Analyzes income stability and employment risk
2. **Risk Agent** - Calculates debt-to-income ratio and risk level
3. **Decision Agent** - Makes approval/rejection decision based on risk profile
4. **Compliance Agent** - Finalizes decision with timestamp and status

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn streamlit langgraph langchain requests python-dotenv
```

### Environment Setup

Create a `.env` file in `Loan AI Project/` with your API keys:
```
LLMGW_API_KEY=your_api_key_here
LLMGW_BASE_URL=https://llmgw-wp.tekstac.com
```

### Running the Application

**Terminal 1 - Start FastAPI Backend:**
```bash
cd "Loan AI Project"
uvicorn api:app --host 127.0.0.1 --port 8000
```

**Terminal 2 - Start Streamlit Frontend:**
```bash
cd "Loan AI Project"
streamlit run app.py --server.port 8501
```

Access the application at: **http://localhost:8501**

## 📊 Application Flow

1. User submits loan application with personal details
2. Profile Agent analyzes income stability and employment risk
3. Risk Agent calculates debt-to-income ratio
4. Decision Agent determines approval/rejection
5. Compliance Agent adds final decision with timestamp
6. Results displayed in UI with detailed analysis

## 📁 Project Structure

```
Capstone Project/
├── Agents/
│   ├── profile_agent.py        # Income & employment analysis
│   ├── risk_agent.py           # Risk calculation
│   ├── decision_agent.py       # Approval decision
│   └── compliance_agent.py     # Compliance check & finalization
├── Loan AI Project/
│   ├── api.py                  # FastAPI endpoints
│   ├── app.py                  # Streamlit UI
│   ├── orchestrator.py         # LangGraph pipeline
│   └── .env                    # API credentials (not in git)
├── venv/                       # Virtual environment (not in git)
└── README.md
```

## 🔧 API Endpoints

### POST `/loan`
Process a loan application.

**Request:**
```json
{
  "age": 30,
  "income": 60000,
  "employment": "Full-time",
  "loan_amount": 100000
}
```

**Response:**
```json
{
  "input": { ... },
  "profile": {
    "income_stability": "High",
    "employment_risk": "Low"
  },
  "risk": {
    "dti": 1.67,
    "risk_level": "High"
  },
  "decision": "REJECTED",
  "final": {
    "final_decision": "REJECTED",
    "timestamp": "2026-06-17 21:11:04.442967",
    "status": "Processed"
  }
}
```

## 🎨 UI Features

- **Modern Gradient Design** - Professional, visually appealing interface
- **Real-time Analysis** - Quick stats and DTI calculation
- **Color-Coded Results** - Green for approval, orange for rejection
- **Detailed Breakdown** - Profile, risk, and final decision sections
- **Expandable Details** - Full JSON results for debugging
- **Error Handling** - Clear error messages for API issues

## 📝 Notes

- `.env` file is excluded from git to protect API keys
- Virtual environment (`venv/`) is excluded from git
- All sensitive files are listed in `.gitignore`

---

**Developed for Capstone Project | LangGraph & FastAPI with Streamlit**
