import streamlit as st
import matplotlib.pyplot as plt

# 🌟 App Title
st.title("💰 Financial Risk Analytics Dashboard")
st.write("📊 Enter borrower details to assess loan risk")

# 🧾 Inputs
income = st.number_input("💼 Annual Income", min_value=0)
credit_score = st.number_input("📉 Credit Score", min_value=300, max_value=850)
debt_ratio = st.slider("📊 Debt to Income Ratio", 0.0, 1.0, 0.3)
loan_amount = st.number_input("🏦 Loan Amount", min_value=0)

# 🚀 Button
if st.button("🔍 Assess Risk"):

    # 🧠 Risk Score Formula
    score = (
        (loan_amount / (income + 1)) * 50
        + (700 - credit_score) * 0.1
        + debt_ratio * 50
    )

    # 🎯 Risk Classification
    if score < 30:
        level = "🟢 Low Risk"
        color = "green"
        suggestion = "✅ Good candidate for loan approval."

    elif score < 70:
        level = "🟠 Medium Risk"
        color = "orange"
        suggestion = "⚠️ Review financial history before approval."

    else:
        level = "🔴 High Risk"
        color = "red"
        suggestion = "❌ High chance of default. Reject or require collateral."

    # 📊 Results
    st.subheader(f"📌 Risk Score: {score:.2f}")
    st.markdown(f"### Risk Level: :{color}[{level}]")
    st.info(f"💡 Suggestion: {suggestion}")

    # 🧠 Risk Explanation
    reasons = []

    if credit_score < 600:
        reasons.append("📉 Low credit score")

    if debt_ratio > 0.4:
        reasons.append("📊 High debt-to-income ratio")

    if income < 30000:
        reasons.append("💼 Low annual income")

    if loan_amount > 50000:
        reasons.append("🏦 Large loan amount")

    # ✅ Safe Applicant Explanation
    if len(reasons) == 0:
        reasons.append("✅ Strong financial profile")
        reasons.append("✅ Healthy credit score")
        reasons.append("✅ Manageable debt ratio")

    st.subheader("📌 Risk Explanation")

    for reason in reasons:
        st.write("-", reason)

    # 📈 Progress Bar
    st.progress(min(int(score), 100))

    # 📊 Visualization
    fig, ax = plt.subplots()

    ax.bar(
        ["💼 Income", "📉 Credit Score", "📊 Debt Ratio", "🏦 Loan Amount"],
        [income, credit_score, debt_ratio * 100, loan_amount]
    )

    ax.set_title("📊 Borrower Financial Profile")

    st.pyplot(fig)