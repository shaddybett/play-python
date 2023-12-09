import sqlite3
CONN = sqlite3('db/play.db')
CURSOR = CONN.CURSOR

class Dog:
 
    def __init__(self,name,breed):
        self.id = None
        self.name = name
        self.breed = breed
      

    @classmethod
    def create_table(self):
        """
        CREATE TABLE IF NOT EXISTS pets(
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT
        );
        """
    def insert(self):
        """
        INSERT INTO pets
        """    