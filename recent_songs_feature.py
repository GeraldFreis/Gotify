"""Library / Framework imports"""
import tkinter as tk
import tkinter.font as font
import  sqlite3 as sql


"""Modular Imports"""
from colours import deep_black, unhighlighted_text
from searching_feature_backend import real_search

"""Recent songs configuration"""

class RecentSongs():

    def __init__(self):

        # database connection
        self.dbcon = sql.connect(r"databases/recent_searches.db")


        """Tkinter window"""
        self.main_recent_song_window = tk.Tk()
        self.main_recent_song_window.title("Recent Songs")
        self.main_recent_song_window.config(bg=deep_black)
        self.main_recent_song_window.geometry("1200x800+0+0")
    
    def displaying_songs(self):

        """Functions"""
        def retreiving_recent_songs():

            # creating lists to store recent searches
            retreiving_query = '''SELECT * FROM searches'''
            all_songs_raw_list = list(self.dbcon.execute(retreiving_query))

            # finding recent 20 songs and appending them to the display songs
            displayed_songs = list()

            for rows in all_songs_raw_list:
                displayed_songs.append(rows[0])
            
            return displayed_songs
        
        def widgets():

            # fonts
            large_font = font.Font(family="Gothic Medium", size=100)
            small_font = font.Font(family="Gothic Medium", size=10)

            """Frames"""

            # gotify label frame
            gotify_frame = tk.Frame(master=self.main_recent_song_window,
            bg=deep_black).grid(row=0, column=1)

            # song display frame
            song_frame = tk.Frame(master=self.main_recent_song_window,
            bg=deep_black,
            width=800, height=600).grid(row=2, column=1, rowspan=20)

            # centering frame
            centering_frame = tk.Frame(master=self.main_recent_song_window,
            bg=deep_black,
            width=200, height=0).grid(row=0, column=0, rowspan=20)

            """Main Labels"""
            
            # gotify label
            gotify_label = tk.Label(master=self.main_recent_song_window,
            text="Gotify",
            font=large_font,
            bg=deep_black,
            fg=unhighlighted_text).grid(row=0, column=1)

            # songs to display
            songs_to_display = retreiving_recent_songs()
            beginning_row = 2

            for song in songs_to_display:
                # print(song)
                def compiled_real_search():
                    real_search(search=song)
                
                song_label = tk.Button(master=self.main_recent_song_window,
                bg=deep_black, fg=unhighlighted_text,
                command=compiled_real_search,
                text=song,
                font=small_font).grid(row=beginning_row, column=1)

                beginning_row += 1
            
            self.main_recent_song_window.mainloop()

        widgets()


def recent_songs_compiled():
    recentsongs = RecentSongs()
    recentsongs.displaying_songs()

# recent_songs_compiled()
