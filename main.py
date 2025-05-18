# This is a simple fitness tracking program
# It allows the user to log exercise and nutrition data on a daily basis
# It also allows the user to view their progress over time

import tkinter as tk
from tkinter import *

def new_entry():
    print("New Entry")

def start_app():
    print("Welcome to the Hi-Fi Fitness Tracker!")
	# TODO: Implement the main application logic here
    root = Tk()
    root.title("Hi-Fi Fitness Tracker")
    root.geometry("400x400")
    btn = Button(root, text = "Create new entry", command = new_entry)
    btn.grid(column=2, row=2)
    root.mainloop()

start_app()
