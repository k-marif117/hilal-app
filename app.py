from flask import Flask, request, jsonify
from datetime import datetime
import numpy as np

app = Flask(__name__)

def simple_model(lat, lon):
    score = lat * 0.1 + lon * 0.05
    prob = 1 / (1 + np.exp(-score))
    return prob * 100

@app.route("/")
def home():
    return "Hilal App Running"

@app.route("/api")
def api():
    lat = float(request.args["lat"])
    lon = float(request.args["lon"])
    prob = simple_model(lat, lon)
    return jsonify({"probability": round(prob, 1)})

if __name__ == "__main__":
    app.run()
