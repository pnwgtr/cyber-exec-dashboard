# Streamlit Multi-Page Cybersecurity Dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Sidebar Navigation
page = st.sidebar.selectbox("Select a page", [
    "Dashboard",
    "Incidents",
    "Tool Inventory",
    "Culture & Awareness",
    "Compliance"
])

# Dashboard Page
if page == "Dashboard":
    st.title("Cybersecurity Executive Dashboard")
    st.caption("High-level summary of current cybersecurity posture.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Critical Vulns (30d)", "11", "-4")
    col2.metric("Phishing Emails Blocked", "760", "-140")
    col3.metric("Endpoint Coverage", "87%")

    st.subheader("MFA Adoption Trend")
    mfa_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'MFA %': [70, 75, 80, 85, 88, 92]
    })
    fig, ax = plt.subplots()
    ax.plot(mfa_data['Month'], mfa_data['MFA %'], marker='o')
    ax.set_ylabel("MFA Adoption (%)")
    st.pyplot(fig)

# Incidents Page
elif page == "Incidents":
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
elif page == "Tool Inventory":
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
elif page == "Culture & Awareness":
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
elif page == "Compliance":
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
