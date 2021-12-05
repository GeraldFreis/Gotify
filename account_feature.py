"""Library / Framework imports"""
import tkinter as tk
import tkinter.font as font

"""Modular imports"""
from colours import (deep_black, unhighlighted_text)

"""Bar to say hello to the person logging in"""

class AccountBar:

    def __init__(self, window, username):

        # text variable
        self.username = "Hello: "

        """Making the main widget"""
        self.main_widget_frame = tk.Frame(window,
        bg=deep_black,
        width=5, height=1).grid(row=1, column=5, columnspan=2)

        """Features"""
        # fonts
        self.large_font = font.Font(family="Gothic Medium", size=40)
        self.name_label = tk.Label(master=self.main_widget_frame,
        text='Hello {}'.format(username),
        width=6, height=1,
        font=self.large_font,
        border=0,
        bg=deep_black,
        fg=unhighlighted_text,
        anchor='center')

    def apply(self):
        self.name_label.grid(row=1, column=5, columnspan=2)
