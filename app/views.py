# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/findme')
def findme():
    return render_template("findme.html")

@app.route('/certificates')
def certificates():
    return render_template("certificates.html")