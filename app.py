from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_cors import CORS
import config, csv, datetime
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
CORS(app)
client = Client(config.API_KEY, config.API_SECRET, tld='us')
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    title = 'CryptoCompare'

    info = client.get_account()

    balances = info['balances']

    #print(balances)


    return render_template('index.html', title=title, my_balances=balances)

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'


@app.route('/history')
def history():
    #candlesticks = client.get_all_tickers()
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 May, 2021", "21 May, 2021")
    
    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4]
        }
        
        processed_candlesticks.append(candlestick)
    
    return jsonify(processed_candlesticks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

