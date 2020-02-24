import os

pjdir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "jet-tech-blog"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(pjdir, "techblog.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
