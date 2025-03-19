"""Modul create objects in database"""

from app import db


class Club(db.Model):
    """Class creating table db  Club"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    employees = db.relationship("Employee", back_populates="club", lazy=True)


class Employee(db.Model):
    """Class creating table db Employee"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    club = db.relationship("Club", back_populates="employees")

    def serialize(self):
        """Function to serialize object Employee from API"""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "club_id": self.club_id,
            "club": {
                "id": self.club_id,
                "title": self.club.title,
                "location": self.club.location,
            },
        }


class User(db.Model):
    """Class creating table db User"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
