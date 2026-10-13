from flask import Flask, render_template
from books import BOOKS
from datetime import date
app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html", 
        site_title="Книжная полка",
        book_count=len(BOOKS),
        first_book=BOOKS[0]
        )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/book/<int:book_id>")
def book(book_id:int = None):
    valid_ids = [book["id"] for book in BOOKS]
    if book_id not in valid_ids:
        return ("Некорректная  книга", 400)
    book_dict = [book for book in BOOKS if book["id"]==book_id][0]
    return render_template("book.html", book=book_dict, current_year=date.today().year)



if __name__ == "__main__":
    app.run(debug=True)
























