from datetime import date
from flask import render_template

from app import app


@app.route('/')
def home():
    today_date = date.today().strftime("%Y-%m-%d")
    subject_name = "Engenharia de Software"
    return render_template('home.html', today_date=today_date, subject_name=subject_name)
