import sqlite3 as sql
import os

def pathDB(path="db/data/dataBaseTest.db"):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        connection = sql.connect(path) 
        cursor = connection.cursor()
    else: 
        connection = sql.connect(path) 
        cursor = connection.cursor()
    return cursor , connection
   
   