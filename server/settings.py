import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://root:pass@localhost/prod_db'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://root:pass@localhost/test_db'


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # SQLALCHEMY_ECHO = True
