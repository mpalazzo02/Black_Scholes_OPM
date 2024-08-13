from py_vollib.black_scholes import black_scholes

def calculate_option_price(option_type, S, K, T, r, sigma):
    """
    Calculate the Black-Scholes option price using py_vollib.

    Parameters:
        option_type (str): 'c' for call, 'p' for put
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility of the underlying asset

    Returns:
        float: Calculated option price
    """
    return black_scholes(option_type, S, K, T, r, sigma)