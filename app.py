from flask import Flask, render_template, request
import smtplib
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
# db = SQLAlchemy(app)

@app.route('/')
def index():
    title = "Fedora's Blog"
    names = ['tim', 'tom', 'tonny']
    return render_template('index.html', title = title, names = names)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/subcribe/')
def subcribe():
    return render_template('subcribe.html')

@app.route('/form/', methods = ['POST'])
def form():
    email = request.form.get('email')
    name = request.form.get('name')
    message = "Thank you for subcribing to our newsletter."
    if not email or not name:
        error_statement = "All fields required ..."
        return render_template("fail.html", error_statement = error_statement)

    return render_template('form.html', name = name)