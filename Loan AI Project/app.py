import streamlit as st # pyright: ignore[reportMissingImports]
import requests
from datetime import datetime

st.set_page_config(
    page_title="Loan Approval AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .approval {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    }
    .rejection {
        background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);
    }
    .result-section {
        margin-top: 2rem;
        padding: 2rem;
        border-radius: 10px;
        background: #f8f9fa;
        border-left: 5px solid #667eea;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 💰 Loan Approval AI System")
st.markdown("*Intelligent loan application processing powered by AI agents*")
st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📋 Application Details")

    col_left, col_right = st.columns(2)

    with col_left:
        age = st.number_input(
            "👤 Age",
            min_value=18,
            max_value=100,
            value=30,
            step=1
        )
        income = st.number_input(
            "💵 Annual Income ($)",
            min_value=0,
            value=60000,
            step=5000
        )

    with col_right:
        employment = st.selectbox(
            "💼 Employment Type",
            ["Full-time", "Self-employed"]
        )
        loan_amount = st.number_input(
            "🏦 Loan Amount ($)",
            min_value=0,
            value=100000,
            step=10000
        )

with col2:
    st.markdown("### 📊 Quick Stats")
    if income > 0:
        dti = (loan_amount / 12) / (income / 12)
        st.metric("Debt-to-Income", f"{dti:.2f}")
    st.metric("Employment Risk", "🟢 Low" if employment == "Full-time" else "🟡 Medium")

st.divider()

col_submit, col_reset = st.columns(2)

with col_submit:
    submit_btn = st.button("🚀 Submit Application", use_container_width=True, type="primary")

with col_reset:
    if st.button("🔄 Reset Form", use_container_width=True):
        st.rerun()

if submit_btn:
    payload = {
        "age": age,
        "income": income,
        "employment": employment,
        "loan_amount": loan_amount
    }

    try:
        with st.spinner("🔍 Analyzing your application..."):
            response = requests.post("http://127.0.0.1:8000/loan", json=payload, timeout=10)
            result = response.json()

        st.markdown("### ✨ Analysis Result")

        decision = result.get("decision", "UNKNOWN")

        if decision == "APPROVED":
            st.markdown("""
                <div class="result-section approval" style="border-left-color: #38ef7d;">
                    <h2 style="color: white; margin: 0;">✅ Application Approved!</h2>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="result-section rejection" style="border-left-color: #ff6a00;">
                    <h2 style="color: white; margin: 0;">❌ Application Rejected</h2>
                </div>
            """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            profile = result.get("profile", {})
            st.markdown("#### 👤 Profile Analysis")
            st.write(f"**Income Stability:** {profile.get('income_stability', 'N/A')}")
            st.write(f"**Employment Risk:** {profile.get('employment_risk', 'N/A')}")

        with col2:
            risk = result.get("risk", {})
            st.markdown("#### ⚠️ Risk Assessment")
            st.write(f"**DTI Ratio:** {risk.get('dti', 'N/A')}")
            st.write(f"**Risk Level:** {risk.get('risk_level', 'N/A')}")

        with col3:
            final = result.get("final", {})
            st.markdown("#### 📋 Final Decision")
            decision_display = "✅ APPROVED" if decision == "APPROVED" else "❌ REJECTED"
            st.write(f"**Decision:** {decision_display}")
            st.write(f"**Status:** {final.get('status', 'N/A')}")
            st.write(f"**Time:** {final.get('timestamp', 'N/A')}")

        st.divider()
        st.markdown("#### 📊 Full Analysis Details")
        with st.expander("View detailed results"):
            st.json(result)

    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to API. Make sure FastAPI is running on http://127.0.0.1:8000")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

