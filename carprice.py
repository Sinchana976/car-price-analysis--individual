import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Car Price Dashboard",
    page_icon="🚗",
    layout="wide"
)

# ---------------- LOAD DATA ----------------

df = pd.read_csv("cleaned_car.csv")

# ---------------- STYLE ----------------

st.markdown("""
<style>
.main-title{
    text-align:center;
    color:#2E8B57;
    font-size:40px;
    font-weight:bold;
}

.kpi-card{
    background-color:#f0f0f0;
    padding:20px;
    border-radius:12px;
    text-align:center;
    box-shadow:2px 2px 8px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown('<p class="main-title">🚗 Car Price Analytics Dashboard</p>', unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.header("🔎 Filter")

fuel = st.sidebar.multiselect(
    "Fuel Type",
    df['Fuel_type'].unique(),
    default=df['Fuel_type'].unique()
)

gear = st.sidebar.multiselect(
    "Gear Box",
    df['Gear_box_type'].unique(),
    default=df['Gear_box_type'].unique()
)

# ---------------- FILTER ----------------

filtered_df = df[
    (df['Fuel_type'].isin(fuel)) &
    (df['Gear_box_type'].isin(gear))
]

# ---------------- KPIs ----------------

avg_price = filtered_df['Price'].mean()
max_price = filtered_df['Price'].max()
min_price = filtered_df['Price'].min()
cars = filtered_df.shape[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Avg Price", f"${avg_price:,.0f}")
c2.metric("Max Price", f"${max_price:,.0f}")
c3.metric("Min Price", f"${min_price:,.0f}")
c4.metric("Total Cars", cars)

st.markdown("---")

# ---------------- ROW 1 ----------------

col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        filtered_df.groupby('Manufacturer')['Price'].mean().reset_index(),
        x='Manufacturer',
        y='Price',
        title="Price by Manufacturer"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.line(
        filtered_df.groupby('Prod._year')['Price'].mean().reset_index(),
        x='Prod._year',
        y='Price',
        markers=True,
        title="Price Trend by Year"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- ROW 2 (PIE CHARTS) ----------------

col3, col4 = st.columns(2)

with col3:
    fuel_chart = filtered_df.groupby('Fuel_type')['Price'].mean().reset_index()

    fig3 = px.pie(
        fuel_chart,
        names='Fuel_type',
        values='Price',
        hole=0.4,
        title="Fuel Type Distribution"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    gear_chart = filtered_df.groupby('Gear_box_type')['Price'].mean().reset_index()

    fig4 = px.pie(
        gear_chart,
        names='Gear_box_type',
        values='Price',
        title="Gear Box Distribution"
    )
    st.plotly_chart(fig4, use_container_width=True)

# ---------------- ROW 3 ----------------

col5, col6 = st.columns(2)

with col5:
    fig5 = px.histogram(
        filtered_df,
        x='Price',
        nbins=30,
        title="Price Distribution"
    )
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    fig6 = px.box(
        filtered_df,
        x='Fuel_type',
        y='Price',
        title="Price vs Fuel Type"
    )
    st.plotly_chart(fig6, use_container_width=True)

# ---------------- DATA ----------------

st.subheader("📊 Data Preview")
st.dataframe(filtered_df.head(20))