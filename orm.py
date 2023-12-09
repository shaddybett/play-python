import sqlite3
CONN = sqlite3.connect('db/ormpets.db')
CURSOR = CONN.cursor()

class Dog:
    def __init__(self,name,breed):
        self.id = None
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):

        sql = """
        CREATE TABLE IF NOT EXISTS pets(
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT        
        )
        """
        CURSOR.execute(sql)
        CONN.commit()
   
    def insert(self):
        sql = """
            INSERT INTO pets(name,breed)
            VALUES
            (?,?)
       """  
        CURSOR.execute(sql(self.name,self.breed))
        CONN.commit()  

    def save(self):
        CONN.commit()    
        
