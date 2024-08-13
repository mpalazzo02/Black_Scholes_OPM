from py_vollib.black_scholes.greeks.analytical import delta, gamma, theta, vega, rho

def calculate_greeks(option_type, S, K, T, r, sigma):
    """
    Calculate the Greeks for a given option using py_vollib.

    Parameters:
        option_type (str): 'c' for call, 'p' for put
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility of the underlying asset

    Returns:
        dict: A dictionary containing the calculated Greeks (Delta, Gamma, Theta, Vega, Rho)
    """
    return {
        "Delta": delta(option_type, S, K, T, r, sigma),
        "Gamma": gamma(option_type, S, K, T, r, sigma),
        "Theta": theta(option_type, S, K, T, r, sigma),
        "Vega": vega(option_type, S, K, T, r, sigma),
        "Rho": rho(option_type, S, K, T, r, sigma)
    }