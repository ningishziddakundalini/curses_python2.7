#curses_keycode.py
import curses as crs
from curses import panel
import os
import subprocess
import time

def main(stdscr):
    #initiate
    stdscr.addstr("press enter to quit")
    crs.curs_set(0)
    stdscr = crs.initscr()

    while True:
        key = stdscr.getch()
        if key == 10:
            stdscr.clear()
            stdscr.move(8, 12)
            stdscr.addstr("you pessed key 10 'enter' guit program")
            stdscr.getch()
            break

        #show the keycode and key
        stdscr.clear() 
        stdscr.move(8, 12)
        str_chr =   "The key code of '{}' is {}". format(chr(key), str(key))
        stdscr.addstr(str_chr)

    crs.endwin()

crs.wrapper(main)
