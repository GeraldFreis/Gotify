"""Library / Framework Imports"""
from sqlite3.dbapi2 import DataError, DatabaseError
import tkinter as tk
from tkinter import *
import sqlite3 as sql

"""Modular imports"""
from colours import deep_black, unhighlighted_text

"""Liked Song Class"""


class LikedSongs():

    def __init__(self):

        # initialising the databases
        self.dbcon = sql.connect(r'databases/liked_songs.db')
        self.dbcursor = self.dbcon.cursor()

        # creating table if it does not already exist
        try:
            sql_query = '''CREATE TABLE likedsongs (song, number)'''
            self.dbcon.execute(sql_query)
            self.dbcon.commit()

        except DatabaseError or DataError:
            print("There was a problem in initialising the tables in database 'liked_songs' ")

    def creating_question_tab(self):

        self.main_window = Tk()
        self.main_window.title("Add Song to Liked Songs")
        self.main_window_geometry("300x300+400+500")
        self.main_window.config(bg=deep_black)

        """Features for the window"""

    def adding_liked_song(self, song):

        def returning_number(self):

            try:
                # extracting list
                raw_list = list(self.dbcon.execute('''SELECT * FROM likedsongs'''))

                # sorting the list by number
                raw_list.sort(reverse=True)

                # finding latest pair and hence number
                latest_pair = raw_list[0]
                latest_number = int(latest_pair[1])
                return latest_number

            except DataError or DatabaseError:
                print("There was a problem retrieving the most recent number")
                latest_number = 0

        try:
            sql_query = '''INSERT INTO likedsongs VALUES (?, ?)'''

            number = returning_number() + 1
            data = song, number

            self.dbcon.execute(sql_query, data)
            self.dbcon.commit()
        except DatabaseError or DataError:
            print("There was a problem within adding liked songs feature")
        

