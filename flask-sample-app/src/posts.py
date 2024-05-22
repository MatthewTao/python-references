from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from src.database import get_db

bp = Blueprint("posts", __name__)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_db()
            db.execute(
                "INSERT INTO post (author, message) VALUES (?, ?)",
                (author, message),
            )
            db.commit()
            current_app.logger.info("New post created")
            flash(f"Thanks for posting, {author}!", category="success")
            # Redirect to another page to view the added item
            return redirect(url_for("posts.posts"))
        else:
            flash("Could not post the message.", category="error")
    else:
        # It's just the GET method to get the form I suppose
        return render_template("posts/create.html")


@bp.route("/posts")
def posts():
    db = get_db()
    posts = db.execute(
        "SELECT author, message, created FROM post ORDER BY created DESC"
    ).fetchall()
    return render_template("posts/posts.html", posts=posts)
