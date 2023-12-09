import sqlite3
CONN = sqlite3('db/play.db')
CURSOR = CONN.CURSOR

class Dog:
    def __init__(self,name,breed) -> None:
        self.name = name