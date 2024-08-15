from black_scholes_model import calculate_option_price
from greeks_calculator import calculate_greeks
from implied_volatility import calculate_implied_volatility

def main():
    S = 100  # Current stock price
    K = 100  # Strike price
    T = 1  # Time to expiration in years
    r = 0.05  # Risk-free interest rate
    sigma = 0.2  # Volatility

    # Calculate option prices using py_vollib
    call_price = calculate_option_price('c', S, K, T, r, sigma)
    put_price = calculate_option_price('p', S, K, T, r, sigma)

    print(f"Call Option Price (py_vollib): {call_price:.2f}")
    print(f"Put Option Price (py_vollib): {put_price:.2f}")

    # Calculate Greeks for the call option
    call_greeks = calculate_greeks('c', S, K, T, r, sigma)
    print("\nCall Option Greeks:")
    for greek, value in call_greeks.items():
        print(f"{greek}: {value:.4f}")

    # Calculate Greeks for the put option
    put_greeks = calculate_greeks('p', S, K, T, r, sigma)
    print("\nPut Option Greeks:")
    for greek, value in put_greeks.items():
        print(f"{greek}: {value:.4f}")

    # Calculate implied volatility for call and put options
    iv_call = calculate_implied_volatility(call_price, S, K, T, r, 'c')
    iv_put = calculate_implied_volatility(put_price, S, K, T, r, 'p')

    print(f"\nImplied Volatility (Call): {iv_call:.4f}")
    print(f"Implied Volatility (Put): {iv_put:.4f}")

if __name__ == "__main__":
    main()