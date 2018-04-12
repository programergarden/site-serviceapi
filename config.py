
class Config(object):
    pass

class ProductConfig(Config):
    pass

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/programergarden?charset=utf8mb4'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True