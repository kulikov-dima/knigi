from datetime import date

from flask import Flask, render_template, abort
from books import BOOKS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        site_name="Книжная полка",
        books_count=len(BOOKS),
        books=BOOKS,
    )


@app.route("/book/<int:book_id>")
def book(book_id):
    for b in BOOKS:
        if b["id"] == book_id:
            return render_template("book.html", book=b, current_year=date.today().year)
    abort(404)   # 3.7


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
