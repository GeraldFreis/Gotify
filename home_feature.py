"""Global Libraries / Frameworks importing"""
import tkinter as tk

"""Modular imports"""
from colours import deep_black, unhighlighted_text

"""HomeFeature class"""

class HomeFeature():

    def __init__(self, mainwindow):
        self.main_frame = tk.Frame(master=mainwindow,
        bg=deep_black).grid(row=2, column=4, rowspan=18, columnspan=5)
    
    def constructing_widgets(self):

        """using buttons to make the widgets"""
        self.liked_songs_button = tk.Button(master=self.main_frame,
        bg=deep_black, fg=unhighlighted_text,
        text="Liked Songs")

        self.recent_searches_button = tk.Button(master=self.main_frame,
        bg=deep_black, fg=unhighlighted_text,
        text="Recent Searches")

        self.search_button = tk.Button(master=self.main_frame,
        bg=deep_black, fg=unhighlighted_text,
        text="Search")

        """Applying widgets"""
        def apply():
            self.liked_songs_button.grid(row=3, column=5, rowspan=2, columnspan=2)
            self.recent_searches_button.grid(row=6, column=8, rowspan=2, columnspan=2)
            self.search_button.grid(row=9, column=5, rowspan=2, columnspan=2)

def homefeature_compiled():
    home_feature = HomeFeature()
