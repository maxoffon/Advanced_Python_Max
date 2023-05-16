from sqlalchemy import create_engine, select, Column, Integer, Text, Date, Float, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from flask import Flask, jsonify

engine = create_engine("sqlite:///python.db")
Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__)
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.count}, {self.release_date}, {self.author_id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    @classmethod
    def get_all_students_with_scholarship(cls):
        return session.query(Student).filter_by(scholarship=True).all()

    @classmethod
    def get_all_with_higher_avg_score(cls, custom):
        return session.query(Student).filter(Student.average_score > custom).all()

class Receiving(Base):
    __tablename__ = 'receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    @hybrid_property
    def count_date_with_book(self):
        return self.date_of_return - self.date_of_issue

@app.before_request
def brfunc():
    Base.metadata.create_all(bind=engine)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/books', methods=['GET'])
def get_all_books():
    books = session.execute(select(Book.id, Book.name, Book.count, Book.release_date, Book.author_id)).all()
    return books[0]

if __name__ == "__main__":
    app.run(debug=True)