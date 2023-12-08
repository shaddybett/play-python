class Cats:
    all = []
    def __init__(self,name,breed,age) -> None:
        self.name = name
        self.breed = breed
        self.age = age
        self.add_cat_to_cats(self)
    @classmethod
    def add_cat_to_cats(cls, cat):
        cls.all.append(cat)
    def save(self,cursor):
        cursor.execute(
            'INSERT INTO cats (name,breed,age)VALUES(?,?,?)',
            (self.name,self.breed,self.age)
        )    

import sqlite3
db_connection = sqlite3.connect('db/orm.db')
db_cursor = db_connection.cursor()

Cats('Maru', "scottish fold", 3)
Cats('Hana', 'tortoise', 1)

for cat in Cats.all:
    cat.save(db_cursor)        

        
