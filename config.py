"""Configuration modul"""
import os


class Config:
    """Configuration class"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
