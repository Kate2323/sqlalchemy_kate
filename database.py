from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_book = db.Column(db.String, nullable=True)
    added = db.Column(db.DateTime, nullable=False, default=func.now())

    genre_id = db.Column(db.Integer, db.ForeignKey("department.id", ondelete='SET NULL'))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"User(name_of_book={self.name_book!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = relationship(
        "Book", back_populates="genre"
    )

    def __repr__(self):
        return f"Genre(genre={self.name!r})"


