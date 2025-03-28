"""Configuration modul"""
import os


base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    """Base Configuration class"""
    APP_NAME = os.getenv("APP_NAME", "Flask_app")
    SECRET_KEY = os.getenv("SECRET_KEY", "Ensure you set a secret key")

    @staticmethod
    def configure(app):
        pass

class DevelopmentConfig(BaseConfig):
    """Development Configuration class"""
    DEBUG = True
    DATABASE_URL = os.getenv("DEV_DATABASE_URL", "sqlite:///" + os.path.join(base_dir, "dev.db"))

class ProductionConfig(BaseConfig):
    """Production Configuration class"""
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(base_dir, "dev.db"))


config = dict(development=DevelopmentConfig, production=ProductionConfig)
