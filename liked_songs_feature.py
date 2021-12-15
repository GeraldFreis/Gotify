"""Library / Framework Imports"""
from sqlite3.dbapi2 import DataError, DatabaseError
import tkinter as tk
from tkinter import *
import tkinter.font as font
import sqlite3 as sql

"""Modular imports"""
from colours import deep_black, unhighlighted_text
try:
    from searching_feature_backend import real_search
except:
    pass

"""Liked Song Class"""


class LikedSongs():

    def __init__(self, search, search_window):

        # initialising the databases
        self.dbcon = sql.connect(r'databases/liked_songs.db')
        self.dbcursor = self.dbcon.cursor()

        # search
        self.user_search = search

        # search window
        self.main_search_window = search_window

        # # creating table if it does not already exist
        # try:
        #     sql_query = '''CREATE TABLE likedsongs (song, number)'''
        #     self.dbcon.execute(sql_query)
        #     self.dbcon.commit()

        # except DatabaseError or DataError:
        #     print("There was a problem in initialising the tables in database 'liked_songs' ")
        #     pass


    def creating_question_tab(self):

        self.main_window = tk.Tk()
        self.main_window.title("Add Song to Liked Songs")
        self.main_window.geometry("500x100+400+500")
        self.main_window.config(bg=deep_black)

        # fonts
        self.large_font = font.Font(family="Gothic Medium", size=100)
        self.medium_font = font.Font(family="Gothic Medium", size=20)
        self.small_font = font.Font(family="Gothic Medium", size=10)

        """Features for the window"""

        # commands for buttons
        #   # save song command
        def save_song():

            def adding_liked_song(song):

                    def returning_number():

                        try:
                            # extracting list
                            raw_list = list(self.dbcon.execute('''SELECT * FROM likedsongs'''))

                            # sorting the list by number
                            raw_list.sort(reverse=True)

                            # finding latest pair and hence number
                            try:
                                latest_pair = raw_list[0]
                                latest_number = int(latest_pair[1])
                            except IndexError:
                                latest_number = 0
                                print("Index out of range - code line 75 in liked songs feature")
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


            adding_liked_song(self.user_search)

            real_search(self.user_search)

            self.main_search_window.destroy()
            self.main_window.destroy()

        #   # no button command
        def no_option():
            real_search(self.user_search)
            self.main_search_window.destroy()
            self.main_window.destroy()

        # labels
        self.question_label = tk.Label(master=self.main_window,
        text="Would you like to save this song",
        font=self.small_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=0)

        # buttons
        self.save_song_button = tk.Button(master=self.main_window,
        text="Save",
        command=save_song,
        font=self.small_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=1)

        self.no_button = tk.Button(master=self.main_window,
        text="Not this one",
        command=no_option,
        font=self.small_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=1)

        # applying all features
        self.question_label.grid(row=1, column=2, columnspan=2)
        self.save_song_button.grid(row=2, column=1)
        self.no_button.grid(row=2, column=4)

        # mainloop
        self.main_window.mainloop()


# likedsong = LikedSongs('hi')
# likedsong.creating_question_tab()

class LikedSongsScreen():
    def __init__(self):
        self.dbcon = sql.connect("databases/liked_songs.db")
        
        """Setting up the main interface"""
        self.main_window = tk.Tk()
        self.main_window.config(bg=deep_black)
        self.main_window.geometry("990x700+210+0")
        self.main_window.title("Liked Songs")

        """Fonts"""
        self.large_font = font.Font(family="Gothic Medium", size=40)
        self.medium_font = font.Font(family="Gothic Medium", size=20)
        self.small_font = font.Font(family="Gothic Medium", size=10)

    """Creating the widgets to be applied onto the screen"""
    def create_widgets(self):

        # retrieving a list of liked songs
        def retrieving_songs():
            retreiving_query = '''SELECT * FROM likedsongs'''
            retrieved_list = list(self.dbcon.execute(retreiving_query))
            return retrieved_list
        
        # creating the widgets
        self.centering_frame = tk.Frame(master=self.main_window,
        bg=deep_black, width=400).grid(row=0, column=0)

        self.gotify_label = tk.Label(master=self.main_window,
        text="Gotify",
        font=self.large_font,
        bg=deep_black,
        fg=unhighlighted_text,
        activeforeground=deep_black,
        anchor='center')

        self.songs = retrieving_songs()
        self.songs_list = list()
        for song in self.songs:
            self.songs_list.append(song[0])

        # self.main_window.mainloop()
    
    def apply(self):
        self.gotify_label.grid(row=0, column=2)
        
        """Creating the liked_songs distribution"""
        rowcount = 1
        columncount = 1
        for song in self.songs_list:

            columncount += 1

            if rowcount <= 30:

                if columncount <= 3:
                    lbl = tk.Button(master=self.main_window,
                    text=song,
                    height=3, width=5).grid(
                        row=rowcount, column=columncount, padx=2, pady=2)
                
                elif columncount == 4:
                    columncount = 0
                    rowcount += 1
            else:
                pass

        self.main_window.mainloop()



def liked_songs_screen_compiled():
    liked_songs_screen = LikedSongsScreen()
    liked_songs_screen.create_widgets()
    liked_songs_screen.apply()
