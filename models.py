# models.py
from flask_login import UserMixin
from extensions import db

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    predictions = db.relationship('Prediction', backref='user', lazy=True)

# Prediction Model
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    visibility = db.Column(db.Float, nullable=False)
    solar_radiation = db.Column(db.Float, nullable=False)
    rainfall = db.Column(db.Float, nullable=False)
    snowfall = db.Column(db.Float, nullable=False)
    seasons = db.Column(db.String(50), nullable=False)
    holiday = db.Column(db.String(20), nullable=False)
    functioning_day = db.Column(db.String(20), nullable=False)
    prediction = db.Column(db.Integer, nullable=False)
