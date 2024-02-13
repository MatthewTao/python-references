from dotenv import load_dotenv
from flask import Flask
import os

from board import  database, errors, pages, posts


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    app.logger.debug(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    app.logger.debug(f"Using Database: {app.config.get('DATABASE')}")

    database.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404, errors.page_not_found)

    return app


# OR just as simple as below will get something going
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello, World!"
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)
