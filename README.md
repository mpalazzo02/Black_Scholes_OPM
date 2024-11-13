# Black_Scholes_OPM
## Black Scholes OPM

This repository contains the code and resources for the Black-Scholes Option Pricing Model (OPM) project. The Black-Scholes model is a widely-used mathematical model for pricing European options and is a cornerstone of modern financial theory.

## Overview

The project provides an interactive dashboard for calculating and visualising the price of Call and Put options using the Black-Scholes model. The dashboard also allows users to explore the Greeks, which are sensitivities of the option's price to various factors.

## Key Features
Option Pricing: Calculate the fair value of Call and Put options based on the Black-Scholes model.
Interactive Dashboard: Explore how different parameters (e.g., asset price, strike price, volatility) affect option pricing.
Greeks Visualisation: Analyse the sensitivities (Delta, Gamma, Theta, Vega, Rho) and their impact on option pricing.
Heatmaps: Visualise how option prices change over a range of spot prices and volatilities.
Installation

To run this project locally, clone the repository and install the required dependencies:

bash
Copy code
git clone https://github.com/mpalazzo02/Black_Scholes_OPM.git
cd Black_Scholes_OPM
pip install -r requirements.txt
Usage

Launch the Streamlit app to interact with the Black-Scholes dashboard:

bash
Copy code
streamlit run streamlit_app.py
Technologies Used

Python: Core programming language.
Streamlit: Web framework for creating the interactive dashboard.
NumPy: Numerical computing library for calculations.
Matplotlib & Seaborn: Data visualisation libraries.
Plotly: For creating interactive gauge charts.
Py_vollib: For calculating option prices and Greeks.


## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.


## Contact

Created by Michele Palazzo - feel free to reach out via email michele_palazzo@icloud.com
