#curses_wrapper.py
import curses
from curses import wrapper

def main(stdscr):
    # Proceed with your program
    print("Running some program")
    # Clear screen
    stdscr.clear()

# wrapper is a function that does all of the setup and teardown, and makes sure
# your program cleans up properly if it errors!
wrapper(main)

