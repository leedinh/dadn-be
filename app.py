import fb
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name') # GET Parameter: ?name=Guest
    res = requests.get('https://io.adafruit.com/api/v2/anhtriet/feeds/bbc-temp/data')
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)