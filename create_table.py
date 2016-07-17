import sqlite3

conn = sqlite3.connect('big.db')

print("Opened database successfully")
conn.execute('''CREATE TABLE MOVIE
           (ID INT PRIMARY KEY NOT NULL,
            SCORE DECIMAL(3,1) NOT NULL,
            MOVIENAME TEXT NOT NULL);''')
print("Table created successfully")
