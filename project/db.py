#This function returns a connection instance to the corresponding database specified by user input
import sqlite3
def db_connect(database):
    connection = sqlite3.connect(database)
    print('Connected to database successfully')
    return connection