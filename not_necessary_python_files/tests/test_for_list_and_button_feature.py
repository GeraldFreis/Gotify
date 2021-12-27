from sqlite3.dbapi2 import DataError, DatabaseError
import tkinter as tk
import tkinter.font as font
import sqlite3 as sql


"""Functions"""

# button print funct
def printbutt_1():
    print(songlist[0])



mainwin = tk.Tk()
mainwin.geometry("800x800")

"""Song initialisation"""
try:
    dbcon = sql.connect("databases/liked_songs.db")
    query = "SELECT * FROM likedsongs"
    dblist = list(dbcon.execute(query))

    songlist = list()

    for row in dblist: songlist.append(row[0])

except DataError:
    print("No vals in table / table not found")


"""Attributes and widgets"""
title = tk.Label(master=mainwin,
text="Playlist").grid(row=0, column=1)

song_1 = tk.Button(master=mainwin,
text=songlist[0],
command=printbutt_1).grid(row=1, column=0)

song_2 = tk.Button(master=mainwin,
text=songlist[1]).grid(row=2, column=0)

song_3 = tk.Button(master=mainwin,
text=songlist[2]).grid(row=3, column=0)

mainwin.mainloop()
