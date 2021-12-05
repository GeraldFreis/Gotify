"""Library / Framework importing"""
import urllib
import sqlite3 as sql
from sqlite3.dbapi2 import DataError, DatabaseError
import tkinter as tk

"""Modular imports"""
from searching_feature_frontend import search

def real_search(search):
    urllib.open("www.google.com+search")

def writing_search_to_db(self, search):

    """Initialising database"""

    self.dbcon = sql.connect(r"databases/recent_searches.db")
    self.dbcursor = self.dbcon.cursor()

    """writing features"""

    # checking if the tabels exist and if not creating them
    try:
        creating_database_query = '''CREATE TABLE searches (search, number)'''
        self.dbcon.execute(creating_database_query)
        self.dbcon.commit()

    except DatabaseError or DataError:
        print("Table already exists")
    
    # finding most recent number and hence the number to use for the searches
    try:
        retrieving_number_query = '''SELECT * FROM searches COLUMN number'''
        raw_number_list = list(self.dbcon.execute(retrieving_number_query))
        sorted_number_list = raw_number_list.sort(reverse=True)
        self.last_number = sorted_number_list[0]

    except DataError or DatabaseError:
        print("Something went wrong here at line 52")
    
    # writing the search to the table
    try:
        number = self.last_number + 1
        adding_search_query = '''INSERT INTO searches VALUES (?, ?)'''
        data = (search, number)
        self.dbcon.execute(adding_search_query, data)

    except DatabaseError or DataError:
        print('n')
