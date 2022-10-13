from flask import Flask, redirect, render_template, request
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

