"""Library / Framework imports"""
import tkinter as tk
from tkinter import *
import sqlite3 as sq
from bottombar_feature import BottomBar
# import bs4 as bs

"""Modular imports"""
from colours import main_black_background, deep_black
from sidebar_feature import SideBar
from userlogin_feature import Login, login_conditional_test, returning_username
from account_feature import AccountBar



main_window_conditional_test = True

"""Window initialisation and settings"""

while login_conditional_test is True:

    """Initialising login screen"""
    login_screen = Login()
    login_screen.apply()

    if main_window_conditional_test is True:
        main_window = tk.Tk()
        main_window['bg'] = main_black_background
        main_window.geometry("1200x800+0+0")
        main_window.title("GOTIFY")

        if main_window.winfo_exists:
            main_window_conditional_test = False
            login_conditional_test = False


        """Initialising classes"""

        # sidebar
        sidebar = SideBar(window=main_window)
        sidebar.apply()

        # bottom bar
        bottombar = BottomBar(window=main_window)
        bottombar.apply()

        # account bar
        accountbar = AccountBar(window=main_window, username=returning_username())
        accountbar.apply()

        """Applying everything"""
        main_window.mainloop()