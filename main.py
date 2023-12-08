from cat import Cats
from database import db_cursor
from database import db_connection

Cats('Maru', "Scottish Fold", 3)
Cats('Hana', 'Tortoise', 1)

for cat in Cats.all:
    cat.save(db_cursor)

# Commit the changes and close the connection
db_connection.commit()
db_connection.close()
