"""Configuration modul"""

class Config:
    """Configuration class"""
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@db/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
