#curses_breath.py
import curses
from curses import wrapper

import time

def main(stdscr):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    stdscr.clear()
#   amount of characters
    width = 8
#   repeats if width is > count
    count = 1
#   1 = go right and -1 = go left
    direction = 1

    while True:
        # must be typing in something cant reverse it with clear 
        key_input = stdscr.getch()
        # Clear out anything else the user has typed in so it can run?
        curses.flushinp()
        stdscr.clear()

        # If the user presses p, increase the width of the springy bar
        if key_input == ord('p'):
            width += 1
        # Draw a springy bar
        stdscr.addstr("#" * count)
        count += direction
#       go forth
        if count == width:
            direction = -1
#       go back
        elif count == 0:
            direction = 1
        # Wait 1/10 of a second. Read below to learn about how to avoid
        # problems with using time.sleep with getch!
        time.sleep(0.1)


# wrapper is a function that does all of the setup and teardown, and makes sure
# your program cleans up properly if it errors!
wrapper(main)

