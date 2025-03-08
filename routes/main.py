"""Modul main routes"""

from flask import render_template
from app import app
from models.models import Plant


@app.route('/')
def main():
    """Main function"""
    plants = Plant.get_data()
    return render_template('index.html', plants=plants)
