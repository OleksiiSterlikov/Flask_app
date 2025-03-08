"""Modul create objects in database"""

from app import db


class Club(db.Model):
    """Class creating object Club"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    