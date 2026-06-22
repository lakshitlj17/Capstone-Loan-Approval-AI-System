# 📋 Demo Test Data - Copy & Paste Ready

Use these pre-prepared test cases during your recording for smooth demonstrations.

---

## Scenario 1: **APPROVED** ✅ (Low Risk Profile)

**Description**: Stable employed person with good income-to-loan ratio

### Input Values:
```
Age: 45
Income: 150,000
Employment: Full-time
Loan Amount: 75,000
```

### Expected Output:
- **Debt-to-Income Ratio**: ~0.50 (50%)
- **Risk Level**: Low to Moderate
- **Decision**: APPROVED ✅
- **Status**: Processed

### Why This Works:
- Age shows maturity and stability
- High income relative to loan amount
- DTI well below 1.0 threshold
- Established employment

---

## Scenario 2: **REJECTED** ❌ (High Risk Profile)

**Description**: Young applicant with insufficient income for large loan

### Input Values:
```
Age: 25
Income: 35,000
Employment: Full-time
Loan Amount: 200,000
```

### Expected Output:
- **Debt-to-Income Ratio**: ~5.71 (571%)
- **Risk Level**: Very High
- **Decision**: REJECTED ❌
- **Status**: Processed

### Why This Gets Rejected:
- Extremely high DTI (>5.0)
- Income insufficient for loan amount
- High financial risk
- Likely default probability

---

## Scenario 3: **MODERATE RISK** ⚠️ (Borderline Case)

**Description**: Mid-range applicant with moderate financial metrics

### Input Values:
```
Age: 35
Income: 80,000
Employment: Full-time
Loan Amount: 100,000
```

### Expected Output:
- **Debt-to-Income Ratio**: ~1.25 (125%)
- **Risk Level**: Moderate
- **Decision**: May vary (depends on compliance rules)
- **Status**: Processed

### Why It's Borderline:
- DTI slightly above 1.0
- Income reasonable but not high
- Moderate age suggests some stability
- Risk factors balanced

---

## Scenario 4: **LOW RISK** ✅ (Excellent Profile)

**Description**: Established professional with strong financial position

### Input Values:
```
Age: 50
Income: 250,000
Employment: Full-time
Loan Amount: 80,000
```

### Expected Output:
- **Debt-to-Income Ratio**: ~0.32 (32%)
- **Risk Level**: Low
- **Decision**: APPROVED ✅
- **Status**: Processed

### Why This Is Approved:
- Very low DTI (< 0.5)
- High income significantly exceeds loan
- Mature age indicates stability
- Strong financial position

---

## Scenario 5: **EDGE CASE** 🔍 (Interesting Profile)

**Description**: Young but high-earning professional

### Input Values:
```
Age: 28
Income: 120,000
Employment: Full-time
Loan Amount: 90,000
```

### Expected Output:
- **Debt-to-Income Ratio**: ~0.75 (75%)
- **Risk Level**: Low to Moderate
- **Decision**: APPROVED ✅
- **Status**: Processed

### Why It's Interesting:
- Young age (typically higher risk)
- But high income (reduces risk)
- Good DTI despite young profile
- Shows system adapts to multiple factors

---

## API Testing Commands (Paste in Terminal)

### Scenario 1 (Approved):
```bash
curl -X POST http://localhost:8000/loan \
  -H "Content-Type: application/json" \
  -d '{"age": 45, "income": 150000, "employment": "Full-time", "loan_amount": 75000}'
```

### Scenario 2 (Rejected):
```bash
curl -X POST http://localhost:8000/loan \
  -H "Content-Type: application/json" \
  -d '{"age": 25, "income": 35000, "employment": "Full-time", "loan_amount": 200000}'
```

### Scenario 3 (Moderate):
```bash
curl -X POST http://localhost:8000/loan \
  -H "Content-Type: application/json" \
  -d '{"age": 35, "income": 80000, "employment": "Full-time", "loan_amount": 100000}'
```

### Scenario 4 (Low Risk):
```bash
curl -X POST http://localhost:8000/loan \
  -H "Content-Type: application/json" \
  -d '{"age": 50, "income": 250000, "employment": "Full-time", "loan_amount": 80000}'
```

### Scenario 5 (Edge Case):
```bash
curl -X POST http://localhost:8000/loan \
  -H "Content-Type: application/json" \
  -d '{"age": 28, "income": 120000, "employment": "Full-time", "loan_amount": 90000}'
```

---

## Quick Reference: DTI Calculation

**Formula**: Loan Amount ÷ Annual Income = DTI

### Risk Levels by DTI:
- **DTI < 0.5**: Low Risk ✅ (Likely Approved)
- **DTI 0.5 - 1.0**: Moderate Risk ⚠️ (Usually Approved)
- **DTI 1.0 - 2.0**: High Risk ⚠️ (Often Rejected)
- **DTI > 2.0**: Very High Risk ❌ (Usually Rejected)

---

## Narration Script by Scenario

### When Testing Scenario 1:
```
"First, let's test a strong applicant. This is someone 45 years old 
with a good income of $150,000 and requesting a $75,000 loan. 
You can see the debt-to-income ratio is healthy at 0.50, 
so this application gets APPROVED."
```

### When Testing Scenario 2:
```
"Now let's see what happens with a higher-risk profile. 
This applicant is younger (25) with lower income ($35,000) 
but requesting a large loan ($200,000). 
The DTI jumps to 5.71 - far too high. This application is REJECTED."
```

### When Testing Scenario 3:
```
"Here's an interesting middle case. The applicant is 35 with 
$80,000 income and a $100,000 loan request. 
The DTI is 1.25 - right on the borderline. 
The system carefully evaluates this based on all factors."
```

### When Testing Scenario 4:
```
"For comparison, here's an excellent profile. 
Age 50, income $250,000, requesting only $80,000. 
The DTI is just 0.32 - very strong. 
This is definitely APPROVED."
```

### When Testing Scenario 5:
```
"Finally, let's see how the system handles conflicting signals. 
This applicant is young (28) but with high income ($120,000). 
The DTI is good at 0.75. The system correctly weighs both factors 
and approves based on the strong income. Shows the system isn't just age-biased."
```

---

## Employment Types to Mention

When narrating, you can reference these employment types:
- **Full-time**: Standard permanent employment
- **Part-time**: May indicate lower stability
- **Self-employed**: Higher uncertainty in income
- **Contract**: Time-limited engagement risk

---

## Tips for Demo Flow

1. **Start with Scenario 1** (successful case - builds confidence)
2. **Show Scenario 2** (rejection case - shows system boundaries)
3. **Demonstrate Scenario 3** (borderline - shows nuance)
4. **Compare with Scenario 4** (best case - dramatic contrast)
5. **Explain Scenario 5** (complexity - shows sophistication)

---

## Optional: Load Testing Data

If you want to show multiple applications at once:

```bash
# Create a test file with multiple applications
cat > test_data.json << 'EOF'
[
  {"age": 45, "income": 150000, "employment": "Full-time", "loan_amount": 75000},
  {"age": 25, "income": 35000, "employment": "Full-time", "loan_amount": 200000},
  {"age": 35, "income": 80000, "employment": "Full-time", "loan_amount": 100000},
  {"age": 50, "income": 250000, "employment": "Full-time", "loan_amount": 80000},
  {"age": 28, "income": 120000, "employment": "Full-time", "loan_amount": 90000}
]
EOF
```

---

## Remember During Recording

✅ Fill in values **slowly** - viewers should see what you're typing  
✅ Wait for results to fully load before moving to next step  
✅ Point out the DTI calculation on screen  
✅ Explain WHY each decision was made  
✅ Pause between scenarios for narration  

---

**Good luck with your recording! Use these scenarios to show the system's capabilities and robustness.**
