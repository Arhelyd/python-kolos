from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# engine = create_engine ('sqlite:///books_zad4.db', echo = True)
engine = create_engine('sqlite:///books_zad4.db')


# ORM
class Authors(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    author_name = Column(String(100), unique=True)
    books = relationship("Books", back_populates="author")


class Books(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    title = Column(String(100), unique=True)
    genre = Column(String(100))
    author = relationship("Authors", back_populates="books")
    borrowing = relationship("Borrowings", back_populates="book")


class Readers(Base):
    __tablename__ = 'readers'
    reader_id = Column(Integer, primary_key=True)
    reader_name = Column(String(100), unique=True)
    borrowings = relationship("Borrowings", back_populates="reader")


class Borrowings(Base):
    __tablename__ = 'borrowings'
    borrow_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.book_id', ondelete='CASCADE'),
                     unique=True)
    reader_id = Column(Integer, ForeignKey('readers.reader_id'))
    book = relationship("Books", back_populates="borrowing")
    reader = relationship("Readers", back_populates="borrowings")


# Create tables
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()

print("AUTHORS TABLE:")
for author in session.query(Authors).all():
    print(author.author_id, author.author_name)

print("BOOKS TABLE:")
for book in session.query(Books).all():
    print(book.book_id, book.author_id, book.title, book.genre)

print("READERS TABLE:")
for reader in session.query(Readers).all():
    print(reader.reader_id, reader.reader_name)

print("BORROWINGS TABLE:")
for borrow in session.query(Borrowings):
    print(borrow.borrow_id, '-', borrow.book.author.author_name,
          '-', borrow.book.title, '-', borrow.reader.reader_name)

# Add reader
try:
    session.add(Readers(reader_name='Lech Majewski'))
    session.commit()
except exc.SQLAlchemyError as ex:
    session.rollback()

# Add borrowing
try:
    b_id = session.query(Books.book_id).\
           filter(Books.title == 'Harry Potter i więzień Azbakanu').scalar()
    r_id = session.query(Readers.reader_id).\
           filter(Readers.reader_name == 'Lech Majewski').scalar()
except exc.SQLAlchemyError as ex:
    session.rollback()

session.commit()
session.close()
