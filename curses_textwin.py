#curses_textwin.py
import curses
import curses.textpad
from curses import wrapper
import time

def main(stdscr):
    stdscr = curses.initscr()
    curses.echo()

    begin_x = 10
    begin_y = 7
    height = 8
    width = 40
    win = curses.newwin(height, width, begin_y, begin_x)

    tb = curses.textpad.Textbox(win)
    text = tb.edit()
    curses.addstr(4,1,text.encode('utf_8'))

    while 1:
        c = stdscr.getch()
        if c == ord('p'): 
            pass
        elif c == ord('q'):  
            break # Exit the while()
        elif c == curses.KEY_HOME: 
            x = y = 0

    curses.endwin()
wrapper(main)
