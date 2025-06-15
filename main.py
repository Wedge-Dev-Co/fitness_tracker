
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

# All functions for the application

## ------------------------------------
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
    entry_page.geometry("600x800")
    entry_page.mainloop()


# ------------------------------------ MAIN APPLICATION ------------------------------------

# Main application logic

## ------------------------------------
# FUNCTION: start_app()
#
# Begins running the main application
#
def start_app():
    print("Welcome to the Hi-Fi Fitness Tracker!")
	# TODO: Implement the main application logic here
    root = Tk()
    root.title("Hi-Fi Fitness Tracker")
    root.geometry("400x200")
    root.configure(bg="black")
    # Create a label for the title
    title_label = Label(root, text="Hi-Fi Fitness Tracker", font=("Arial", 24), bg="black", fg="white")
    title_label.pack(pady=20)
    # Create a button to start a new entry
    new_entry_button = Button(root, text="New Entry", font=("Arial", 18), bg="white", fg="black", command=new_entry)
    new_entry_button.pack(pady=20)
    # Run the main loop    
    root.mainloop()

start_app()
