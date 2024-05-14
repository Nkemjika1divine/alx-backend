#!/usr/bin/env python3
"""module for flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    """renders 0-index.html"""
    return render_template("0-index.html")
