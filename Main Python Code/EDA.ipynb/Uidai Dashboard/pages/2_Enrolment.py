import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Aadhaar Enrolment Trends")

df = pd.read_csv("data/uidai_clean.csv")

age = st.selectbox("Select Age Group", df["age_group"].unique())

filtered = df[df["age_group"] == age]

fig = px.line(
    filtered,
    x="year",
    y="enrolment_count",
    title=f"Enrolment Growth – {age}"
)

st.plotly_chart(fig, use_container_width=True)


