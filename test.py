#curses_gitstatus.py
from time import sleep
import curses, curses.panel
import os

def test(stdscr):
    #stdscr.clear()
    stdscr.box()

    while True:
        key = stdscr.getch()

        if key == ord("r"):
            stdscr.clear()
            stdscr.box()

        if key == 10:
            curses.endwin()
            os.system("git status")
            stdscr = curses.initscr()
            stdscr.addstr(23,0 ,"press")

        if key == ord("q"):
            break

if __name__ == '__main__':
    curses.wrapper(test)


