import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Page configuration
st.set_page_config(page_title="Cybersecurity Executive Dashboard", layout="wide")

# Title
st.title("Cybersecurity Executive Dashboard")
st.caption("This dashboard provides a high-level view of cybersecurity posture, operational risks, and strategic readiness.")

# === KPI Overview Cards ===
st.header("Key Performance Indicators")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Critical Vulns (30d)", "11", "-4")
col1.caption("Number of unresolved critical vulnerabilities in the last 30 days.")
col2.metric("Phishing Emails Blocked", "760", "-140")
col2.caption("Email threats intercepted this month.")
col3.metric("Endpoint Coverage", "87%")
col3.caption("Percent of known assets reporting to EDR.")
col4.metric("MFA Adoption", "92%")
col4.caption("Percentage of users with multifactor authentication enabled.")
col5.metric("Incidents This Month", "3")
col5.caption("Confirmed incidents investigated this month.")

st.markdown("---")

# === Vulnerability Remediation Trend ===
st.subheader("Vulnerability Remediation Trend")
st.caption("Shows monthly reduction in open critical vulnerabilities.")

vuln_data = pd.DataFrame({
    'Date': pd.date_range(end=pd.Timestamp.today(), periods=6, freq='M'),
    'Critical Vulns': [45, 39, 31, 22, 15, 11]
})
fig1, ax1 = plt.subplots()
ax1.plot(vuln_data['Date'], vuln_data['Critical Vulns'], marker='o')
ax1.set_ylabel("Open Critical Vulns")
ax1.set_xlabel("Month")
ax1.set_title("Critical Vulnerabilities Over Time")
st.pyplot(fig1)

# === Phishing Block Trend ===
st.subheader("Phishing Detection Trend")
st.caption("Monthly phishing email block volume.")

phishing_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Blocked Emails': [820, 640, 975, 1120, 900, 760]
})
fig2, ax2 = plt.subplots()
ax2.bar(phishing_data['Month'], phishing_data['Blocked Emails'])
ax2.set_ylabel("Blocked Emails")
ax2.set_title("Phishing Emails Blocked per Month")
st.pyplot(fig2)

# === MFA Adoption ===
st.subheader("MFA Adoption Trend")
st.caption("Tracks growth in multifactor authentication coverage.")

mfa_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'MFA Adoption %': [70, 75, 80, 85, 88, 92]
})
fig3, ax3 = plt.subplots()
ax3.plot(mfa_data['Month'], mfa_data['MFA Adoption %'], marker='o')
ax3.set_ylabel("MFA Adoption (%)")
ax3.set_title("MFA Adoption Rate Over Time")
st.pyplot(fig3)

st.markdown("---")

# === Endpoint Health ===
st.header("Endpoint and Asset Health")

endpoint_labels = ['Healthy', 'At Risk', 'Offline']
endpoint_sizes = [70, 20, 10]
fig4, ax4 = plt.subplots()
ax4.pie(endpoint_sizes, labels=endpoint_labels, autopct='%1.1f%%', startangle=90)
ax4.axis('equal')
st.caption("Distribution of endpoint health statuses from EDR platform.")
st.pyplot(fig4)

# === Risky Devices Table ===
st.subheader("Top 5 At-Risk Devices")
st.caption("Devices exhibiting signs of elevated risk or non-compliance.")
risky_df = pd.DataFrame({
    'Device': ['LPT1234', 'LPT5678', 'SRV001', 'LPT9999', 'SRV999'],
    'Department': ['Marketing', 'Finance', 'IT', 'Gaming', 'Ops'],
    'Risk Reason': ['Missing patches', 'Old OS', 'AV disabled', 'No EDR', 'Not seen in 7 days'],
    'Last Seen': ['3 days ago', 'Yesterday', '5 days ago', '10 days ago', 'Unknown']
})
st.dataframe(risky_df, use_container_width=True)

st.markdown("---")

# === Incidents Summary ===
st.header("Recent Cybersecurity Incidents")
st.caption("Confirmed security incidents and mitigation outcomes.")

incident_df = pd.DataFrame({
    'Date': ['2025-05-01', '2025-05-10', '2025-05-19'],
    'Type': ['Phishing', 'Credential Theft', 'Ransomware Attempt'],
    'Impact': ['None', 'Single user affected', 'Blocked by EDR'],
    'Status': ['Resolved', 'Resolved', 'Mitigated']
})
st.dataframe(incident_df, use_container_width=True)

# === Business Risk Table ===
st.subheader("Business Risk Summary")
st.caption("Mapped security risks with mitigation recommendations.")

risk_df = pd.DataFrame({
    'Risk Area': ['Legacy Systems', 'Email Threats', 'Patch Management', 'Shadow IT'],
    'Risk Level': ['High', 'Medium', 'Medium', 'High'],
    'Description': [
        'Unpatchable systems in production.',
        'Increased phishing attempts this quarter.',
        'Delayed patch cycles in operations.',
        'Unauthorized software observed in network.'
    ],
    'Recommendation': [
        'Isolate or decommission outdated systems.',
        'Enhance filters and increase user testing.',
        'Enforce regular patch SLAs.',
        'Implement SaaS access monitoring tools.'
    ]
})
st.dataframe(risk_df, use_container_width=True)

# === Tool Inventory ===
st.header("Security Tool Inventory")
st.caption("Overview of active security tools, categories, and notes.")

tool_df = pd.DataFrame({
    'Tool': ['CrowdStrike', 'Defender', 'Tenable', 'Chronicle', 'Abnormal'],
    'Category': ['EDR', 'EDR', 'Vuln Mgmt', 'SIEM', 'Email Security'],
    'Owner': ['SecOps', 'IT', 'SecOps', 'SecOps', 'SecOps'],
    'Status': ['Active', 'Partial', 'Active', 'Active', 'Active'],
    'Notes': ['Fully deployed', 'Overlap with CS', 'Weekly scans', 'GCP integration', 'Stops BEC']
})
st.dataframe(tool_df, use_container_width=True)

# === Culture Metrics ===
st.header("Security Culture and Awareness")
st.caption("Pulse check on end-user attitudes and readiness.")

culture_df = pd.DataFrame({
    'Question': [
        'Do you know who to contact in a cyber emergency?',
        'Would you report a suspicious email?',
        'Does security interfere with your job?'
    ],
    'Yes %': [82, 94, 29],
    'No %': [18, 6, 71]
})
st.dataframe(culture_df)

# === Compliance Scorecard ===
st.header("Compliance Readiness Scorecard")
st.caption("Current state against major frameworks.")

compliance_df = pd.DataFrame({
    'Framework': ['NIST CSF', 'PCI DSS 4.0'],
    'Compliance Score': [72, 64],
    'Gaps Noted': [
        'Recovery & Response functions underdeveloped',
        'Admin MFA and segmentation gaps'
    ]
})
st.dataframe(compliance_df)

# === Filters (Sidebar) ===
st.sidebar.header("Filters")
st.sidebar.date_input("Date Range", [datetime.date(2025, 1, 1), datetime.date.today()])
st.sidebar.selectbox("Department", options=["All", "HR", "Finance", "Gaming", "Ops", "IT", "Marketing"])
st.sidebar.selectbox("Threat Category", options=["All", "Phishing", "Ransomware", "Malware", "Insider", "Other"])
