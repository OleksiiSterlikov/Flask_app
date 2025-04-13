
from app import db
from app.models.utils import ModelMixin


class Recipient(db.Model, ModelMixin):
    """Class creating table db Recipient"""
    __tablename__ = "recipients"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(16), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    birthday = db.Column(db.DateTime, nullable=False)

    active = db.Column(db.Boolean, default=True)
