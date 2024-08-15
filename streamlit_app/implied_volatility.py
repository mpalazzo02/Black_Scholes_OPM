from py_vollib.black_scholes.implied_volatility import implied_volatility

def calculate_implied_volatility(option_price, S, K, T, r, option_type):
    """
    Calculate the implied volatility given an option price using py_vollib.

    Parameters:
        option_price (float): Observed market price of the option
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate
        option_type (str): 'c' for call, 'p' for put

    Returns:
        float: Implied volatility
    """
    return implied_volatility(option_price, S, K, T, r, option_type)