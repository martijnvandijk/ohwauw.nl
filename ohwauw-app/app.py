from flask import Flask, redirect, render_template, request, jsonify
from lines import lines
import random

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def ohwauw():
    wauw = random.choice(lines)
    return render_template('homepage.html', wauw=wauw)

@app.route("/wauw", methods = ["GET"])
def specificwauw():
    line = request.args.get('wauw', default = -1, type=int)
    if line = -1:
        wauw = random.choice(lines)
    else:
        wauw = lines[line]
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
