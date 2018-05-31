#curses_getmaxyx.py
import curses
from glob import glob
from curses import panel
from curses import wrapper

def main(stdscr):
    stdscr = curses.initscr()
    curses.curs_set(0)
    y = stdscr.getmaxyx()[0]
    x = stdscr.getmaxyx()[1]
    stdscr_y = y/4

    stdscr.addstr(stdscr_y+0,0, str(y))
    stdscr.addstr(stdscr_y+1,0, str(x))
    stdscr.refresh()

    stdscr.getch()

    curses.endwin()
wrapper(main)

