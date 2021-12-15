"""Global Libraries / Frameworks importing"""
import tkinter as tk
import tkinter.font as font

"""Modular imports"""
from colours import deep_black, unhighlighted_text

"""HomeFeature class"""

class HomeFeature():

    def __init__(self, mainwindow):
        self.main_frame = tk.Frame(master=mainwindow,
        bg=deep_black).grid(row=2, column=3, rowspan=18, columnspan=5)

        """Fonts"""
        self.used_font = font.Font(family="Gothic Medium", size=40)
    def constructing_widgets(self):

        """using buttons to make the widgets"""
        self.liked_songs_button = tk.Button(master=self.main_frame,
        bg=deep_black,
        font=self.used_font,
        activebackground=deep_black,
        width=10, height=3,
        text="Liked Songs")

        self.recent_searches_button = tk.Button(master=self.main_frame,
        bg=deep_black,
        fg=deep_black,
        font=self.used_font,
        width=14, height=3,
        text="Recent Searches")

        self.search_button = tk.Button(master=self.main_frame,
        bg=deep_black,
        width=10, height=3,
        font=self.used_font,
        text="Search")

        """Applying widgets"""
        def apply():
            self.liked_songs_button.grid(row=3, column=3, rowspan=2, columnspan=2)
            self.recent_searches_button.grid(row=3, column=5, rowspan=2, columnspan=2)
            self.search_button.grid(row=6, column=3, rowspan=2, columnspan=2)

        apply()
