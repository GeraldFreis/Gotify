"""Library / Framework imports"""
import tkinter as tk

"""Modular imports"""
from colours import (deep_black, unhighlighted_text)
from userlogin_feature import username

class AccountBar:

    def __init__(self, window):
        global username
        """Making the main widget"""
        self.main_widget_frame = tk.Frame(window,
        bg=deep_black).grid(row=1, column=5, columnspan=2)

        """Features"""
        self.name_label = tk.Label(master=window,
        textvariable=username,
        border=0,
        bg=deep_black,
        fg=unhighlighted_text)

    def apply(self, username):
        self.name_label.grid(row=1, column=5)
        print(username)

