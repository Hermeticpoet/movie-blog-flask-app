import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLAlCHEMY_DATABASE_URI = os.environ.get('SQLAlCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.googlemail.com"
    PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
