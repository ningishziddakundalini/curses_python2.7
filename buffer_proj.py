#buffer_proj.py
import curses
import os
from glob import glob
from curses import panel
from curses import wrapper

def main(stdscr):
    curses.curs_set(0)
    stdscr = curses.initscr()
    stdscr.refresh()

    pad = curses.newpad(50, 30)
    pad_length = 6
    pad_ypos =  stdscr.getmaxyx()[0]/6
    pad.box()
    pad.border(124,124, 0,0)

    position = 0 
    file_list = glob("*.py")
    offset = 0

    while True:
        #display
        for i, x in enumerate(file_list):
            if position == i:
                mod = curses.A_REVERSE
            else:
                mod = curses.A_NORMAL

            pad.addstr(i, 0, file_list[i], mod)
            pad.refresh(offset ,0, pad_ypos,6 , pad_length+pad_ypos,75)

        key = pad.getch() 

        #pad down
        if key == ord("j") and position < len(file_list)-1:
            position += 1
            if key == ord("j") and offset < len(file_list)-pad_length-1:
                offset +=1

        #pad up
        if key == ord("k") and position > -0:
            position -= 1
            if key == ord("k") and offset > 0:
                offset -=1

        #display widget name
        if key == 10:
            win1.clear()
            win1.addstr(file_list[position])
            win1.refresh()

        #exit
        if key == ord("q"):
            break

    curses.endwin()
wrapper(main)

