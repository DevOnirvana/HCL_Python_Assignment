import sqlite3
from helpers.singleton import Singleton

#Helper function to insert the parsed data into a table in the database
def insert_to_db(data, c):
    to_db = [(row['Result Time'], row['Granularity Period'], row['Object Name'], row['Cell ID'], row['CallAttempts'] ) for row in data ]
    try:
        #if table already exists
        c.executemany('''INSERT INTO new_table VALUES (?,?,?,?,?)''',  to_db)
        print('Data added succesfully')
    except:
        #if there is no existing table, create table and enter the parsed data
        c.execute('''CREATE TABLE new_table
                                        (Result Time, Granularity Period, Object Name, Cell ID, CallAttempts)''')
        c.executemany('''INSERT INTO new_table VALUES (?,?,?,?,?)''',  to_db)
        print('Table created and Data added successfully')

#Helper function to lookup the concerned table in the database
def lookup_db(curr):
    try:
        curr.execute('''SELECT * FROM new_table''')
        data = curr.fetchall()
        print("Below is the table where parsed data is stored")
        for row in data:
            print(row)
    except:
        print('No table with such name ')

#We create a class a class and we decorate it with the Singleton class
#The Singleton class implements the Singleton Design Pattern
#Now there is a only one single instance of a database at a time
@Singleton
class DBConnection:
    db_connection = None
    def db_connect(self, db):
        if self.db_connection is None: # Creates a new connection if only there is nno existing connection or returns the existing
            self.db_connection = sqlite3.connect(db)
            print('Database connected Successfully')
        return self.db_connection
