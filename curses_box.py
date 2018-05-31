#curses_box.py
import curses
from curses import panel
import os

def main(screen):
    screen.immedok(True)
    screen.box()
    screen.border(124, 124, 95, 95)
    screen.addstr("screen")

    try:
        box1 = curses.newwin(8, 8, 6, 6)
        box1.immedok(True)
        box1.box()    
        box1.border(124, 124, 95, 95)
        box1.addstr("box1")
        screen.getch()

    finally:
        curses.endwin()

curses.wrapper(main)
