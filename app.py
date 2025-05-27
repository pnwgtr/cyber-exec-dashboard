# Streamlit Multi‑Page Cybersecurity Dashboard with Horizontal Navigation
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# ---------- Page & Theme ----------
st.set_page_config(layout="wide")  # full‑width layout
preview_bg = "#f0f2f6"             # soft grey plot background

# ---------- Global Style ----------
# enlarge horizontal tab text
st.markdown(
    """
    <style>
/* fallback 1: target the tab button itself */
button[data-baseweb="tab"] span {
    font-size: 24px !important;
    font-weight: 800 !important;
}
/* fallback 2: any direct child span of tab button */
div[data-testid="stTabs"] button span {
    font-size: 24px !important;
    font-weight: 800 !important;
}
</style>
    """,
    unsafe_allow_html=True,
)

# ---------- Helper to build mini chart ----------
def mini_line(data, color, title):
    fig, ax = plt.subplots(figsize=(3, 2))
    fig.patch.set_facecolor("none")
    ax.set_facecolor(preview_bg)
    ax.plot(data, marker="o", color=color)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=10)
    st.pyplot(fig, use_container_width=True)


def mini_bar(labels, values, color, title):
    fig, ax = plt.subplots(figsize=(3, 2))
    fig.patch.set_facecolor("none")
    ax.set_facecolor(preview_bg)
    ax.bar(labels, values, color=color)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=10)
    st.pyplot(fig, use_container_width=True)

# ---------- Horizontal Navigation ----------
tabs = st.tabs([
    "Dashboard",
    "Vulnerabilities",
    "Phishing",
    "MFA Adoption",
    "Incidents",
    "Tool Inventory",
    "Culture & Awareness",
    "Compliance"
])

# ===============  DASHBOARD  ===============
with tabs[0]:
    st.title("Cybersecurity Executive Dashboard")
    st.caption("High‑level summary of current cybersecurity posture.")

    # KPI cards
    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("Critical Vulns (30d)", "11", "-4 🔻")
    k2.metric("Phishing Emails Blocked", "760", "-140 🔻")
    k3.metric("Endpoint Coverage", "87%", "+3% 🔺")
    k4.metric("MFA Adoption", "92%", "+4% 🔺")
    k5.metric("Incidents This Month", "3", "+1 🔺")

    st.markdown("---")
    

    # ----- Mini‑chart ribbon -----
    with st.container():
        # Row 1
        c1, c2, c3 = st.columns(3)
        with c1:
            
            mini_line([45, 39, 31, 22, 15, 11], "#1f77b4", "Vuln Trend")
        with c2:
            
            mini_bar(['Jan','Feb','Mar','Apr','May','Jun'], [820,640,975,1120,900,760], "#ff7f0e", "Phishing Trend")
        with c3:
            
            mini_line([70,75,80,85,88,92], "#2ca02c", "MFA Trend")

        st.divider()

        # Row 2
        c4, c5, c6 = st.columns(3)
        with c4:
            
            mini_bar(['Apr','May'], [2,3], "#d62728", "Incidents")
        with c5:
            
            mini_bar(['CrowdStrike','Defender','Tenable'], [100,60,100], "#9467bd", "Tool Coverage")
        with c6:
            
            mini_bar(['NIST CSF','PCI DSS'], [72,64], "#8c564b", "Compliance")

# ===============  VULNERABILITIES  ===============
with tabs[1]:
    st.title("Vulnerability Remediation Trend")
    st.caption("Monthly reduction in open critical vulnerabilities.")
    vuln_df = pd.DataFrame({
        "Date": pd.date_range(end=pd.Timestamp.today(), periods=6, freq="M"),
        "Critical Vulns": [45, 39, 31, 22, 15, 11]
    })
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("none")
    ax.set_facecolor(preview_bg)
    ax.plot(vuln_df["Date"], vuln_df["Critical Vulns"], marker="o", color="#1f77b4")
    ax.set_ylabel("Open Critical Vulns")
    ax.set_xlabel("Month")
    ax.set_title("Critical Vulnerabilities Over Time")
    st.pyplot(fig, use_container_width=True)

# ===============  PHISHING  ===============
with tabs[2]:
    st.title("Phishing Detection Trend")
    st.caption("Monthly phishing email block volume.")
    fishing_df = pd.DataFrame({
        "Month": ['Jan','Feb','Mar','Apr','May','Jun'],
        "Blocked Emails": [820,640,975,1120,900,760]
    })
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("none")
    ax.set_facecolor(preview_bg)
    ax.bar(fishing_df["Month"], fishing_df["Blocked Emails"], color="#ff7f0e")
    ax.set_ylabel("Blocked Emails")
    ax.set_title("Phishing Emails Blocked per Month")
    st.pyplot(fig, use_container_width=True)

# ===============  MFA ADOPTION  ===============
with tabs[3]:
    st.title("MFA Adoption Trend")
    st.caption("Growth in multifactor authentication coverage.")
    mfa_df = pd.DataFrame({
        "Month": ['Jan','Feb','Mar','Apr','May','Jun'],
        "MFA %": [70,75,80,85,88,92]
    })
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("none")
    ax.set_facecolor(preview_bg)
    ax.plot(mfa_df["Month"], mfa_df["MFA %"], marker="o", color="#2ca02c")
    ax.set_ylabel("MFA Adoption (%)")
    ax.set_title("MFA Adoption Rate Over Time")
    st.pyplot(fig, use_container_width=True)

# ===============  INCIDENTS  ===============
with tabs[4]:
    st.title("Incident Response Details")
    st.caption("Recent security incidents and mitigation status.")
    incident_df = pd.DataFrame({
        "Date": ['2025‑05‑01','2025‑05‑10','2025‑05‑19'],
        "Type": ['Phishing','Credential Theft','Ransomware Attempt'],
        "Impact": ['None','Single user','Blocked by EDR'],
        "Status": ['Resolved','Resolved','Mitigated']
    })
    st.dataframe(incident_df, use_container_width=True)

# ===============  TOOL INVENTORY  ===============
with tabs[5]:
    st.title("Security Tool Inventory")
    st.caption("Tool categories, owners, and deployment status.")
    tool_df = pd.DataFrame({
        "Tool": ['CrowdStrike','Defender','Tenable','Chronicle','Abnormal'],
        "Category": ['EDR','EDR','Vuln Mgmt','SIEM','Email Security'],
        "Owner": ['SecOps','IT','SecOps','SecOps','SecOps'],
        "Status": ['Active','Partial','Active','Active','Active']
    })
    st.dataframe(tool_df, use_container_width=True)

# ===============  CULTURE & AWARENESS  ===============
with tabs[6]:
    st.title("Security Culture and Awareness")
    st.caption("User behaviour, training results, and phishing test feedback.")
    culture_df = pd.DataFrame({
        "Question": [
            "Know who to call in a cyber emergency?",
            "Would report a suspicious email?",
            "Does security interfere with your job?"
        ],
        "Yes %": [82,94,29],
        "No %": [18,6,71]
    })
    st.dataframe(culture_df)

# ===============  COMPLIANCE  ===============
with tabs[7]:
    st.title("Compliance Scorecard")
    st.caption("Alignment with major regulatory frameworks.")
    comp_df = pd.DataFrame({
        "Framework": ['NIST CSF','PCI DSS 4.0'],
        "Compliance Score": [72,64],
        "Gaps Noted": [
            "Recovery & Response underdeveloped",
            "Admin MFA and segmentation gaps"
        ]
    })
    st.dataframe(comp_df)
