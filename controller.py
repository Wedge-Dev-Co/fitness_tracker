# ------------------------------------ IMPORTS ------------------------------------

# All imported modules

import tkinter as tk
import datetime
from tkinter import *
from classes import *


# ------------------------------------ FUNCTIONS ------------------------------------

# All functions for the application

# ------------------------------------
# FUNCTION: get_current_entry()
#
# Returns the current daily entry
# TODO: Integrate with database
def get_current_entry(entries):
   if entries[0].date == datetime.date.today():
        return entries[0]
   return None


## ------------------------------------
# FUNCTION: new_entry()
#
# Initializes a new daily entry
#
def new_entry():
    print("creating new entry")
    entry = daily_entry()
    return entry
