import sqlite3
CONN = sqlite3('db/play.db')
CURSOR = CONN.CURSOR

class Dog:
    pets = []
    def __init__(self,name,breed) -> None:
        self.name = name
        self.breed = breed
        .add_pets_to_pets(self)