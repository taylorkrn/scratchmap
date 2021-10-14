import os

class Config:
    #Key generated through secrets.token_hex(16) saved in the environment variables on Windows OS
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #Mail Setup - Login and password are saved in the Windows environment variables
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('GMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')
