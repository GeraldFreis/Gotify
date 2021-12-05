"""Library / Framework importing"""
import urllib
import sqlite3 as sql
from sqlite3.dbapi2 import DataError, DatabaseError
import tkinter as tk
import webbrowser as wb


"""Modular imports"""

def real_search(search):
    wb.open("https://www.youtube.com/results?search_query={}".format(search))

def writing_search_to_db(search):

    """Initialising database"""

    dbcon = sql.connect(r"databases/recent_searches.db")
    dbcursor = dbcon.cursor()

    """writing features"""

    # checking if the tabels exist and if not creating them
    try:
        creating_database_query = '''CREATE TABLE searches (search, number)'''
        dbcon.execute(creating_database_query)
        dbcon.commit()

    except DatabaseError or DataError:
        print('')
    
    # finding most recent number and hence the number to use for the searches
    try:
        retrieving_number_query = '''SELECT * FROM searches'''
        raw_pair_list = list(dbcon.execute(retrieving_number_query))
        raw_pair_list.sort(reverse=True)
        latest_pair = raw_pair_list[0]
        last_number = latest_pair[1]

    except DataError or DatabaseError:
        print("Something went wrong here at line 39")
    
    # writing the search to the table
    try:
        number = last_number + 1
        adding_search_query = '''INSERT INTO searches VALUES (?, ?)'''
        data = (search, number)
        dbcon.execute(adding_search_query, data)
        dbcon.commit()

        print('added search to database')

    except DatabaseError or DataError:
        print('n')
