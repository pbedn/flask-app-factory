from flask import Flask, jsonify


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    from .models import db
    db.init_app(app)

    from .models import db
    db.init_app(app)

    from .views import auth

    @app.route('/')
    def index():
        return jsonify({'ok': True})

    from .api import api
    app.register_blueprint(api)

    return app
