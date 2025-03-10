"""Modul create objects in database"""

from app import db


class Club(db.Model):
    """Class creating object Club"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    employees = db.relationship("Employee", back_populates="club", lazy=True)


class Employee(db.Model):
    """Class creating object Employee"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    club = db.relationship("Club", back_populates="employees")
