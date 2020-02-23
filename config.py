import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = "the hardest string to guess 3v4r"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False