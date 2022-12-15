import sqlite3


sql_authors_table = '''CREATE TABLE IF NOT EXISTS authors (
                       author_id INTEGER PRIMARY KEY,
                       author_name text,
                       UNIQUE(author_name))
                    '''

sql_books_table = '''CREATE TABLE IF NOT EXISTS books (
                     book_id INTEGER PRIMARY KEY,
                     author_id INTEGER,
                     title text,
                     genre text,
                     FOREIGN KEY(author_id) REFERENCES authors(autor_id),
                     UNIQUE(title))
                  '''

sql_readers_table = '''CREATE TABLE IF NOT EXISTS readers (
                       reader_id INTEGER PRIMARY KEY,
                       reader_name text,
                       UNIQUE(reader_name))
                    '''

sql_borrowings_table = '''CREATE TABLE IF NOT EXISTS borrowings (
                          borrow_id INTEGER PRIMARY KEY,
                          book_id INTEGER,
                          reader_id INTEGER,
                          FOREIGN KEY(book_id) REFERENCES books(book_id),
                          FOREIGN KEY(reader_id) REFERENCES readers(reader_id),
                          UNIQUE(book_id))
                       '''


def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)


def insert_author(conn, author_r):
    sql = '''INSERT OR IGNORE INTO authors(author_name)
              VALUES(?)'''
    cur = conn.cursor()
    cur.execute(sql, author_r)
    return cur.lastrowid


def insert_book(conn, book_r):
    sql = '''INSERT OR IGNORE INTO books(author_id,title,genre)
              VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, book_r)
    return cur.lastrowid


def insert_reader(conn, reader_r):
    sql = '''INSERT OR IGNORE INTO readers(reader_name)
              VALUES(?)'''
    cur = conn.cursor()
    cur.execute(sql, reader_r)
    return cur.lastrowid


def insert_borrow(conn, borrow_r):
    sql = '''INSERT OR IGNORE INTO borrowings(book_id,reader_id)
             VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, borrow_r)
    return cur.lastrowid


def del_borrow(conn, b_id):
    sql = "DELETE FROM borrowings WHERE borrow_id=(?)"
    cur = conn.cursor()
    cur.execute(sql, (b_id,))
    return cur.lastrowid


connection = sqlite3.connect('books_zad3.db')
cursor = connection.cursor()

# authors
create_table(connection, sql_authors_table)
insert_author(connection, ('Joan Rowling', ))

# books
create_table(connection, sql_books_table)
cursor.execute('SELECT author_id FROM authors WHERE author_name=?',
               ('Joan Rowling',))

(a_id, ) = cursor.fetchone()

insert_book(connection, (a_id, 'Harry Potter i Kamień Filozoficzny',
            'fantasy'))
insert_book(connection, (a_id, 'Harry Potter i Komnata Tajemnic', 'fantasy'))
insert_book(connection, (a_id, 'Harry Potter i więzień Azbakanu', 'fantasy'))
insert_book(connection, (a_id, 'Harry Potter i Czara Ognia', 'fantasy'))
insert_book(connection, (a_id, 'Harry Potter i Zakon Feniksa', 'fantasy'))
insert_book(connection, (a_id, 'Harry Potter i Książę Półkrwii', 'fantasy'))
insert_book(connection, (a_id, 'Harry Potter i Insygnia Śmierci', 'fantasy'))

# readers
create_table(connection, sql_readers_table)

insert_reader(connection, ('Jan Kowalski',))
insert_reader(connection, ('Kazimierz Nowak',))
insert_reader(connection, ('Tadeusz Opolski',))
insert_reader(connection, ('Józef Malinowski',))

# borrowings
create_table(connection, sql_borrowings_table)

# find book ID by title
cursor.execute('SELECT book_id FROM books WHERE title=?',
               ('Harry Potter i Czara Ognia',))
(bid,) = cursor.fetchone()

# find reader ID by name
cursor.execute('SELECT reader_id FROM readers WHERE reader_name=?',
               ('Kazimierz Nowak',))
(rid,) = cursor.fetchone()

# insert borrowing 1
insert_borrow(connection, (bid, rid))

cursor.execute('SELECT book_id FROM books WHERE title=?',
               ('Harry Potter i Insygnia Śmierci',))
(bid,) = cursor.fetchone()

# find reader ID by name
cursor.execute('SELECT reader_id FROM readers WHERE reader_name=?',
               ('Jan Kowalski',))
(rid,) = cursor.fetchone()

# insert borrowing 2
insert_borrow(connection, (bid, rid))

# show tables
print('AUTHORS TABLE:')
for row in cursor.execute('SELECT * FROM authors'):
    print(row)

print('BOOKS TABLE:')
for row in cursor.execute('SELECT * FROM books'):
    print(row)

print('READERS TABLE:')
for row in cursor.execute('SELECT * FROM readers'):
    print(row)

print('RAW BORROWINGS TABLE:')
for row in cursor.execute('SELECT * FROM borrowings'):
    print(row)

print('BORROWINGS TABLE:')
for row in cursor.execute('''SELECT borrow_id, author_id, title,reader_name
                             FROM borrowings
                             INNER JOIN books ON
                             books.book_id=borrowings.book_id
                             INNER JOIN readers ON
                             readers.reader_id=borrowings.reader_id'''):
    print(row)

# delete borrowing 1
del_borrow(connection, 1)

print('BORROWINGS TABLE:')
for row in cursor.execute('''
                SELECT borrow_id,author_name,title,reader_name FROM borrowings
                INNER JOIN authors ON authors.author_id=books.author_id
                INNER JOIN books ON books.book_id=borrowings.book_id
                INNER JOIN readers ON readers.reader_id=borrowings.reader_id
                '''):
    print(row)

# rollback 
connection.rollback()

connection.commit()
connection.close()
