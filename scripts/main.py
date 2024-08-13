from black_scholes_model import calculate_option_price

def main():
    S = 100  # Current stock price
    K = 100  # Strike price
    T = 1  # Time to expiration in years
    r = 0.05  # Risk-free interest rate
    sigma = 0.2  # Volatility

    # Calculate call and put option prices using py_vollib
    call_price = calculate_option_price('c', S, K, T, r, sigma)
    put_price = calculate_option_price('p', S, K, T, r, sigma)

    print(f"Call Option Price (py_vollib): {call_price:.2f}")
    print(f"Put Option Price (py_vollib): {put_price:.2f}")

if __name__ == "__main__":
    main()