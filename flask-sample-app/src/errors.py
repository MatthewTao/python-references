from flask import current_app, render_template, request


def page_not_found(e):
    current_app.logger.error(f"'{e.name}' error ({e.code}) at {request.url}")
    return render_template("errors/404.html"), 404
