"""Library / framework importing"""
import sqlite3 as sql
from sqlite3.dbapi2 import DataError, DatabaseError
import tkinter as tk
import tkinter.font as font

"""Modular imports"""
from colours import deep_black, unhighlighted_text

"""Globals"""
existing_account_test = False
username = str()

"""Database class"""

class Database:
    def __init__(self):
        
        # database connection
        self.dbcon = sql.connect(r"databases\user_list.db")
        self.dbcursor = self.dbcon.cursor()



    def create_database(self):

        try:
            self.dbcursor.execute('''CREATE TABLE users (username, password)''')
            self.dbcon.commit()

            print("database created")

        except DatabaseError:
            print("database already exists")
    




    def returning_user_window(self):

        def retrieving_user(name):

            global username

            try:
                query = '''SELECT * FROM users'''
                list_of_names = list(self.dbcursor.execute(query))
                # print(list_of_names)
                for pair in list_of_names:
                    for word in pair:
                        if word == name:
                            print("moving you into the app {}".format(name))
                            existing_account_test = True
                            username = name
                            return existing_account_test, username
                        return username
                    return username
                return username

            except DatabaseError or DataError:
                print("Your account was not found")

        """Main window initialisation"""
        self.returning_window = tk.Tk()
        self.returning_window.config(bg=deep_black)
        self.returning_window.geometry("800x600+300+200")
        self.returning_window.title("Returning User")

        # fonts used
        
        self.large_font = font.Font(family="Gothic Medium", size=40)
        self.medium_font = font.Font(family="Gothic Medium", size=20)
        self.small_font = font.Font(family="Gothic Medium", size=10)

        """Label initialisation"""
        self.gotify_label = tk.Label(master=self.returning_window,
        text="Gotify",
        font=self.large_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=0)

        self.enter_name_label = tk.Label(master=self.returning_window,
        text="Please enter your name below",
        font=self.small_font,
        border=0,
        bg=deep_black,
        fg=unhighlighted_text)

        self.name_label = tk.Label(master=self.returning_window,
        text="Name: ",
        border=0,
        bg=deep_black,
        fg=unhighlighted_text)

        self.name_entry_field_contents = tk.StringVar()
        self.name_entry_field = tk.Entry(master=self.returning_window, textvariable=self.name_entry_field_contents)

        # method to retrieve the name
        def retrieving_entry_field():
            self.username = self.name_entry_field_contents.get()

            # print(self.username)
            retrieving_user(self.username)
            
            # mainwindow.destroy()
            self.returning_window.destroy()

            return self.username

        self.enter_button = tk.Button(master=self.returning_window,
        command=retrieving_entry_field,
        bg=deep_black,
        border=1,
        height=1, width=10)

        """Applying all assets to the frame"""
        self.gotify_label.grid(row=1, column=1, columnspan=3, 
        pady=20)
        self.enter_name_label.grid(row=2, column=2, 
        pady=10)
        self.name_label.grid(row=3, column=1, 
        pady=10)
        self.name_entry_field.grid(row=3, column=2, columnspan=2, 
        pady=10)
        self.enter_button.grid(row=4, column=2, 
        pady=10)

        self.returning_window.mainloop()

    def new_user(self):
        global username
        """Setting main new user login window up"""
        self.new_user_login_window = tk.Tk()
        self.new_user_login_window.geometry()
        self.new_user_login_window.config(bg=deep_black)
        self.new_user_login_window.geometry("800x600+300+200")
        self.new_user_login_window.title("New User")

        # centering frame 
        self.centering_frame = tk.Frame(master=self.new_user_login_window,
        height=200,
        width=240,
        bg=deep_black)

        """Functions"""
        # adding the user to the database
        def adding_user(name):
            self.dbcon = sql.connect(r"databases\user_list.db")
            self.dbcursor = self.dbcon.cursor()
            try:
                data = (name, '')
                query = '''INSERT INTO users VALUES (?, ?)'''
                self.dbcursor.execute(query, data)
                self.dbcon.commit()

                print("hello {} you have been signed up".format(name))
                
            except DatabaseError or DataError:
                print("Problem in adding data to the database")

        """Setting up features"""
        # fonts
        self.large_font = font.Font(family="Gothic Medium", size=40)
        self.medium_font = font.Font(family="Gothic Medium", size=20)
        self.small_font = font.Font(family="Gothic Medium", size=10)

        # gotify text at the top
        self.gotify_label = tk.Label(master=self.new_user_login_window,
        text="Gotify",
        font=self.large_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=0)

        # entering data below text
        self.guide_label = tk.Label(master=self.new_user_login_window,
        text="Please enter your name below to set up an account",
        font=self.small_font,
        border=0,
        bg=deep_black,
        fg=unhighlighted_text)

        # name label
        self.name_label = tk.Label(master=self.new_user_login_window,
        text="Name: ",
        font=self.medium_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=0)

        # entry field
        self.entry_contents = tk.StringVar()
        self.entry_field = tk.Entry(master=self.new_user_login_window,
        textvariable=self.entry_contents)

        # returning entry contents
        def returning_contents():
            username = self.entry_field.get()
            adding_user(username)
            self.new_user_login_window.destroy()
            return username

        # enter button
        self.enter_button = tk.Button(master=self.new_user_login_window,
        bg=deep_black,
        fg=unhighlighted_text,
        command=returning_contents,
        text="Proceed")

        """Applying all widgets to the main frame"""
        self.centering_frame.grid(row=0, column=0)
        self.gotify_label.grid(row=1, column=1, columnspan=3)
        self.guide_label.grid(row=2, column=1, columnspan=3,
        pady=10)
        self.name_label.grid(row=3, column=1,
        pady=10, padx=15)
        self.entry_field.grid(row=3, column=2, columnspan=2,
        pady=10, padx=4)
        self.enter_button.grid(row=4, column=2,
        pady=4, padx=3)

        # mainloop
        self.new_user_login_window.mainloop()

data = Database()
# data.new_user()
data.returning_user_window()