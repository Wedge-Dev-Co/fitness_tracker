
# Project: Hi-Fi Fitness Tracker
# Author(s): Taylor C. Powell

#

# This is a simple fitness tracking program
# It allows the user to log exercise and nutrition data on a daily basis
# It also allows the user to view their progress over time

#

# ------------------------------------ IMPORTS ------------------------------------

# All imported modules

from ui_control import *


# ------------------------------------ MAIN APPLICATION ------------------------------------

# Main application logic

## ------------------------------------
# FUNCTION: start_app()
#
# Begins running the main application
#
def start_app():
    print("Welcome to the Hi-Fi Fitness Tracker!")
    display_home()

start_app()
