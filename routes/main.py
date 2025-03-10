"""Modul main routes"""

from flask import render_template
from app import app
from models.models import Club


@app.route('/')
def main():
    """Main function"""
    clubs = Club.query.order_by(Club.title.asc()).all()
    return render_template('index.html', clubs=clubs)
