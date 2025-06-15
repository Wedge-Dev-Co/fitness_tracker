
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


# ------------------------------------
# FUNCTION: get_current_entry()
#
# Returns the current daily entry
# TODO Correctly implement this function
def get_current_entry():
   current_entry = None # This line is for testing purposes only
   return current_entry


# ------------------------------------
# FUNCTION: display_entry()
#
# Displays the input entry
#
def display_entry(entry):
    # Initialize entry ui page
    entry_page = Tk()
    entry_page.title("Entry")
    entry_page.geometry("600x800")
    entry_page.configure(bg="black")

    # Create a label for the title
    title_label = Label(entry_page, text="Entry: " + str(entry.day_of_week) + ", " + str(entry.date), font=("Arial", 24), bg="black", fg="white")
    title_label.pack(pady=20)

    # Create a button to add a workout
    add_workout_button = Button(entry_page, text="Exercise", font=("Arial", 18), bg="white", fg="black", command=lambda: entry.add_workout(workout("Workout " + str(len(entry.workouts) + 1), None, None)))
    add_workout_button.pack(pady=20)

    # Create a button to add nutrition
    add_nutrition_button = Button(entry_page, text="Nutrition", font=("Arial", 18), bg="white", fg="black", command=lambda: entry.add_nutrition(nutrition("Nutrition " + str(len(entry.nutrition) + 1), None, None)))
    add_nutrition_button.pack(pady=20)

    # Create a button to add comments
    add_comments_button = Button(entry_page, text="Comments", font=("Arial", 18), bg="white", fg="black", command=lambda: entry.add_comments("Comments " + str(len(entry.comments) + 1)))
    add_comments_button.pack(pady=20)

    # Create a button to save the entry
    save_button = Button(entry_page, text="Save entry", font=("Arial", 18), bg="white", fg="black", command=lambda: save_entry(entry))
    save_button.pack(pady=20)

    # Run the main loop
    entry_page.mainloop()


## ------------------------------------
# FUNCTION: new_entry()
#
# Initializes a new daily entry
#
def new_entry():
    print("creating new entry")
    entry = daily_entry()
    return entry


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

    # if there is no current entry, create a button to start a new entry
    if get_current_entry() == None:
        print("No current entry, creating new entry button")
        new_entry_button = Button(root, text="New entry", font=("Arial", 18), bg="white", fg="black", command=new_entry)
        new_entry_button.pack(pady=20)
    else:
        print("Current entry exists, creating view entry button")
        view_entry_button = Button(root, text="View current entry", font=("Arial", 18), bg="white", fg="black", command=lambda: view_entry(get_current_entry()))
        view_entry_button.pack(pady=20)
        #     # Display current progress
        # progress_label = Label(root, text="Current progress: " + str(current_entry.get_total_duration()) + " minutes of exercise", font=("Arial", 18), bg="black", fg="white")
        # progress_label.pack(pady=20)
    
    # if past entries exist, create a button to view past entries
    # if len(get_past_entries(user)) > 1: # if the current entry is the only entry that exists, don't show the past entries button
    #     view_past_entries_button = Button(root, text="View past entries", font=("Arial", 18), bg="white", fg="black", command=view_past_entries)
    #     view_past_entries_button.pack(pady=20)

    # Run the main loop    
    root.mainloop()

start_app()
