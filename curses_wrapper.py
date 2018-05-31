#curses_wrapper.py
import curses as crs
import os
from curses import wrapper

def main(stdscr):
    crs.initscr()
    crs.endwin()
    os.system("git status")
    stdscr.getch()
    os.system("clear")

# wrapper is a function that does all of the setup and teardown, and makes sure
# your program cleans up properly if it errors!
wrapper(main)

