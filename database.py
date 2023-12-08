import sqlite3

db_connection = sqlite3.connect('db/orm.db')
db_cursor = db_connection.cursor()
