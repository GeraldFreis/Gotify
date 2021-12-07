"""Library / Framework imports"""
import tkinter as tk
import  sqlite3 as sql


"""Modular Imports"""
from colours import deep_black, unhighlighted_text

"""Recent songs configuration"""

class RecentSongs():

    def __init__(self):

        # database connection
        self.dbcon = sql.connect(r"databases\recent_searches.db")

    def displaying_songs(self):

        """Functions"""
        def retreiving_recent_songs():

            # creating lists to store recent searches
            retreiving_query = '''SELECT * FROM searches'''
            all_songs_raw_list = list(self.dbcon.execute(retreiving_query))
            all_songs_raw_list.sort(reverse=True)

            # finding recent 20 songs and appending them to the display songs
            displayed_songs = list()

            for rows in all_songs_raw_list:
                displayed_songs.append(rows[0])
            
            return displayed_songs
        
        def widgets():

            """Initialising the main widget"""
            main_recent_song_window = tk.Tk()
            main_recent_song_window.title("Recent Songs")
            main_recent_song_window.config(bg=deep_black)
            main_recent_song_window.geometry("1200x800+0+0")

            """Frames"""

            # gotify label frame
            gotify_frame = tk.Frame(master=main_recent_song_window,
            bg=deep_black,
            width=800, height=100).grid(row=0, column=1)

            # song display frame
            song_frame = tk.Frame(master=main_recent_song_window,
            bg=deep_black,
            width=800, height=600).grid(row=2, column=1)

            # centering frame
            centering_frame = tk.Frame(master=main_recent_song_window,
            bg=deep_black,
            width=200, height=0).grid(row=0, column=0, rowspan=20)

            """Main Labels"""




