from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "53dc65fa03735fe646d1e753"
db.init_app(app)
        
from market import routes
from market import models