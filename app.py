import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Urban Planning Research Tool",
    layout="wide"
)

st.title(" Urban Planning Research Tool")
st.caption("Real-world Kaggle City Dataset Analysis")

# ---------------- LOAD DATA ----------------
census = pd.read_csv("data/census.csv")
zoning = pd.read_csv("data/zoning.csv")
transport = pd.read_csv("data/transport.csv")

# Normalize column names
census.columns = census.columns.str.lower()

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([
    " City Demographics (Kaggle)",
    " Population Analysis",
    " Zoning & Transport"
])

# ---------------- TAB 1 ----------------
with tab1:
    st.subheader("City-Level Demographics")

    city = st.selectbox(
        "Select City",
        sorted(census["city"].dropna().unique())
    )

    city_data = census[census["city"] == city]
    st.dataframe(city_data)

    st.metric(
        "Population",
        int(city_data["population"].values[0])
    )

# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("Population Analysis")

    st.write("### Top 10 Most Populated Cities")
    top_cities = census.sort_values(
        "population",
        ascending=False
    ).head(10)

    st.bar_chart(
        top_cities.set_index("city")["population"]
    )

    st.write("### Country-wise Population (Top 10)")
    country_pop = (
        census.groupby("country")["population"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(country_pop)

# ---------------- TAB 3 ----------------
with tab3:
    st.subheader("Zoning Data")
    st.dataframe(zoning)

    st.subheader("Transport Network")
    st.dataframe(transport)


