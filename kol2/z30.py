import sqlite3
sql_test_table = '''CREATE TABLE IF NOT EXISTS test (
id integer,
name text,
value real
)'''
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute(sql_test_table)
connection.commit()
connection.close()