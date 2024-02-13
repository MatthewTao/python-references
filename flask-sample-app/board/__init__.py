from flask import Flask
from board import pages


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)

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
