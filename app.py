# Streamlit Multi-Page Cybersecurity Dashboard with Buttons
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Navigation using buttons
st.sidebar.title("Navigation")
pages = [
    "Dashboard",
    "Vulnerabilities",
    "Phishing",
    "MFA Adoption",
    "Incidents",
    "Tool Inventory",
    "Culture & Awareness",
    "Compliance"
]

selected_page = None
for p in pages:
    if st.sidebar.button(p):
        selected_page = p

# Default to Dashboard if no button is pressed yet
if selected_page is None:
    selected_page = "Dashboard"

# Dashboard Page
if selected_page == "Dashboard":
    st.title("Cybersecurity Executive Dashboard")
    st.caption("High-level summary of current cybersecurity posture.")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Critical Vulns (30d)", "11", "-4")
    col2.metric("Phishing Emails Blocked", "760", "-140")
    col3.metric("Endpoint Coverage", "87%")
    col4.metric("MFA Adoption", "92%")
    col5.metric("Incidents This Month", "3")

# Vulnerabilities Page
elif selected_page == "Vulnerabilities":
    st.title("Vulnerability Remediation Trend")
    st.caption("Shows monthly reduction in open critical vulnerabilities.")
    vuln_data = pd.DataFrame({
        'Date': pd.date_range(end=pd.Timestamp.today(), periods=6, freq='M'),
        'Critical Vulns': [45, 39, 31, 22, 15, 11]
    })
    fig, ax = plt.subplots()
    ax.plot(vuln_data['Date'], vuln_data['Critical Vulns'], marker='o')
    ax.set_ylabel("Open Critical Vulns")
    ax.set_xlabel("Month")
    ax.set_title("Critical Vulnerabilities Over Time")
    st.pyplot(fig)

# Phishing Page
elif selected_page == "Phishing":
    st.title("Phishing Detection Trend")
    st.caption("Monthly phishing email block volume.")
    phishing_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Blocked Emails': [820, 640, 975, 1120, 900, 760]
    })
    fig, ax = plt.subplots()
    ax.bar(phishing_data['Month'], phishing_data['Blocked Emails'])
    ax.set_ylabel("Blocked Emails")
    ax.set_title("Phishing Emails Blocked per Month")
    st.pyplot(fig)

# MFA Adoption Page
elif selected_page == "MFA Adoption":
    st.title("MFA Adoption Trend")
    st.caption("Tracks growth in multifactor authentication coverage.")
    mfa_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'MFA %': [70, 75, 80, 85, 88, 92]
    })
    fig, ax = plt.subplots()
    ax.plot(mfa_data['Month'], mfa_data['MFA %'], marker='o')
    ax.set_ylabel("MFA Adoption (%)")
    ax.set_title("MFA Adoption Rate Over Time")
    st.pyplot(fig)

# Incidents Page
elif selected_page == "Incidents":
    st.title("Incident Response Details")
    st.caption("Recent security incidents and mitigation status.")
    incident_df = pd.DataFrame({
        'Date': ['2025-05-01', '2025-05-10', '2025-05-19'],
        'Type': ['Phishing', 'Credential Theft', 'Ransomware Attempt'],
        'Impact': ['None', 'Single user affected', 'Blocked by EDR'],
        'Status': ['Resolved', 'Resolved', 'Mitigated']
    })
    st.dataframe(incident_df, use_container_width=True)

# Tool Inventory Page
elif selected_page == "Tool Inventory":
    st.title("Security Tool Inventory")
    st.caption("Tool categories, owners, and status.")
    tool_df = pd.DataFrame({
        'Tool': ['CrowdStrike', 'Defender', 'Tenable', 'Chronicle', 'Abnormal'],
        'Category': ['EDR', 'EDR', 'Vuln Mgmt', 'SIEM', 'Email Security'],
        'Owner': ['SecOps', 'IT', 'SecOps', 'SecOps', 'SecOps'],
        'Status': ['Active', 'Partial', 'Active', 'Active', 'Active']
    })
    st.dataframe(tool_df, use_container_width=True)

# Culture & Awareness Page
elif selected_page == "Culture & Awareness":
    st.title("Security Culture and Awareness")
    st.caption("User behavior, training results, and phishing test feedback.")
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

# Compliance Page
elif selected_page == "Compliance":
    st.title("Compliance Scorecard")
    st.caption("Alignment with major regulatory frameworks.")
    compliance_df = pd.DataFrame({
        'Framework': ['NIST CSF', 'PCI DSS 4.0'],
        'Compliance Score': [72, 64],
        'Gaps Noted': [
            'Recovery & Response functions underdeveloped',
            'Admin MFA and segmentation gaps'
        ]
    })
    st.dataframe(compliance_df)
