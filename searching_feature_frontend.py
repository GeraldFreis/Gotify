"""Library / Framework imports"""
from sqlite3.dbapi2 import DataError, DatabaseError
import tkinter as tk
from tkinter import ttk as ttk
from PIL import Image, ImageTk
import tkinter.font as font
import sqlite3 as sql
# import beautifulsoup4 as bs

"""Modular Imports"""
from colours import (deep_black,
unhighlighted_text, main_black_background)
from searching_feature_backend import writing_search_to_db
from liked_songs_feature import LikedSongs

"""Globals"""
search = str()

"""Main Class"""

class Searching:

    def __init__(self):

        """Making the screen to search"""
        self.main_search_window = tk.Tk()
        self.main_search_window.geometry("1200x800+0+0")
        self.main_search_window.title("Search for a song or album")
        self.main_search_window.config(bg=deep_black)


    def searching_feature(self):
        """Fonts"""
        
        self.large_font = font.Font(family="Gothic Medium", size=400)
        self.medium_font = font.Font(family="Gothic Medium", size=20)
        self.small_font = font.Font(family="Gothic Medium", size=10)

        """Tkinter features"""

        # centering frame
        # self.centering_frame = tk.Frame(master=self.main_search_window,
        # width=300, height=150,
        # bg=deep_black)


        # frames
        """Setting up features"""   
        
        main_font = font.Font(family="Gothic Medium", size=40)
        new_main_font = font.Font(family="Gothic Medium", size=100)

        self.frame_to_center = tk.Frame(master=self.main_search_window, bg=deep_black, width=400, height=50, border=0)
        
        # frame for labels
        
        self.search_label_frame = tk.Frame(master=self.main_search_window, bg=deep_black, width=400, height=200, border=0)


        # Gotify Label and image
        try:
            # resizing image
            self.spotify_icon_img = (Image.open(fp=r"images\spotify-logo.png"))
            self.spotify_icon_img = self.spotify_icon_img.resize((440,325), Image.ANTIALIAS)
            self.spotify_icon_img = ImageTk.PhotoImage(master=self.main_search_window, image=self.spotify_icon_img)
        
        except FileNotFoundError or FileExistsError:
            print("You do not have the necessary assets in this directory")
        

        self.gotify_label = tk.Label(master=self.search_label_frame,
        text="Gotify",
        font=new_main_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=0)

        """Aesthetics"""
        self.spotify_logo_icon = tk.Button(master=self.main_search_window,
        bg=deep_black,
        image=self.spotify_icon_img,
        border=0,
        height=325,
        width=400)


        # guide label

        self.guide_label = tk.Label(master=self.main_search_window,
        text="Enter your search beneath",
        font=self.medium_font,
        fg=unhighlighted_text,
        bg=deep_black,
        height=2,
        border=0)

        # # search label
        self.search_label = tk.Label(master=self.main_search_window,
        text='Search: ',
        font=self.medium_font,
        fg=unhighlighted_text,
        bg=deep_black,
        border=0)

        # # search entry
        self.entry_contents = tk.StringVar()
        self.entry_field = tk.Entry(master=self.main_search_window,
        textvariable=self.entry_contents,
        width=75)

        # search recent song list
        self.recent_song_list = ttk.Combobox(master=self.main_search_window
        )

        # returning entry contents
        def returning_contents():

            global search

            search = self.entry_field.get()

            writing_search_to_db(search=search)

            likedsong = LikedSongs(search, self.main_search_window)
            likedsong.creating_question_tab()

            self.main_search_window.destroy()

            return search
        
        # enter search button
        self.enter_button = tk.Button(master=self.main_search_window,
        text="Enter Search",
        command=returning_contents,
        font=self.small_font,
        fg=unhighlighted_text,
        bg=deep_black,
        border=1)

        """applying everything"""
        """Tkinter features"""

        # centering frame
        # self.centering_frame.grid(row=0, column=0)

        self.search_label_frame.grid(row=0, column=2, columnspan=2, rowspan=4)
        
        self.frame_to_center.grid(row=0, rowspan=3, column=1, columnspan=1)
        self.gotify_label.grid(row=0, column=1, rowspan=2, columnspan=3)
        self.spotify_logo_icon.grid(row=0, column=1, rowspan=2, columnspan=1)

        self.guide_label.grid(row=3, column=2, columnspan=1)
        self.search_label.grid(row=4, column=1)
        self.entry_field.grid(row=4, column=2)
        self.enter_button.grid(row=5, column=3)
        
    
    # def apply(self):
    #     """Tkinter features"""

    #     # centering frame
    #     # self.centering_frame.grid(row=0, column=0)
        
    #     self.frame_to_center.grid(row=0, rowspan=3, column=1, columnspan=1)
    #     self.gotify_label.grid(row=1, column=3)
    #     self.spotify_logo_icon.grid(row=0, column=1, rowspan=2, columnspan=1)

    #     self.guide_label.grid(row=3, column=2, columnspan=1)
    #     self.search_label.grid(row=4, column=1)
    #     self.entry_field.grid(row=4, column=2)
    #     self.enter_button.grid(row=5, column=3)



        # other frames
        # self.gotify_label_frame.grid(row=0, column=3, rowspan=3, columnspan=4)
        # self.gotify_image_frame.grid(row=0, column=0, rowspan=3, columnspan=4)
        
        # # other features

        # # gotify label
        # self.gotify_label.grid(row=0, column=5, rowspan=3, columnspan=4)
        # # gotify image
        # self.gotify_image_button.grid(row=0, rowspan=2, column=2, columnspan=2)

        # self.guide_label.grid(row=4, column=5, rowspan=2)
        # self.search_label.grid(row=6, column=5)
        # self.entry_field.grid(row=6, column=6, columnspan=3)
        # self.enter_button.grid(row=8, column=5, columnspan=2)

        # screen update
        self.main_search_window.mainloop()


def search_compiled():
    search_class = Searching()
    search_class.searching_feature()
    search_class.apply()

