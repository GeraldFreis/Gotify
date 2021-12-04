import tkinter as tk


main_window = tk.Tk()
main_window.geometry("1200x800+0+0")

img = tk.PhotoImage(master=main_window, file="home_img.png")

l = tk.Label(master=main_window, image=img).grid(row=1, column=1)

main_window.mainloop()