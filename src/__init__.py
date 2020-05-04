from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.distance.routes import distance

    app.register_blueprint(distance)

    return app