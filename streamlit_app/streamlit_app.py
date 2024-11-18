import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from black_scholes_model import calculate_option_price
from greeks_calculator import calculate_greeks
from implied_volatility import calculate_implied_volatility
import plotly.graph_objects as go

from black_scholes_model import calculate_option_price
from greeks_calculator import calculate_greeks
from implied_volatility import calculate_implied_volatility

# Set page config
st.set_page_config(page_title="Black-Scholes Pricing Model", layout="wide", initial_sidebar_state="expanded")

# App Header
st.markdown(
    """
    <h1 style="text-align: center; font-size: 3em; margin-bottom: 10px;">Black-Scholes Pricing Model</h1>
    <p style="text-align: center; font-size: 1.2em; color: #6c757d;">
        Analyse option prices, visualise sensitivities, and explore Greeks interactively.
        
    </p>
    """,
    unsafe_allow_html=True,
)

# Create tabs for organized layout
tabs = st.tabs(["Pricing Inputs", "Option Prices", "Greeks", "Heatmaps"])

# Tab 1: Pricing Inputs
with tabs[0]:
    st.subheader("Input Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        S = st.number_input("Spot Price (S)", value=100.0, step=1.0)
        T = st.number_input("Time to Maturity (Years, T)", value=1.0, step=0.01)
    with col2:
        K = st.number_input("Strike Price (K)", value=100.0, step=1.0)
        r = st.number_input("Risk-Free Rate (r)", value=0.05, step=0.01)
    with col3:
        sigma = st.number_input("Volatility (σ)", value=0.2, step=0.01)
        option_type = st.selectbox("Option Type", ["Call", "Put"])

# Tab 2: Option Prices
with tabs[1]:
    st.subheader("Option Prices")
    call_price = calculate_option_price('c', S, K, T, r, sigma)
    put_price = calculate_option_price('p', S, K, T, r, sigma)
    st.metric("CALL Price", f"${call_price:.2f}", delta=None, delta_color="normal")
    st.metric("PUT Price", f"${put_price:.2f}", delta=None, delta_color="inverse")

# Tab 3: Greeks
with tabs[2]:
    st.subheader("Option Greeks")
    greeks = calculate_greeks(option_type[0].lower(), S, K, T, r, sigma)
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Delta", f"{greeks['Delta']:.4f}")
    col2.metric("Gamma", f"{greeks['Gamma']:.4f}")
    col3.metric("Theta", f"{greeks['Theta']:.4f}")
    col4.metric("Vega", f"{greeks['Vega']:.4f}")
    col5.metric("Rho", f"{greeks['Rho']:.4f}")

with tabs[3]:
    st.subheader("Option Pricing Heatmaps")

    # Input for Spot Prices and Volatilities
    min_spot = st.number_input("Minimum Spot Price", value=80.0, step=1.0)
    max_spot = st.number_input("Maximum Spot Price", value=120.0, step=1.0)
    min_vol = st.number_input("Minimum Volatility", value=0.1, step=0.01)
    max_vol = st.number_input("Maximum Volatility", value=0.4, step=0.01)

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
