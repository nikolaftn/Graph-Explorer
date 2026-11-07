"""Flask application scaffold."""

from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return "Graph Explorer scaffold"

    return app


def main() -> None:
    create_app().run(debug=True)
