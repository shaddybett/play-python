import sqlite3
CONN = sqlite3.connect('db/ormpets.db')
CURSOR = CONN.cursor

class Dog:
    def __init__(self) -> None:
        pass
