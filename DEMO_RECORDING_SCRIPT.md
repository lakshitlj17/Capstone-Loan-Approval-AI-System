# 🎥 Loan Approval AI System - Demo Recording Script

**Total Duration**: ~15-20 minutes  
**Format**: MP4 or MKV via OBS Studio

---

## Part 1: Introduction (1-2 minutes)

**What to show on screen**: Desktop/OBS scene with title

**Script to narrate**:
```
"Hello! Today I'm showcasing the Loan Approval AI System, 
a multi-agent AI pipeline built with LangGraph and FastAPI. 
This system automates loan application processing through 
intelligent analysis agents.

The system has four key components:
1. Profile Agent - Analyzes income and employment stability
2. Risk Agent - Calculates debt-to-income ratio
3. Decision Agent - Makes approval/rejection decisions
4. Compliance Agent - Ensures regulatory compliance

Let me walk you through the complete architecture and 
live demonstration of the application."
```

---

## Part 2: Project Structure & Code Overview (3-4 minutes)

**Actions**:
1. Open file explorer
2. Navigate to `/home/ubuntu/Desktop/Capstone Project/`
3. Show folder structure:
   - `Agents/` folder
   - `Loan AI Project/` folder
   - `workflows/` folder

**Script**:
```
"Let's look at the project structure. We have:

1. Agents folder - Contains four specialized agents:
   - profile_agent.py: Analyzes income stability and employment type
   - risk_agent.py: Calculates debt-to-income ratio
   - decision_agent.py: Makes final approval decision
   - compliance_agent.py: Applies regulatory rules

2. Loan AI Project folder - The main application:
   - app.py: Streamlit frontend interface
   - api.py: FastAPI backend server
   - orchestrator.py: LangGraph pipeline orchestration

3. Configuration files for managing prompts and settings
```

**Action**: Open one agent file (e.g., `profile_agent.py`)
```bash
code /home/ubuntu/Desktop/Capstone\ Project/Agents/profile_agent.py
```

**Script**:
```
"Let me show you one of the agents. Here's the Profile Agent.
It analyzes the applicant's income stability and employment type.
The agent uses Claude AI through the LLM Gateway to process this information.

[Point to key parts]:
- Input validation
- LLM prompt crafting
- Response parsing
- Error handling
```

---

## Part 3: Backend Architecture (2-3 minutes)

**Action**: Open `orchestrator.py`
```bash
code /home/ubuntu/Desktop/Capstone\ Project/Loan\ AI\ Project/orchestrator.py
```

**Script**:
```
"The orchestrator uses LangGraph to create a workflow pipeline.
This is where all four agents work together:

1. First, the Profile Agent runs to analyze income and employment
2. The Risk Agent then calculates the debt-to-income ratio
3. Based on that risk assessment, the Decision Agent approves or rejects
4. Finally, the Compliance Agent adds final compliance checks

All this happens in parallel when possible, making it efficient.
The outputs from each agent feed into the next step."
```

---

## Part 4: API Endpoints (2 minutes)

**Action**: Open `api.py`
```bash
code /home/ubuntu/Desktop/Capstone\ Project/Loan\ AI\ Project/api.py
```

**Script**:
```
"The FastAPI backend provides a simple REST endpoint:

POST /loan - Accepts loan application data with:
- age: Applicant's age
- income: Annual income
- employment: Employment type
- loan_amount: Requested loan amount

The API returns a complete analysis with:
- Profile assessment
- Risk calculation
- Final decision
- Compliance status with timestamp

Let me now show you the frontend where users interact with this API."
```

---

## Part 5: Starting the Application (2-3 minutes)

**Action**: Open terminal (split screen or new window)

**Terminal 1 - Start Backend**:
```bash
cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project"
python -m uvicorn api:app --host 127.0.0.1 --port 8000 --reload
```

**Narrate**:
```
"First, I'm starting the FastAPI backend server on port 8000.
The server is now running and ready to process loan applications."
```

Wait for server to start (you'll see: "Uvicorn running on http://127.0.0.1:8000")

**Terminal 2 - Start Frontend**:
```bash
cd "/home/ubuntu/Desktop/Capstone Project/Loan AI Project"
streamlit run app.py --server.port 8501
```

**Narrate**:
```
"Now starting the Streamlit frontend on port 8501.
This provides our user interface for the loan application system."
```

Wait for Streamlit to start (you'll see: "You can now view your Streamlit app")

---

## Part 6: Frontend UI Walkthrough (4-5 minutes)

**Action**: Open browser to `http://localhost:8501`

**Script**:
```
"Here's the Loan Approval AI System interface. Notice the 
modern gradient design with a professional layout.

The interface has several sections:
1. Title and description of the system
2. Input fields for loan application details
3. A submit button to process the application
4. Analysis results section
```

**Section 1: Input Form** (1 minute)
```
"Let me fill in a sample loan application:
- Age: 32
- Income: 75,000 per year
- Employment: Full-time
- Loan Amount: 150,000

[Fill in the form with these values]
```

**Section 2: Submit Application** (30 seconds)
```
"Now I'll click the Submit Application button to process this."
```

Click Submit and wait for results.

**Script for Results**:
```
"The system is now processing the application through all four agents:
1. Profile analysis
2. Risk calculation  
3. Decision making
4. Compliance check

This happens in seconds thanks to the efficient pipeline architecture."
```

---

## Part 7: Analyzing Results (3-4 minutes)

**Action**: After results load, show each section:

**Script**:
```
"Here are the results:

PROFILE ANALYSIS:
- Income Stability: [Show the assessment]
- Employment Risk: [Show the assessment]

RISK METRICS:
- Debt-to-Income Ratio: [Show calculation]
- Risk Level: [Show classification]

FINAL DECISION:
- Decision: [APPROVED/REJECTED]
- Timestamp: [Show processing time]
- Status: [Processed]

The decision is based on all the analysis from our four specialized agents.
```

**Action**: Test another scenario
```
"Let me test a different scenario to show how the system handles 
various risk profiles."
```

Test with different values (e.g., higher income or lower loan amount):
- Age: 28
- Income: 120,000
- Employment: Full-time
- Loan Amount: 80,000

**Script**:
```
"With a lower debt-to-income ratio, we can see a different risk profile
and decision outcome. This demonstrates how the system adapts 
to different financial situations."
```

---

## Part 8: Code Quality & Features (2 minutes)

**Script**:
```
"Key features of this system:

1. MULTI-AGENT ARCHITECTURE:
   - Each agent specializes in one aspect
   - Agents work together in a pipeline
   - Results are combined for final decision

2. REAL-TIME PROCESSING:
   - Applications processed in seconds
   - Instant feedback to users
   - Detailed analysis breakdown

3. ERROR HANDLING:
   - Graceful error handling
   - User-friendly error messages
   - Clear logging for debugging

4. COMPLIANCE:
   - Compliance agent ensures regulatory standards
   - Timestamps for audit trails
   - Full decision history available
```

---

## Part 9: Testing Different Scenarios (2-3 minutes)

**Scenario 1: High Income, Low Loan**
```
Age: 45, Income: 200,000, Loan: 50,000
Expected: APPROVED (very low DTI)
```

**Scenario 2: Low Income, High Loan**
```
Age: 25, Income: 30,000, Loan: 300,000
Expected: REJECTED (very high DTI)
```

**Scenario 3: Mid-range**
```
Age: 35, Income: 80,000, Loan: 100,000
Expected: MODERATE risk
```

**Script**:
```
"By testing multiple scenarios, we can see how the system
consistently applies its decision logic across different situations.
The multi-agent approach ensures fair and thorough evaluation."
```

---

## Part 10: Behind the Scenes - API Testing (2 minutes)

**Action**: Open terminal with curl command

**Script**:
```
"Let me also show you the raw API response that powers the UI."
```

Run a curl command:
```bash
curl -X POST http://localhost:8000/loan \
  -H "Content-Type: application/json" \
  -d '{"age": 35, "income": 85000, "employment": "Full-time", "loan_amount": 120000}'
```

**Script**:
```
"Here's the complete JSON response from our API. You can see:
- All agent outputs
- Complete risk analysis
- Final decision with timestamp
- Status confirmation

This is the raw data that powers both the UI and external integrations."
```

---

## Part 11: Conclusion (1 minute)

**Script**:
```
"In summary, the Loan Approval AI System demonstrates:

✅ Multi-agent AI orchestration with LangGraph
✅ Clean REST API with FastAPI
✅ Professional UI with Streamlit
✅ Real-time loan decision processing
✅ Compliance-aware automation
✅ Scalable architecture

This system can be easily integrated with banking platforms,
enhanced with additional agents, or adapted for other 
financial decision-making scenarios.

Thank you for watching!"
```

---

## Recording Checklist

- [ ] OBS configured with MP4/MKV output
- [ ] Microphone levels tested
- [ ] Screen resolution set appropriately
- [ ] Internet connection stable (for API calls)
- [ ] Have test data prepared
- [ ] .env file has valid API keys
- [ ] Both backend and frontend ready to start
- [ ] Browser zoomed in (125-150%) for better visibility
- [ ] Start recording BEFORE opening browser
- [ ] Narrate clearly and pace your speech

---

## Tips for Better Recording

1. **Pause when needed** - It's okay to pause and restart sections
2. **Edit later** - You can trim silence and combine takes in video editors
3. **Clear audio** - Speak slowly and clearly
4. **Show key points** - Highlight important code sections
5. **Test first** - Do a quick test run before final recording

---

**Estimated Total Runtime**: 15-20 minutes
**Output File**: `loan_system_demo.mp4` or `loan_system_demo.mkv`
