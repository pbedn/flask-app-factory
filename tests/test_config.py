from server import create_app


class TestConfig:
    def test_dev_config(self):
        """ Tests if the development config loads correctly """

        app = create_app('server.settings.DevelopmentConfig')

        assert app.config['DEBUG'] is True
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///database.db'

    def test_test_config(self):
        """ Tests if the test config loads correctly """

        app = create_app('server.settings.TestingConfig')

        assert app.config['DEBUG'] is True
        assert app.config['TESTING'] is True
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'

    def test_prod_config(self):
        """ Tests if the production config loads correctly """

        app = create_app('server.settings.ProductionConfig')
        assert app.config['DEBUG'] is False
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///database.db'
