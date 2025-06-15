
# Project: Hi-Fi Fitness Tracker
# Author(s): Taylor C. Powell

# This is a simple fitness tracking program
# It allows the user to log exercise and nutrition data on a daily basis
# It also allows the user to view their progress over time

# ------------------------------------ IMPORTS ------------------------------------

import tkinter as tk
from tkinter import *
from classes import *

# ------------------------------------ FUNCTIONS ------------------------------------

# FUNCTION: new_entry()
#
# Initializes a new daily entry
#
def new_entry():
    print("New Entry")
    entry = daily_entry("2024-06-01", "Monday", 150)
    # Display entry main page
    entry_page = Tk()
    entry_page.title("New Entry")
    entry_page.geometry("400x400")
    entry_page.mainloop()


# ------------------------------------ MAIN APPLICATION ------------------------------------

# FUNCTION: start_app()
#
# Begins running the main application
#
def start_app():
    print("Welcome to the Hi-Fi Fitness Tracker!")
	# TODO: Implement the main application logic here
    root = Tk()
    root.title("Hi-Fi Fitness Tracker")
    root.geometry("400x1200")
    btn = Button(root, text = "Create new entry", command = new_entry)
    btn.grid(column=2, row=2)
    root.mainloop()

start_app()
