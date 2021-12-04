import tkinter as tk

from colours import (deep_black, 
sidebar_background_grey, 
unhighlighted_text, 
highlighted_text)

song_title = "Song Name:"


"""Bottom bar class"""

class BottomBar:
    def __init__(self, window):
        self.bottom_bar_frame = tk.Frame(master=window,
        background=deep_black, 
        border=0, 
        width=1000, 
        height=100).grid(row=27, column=4, rowspan=4, columnspan=2)

        self.song_title = tk.Button(master=self.bottom_bar_frame,
        text="Song Name",
        bg=deep_black,
        fg=unhighlighted_text,
        activeforeground=highlighted_text,
        border=0)

    def apply(self):
        self.song_title.grid(row=27, column=4, columnspan=2)
