"""Library / framework import"""
import tkinter as tk
from tkinter.constants import LEFT, W
import tkinter.font as font
from PIL import Image, ImageTk

"""Modular imports"""
from colours import (deep_black, 
unhighlighted_text, 
highlighted_text)
# from my_fonts import (main_font)

from searching_feature_frontend import search_compiled
from recent_songs_feature import recent_songs_compiled
from home_feature import HomeFeature
from liked_songs_feature import liked_songs_screen_compiled

"""Sidebar class"""

class SideBar():
    def __init__(self, window):


        main_font = font.Font(family="Gothic Medium", size=15)
        
        self.frame_side = tk.Frame(window, background=deep_black, width=200, height=800).grid(row=1, column=1,rowspan=30, columnspan=2)
        
        """Assets handeling"""

        try:
            # setting up images
            self.settings_icon_img = (Image.open(fp=r"images/settings_img.png"))
            self.home_icon_img = (Image.open(fp=r"images/home_img.png"))
            self.search_icon_img = (Image.open(fp=r"images/search_img.png"))
            self.your_library_icon_img = (Image.open(fp=r"images/your_library_img.png"))
            self.bar_icon_img = (Image.open(fp=r"images/bar_img.png"))
        
            # resizing images
            self.settings_icon_img_resized = self.settings_icon_img.resize((50, 20), Image.ANTIALIAS)
            self.home_icon_img_resized =  self.home_icon_img.resize((45, 45), Image.ANTIALIAS)
            self.search_icon_img_resized = self.search_icon_img.resize((45, 40), Image.ANTIALIAS)
            self.your_library_icon_img_resized = self.your_library_icon_img.resize((45, 45), Image.ANTIALIAS)
            self.bar_icon_img_resized = self.bar_icon_img.resize((210, 50), Image.ANTIALIAS)

            # reattributing images
            self.settings_icon_img = ImageTk.PhotoImage(master=self.frame_side, image=self.settings_icon_img_resized)
            self.home_icon_img = ImageTk.PhotoImage(master=self.frame_side, image=self.home_icon_img_resized)
            self.search_icon_img = ImageTk.PhotoImage(master=self.frame_side, image=self.search_icon_img_resized)
            self.your_library_icon_img = ImageTk.PhotoImage(master=self.frame_side, image=self.your_library_icon_img_resized)
            self.bar_icon_img = ImageTk.PhotoImage(master=self.frame_side, image=self.bar_icon_img_resized)


        except FileExistsError or FileNotFoundError:
            print("Necessary files are not in directory")


        """Command initialisation"""

        # home command
        def home_command():
            home_feature = HomeFeature(mainwindow=window)
            home_feature.constructing_widgets()

        """Settings button"""
        self.setting_button = tk.Button(master=self.frame_side,
         image=self.settings_icon_img,
         width=50,
         height=20,
         pady=10,
         bg=deep_black,
         border=0)

        """Home button"""
        self.home_button = tk.Button(master=self.frame_side, 
         text="Home",
         bg=deep_black, 
         fg=unhighlighted_text,
         activeforeground=highlighted_text,
         font=main_font,
         command=home_command,
         height=1,
         width=10,
         border=0)
        
        # home image
        self.home_icon = tk.Button(master=self.frame_side, 
        image=self.home_icon_img,
        command=home_command,
        border=0,
        bg=deep_black)
        # bg=deep_black,
        # height=33

        """Search button"""
        self.search_button = tk.Button(master=self.frame_side,
        text="Search",
        command=search_compiled,
        bg=deep_black,
        fg=unhighlighted_text,
        activeforeground=highlighted_text,
        font=main_font,
        height=1,
        width=10,
        border=0)

        # search image
        self.search_icon = tk.Button(master=self.frame_side, 
        image=self.search_icon_img, 
        bg=deep_black,
        command=search_compiled,
        height=33,
        border=0)

        """Your library Button"""
        self.your_library_button = tk.Button(master=self.frame_side,
        text="Your Library",
        bg=deep_black,
        fg=unhighlighted_text,
        activeforeground=highlighted_text,
        font=main_font,
        height=1,
        width=10,
        border=0)

        # your library image
        self.your_library_icon = tk.Button(master=self.frame_side,
        image=self.your_library_icon_img,
        bg=deep_black,
        height=35,
        border=0)

        # bars beneath images
        self.bar_icon_1 = tk.Button(master=self.frame_side,
        image=self.bar_icon_img,
        bg=deep_black,
        height=4,
        width=200,
        border=0)

        self.bar_icon_2 = tk.Button(master=self.frame_side,
        image=self.bar_icon_img,
        bg=deep_black,
        border=0,
        height=4,
        width=200)



        # bar side image
        # self.bar_icon_1_side = tk.Button(master=self.frame_on_side_of_frame_side,
        # image=bar_img,
        # bg=sidebar_background_black,
        # height=800,
        # width=3)

        self.liked_songs_button = tk.Button(master=self.frame_side,
        text="Liked Songs",
        command=liked_songs_screen_compiled,
        bg=deep_black,
        fg=unhighlighted_text,
        height=1, width=10,
        border=0)

        self.create_playlist_button = tk.Button(master=self.frame_side,
        text="Create Playlist",
        bg=deep_black,
        fg=unhighlighted_text,
        height=1, width=10,
        border=0)

        self.recent_songs_button = tk.Button(master=self.frame_side,
        text="Recent Songs",
        command=recent_songs_compiled,
        bg=deep_black,
        fg=unhighlighted_text,
        height=1, width=10,
        border=0)

    """drawing everything to the main window"""

    def apply(self):
        # icons
        self.home_icon.grid(row=2, column=1)
        self.setting_button.grid(row=1, column=1)
        self.search_icon.grid(row=3, column=1, pady=5)
        self.your_library_icon.grid(row=4, column=1)
        self.bar_icon_1.grid(row=5, column=1, columnspan=2)
        self.bar_icon_2.grid(row=9, column=1, columnspan=2)

        # buttons
        self.home_button.grid(row=2, column=2)
        self.search_button.grid(row=3, column=2, pady=5)
        self.your_library_button.grid(row=4, column=2)
        self.liked_songs_button.grid(row=7, column=2)
        self.create_playlist_button.grid(row=8, column=2)
        self.recent_songs_button.grid(row=10, column=2)
        # self.bar_icon_1_side.grid(row=1, column=1)
