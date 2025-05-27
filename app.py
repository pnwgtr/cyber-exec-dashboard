# Streamlit Cybersecurity Dashboard with Custom Horizontal Button Navigation
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# ---------- Page config ----------
st.set_page_config(layout="wide")
preview_bg = "#f0f2f6"

# ---------- Global style: big, bold nav buttons ----------
st.markdown(
    """
    <style>
/* Nav buttons equally distributed & centered text */
div[data-testid="column"] button {
    width: 100% !important;      /* fill column width */
    text-align: center !important;
    font-size: 1.8rem !important;
    font-weight: 800 !important;
    padding: 1rem 0 !important;
    display: block !important;
}

/* Center metric labels and values */
div[data-testid="stMetric-label"] {
    text-align: center !important;
    font-weight: 700;
}

div[data-testid="stMetric-value"] {
    text-align: center !important;
    font-weight: 800;
}


</style>
    """,
    unsafe_allow_html=True,
)

# ---------- Helper mini‑charts ----------

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

# ---------- Custom navigation bar ----------
PAGES = [
    "Dashboard",
    "Vulnerabilities",
    "Phishing",
    "MFA Adoption",
    "Incidents",
    "Tool Inventory",
    "Culture",
    "Compliance",
]

if "page" not in st.session_state:
    st.session_state["page"] = "Dashboard"

nav_cols = st.columns(len(PAGES))
for col, page_name in zip(nav_cols, PAGES):
    if col.button(page_name, key=f"nav_{page_name}"):
        st.session_state["page"] = page_name

page = st.session_state["page"]

# ---------- Dashboard ----------
if page == "Dashboard":
    st.title("Cybersecurity Executive Dashboard")
    st.caption("High‑level summary of current cybersecurity posture.")

    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("Critical Vulns (30d)", "11", "-4 🔻")
    k2.metric("Phishing Emails Blocked", "760", "-140 🔻")
    k3.metric("Endpoint Coverage", "87%", "+3% 🔺")
    k4.metric("MFA Adoption", "92%", "+4% 🔺")
    k5.metric("Incidents This Month", "3", "+1 🔺")

    st.markdown("---")

    with st.container():
        r1c1, r1c2, r1c3 = st.columns(3)
        with r1c1:
            mini_line([45, 39, 31, 22, 15, 11], "#1f77b4", "Vuln Trend")
            sub1, sub2, sub3 = st.columns([1,2,1])
            with sub2:
                if st.button("See detailed chart", key="box_vuln", help="Open full Vulnerabilities chart"):
                    st.session_state["page"] = "Vulnerabilities"
        with r1c2:
            mini_bar(["Jan","Feb","Mar","Apr","May","Jun"], [820,640,975,1120,900,760], "#ff7f0e", "Phishing Trend")
            sub1, sub2, sub3 = st.columns([1,2,1])
            with sub2:
                if st.button("See detailed chart", key="box_phish", help="Open full Phishing chart"):
                    st.session_state["page"] = "Phishing"
        with r1c3:
            mini_line([70,75,80,85,88,92], "#2ca02c", "MFA Trend")
            sub1, sub2, sub3 = st.columns([1,2,1])
            with sub2:
                if st.button("See detailed chart", key="box_mfa", help="Open full MFA chart"):
                    st.session_state["page"] = "MFA Adoption"

        st.divider()
        r2c1, r2c2, r2c3 = st.columns(3)
        with r2c1:
            mini_bar(["Apr","May"], [2,3], "#d62728", "Incidents")
            sub1, sub2, sub3 = st.columns([1,2,1])
            with sub2:
                if st.button("See detailed chart", key="box_incidents", help="Open full Incidents chart"):
                    st.session_state["page"] = "Incidents"
        with r2c2:
            mini_bar(["CrowdStrike","Defender","Tenable"], [100,60,100], "#9467bd", "Tool Coverage")
            sub1, sub2, sub3 = st.columns([1,2,1])
            with sub2:
                if st.button("See detailed chart", key="box_tools", help="Open full Tool Coverage chart"):
                    st.session_state["page"] = "Tool Inventory"
        with r2c3:
            mini_bar(["NIST CSF","PCI DSS"], [72,64], "#8c564b", "Compliance")
            sub1, sub2, sub3 = st.columns([1,2,1])
            with sub2:
                if st.button("See detailed chart", key="box_compliance", help="Open full Compliance chart"):
                    st.session_state["page"] = "Compliance"

# ---------- Vulnerabilities ----------
elif page == "Vulnerabilities":
    st.title("Vulnerability Remediation Trend")
    vuln_df = pd.DataFrame({
        "Date": pd.date_range(end=pd.Timestamp.today(), periods=6, freq="M"),
        "Critical Vulns": [45,39,31,22,15,11]
    })
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("none")
    ax.set_facecolor(preview_bg)
    ax.plot(vuln_df["Date"], vuln_df["Critical Vulns"], marker="o", color="#1f77b4")
    ax.set_ylabel("Open Critical Vulns")
    ax.set_xlabel("Month")
    st.pyplot(fig, use_container_width=True)

# ---------- Phishing ----------
elif page == "Phishing":
    st.title("Phishing Detection Trend")
    phishing_df = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "Blocked Emails": [820,640,975,1120,900,760]
    })
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("none")
    ax.set_facecolor(preview_bg)
    ax.bar(phishing_df["Month"], phishing_df["Blocked Emails"], color="#ff7f0e")
    ax.set_ylabel("Blocked Emails")
    st.pyplot(fig, use_container_width=True)

# ---------- MFA Adoption ----------
elif page == "MFA Adoption":
    st.title("MFA Adoption Trend")
    mfa_df = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "MFA %": [70,75,80,85,88,92]
    })
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("none")
    ax.set_facecolor(preview_bg)
    ax.plot(mfa_df["Month"], mfa_df["MFA %"], marker="o", color="#2ca02c")
    ax.set_ylabel("MFA Adoption (%)")
    st.pyplot(fig, use_container_width=True)

# ---------- Incidents ----------
elif page == "Incidents":
    st.title("Incident Response Details")
    incident_df = pd.DataFrame({
        "Date": ["2025‑05‑01","2025‑05‑10","2025‑05‑19"],
        "Type": ["Phishing","Credential Theft","Ransomware Attempt"],
        "Impact": ["None","Single user","Blocked by EDR"],
        "Status": ["Resolved","Resolved","Mitigated"]
    })
    st.dataframe(incident_df, use_container_width=True)

# ---------- Tool Inventory ----------
elif page == "Tool Inventory":
    st.title("Security Tool Inventory")
    tool_df = pd.DataFrame({
        "Tool": ["CrowdStrike","Defender","Tenable","Chronicle","Abnormal"],
        "Category": ["EDR","EDR","Vuln Mgmt","SIEM","Email Security"],
        "Owner": ["SecOps","IT","SecOps","SecOps","SecOps"],
        "Status": ["Active","Partial","Active","Active","Active"]
    })
    st.dataframe(tool_df, use_container_width=True)

# ---------- Culture & Awareness ----------
elif page == "Culture":
    st.title("Security Culture and Awareness")
    st.title("Security Culture and Awareness")
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

# ---------- Compliance ----------
else:
    st.title("Compliance Scorecard")
    comp_df = pd.DataFrame({
        "Framework": ["NIST CSF", "PCI DSS 4.0"],
        "Compliance Score": [72, 64],
        "Gaps Noted": [
            "Recovery & Response underdeveloped",
            "Admin MFA and segmentation gaps"
        ]
    })
    st.dataframe(comp_df, use_container_width=True)
