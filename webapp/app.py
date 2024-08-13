import sys
import os


from flask import Flask, render_template, request
from black_scholes_model import calculate_option_price
from greeks_calculator import calculate_greeks
from implied_volatility import calculate_implied_volatility

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        S = float(request.form['S'])
        K = float(request.form['K'])
        T = float(request.form['T'])
        r = float(request.form['r'])
        sigma = float(request.form['sigma'])
        option_type = request.form['option_type']

        # Calculate the option price, Greeks, and implied volatility
        option_price = calculate_option_price(option_type, S, K, T, r, sigma)
        greeks = calculate_greeks(option_type, S, K, T, r, sigma)
        iv = calculate_implied_volatility(option_price, S, K, T, r, option_type)

        return render_template('index.html', option_price=option_price, greeks=greeks, iv=iv,
                               S=S, K=K, T=T, r=r, sigma=sigma, option_type=option_type)

    return render_template('index.html', option_price=None, greeks=None, iv=None)

if __name__ == '__main__':
    app.run(debug=True)