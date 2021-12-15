import tkinter as tk
from tkinter.constants import END
import tkinter.font as font
import sqlite3 as sql

from colours import deep_black, unhighlighted_text

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


liked_songs_screen = LikedSongsScreen()
liked_songs_screen.create_widgets()
liked_songs_screen.apply()