# first we import sqlite3
import sqlite3
# we then import os which helps in navigation to the db directory
import os

# Get the absolute path to the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Corrected: sqlite3.connect instead of sqlite3
# we make a connection to the database which for our case is play.db
CONN = sqlite3.connect('db/play.db')
# we make a cursor used to execute sql commands
CURSOR = CONN.cursor()

class Dog:
 
    def __init__(self, name, breed):
        self.id = None
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):

        # Corrected: Added the execution of the SQL statement
        sql = """
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def insert(self):

        # Corrected: Added the execution of the SQL statement
        sql = """
            INSERT INTO pets (name, breed)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.breed))
        CONN.commit()

    def save(self):
        # Corrected: Changed 'CURSOR.save' to 'CONN.commit' to save changes to the database
        CONN.commit()
    @classmethod
    def fetch_all(cls):
        sql = 'SELECT * FROM pets'
        return CURSOR.fetchall()     

Dog.create_table()
my_dog = Dog(name='Jojo',breed='T9')
my_dog.insert()
CONN.commit()  

all_dogs = Dog.fetch_all()
for dog in all_dogs:
    print(dog)
