"""Planning this feature"""

"""How will it work?
- Be a button to activate when the user presses on a song
- Nest this in a window named song_edit feature
- The button will open a window with all of the playlists created
- These playlists will be buttons"""

"""Features:
- creating playlist feature...
---> What this feature will do:
-----> Create a new window for the playlists and use a playlist scaffold
-------> scaffold has empty rows and an Enter box that will be set as the name
-----> Add a table with the playlists name into the database folder
------> 3 columns: song, author, duration"""

"""Global Library / Framework importing"""
from sqlite3.dbapi2 import OperationalError
import tkinter as tk
import tkinter.font as font
import sqlite3 as sql
from PIL import Image, ImageTk

"""Modular imports"""
from colours import deep_black, unhighlighted_text
from spotify_logo_feature import spotify_button


"""Standalone functions"""
def creating_playlist_table(name: str):  # creating the new_playlists

    dbcon = sql.connect("databases/playlists.db")
    query = '''CREATE TABLE {} (songname, author, duration)'''.format(name)

    try:
        dbcon.execute(query)
    except OperationalError:
        print("Table exists try a different name")

    dbcon.commit()


"""Creating playlist feature"""


class CreatingPlaylist():

    def __init__(self):

        # setting up database connection
        self.dbcon = sql.connect("databases/playlists.db")

        # setting up the main window
        self.main_window = tk.Tk()
        self.main_window.config(bg=deep_black)
        self.main_window.geometry("990x700+210+0")
        self.main_window.title("New Playlist")

        # importing the spotify icon image
        try:
            self.spotify_icon = Image.open(fp="images/spotify-logo.png")
            self.spotify_icon_resized = self.spotify_icon.resize((220, 150), Image.ANTIALIAS)
            self.spotify_icon = ImageTk.PhotoImage(master=self.main_window, image=self.spotify_icon_resized)

        except FileNotFoundError or FileExistsError:
            print("You do not have the spotify icon asset")

        # initialising fonts
        self.large_font = font.Font(family="Gothic Medium", size=40)


    def creating_widgets(self):
        
        # gotify image
        self.gotify_image = tk.Button(master=self.main_window,
        image=self.spotify_icon,
        command=spotify_button,
        bg=deep_black,
        fg=deep_black)

        # making the entry box for the user to type the playlist name
        self.entry_text = tk.StringVar()
        self.entry_field = tk.Entry(master=self.main_window,
        textvariable=self.entry_text,
        width=30)

        def applying_playlist_name():

            self.playlist_name = self.entry_field.get()
            creating_playlist_table(self.playlist_name)

            self.playlist_label = tk.Label(master=self.main_window,
            text=self.playlist_name,
            font=self.large_font,
            bg=deep_black,
            fg=unhighlighted_text,
            border=0).grid(row=0, column=1, columnspan=3)

            self.entry_field.destroy()
            self.enter_button.destroy()
        
        self.enter_button = tk.Button(master=self.main_window,
        text="Enter",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0,
        command=applying_playlist_name,
        anchor='w')

        """Title bar things"""
        # songs 
        self.songname_title = tk.Label(master=self.main_window,
        text="Song Name",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0, width=20)

        # author
        self.author_title = tk.Label(master=self.main_window,
        text="Author",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0, width=20)

        # duration
        self.duration_title = tk.Label(master=self.main_window,
        text="Duration",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0, width=20)

    
    def applying_widgets(self):

        # applying gotify image
        self.gotify_image.grid(row=0, column=0, padx=20)
        # self.gotify_label.grid(row=0, column=1)

        # applying the entry field
        self.entry_field.grid(row=0, column=1, columnspan=3)
        self.enter_button.grid(row=0, column=3)

        # titlebar
        self.songname_title.grid(row=2, column=1)
        self.author_title.grid(row=2, column=2)
        self.duration_title.grid(row=2, column=3)

        # screen
        self.main_window.mainloop()


def creatingplaylist_compiled():
    creating_playlist = CreatingPlaylist()
    creating_playlist.creating_widgets()
    creating_playlist.applying_widgets()

creatingplaylist_compiled()
