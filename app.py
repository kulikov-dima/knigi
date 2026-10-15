from datetime import date

from flask import Flask, render_template, abort, request
from books import BOOKS

app = Flask(__name__)


def all_genres():
    """5.7 — все жанры без повторов, по алфавиту."""
    genres = set()
    for book in BOOKS:
        for genre in book["genres"]:
            genres.add(genre)
    return sorted(genres)


@app.route("/")
def index():
    genre = request.args.get("genre")   # 5.6
    sort = request.args.get("sort")     # 5.8

    books = BOOKS
    if genre:
        books = [b for b in books if genre in b["genres"]]
    if sort == "year":
        books = sorted(books, key=lambda b: b["year"])
    elif sort == "title":
        books = sorted(books, key=lambda b: b["title"])

    return render_template(
        "index.html",
        site_name="Книжная полка",
        books=books,
        genres=all_genres(),
        current_genre=genre,
        current_sort=sort,
        active="index",
    )


@app.route("/table")
def table():
    return render_template("table.html", books=BOOKS, active="table")


@app.route("/classic")
def classic():
    return render_template("classic.html", books=BOOKS)


@app.route("/book/<int:book_id>")
def book(book_id):
    for b in BOOKS:
        if b["id"] == book_id:
            return render_template("book.html", book=b, current_year=date.today().year)
    abort(404)


@app.route("/about")
def about():
    return render_template("about.html", active="about")


if __name__ == "__main__":
    app.run(debug=True)
