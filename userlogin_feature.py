"""Importing Libraries / Frameworks"""
import tkinter as tk
import tkinter.font as font
import sqlite3 as sql
from sqlite3.dbapi2 import DataError, DatabaseError
from PIL import Image, ImageTk


"""Modular imports"""
from colours import (deep_black, 
unhighlighted_text)


"""Globals"""
login_conditional_test = True
username = str()


"""Login class"""
class Login:        
    def __init__(self):

        """Setting up the main window"""

        self.main_login_window = tk.Tk()
        self.main_login_window.config(bg=deep_black)
        self.main_login_window.title("Login Window")
        self.main_login_window.geometry("1200x800+0+0")

        self.spotify_icon_frame = tk.Frame(master=self.main_login_window, bg=deep_black, border=0)


        """Asset handeling"""

        try:
            # resizing image
            self.spotify_icon_img = (Image.open(fp=r"images/spotify-logo.png"))
            self.spotify_icon_img = self.spotify_icon_img.resize((440,325), Image.ANTIALIAS)
            self.spotify_icon_img = ImageTk.PhotoImage(master=self.main_login_window, image=self.spotify_icon_img)
        
        except FileNotFoundError or FileExistsError:
            print("You do not have the necessary assets in this directory")

        """Returning user method"""

        def returning_user_window():
            global username
            self.dbcon = sql.connect(r"databases/user_list.db")
            self.dbcursor = self.dbcon.cursor()

            def retrieving_user(name):

                global username

                try:
                    query = '''SELECT * FROM users'''
                    list_of_names = list(self.dbcursor.execute(query))
                    # print(list_of_names)
                    for pair in list_of_names:
                        for word in pair:
                            if word == name:
                                global username
                                print("moving you into the app {}".format(name))
                                existing_account_test = True
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
                print(self.username)
                self.main_login_window.destroy()
                self.returning_window.destroy()

                return self.username

            self.enter_button = tk.Button(master=self.returning_window,
            command=retrieving_entry_field,
            text="Proceed",
            fg=unhighlighted_text,
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

            return username
        

        """Developer window"""
        def developer():

            print("This is a pass through and name will automatically be g")

            global username
            username = 'g'

            self.main_login_window.destroy()

            return username
        

        """New user method"""
        def new_user():
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
                self.dbcon = sql.connect(r"databases/user_list.db")
                self.dbcursor = self.dbcon.cursor()
                try:
                    global username
                    data = (name, '')
                    username = name
                    query = '''INSERT INTO users VALUES (?, ?)'''
                    self.dbcursor.execute(query, data)
                    self.dbcon.commit()

                    print("hello {} you have been signed up".format(name))
                    return username
                    
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
                self.main_login_window.destroy()
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
            return username

        """Setting up features"""
        
        main_font = font.Font(family="Gothic Medium", size=40)
        new_main_font = font.Font(family="Gothic Medium", size=100)

        self.frame_to_center = tk.Frame(master=self.main_login_window, bg=deep_black, width=400, height=50, border=0)
        
        # frame for labels
        self.label_frame = tk.Frame(master=self.main_login_window, bg=deep_black, width=800, height=600, border=0).grid(row=1, column=2, columnspan=3, rowspan=3)

        # returning user label
        self.returning_user_label = tk.Label(master=self.label_frame,
        text="Returning User",
        font=main_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=0)

        # new user label
        self.new_user_label = tk.Label(master=self.label_frame, 
        text="New User",
        font=main_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=0)

        # gotify
        self.gotify_label = tk.Label(master=self.label_frame,
        text="Gotify",
        font=new_main_font,
        bg=deep_black,
        fg=unhighlighted_text,
        border=0)

        # frame for buttons
        self.button_frame = tk.Frame(master=self.main_login_window, 
        border=0, 
        bg=deep_black, 
        height=100).grid(row=3, column=2, columnspan=3)
        
        # new user button
        self.new_user_button = tk.Button(master=self.button_frame,
        command=new_user,
        width=10,
        height=2,
        bg=deep_black)

        # returning user button
        self.returning_user_button = tk.Button(master=self.button_frame,
        bg=deep_black,
        command=returning_user_window,
        width=10,
        height=2)

        # developer button
        self.dev_button = tk.Button(master=self.button_frame,
        bg=deep_black,
        command=developer)

        """Aesthetics"""
        def spotify_button():
            import webbrowser
            webbrowser.open("https://github.com/GeraldFreis/Gotify")

        self.spotify_logo_icon = tk.Button(master=self.main_login_window,
        bg=deep_black,
        command=spotify_button,
        image=self.spotify_icon_img,
        border=0,
        height=325,
        width=400)

    def check_close(self):
        global login_conditional_test

        if self.main_login_window.winfo_exists is not True:
            login_conditional_test = False
            # print("here")

        # print(login_conditional_test)

        return login_conditional_test


    def apply(self):
        # centering frame
        self.frame_to_center.grid(row=0, rowspan=3, column=1, columnspan=1)

        # labels 
        self.gotify_label.grid(row=1, column=2, columnspan=2, sticky='w')
        self.returning_user_label.grid(row=2, column=1, padx=100)
        self.new_user_label.grid(row=2, column=3)

        # buttons
        self.returning_user_button.grid(row=3, column=1)
        self.new_user_button.grid(row=3, column=3)
        self.dev_button.grid(row=3, column=2)

        # aesthetics
        self.spotify_logo_icon.grid(row=0, column=1, rowspan=2, columnspan=1, sticky='e')

        self.main_login_window.mainloop()


"""Returning username method"""
def returning_username():
    global username
    username
    print(username)
    return username