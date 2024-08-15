import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from black_scholes_model import calculate_option_price
from greeks_calculator import calculate_greeks
from implied_volatility import calculate_implied_volatility
import plotly.graph_objects as go

# App Title
st.title("Black-Scholes Pricing Model")
st.write("""
<style>
    .reportview-container .main .block-container{
        max-width: 98%;
        padding-top: 1em;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)
st.write("""
The **Black-Scholes model** is a mathematical model for pricing an options contract. 
It estimates the variation over time of financial instruments such as stocks and is 
widely used to determine the fair price of options.

This interactive dashboard allows you to calculate the price of Call and Put options using 
the Black-Scholes model, visualise option prices over different market conditions, 
and explore the Greeks, which are sensitivities of the option's price to various factors.
""")

# Sidebar with Sections
st.sidebar.header("Black-Scholes Model")
st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 16px;">
        <b>Created by:</b> <a href='https://www.linkedin.com/in/YOUR-LINKEDIN-URL/' target='_blank' style='color: #0e76a8; text-decoration: none;'>Michele Palazzo</a>
    </div>
    """, unsafe_allow_html=True
)

# Split the Sidebar into Sections
st.sidebar.markdown("### Call and Put Option Inputs")

# Call and Put Option Inputs
with st.sidebar.expander("Option Pricing", expanded=True):
    st.markdown("**Input Parameters for Pricing Call and Put Options**")
    S = st.sidebar.number_input("Current Asset Price", min_value=0.0, value=100.0, step=1.0)
    K = st.sidebar.number_input("Strike Price", min_value=0.0, value=100.0, step=1.0)
    T = st.sidebar.number_input("Time to Maturity (Years)", min_value=0.01, value=1.0, step=0.01)
    sigma = st.sidebar.number_input("Volatility", min_value=0.01, value=0.2, step=0.01)
    r = st.sidebar.number_input("Risk-Free Interest Rate", min_value=0.0, value=0.05, step=0.01)
    option_type = st.sidebar.selectbox("Option Type", ("Call", "Put"))

# Section for Heatmap Inputs
st.sidebar.subheader("Heatmap Parameters")
with st.sidebar.expander("Customize Heatmap", expanded=True):
    st.markdown("**Input Parameters for Generating the Heatmap**")
    min_spot = st.sidebar.number_input("Min Spot Price", min_value=0.0, value=80.0)
    max_spot = st.sidebar.number_input("Max Spot Price", min_value=0.0, value=120.0)
    min_vol = st.sidebar.number_input("Min Volatility for Heatmap", min_value=0.01, value=0.1)
    max_vol = st.sidebar.number_input("Max Volatility for Heatmap", min_value=0.01, value=0.4)

# Create a section for the Greeks in the sidebar
st.sidebar.subheader("Option Greeks")

# Create a function to generate a gauge chart
def create_gauge(name, value, min_value=-1, max_value=1):
    return go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': name, 'font': {'size': 14}},  # Smaller title font
        gauge={'axis': {'range': [min_value, max_value]},
               'bar': {'color': "#1f77b4"}},  # Use a consistent color scheme
        number={'font': {'size': 20}}  # Smaller number font
    ))

# Calculate Option Prices and Greeks
call_price = calculate_option_price('c', S, K, T, r, sigma)
put_price = calculate_option_price('p', S, K, T, r, sigma)
greeks = calculate_greeks(option_type[0].lower(), S, K, T, r, sigma)
iv = calculate_implied_volatility(call_price if option_type == 'Call' else put_price, S, K, T, r, option_type[0].lower())

# Create gauge charts for all the Greeks
delta_gauge = create_gauge("Delta", greeks['Delta'], -1, 1)
gamma_gauge = create_gauge("Gamma", greeks['Gamma'], 0, 0.5)
theta_gauge = create_gauge("Theta", greeks['Theta'], -0.5, 0)
vega_gauge = create_gauge("Vega", greeks['Vega'], 0, 0.5)
rho_gauge = create_gauge("Rho", greeks['Rho'], -0.5, 0.5)

# Update layout to make the gauges smaller and reduce margins
for gauge in [delta_gauge, gamma_gauge, theta_gauge, vega_gauge, rho_gauge]:
    gauge.update_layout(
        width=250,  # Adjust the width of the gauge
        height=250,  # Adjust the height of the gauge
        margin=dict(l=0, r=0, t=20, b=0)  # Reduce the margins
    )

# Display the gauges in the sidebar
st.sidebar.plotly_chart(delta_gauge, use_container_width=True)
st.sidebar.plotly_chart(gamma_gauge, use_container_width=True)
st.sidebar.plotly_chart(theta_gauge, use_container_width=True)
st.sidebar.plotly_chart(vega_gauge, use_container_width=True)
st.sidebar.plotly_chart(rho_gauge, use_container_width=True)

# Main Content Area
st.header("Options Price - Interactive Dashboard")
st.markdown("---")  # Horizontal rule for better sectioning

# Display Option Price with Colored Boxes
col1, col2 = st.columns(2)

col1.markdown(
    f"""
    <div style="background-color:#28a745;padding:20px;border-radius:10px;text-align:center;color:white;font-weight:bold;">
        CALL Value
        <p style="font-size:24px;margin:0;">${call_price:.2f}</p>
    </div>
    """, unsafe_allow_html=True
)

col2.markdown(
    f"""
    <div style="background-color:#dc3545;padding:20px;border-radius:10px;text-align:center;color:white;font-weight:bold;">
        PUT Value
        <p style="font-size:24px;margin:0;">${put_price:.2f}</p>
    </div>
    """, unsafe_allow_html=True
)

# Generate Spot Prices and Volatility Arrays
spot_prices = np.linspace(min_spot, max_spot, 10)
volatilities = np.linspace(min_vol, max_vol, 10)
call_prices = np.zeros((10, 10))
put_prices = np.zeros((10, 10))

# Calculate Option Prices for Heatmap
for i, S in enumerate(spot_prices):
    for j, sigma in enumerate(volatilities):
        call_prices[j, i] = calculate_option_price('c', S, K, T, r, sigma)
        put_prices[j, i] = calculate_option_price('p', S, K, T, r, sigma)

# Plot Heatmaps with Adjusted Layout and Font Sizes
st.subheader("Option Pricing Heatmaps")
fig, ax = plt.subplots(1, 2, figsize=(18, 8))  # Adjust the figure size

sns.heatmap(call_prices, ax=ax[0], xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2),
            cmap="YlGnBu", annot=True, fmt=".2f", cbar_kws={'label': 'CALL Price'}, annot_kws={"size": 10})
ax[0].set_xlabel('Spot Price', fontsize=14)
ax[0].set_ylabel('Volatility', fontsize=14)
ax[0].set_title('Call Price Heatmap', fontsize=16)

sns.heatmap(put_prices, ax=ax[1], xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2),
            cmap="YlOrRd", annot=True, fmt=".2f", cbar_kws={'label': 'PUT Price'}, annot_kws={"size": 10})
ax[1].set_xlabel('Spot Price', fontsize=14)
ax[1].set_ylabel('Volatility', fontsize=14)
ax[1].set_title('Put Price Heatmap', fontsize=16)

fig.tight_layout(pad=2.0)  # Adjust layout padding to improve spacing
st.pyplot(fig)
plt.close(fig)