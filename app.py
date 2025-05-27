import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cybersecurity Executive Dashboard", layout="wide")

# --- MOCK DATA ---
vuln_data = pd.DataFrame({
    'Date': pd.date_range(end=pd.Timestamp.today(), periods=6, freq='M'),
    'Critical Vulns': [45, 39, 31, 22, 15, 11]
})

phishing_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Blocked Emails': [820, 640, 975, 1120, 900, 760]
})

endpoint_coverage = 0.87  # 87%

# --- HEADER ---
st.title("🚨 Cybersecurity Executive Dashboard")
st.markdown("High-level overview of cybersecurity posture and business impact.")

# --- KPI CARDS ---
col1, col2, col3 = st.columns(3)
col1.metric("📉 Critical Vulns (30 days)", "11", "-4")
col2.metric("📥 Phishing Emails Blocked (this month)", "760", "-140")
col3.metric("🛡️ Endpoint Coverage", f"{int(endpoint_coverage * 100)}%", "+3%")

st.markdown("---")

# --- TRENDS ---
st.subheader("📈 Vulnerability Remediation Trend")
fig1, ax1 = plt.subplots()
ax1.plot(vuln_data['Date'], vuln_data['Critical Vulns'], marker='o')
ax1.set_title("Critical Vulnerabilities Over Time")
ax1.set_ylabel("Count")
ax1.set_xlabel("Date")
st.pyplot(fig1)

st.subheader("📧 Phishing Emails Blocked Trend")
fig2, ax2 = plt.subplots()
ax2.bar(phishing_data['Month'], phishing_data['Blocked Emails'])
ax2.set_title("Monthly Phishing Blocks")
ax2.set_ylabel("Count")
st.pyplot(fig2)

# --- RISK TABLE ---
st.subheader("📋 Current Business Risk Areas")
risk_df = pd.DataFrame({
    'Risk Area': ['Legacy Systems', 'Email Threats', 'Patch Management', 'Shadow IT'],
    'Risk Level': ['High', 'Medium', 'Medium', 'High'],
    'Notes': [
        'Multiple unpatchable systems still in prod',
        'Spike in phishing attempts past 90 days',
        'Patch fatigue in key operations teams',
        'Unknown apps communicating with external endpoints'
    ]
})
st.dataframe(risk_df, use_container_width=True)

# --- BUSINESS TRANSLATION ---
st.markdown("### 🧠 Business Impact")
st.markdown("""
- **Rising phishing threats** require continued investment in awareness and detection.
- **Legacy systems** create long-term operational and compliance risk.
- **Improved patching** shows progress, but gaps remain in production systems.
- **Endpoint coverage** at 87% is good — but needs full 100% to reduce blast radius.
""")
