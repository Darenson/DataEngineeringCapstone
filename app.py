from flask import Flask
import requests
from flask import render_template


app = Flask(__name__)

@app.route('/')
def main():
    url = "http://api.coinlayer.com/live?access_key=2d62ccebc7dd67f1b4b04ee5653d9746&symbols=ETH,BTC,LTC,DOGE,BCH&target=USD"
    response = requests.get(url)
    response_json = response.json()
    rates = response_json['rates']
    target = response_json['target']
    

    return render_template('rates.html',rates=rates, target=target)


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port='8000')

