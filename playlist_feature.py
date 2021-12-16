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
import tkinter as tk
import tkinter.font as font
import sqlite3 as sql
from PIL import Image, ImageTk

"""Modular imports"""
from colours import deep_black, unhighlighted_text


"""Standalone functions"""
def creating_playlist_table(name: str):  # creating the new_playlists
    dbcon = sql.connect("databases/playlists.db")
    query = '''CREATE TABLE {} (songname, author, duration)'''.format(name)
    dbcon.execute(query)
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
        bg=deep_black,
        fg=deep_black)

        # making the entry box for the user to type the playlist name
        self.entry_text = tk.StringVar()
        self.entry_field = tk.Entry(master=self.main_window,
        textvariable=self.entry_text)

        def retrieving_playlist_name():
            self.playlist_name = self.entry_field.get()
            creating_playlist_table(self.playlist_name)
        
        self.enter_button = tk.Button(master=self.main_window,
        text="Enter",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0,
        command=retrieving_playlist_name)


        # self.gotify_label = tk.Label(master=self.main_window,
        # text="Gotify",
        # bg=deep_black,
        # fg=unhighlighted_text,
        # width=10, height=2,
        # border=0)
    
    def applying_widgets(self):

        # applying gotify image
        self.gotify_image.grid(row=0, column=0)
        # self.gotify_label.grid(row=0, column=1)

        # applying the entry field
        self.entry_field.grid(row=0, column=3)
        self.enter_button.grid(row=0, column=4)

        # screen
        self.main_window.mainloop()




def creatingplaylist_compiled():
    creating_playlist = CreatingPlaylist()
    creating_playlist.creating_widgets()
    creating_playlist.applying_widgets()

creatingplaylist_compiled()
