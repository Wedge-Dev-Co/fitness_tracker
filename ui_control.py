# Hi-Fi Fitness Tracker
# ui_control.py
# Taylor C. Powell

# Provides functions for controlling the UI


# ------------------------------------ IMPORTS ------------------------------------

from tkinter import *
from controller import *
from classes import *


# ------------------------------------ FUNCTIONS ------------------------------------

# ------------------------------------
# FUNCTION: display_home()
#
# Displays the home page
#  TODO: Integrate with database
# 
def display_home():
    print("Displaying home page")
    # Initialize home ui page
    home_page = Tk()
    home_page.title("Home")
    home_page.geometry("600x800")
    home_page.configure(bg="black")

    # Create a label for the title
    title_label = Label(home_page, text="Hi-Fi Fitness Tracker", font=("Arial", 24), bg="black", fg="white")
    title_label.pack(pady=20)

    # Create a button to create a new entry
    new_entry_button = Button(home_page, text="New Entry", font=("Arial", 18), bg="white", fg="black", command=lambda: display_entry(new_entry()))
    new_entry_button.pack(pady=20)

    # Create a button to view the current entry
    current_entry_button = Button(home_page, text="Current Entry", font=("Arial", 18), bg="white", fg="black", command=lambda: display_entry(get_current_entry(entries)))
    current_entry_button.pack(pady=20)

    # Create a button to view past entries
    past_entries_button = Button(home_page, text="Past Entries", font=("Arial", 18), bg="white", fg="black", command=lambda: print("view past entries"))
    past_entries_button.pack(pady=20)

    # Run the main loop
    home_page.mainloop()


# ------------------------------------
# FUNCTION: display_entry()
#
# Displays the input entry
# TODO: Integrate with database
#
def display_entry(entry):
    # Initialize entry ui page
    entry_page = Tk()
    entry_page.title("Entry: " + str(entry.day_of_week) + ", " + str(entry.date))
    entry_page.geometry("600x800")
    entry_page.configure(bg="black")

    # Create a label for the title
    title_label = Label(entry_page, text="Entry: " + str(entry.day_of_week) + ", " + str(entry.date), font=("Arial", 24), bg="black", fg="white")
    title_label.pack(pady=20)

    # Create a button to add a workout
    add_workout_button = Button(entry_page, text="Add workout", font=("Arial", 18), bg="white", fg="black", command=lambda: entry.add_workout(workout))
    add_workout_button.pack(pady=20)

    # Create a button to add nutrition
    add_meal_button = Button(entry_page, text="Add meal", font=("Arial", 18), bg="white", fg="black", command=lambda: entry.add_meal(meal))
    add_meal_button.pack(pady=20)

    # Create a button to add comments
    comment = StringVar()
    add_comments_button = Button(entry_page, text="Add comments", font=("Arial", 18), bg="white", fg="black", command=lambda: entry.add_comment(comment.get()))
    add_comments_button.pack(pady=20)

    # Create a button to save the entry
    save_button = Button(entry_page, text="Save entry", font=("Arial", 18), bg="white", fg="black", command=lambda: entry.save_entry())
    save_button.pack(pady=20)

    # Run the main loop
    entry_page.mainloop()


