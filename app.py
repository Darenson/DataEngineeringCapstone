from flask import Flask
import requests
from flask import render_template


app = Flask(__name__)

@app.route('/')
def main():
    url = "http://api.coinlayer.com/live?access_key=0b57ed3868a996b0a8cbb0a8c55237e8&target=USD"
    response = requests.get(url)
    response_json = response.json()
    rates = response_json['rates']
    target = response_json['target']
    

    return render_template('rates.html',rates=rates, target=target)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='5000')

