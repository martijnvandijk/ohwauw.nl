from flask import Flask, redirect, render_template, request, jsonify
from lines import lines
import random

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def ohwauw():
    wauw = random.choice(lines)
    return render_template('homepage.html', wauw=wauw)

@app.route("/api/wauw", methods = ["GET"])
def getwauw():
    wauw = random.choice(lines)
    return wauw

@app.route("/api/wauw/json", methods = ["GET"])
def getwauw_json():
    wauw = random.choice(lines)
    return jsonify({
        "wauw": wauw
    })
