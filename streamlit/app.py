import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    poss = pd.read_csv("scored_possessions.csv")
    events = pd.read_csv("events.csv")  # your event-level data
    return poss, events

poss_df, event_df = load_data()

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("Controls")

match_id = st.sidebar.selectbox("Match", poss_df["match_id"].unique())
team = st.sidebar.selectbox("Team", poss_df["team"].unique())

phase = st.sidebar.radio(
    "Mode",
    ["Pre-Match", "In-Match", "Post-Match", "Recruitment", "Deep Dive"]
)

filtered = poss_df[(poss_df["match_id"] == match_id) & (poss_df["team"] == team)]

# -------------------------------
# PRE MATCH
# -------------------------------
if phase == "Pre-Match":
    st.title("Pre-Match Scouting")

    st.subheader("Danger by Play Pattern")
    st.bar_chart(filtered.groupby("play_pattern")["threat_score"].mean())

    st.subheader("Top Dangerous Possessions")
    st.dataframe(filtered.sort_values("threat_score", ascending=False).head(10))

# -------------------------------
# IN MATCH
# -------------------------------
elif phase == "In-Match":
    st.title("In-Match Pattern Recognition")

    temp = filtered.sort_values("timestamp")

    st.line_chart(temp["threat_score"])

# -------------------------------
# POST MATCH
# -------------------------------
elif phase == "Post-Match":
    st.title("Post-Match Debrief")

    threshold = st.slider("Threat Threshold", 0.0, 1.0, 0.65)

    high_threat = filtered[filtered["threat_score"] >= threshold]

    st.write(f"{len(high_threat)} high-threat possessions")

    selected = st.selectbox("Select Possession", high_threat["poss_key"])

# -------------------------------
# RECRUITMENT
# -------------------------------
elif phase == "Recruitment":
    st.title("Player Impact on Threat")

    st.dataframe(
        poss_df.groupby("player")["threat_score"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
    )

# -------------------------------
# DEEP DIVE
# -------------------------------
elif phase == "Deep Dive":
    st.title("Possession Deep Dive")

    selected = st.selectbox("Select Possession", filtered["poss_key"])

    row = filtered[filtered["poss_key"] == selected].iloc[0]

    st.metric("Threat Score", round(row["threat_score"], 3))

    st.subheader("Key Drivers")
    st.write({
        "Nearest Defender": row.get("nearest_def_dist_min", None),
        "Attackers Ahead": row.get("attackers_ahead", None),
        "Defenders Between": row.get("defenders_between", None),
        "Play Pattern": row.get("play_pattern", None)
    })

    st.subheader("Summary")
    st.write(
        f"{row['play_pattern']} with {row.get('attackers_ahead', 'N/A')} attackers ahead, "
        f"{row.get('defenders_between', 'N/A')} defenders between ball and goal, "
        f"and {round(row.get('nearest_def_dist_min', 0),2)}m of space."
    )