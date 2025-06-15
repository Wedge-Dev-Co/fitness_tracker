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
# TODO Maximize computational efficiency
def get_current_entry(entries):
   today = datetime.date.today()
   for entry in entries:
       if entry.date == today:
           return entry
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
