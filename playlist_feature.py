"""Planning this feature"""

"""How will it work?
- Be a button to activate when the user presses on a song
- Nest this in a window named song_edit feature
- The button will open a window with all of the playlists created
- These playlists will be buttons"""

"""Features:
- creating playlist feature...
---> What this feature will do:
-----> Create a new window for the playlists and use a playlist scaffold
-------> scaffold has empty rows and an Enter box that will be set as the name
-----> Add a table with the playlists name into the database folder
------> 3 columns: song, author, duration"""

"""Global Library / Framework importing"""
from sqlite3.dbapi2 import OperationalError
import tkinter as tk
import tkinter.font as font
import sqlite3 as sql
from PIL import Image, ImageTk

"""Modular imports"""
from colours import deep_black, unhighlighted_text
from spotify_logo_feature import spotify_button
from searching_feature_backend import real_search, writing_search_to_db

"""Globals"""
search = str()

"""Standalone functions"""


def creating_playlist_table(name: str):  # creating the new_playlists

    dbcon = sql.connect("databases/playlists.db")
    query = '''CREATE TABLE {} (songname, author, duration)'''.format(name)

    try:
        dbcon.execute(query)

    except OperationalError:
        print("Table exists try a different name")

    dbcon.commit()

def writing_to_playlist_database(tablename, songname, songauthor, songduration):
    dbcon = sql.connect("databases/playlists.db")
    data = (songname, songauthor, songduration)
    query = '''INSERT INTO {} VALUES (?, ?, ?)'''.format(tablename)
    dbcon.execute(query, data)
    dbcon.commit()

def list_of_songs(filename, tablename):
    dbcon = sql.connect(filename)

    query = '''SELECT * FROM {}'''.format(tablename)
    execute = list(dbcon.execute(query))
    song_list = list()

    for row in execute:
        song_list.append(row[0])

    return song_list


def add_song_to_playlist(songtoadd, mainwin):
    songs = tk.Button(master=mainwin,
    text=songtoadd, bg=deep_black, fg=unhighlighted_text,
    border=0).grid(row=4, column=1)


def adding_songs_to_playlist(mainwin):

    """Setting up the window that will contain recent songs, liked songs and searchbar"""
    new_window = tk.Tk()
    new_window.geometry("990x700+210+0")
    new_window.title("Adding Songs")
    new_window.config(bg=deep_black)

    mainwindow = mainwin

    # fonts
    large_font = font.Font(family="Gothic Medium", size=40)

    # recent_songs_rowcount = 3

    # for song in recent_songs_list:

    #     def quickfix():
    #         add_song_to_playlist(songtoadd=song, mainwin=mainwindow)

    #     song_button = tk.Button(master=new_window,
    #     text=song,
    #     bg=deep_black,
    #     command=quickfix,
    #     fg=unhighlighted_text,
    #     border=0).grid(row=recent_songs_rowcount, column=3)

    #     recent_songs_rowcount += 1

    # search bar
    search_bar = tk.Label(master=new_window,
    text="Search", font=large_font,
    width=35, bg=deep_black, fg=unhighlighted_text, border=0).grid(row=1, column=1)

    search_entry_text = tk.StringVar()
    search_entry_field = tk.Entry(master=new_window,
    textvariable=search_bar).grid(row=2, column=1, columnspan=2)

    def search_enter_command():
        global search
        search = search_entry_text.get()
        real_search(search=search)
        writing_search_to_db(search=search)
    
    search_enter_button = tk.Button(master=new_window,
    command=search_enter_command,
    bg=deep_black, fg=unhighlighted_text, border=0).grid(row=2, column=3)    

    """Title Labels and components"""

    # liked songs
    liked_songs_title = tk.Label(master=new_window,
    text="Liked Songs", font=large_font,
    bg=deep_black, fg=unhighlighted_text,
    border=0, width=35).grid(row=1, column=0)

    #   components
    liked_songs_list = list_of_songs(filename="databases/liked_songs.db", tablename="likedsongs")
    
    rowcount = 3

    # for song in liked_songs_list:

    #     def quickfix():
    #         add_song_to_playlist(songtoadd=song, mainwin=mainwindow)

    #     song_button = tk.Button(master=new_window,
    #     text=song,
    #     command=quickfix,
    #     bg=deep_black, fg=unhighlighted_text,
    #     border=0).grid(row=rowcount, column=0)

        # rowcount += 1
    
    
    liked_song_1_name = liked_songs_list[0]
    liked_song_2_name = liked_songs_list[1]
    liked_song_3_name = liked_songs_list[2]
    liked_song_4_name = liked_songs_list[3]
    liked_song_5_name = liked_songs_list[4]
    liked_song_6_name = liked_songs_list[5]
    liked_song_7_name = liked_songs_list[6]
    liked_song_8_name = liked_songs_list[7]
    liked_song_9_name = liked_songs_list[8]
    liked_song_10_name = liked_songs_list[9]
    liked_song_11_name = liked_songs_list[10]
    liked_song_12_name = liked_songs_list[11]
    liked_song_13_name = liked_songs_list[12]
    liked_song_14_name = liked_songs_list[13]
    liked_song_15_name = liked_songs_list[14]
    liked_song_16_name = liked_songs_list[15]
    liked_song_17_name = liked_songs_list[16]
    liked_song_18_name = liked_songs_list[17]
    liked_song_19_name = liked_songs_list[18]
    liked_song_20_name = liked_songs_list[19]

    '''Commands for the buttons'''
    def fixforbutton_1():
        song_1 = tk.Button(master=mainwindow,
        text=liked_song_1_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=4, column=1)

        song_author = 'hello'
        song_duration = 'he'
        writing_to_playlist_database(tablename=search, songname=liked_song_1_name, songauthor=song_author, songduration=song_duration)

    def fixforbutton_2():
        song_2 = tk.Button(master=mainwindow,
        text=liked_song_2_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=5, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_2_name, songauthor='', songduration='')

    
    def fixforbutton_3():
        song_3 = tk.Button(master=mainwindow,
        text=liked_song_3_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=6, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_3_name, songauthor='', songduration='')
    
    def fixforbutton_4():
        song_4 = tk.Button(master=mainwindow,
        text=liked_song_4_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=7, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_4_name, songauthor='', songduration='')
    
    def fixforbutton_5():
        song_5 = tk.Button(master=mainwindow,
        text=liked_song_5_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=8, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_5_name, songauthor='', songduration='')
    
    def fixforbutton_6():
        song_6 = tk.Button(master=mainwindow,
        text=liked_song_6_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=9, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_6_name, songauthor='', songduration='')
    
    def fixforbutton_7():
        song_7 = tk.Button(master=mainwindow,
        text=liked_song_7_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=10, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_7_name, songauthor='', songduration='')
    
    def fixforbutton_8():
        song_8 = tk.Button(master=mainwindow,
        text=liked_song_8_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=11, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_8_name, songauthor='', songduration='')
    
    def fixforbutton_9():
        song_9 = tk.Button(master=mainwindow,
        text=liked_song_9_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=12, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_9_name, songauthor='', songduration='')
    
    def fixforbutton_10():
        song_10 = tk.Button(master=mainwindow,
        text=liked_song_6_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=13, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_10_name, songauthor='', songduration='')
    
    def fixforbutton_11():
        song_11 = tk.Button(master=mainwindow,
        text=liked_song_11_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=14, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_11_name, songauthor='', songduration='')
    
    def fixforbutton_12():
        song_12 = tk.Button(master=mainwindow,
        text=liked_song_6_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=15, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_12_name, songauthor='', songduration='')
    
    def fixforbutton_13():
        song_13 = tk.Button(master=mainwindow,
        text=liked_song_13_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=16, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_13_name, songauthor='', songduration='')
    
    def fixforbutton_14():
        song_14 = tk.Button(master=mainwindow,
        text=liked_song_14_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=17, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_14_name, songauthor='', songduration='')
    
    def fixforbutton_15():
        song_15 = tk.Button(master=mainwindow,
        text=liked_song_15_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=18, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_15_name, songauthor='', songduration='')
    
    def fixforbutton_16():
        song_16 = tk.Button(master=mainwindow,
        text=liked_song_16_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=19, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_16_name, songauthor='', songduration='')
    
    def fixforbutton_17():
        song_17 = tk.Button(master=mainwindow,
        text=liked_song_17_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=20, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_17_name, songauthor='', songduration='')
    
    def fixforbutton_18():
        song_18 = tk.Button(master=mainwindow,
        text=liked_song_18_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=21, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_18_name, songauthor='', songduration='')
    
    def fixforbutton_19():
        song_19 = tk.Button(master=mainwindow,
        text=liked_song_19_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=22, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_19_name, songauthor='', songduration='')
    
    def fixforbutton_20():
        song_20 = tk.Button(master=mainwindow,
        text=liked_song_20_name, bg=deep_black, fg=unhighlighted_text,
        border=0).grid(row=23, column=1)

        writing_to_playlist_database(tablename=search, songname=liked_song_20_name, songauthor='', songduration='')


    liked_song_1 = tk.Button(master=new_window, text=liked_song_1_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_1).grid(row=3, column=0)
    liked_song_2 = tk.Button(master=new_window, text=liked_song_2_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_2).grid(row=4, column=0)
    liked_song_3 = tk.Button(master=new_window, text=liked_song_3_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_3).grid(row=5, column=0)
    liked_song_4 = tk.Button(master=new_window, text=liked_song_4_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_4).grid(row=6, column=0)
    liked_song_5 = tk.Button(master=new_window, text=liked_song_5_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_5).grid(row=7, column=0)
    liked_song_6 = tk.Button(master=new_window, text=liked_song_6_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_6).grid(row=8, column=0)
    liked_song_7 = tk.Button(master=new_window, text=liked_song_7_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_7).grid(row=9, column=0)
    liked_song_8 = tk.Button(master=new_window, text=liked_song_8_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_8).grid(row=10, column=0)
    liked_song_9 = tk.Button(master=new_window, text=liked_song_9_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_9).grid(row=11, column=0)
    liked_song_10 = tk.Button(master=new_window, text=liked_song_10_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_10).grid(row=12, column=0)
    liked_song_11 = tk.Button(master=new_window, text=liked_song_11_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_11).grid(row=13, column=0)
    liked_song_12 = tk.Button(master=new_window, text=liked_song_12_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_12).grid(row=14, column=0)
    liked_song_13 = tk.Button(master=new_window, text=liked_song_13_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_13).grid(row=15, column=0)
    liked_song_14 = tk.Button(master=new_window, text=liked_song_14_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_14).grid(row=16, column=0)
    liked_song_15 = tk.Button(master=new_window, text=liked_song_15_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_15).grid(row=17, column=0)
    liked_song_16 = tk.Button(master=new_window, text=liked_song_16_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_16).grid(row=18, column=0)
    liked_song_17 = tk.Button(master=new_window, text=liked_song_17_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_17).grid(row=19, column=0)
    liked_song_18 = tk.Button(master=new_window, text=liked_song_18_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_18).grid(row=20, column=0)
    liked_song_19 = tk.Button(master=new_window, text=liked_song_19_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_19).grid(row=21, column=0)
    liked_song_20 = tk.Button(master=new_window, text=liked_song_20_name, bg=deep_black, fg=unhighlighted_text, command=fixforbutton_20).grid(row=22, column=0)






    # recent songs
    recent_songs_title = tk.Label(master=new_window,
    text="Recent Songs", font=large_font,
    bg=deep_black, fg=unhighlighted_text,
    border=0, width=35).grid(row=1, column=3)

    #   components
    recent_songs_list = list_of_songs(filename="databases/recent_searches.db", tablename="searches")
    try:
        recent_song_1_name = recent_songs_list[0]
        recent_song_2_name = recent_songs_list[1]
        recent_song_3_name = recent_songs_list[2]
        recent_song_4_name = recent_songs_list[3]
        recent_song_5_name = recent_songs_list[4]
        recent_song_6_name = recent_songs_list[5]
        recent_song_7_name = recent_songs_list[6]
        recent_song_8_name = recent_songs_list[7]
        recent_song_9_name = recent_songs_list[8]
        recent_song_10_name = recent_songs_list[9]
        recent_song_11_name = recent_songs_list[10]
        recent_song_12_name = recent_songs_list[11]
        recent_song_13_name = recent_songs_list[12]
        recent_song_14_name = recent_songs_list[13]
        recent_song_15_name = recent_songs_list[14]
        recent_song_16_name = recent_songs_list[15]
        recent_song_17_name = recent_songs_list[16]
        recent_song_18_name = recent_songs_list[17]
        recent_song_19_name = recent_songs_list[18]
        recent_song_20_name = recent_songs_list[19]

    except IndexError:
        pass
    
    try:
        '''Commands for the buttons'''
        def fixforrecentbutton_1():
            song_1 = tk.Button(master=mainwindow,
            text=recent_song_1_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=4, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_1_name, songauthor='', songduration='')

        def fixforrecentbutton_2():
            song_2 = tk.Button(master=mainwindow,
            text=recent_song_2_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=5, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_2_name, songauthor='', songduration='')
        
        def fixforrecentbutton_3():
            song_3 = tk.Button(master=mainwindow,
            text=recent_song_3_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=6, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_3_name, songauthor='', songduration='')
        
        def fixforrecentbutton_4():
            song_4 = tk.Button(master=mainwindow,
            text=recent_song_4_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=7, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_4_name, songauthor='', songduration='')
        
        def fixforrecentbutton_5():
            song_5 = tk.Button(master=mainwindow,
            text=recent_song_5_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=8, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_5_name, songauthor='', songduration='')
        
        def fixforrecentbutton_6():
            song_6 = tk.Button(master=mainwindow,
            text=recent_song_6_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=9, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_6_name, songauthor='', songduration='')
        
        def fixforrecentbutton_7():
            song_7 = tk.Button(master=mainwindow,
            text=recent_song_7_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=10, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_7_name, songauthor='', songduration='')
        
        def fixforrecentbutton_8():
            song_8 = tk.Button(master=mainwindow,
            text=recent_song_8_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=11, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_8_name, songauthor='', songduration='')
        
        def fixforrecentbutton_9():
            song_9 = tk.Button(master=mainwindow,
            text=recent_song_9_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=12, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_9_name, songauthor='', songduration='')
        
        def fixforrecentbutton_10():
            song_10 = tk.Button(master=mainwindow,
            text=recent_song_6_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=13, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_10_name, songauthor='', songduration='')
        
        def fixforrecentbutton_11():
            song_11 = tk.Button(master=mainwindow,
            text=recent_song_11_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=14, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_11_name, songauthor='', songduration='')
        
        def fixforrecentbutton_12():
            song_12 = tk.Button(master=mainwindow,
            text=recent_song_12_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=15, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_12_name, songauthor='', songduration='')
        
        def fixforrecentbutton_13():
            song_13 = tk.Button(master=mainwindow,
            text=recent_song_13_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=16, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_13_name, songauthor='', songduration='')
        
        def fixforrecentbutton_14():
            song_14 = tk.Button(master=mainwindow,
            text=recent_song_14_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=17, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_14_name, songauthor='', songduration='')
        
        def fixforrecentbutton_15():
            song_15 = tk.Button(master=mainwindow,
            text=recent_song_15_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=18, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_15_name, songauthor='', songduration='')
        
        def fixforrecentbutton_16():
            song_16 = tk.Button(master=mainwindow,
            text=recent_song_16_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=19, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_16_name, songauthor='', songduration='')
        
        def fixforrecentbutton_17():
            song_17 = tk.Button(master=mainwindow,
            text=recent_song_17_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=20, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_17_name, songauthor='', songduration='')
        
        def fixforrecentbutton_18():
            song_18 = tk.Button(master=mainwindow,
            text=recent_song_18_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=21, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_18_name, songauthor='', songduration='')
        
        def fixforrecentbutton_19():
            song_19 = tk.Button(master=mainwindow,
            text=recent_song_19_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=22, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_19_name, songauthor='', songduration='')
        
        def fixforrecentbutton_20():
            song_20 = tk.Button(master=mainwindow,
            text=recent_song_20_name, bg=deep_black, fg=unhighlighted_text,
            border=0).grid(row=23, column=1)

            writing_to_playlist_database(tablename=search, songname=recent_song_20_name, songauthor='', songduration='')

    except UnboundLocalError:
        pass
    
    try:
        recent_song_1 = tk.Button(master=new_window, text=recent_song_1_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_1).grid(row=3, column=3)
        recent_song_2 = tk.Button(master=new_window, text=recent_song_2_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_2).grid(row=4, column=3)
        recent_song_3 = tk.Button(master=new_window, text=recent_song_3_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_3).grid(row=5, column=3)
        recent_song_4 = tk.Button(master=new_window, text=recent_song_4_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_4).grid(row=6, column=3)
        recent_song_5 = tk.Button(master=new_window, text=recent_song_5_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_5).grid(row=7, column=3)
        recent_song_6 = tk.Button(master=new_window, text=recent_song_6_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_6).grid(row=8, column=3)
        recent_song_7 = tk.Button(master=new_window, text=recent_song_7_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_7).grid(row=9, column=3)
        recent_song_8 = tk.Button(master=new_window, text=recent_song_8_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_8).grid(row=10, column=3)
        recent_song_9 = tk.Button(master=new_window, text=recent_song_9_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_9).grid(row=11, column=3)
        recent_song_10 = tk.Button(master=new_window, text=recent_song_10_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_10).grid(row=12, column=3)
        recent_song_11 = tk.Button(master=new_window, text=recent_song_11_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_11).grid(row=13, column=3)
        recent_song_12 = tk.Button(master=new_window, text=recent_song_12_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_12).grid(row=14, column=3)
        recent_song_13 = tk.Button(master=new_window, text=recent_song_13_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_13).grid(row=15, column=3)
        recent_song_14 = tk.Button(master=new_window, text=recent_song_14_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_14).grid(row=16, column=3)
        recent_song_15 = tk.Button(master=new_window, text=recent_song_15_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_15).grid(row=17, column=3)
        recent_song_16 = tk.Button(master=new_window, text=recent_song_16_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_16).grid(row=18, column=3)
        recent_song_17 = tk.Button(master=new_window, text=recent_song_17_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_17).grid(row=19, column=3)
        recent_song_18 = tk.Button(master=new_window, text=recent_song_18_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_18).grid(row=20, column=3)
        recent_song_19 = tk.Button(master=new_window, text=recent_song_19_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_19).grid(row=21, column=3)
        recent_song_20 = tk.Button(master=new_window, text=recent_song_20_name, bg=deep_black, fg=unhighlighted_text, command=fixforrecentbutton_20).grid(row=22, column=3)
    
    except UnboundLocalError:
        pass

    new_window.mainloop()
    


"""Creating playlist feature"""


class CreatingPlaylist():

    def __init__(self):

        # setting up database connection
        self.dbcon = sql.connect("databases/playlists.db")

        # setting up the main window
        self.main_window = tk.Tk()
        self.main_window.config(bg=deep_black)
        self.main_window.geometry("990x700+210+0")
        self.main_window.title("New Playlist")

        # importing the spotify icon image
        try:
            self.spotify_icon = Image.open(fp="images/spotify-logo.png")
            self.spotify_icon_resized = self.spotify_icon.resize((220, 150), Image.ANTIALIAS)
            self.spotify_icon = ImageTk.PhotoImage(master=self.main_window, image=self.spotify_icon_resized)

        except FileNotFoundError or FileExistsError:
            print("You do not have the spotify icon asset")

        # initialising fonts
        self.large_font = font.Font(family="Gothic Medium", size=40)


    def creating_widgets(self):
        
        # gotify image
        self.gotify_image = tk.Button(master=self.main_window,
        image=self.spotify_icon,
        command=spotify_button,
        bg=deep_black,
        fg=deep_black)

        # making the entry box for the user to type the playlist name
        self.entry_text = tk.StringVar()
        self.entry_field = tk.Entry(master=self.main_window,
        textvariable=self.entry_text,
        width=30)

        def applying_playlist_name():

            self.playlist_name = self.entry_field.get()
            creating_playlist_table(self.playlist_name)

            self.playlist_label = tk.Label(master=self.main_window,
            text=self.playlist_name,
            font=self.large_font,
            bg=deep_black,
            fg=unhighlighted_text,
            border=0).grid(row=0, column=1, columnspan=3)

            self.entry_field.destroy()
            self.enter_button.destroy()
        
        self.enter_button = tk.Button(master=self.main_window,
        text="Enter",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0,
        command=applying_playlist_name,
        anchor='w')

        """Title bar things"""
        # songs 
        self.songname_title = tk.Label(master=self.main_window,
        text="Song Name",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0, width=20)

        # author
        self.author_title = tk.Label(master=self.main_window,
        text="Author",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0, width=20)

        # duration
        self.duration_title = tk.Label(master=self.main_window,
        text="Duration",
        bg=deep_black,
        fg=unhighlighted_text,
        border=0, width=20)

        """Other widgets"""
        # adding songs feature
        def quickfix():
            adding_songs_to_playlist(mainwin=self.main_window)

        self.adding_songs_button = tk.Button(master=self.main_window,
        bg=deep_black, fg=unhighlighted_text, text="Add Songs",
        command=quickfix, border=0)

    
    def applying_widgets(self):

        # applying gotify image
        self.gotify_image.grid(row=0, column=0, padx=20)

        # applying the entry field
        self.entry_field.grid(row=0, column=1, columnspan=3)
        self.enter_button.grid(row=0, column=3)

        # titlebar
        self.songname_title.grid(row=2, column=1)
        self.author_title.grid(row=2, column=2)
        self.duration_title.grid(row=2, column=3)

        # other widgets
        self.adding_songs_button.grid(row=3, rowspan=7, column=0)

        # screen
        self.main_window.mainloop()


def creatingplaylist_compiled():
    creating_playlist = CreatingPlaylist()
    creating_playlist.creating_widgets()
    creating_playlist.applying_widgets()

creatingplaylist_compiled()
