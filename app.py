from datetime import date

from flask import Flask, render_template, abort
from books import BOOKS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        site_name="Книжная полка",
        books=BOOKS,
    )


@app.route("/table")
def table():
    return render_template("table.html", books=BOOKS)


@app.route("/classic")
def classic():
    return render_template("classic.html", books=BOOKS)


@app.route("/book/<int:book_id>")
def book(book_id):
    similar = []
    target_book = None
    for b in BOOKS:
        if b["id"] == book_id:
            target_book = b
            break
    if target_book:
        for b in BOOKS:
            if any([g in target_book["genres"] for g in b["genres"]]):
                similar.append(b)
        return render_template("book.html", book=target_book, current_year=date.today().year, similar_books=similar)
    else:
        abort(404)


@app.route("/about")
def about():
    return render_template("about.html")

def find_similar_books(book, books=BOOKS):
    similar = []
    



if __name__ == "__main__":
    app.run(debug=True)
