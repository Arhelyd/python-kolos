import sqlite3

sql_boot_table = '''CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY,
                    author text,
                    title text,
                    genre text )
                 '''


def create_table(conn, create_table_sql):
    conn.cursor().execute(create_table_sql)


def add_book_record(conn, book_record):
    sql = 'INSERT INTO books(author,title,genre) VALUES(?,?,?)'
    cur = conn.cursor()
    cur.execute(sql, book_record)
    return cur.lastrowid


connection = sqlite3.connect('books_zad1_2.db')
cursor = connection.cursor()

create_table(connection, sql_boot_table)

# dodanie nowych rekordów
add_book_record(connection, ('Rowling Joan',
                             'Harry Potter i Kamień Filozoficzny',
                             'fantasy'))
add_book_record(connection, ('Rowling Joan',
                             'Harry Potter i Komnata Tajemnic',
                             'fantasy',))
add_book_record(connection, ('Rowling Joan',
                             'Harry Potter i więzień Azbakanu',
                             'fantasy',))
add_book_record(connection, ('Rowling Joan',
                             'Harry Potter i Czara Ognia',
                             'fantasy',))
add_book_record(connection, ('Rowling Joan',
                             'Harry Potter i Zakon Feniksa',
                             'fantasy'))
add_book_record(connection, ('Rowling Joan',
                             'Harry Potter i Książę Półkrwii',
                             'fantasy'))
add_book_record(connection, ('Rowling Joan',
                             'Harry Potter i Insygnia Śmierci',
                             'fantasy'))

# wydruk wszystkich rekordów z books
print('Przed rollback:')
for row in cursor.execute('SELECT * FROM books'):
    print(row)

# cofnięcie dodania kolejnych rekordów
# zakomentuj jeśli nie ma pliku: books_zad1_2.db
connection.rollback()

# wydruk wszystkich rekordów z books
print('Po rollback:')
for row in cursor.execute('SELECT * FROM books'):
    print(row)

connection.commit()
connection.close()
