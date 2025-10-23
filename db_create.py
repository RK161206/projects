#SQL Library
import sqlite3

#finds or creates a file called 'users.db' This is part of the database.
db_locale = 'users.db'

#THis part of the website connects the two 
connection = sqlite3.connect(db_locale)
c = connection.cursor()
#Create users table if it doesn't exist

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTONCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
connection.commit()
connection.close()
