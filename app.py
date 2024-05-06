#!/usr/bin/env python

import os

from flask import Flask
from flask import render_template

from database import db, Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()

    # fill DB with testing data(fixtures)
    drama = Genre(name="Драма")
    db.session.add(drama)
    for_children = Genre(name="Для детей")
    db.session.add(for_children)

    voina_i_mir = Book(name_book="Война и мир", genre=drama)
    db.session.add(alex)
    palata_6 = Book(name_book="Палата №6", genre=drama)
    db.session.add(daria)
    kolobok = Book(name_book="Колобок", genre=for_children)
    db.session.add(petr)

    db.session.commit()


@app.route("/")
def all_books():
    books = Book.query.all()
    return render_template("all_books.html", books=books)


@app.route("/genre/<int:genre_id>")
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "employees_by_department.html",
        genre_name=genre.name,
        books=genre.books,
    )


if __name__ == '__main__':
    app.run()
