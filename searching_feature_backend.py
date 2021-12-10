"""Library / Framework importing"""
from tkinter.constants import LEFT
import tkinter.ttk as ttk
import urllib
import sqlite3 as sql
from sqlite3.dbapi2 import DataError, DatabaseError
import tkinter as tk
import webbrowser as wb
import mouse 
import time

# from mouseinfo import PyAutoGui as pag

"""Modular imports"""
from colours import deep_black, unhighlighted_text
"""Functions"""

def mouse_funct():
    mouse_pos = mouse.get_position()
    print(mouse_pos)
    video_pos = (150, 300)

    differencex = video_pos[0] - mouse_pos[0]
    differencey = video_pos[1] - mouse_pos[1]

    time.sleep(3.5)
    mouse.move(video_pos[0], video_pos[1], absolute=True, duration=0.01)
    mouse.click(button=LEFT)

def real_search(search):
    if search == '':
        wb.open("https://www.youtube.com/results?search_query=rat&sp=EgIQAQ%253D%253D")
        mouse_funct()
    else:
        wb.open("https://www.youtube.com/results?search_query={}&sp=EgIQAQ%253D%253D".format(search))
        mouse_funct()
    
    # COMMENTED BECAUSE CLICKING FEATURE CAN BE INITIALISED LATER
    # pag.click()


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

        try:
            latest_pair = raw_pair_list[0]
        except IndexError:
            latest_pair = (0,0)

        last_number = latest_pair[1]

    except DataError or DatabaseError or IndexError:
        print("Something went wrong here at line 39")

    
    # writing the search to the table
    try:
        number = last_number + 1
        adding_search_query = '''INSERT INTO searches VALUES (?, ?)'''
        data = (search, number)
        dbcon.execute(adding_search_query, data)
        dbcon.commit()

        print('added search to database')

    except DatabaseError or DataError or IndexError:
        print('n')

"""Combobox"""
def recent_song_combobox(main_window):

    """Connection to database"""
    dbcon = sql.connect(r'databases\recent_searches.db')

    """Retrieving songs"""
    retrieving_query = '''SELECT * FROM searches'''
    all_info_list = list(dbcon.execute(retrieving_query))
    song_list = list()

    for pair in all_info_list:
        song_list.append(pair[0])

    print(song_list)
    """Drawing the combobox"""
    text="Recent Searches"
    song_combobox = ttk.Combobox(master=main_window,
    values=song_list,
    textvariable=text,
    background=deep_black,
    foreground=unhighlighted_text,
    height=10)

    song_combobox.grid(row=5, column=1)

