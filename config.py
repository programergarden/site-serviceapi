
class Config(object):
    pass

class ProductConfig(Config):
    pass

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////db/web.db'