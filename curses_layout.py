#curses_layout.py
import curses
from curses import panel
from curses import wrapper
from time import sleep
import os

#this program is a example of a basic curses layout and is a expiriment to
#create ideas about writing functions to create curses widgets efficiently
#7 jun 2018

def main(stdscr):
    #index
    ''' init layout display_panel upper_window left_window right_window '''

    #init
    dir_list = [
            "/home/git/vim_files/",
            "/home/git/info/"
            ]

    def layout(arg1, arg2):
        y = stdscr.getmaxyx()[0]
        x = stdscr.getmaxyx()[1]
        win_y = int(round(y * arg1, 0))
        win_x = int(round(x * arg2, 0))
        return win_y,win_x

    def display_panel(h,l, y,x, *args):
        win = curses.newwin(h,l, y,x)
        win.box(*args)
        pan = curses.panel.new_panel(win)
        return win,pan

    while True:
        #upper_window    
        win1_y, win1_x = layout(0.20, 1.00)
        win1, pan1 = display_panel(win1_y, win1_x, 0,0, 94,94)
        win1.addstr(1,1, os.getcwd())
        win1.addstr(2,1, "O.o")
        curses.panel.update_panels();win1.refresh()

        #left_window 
        win2_y, win2_x = layout(0.80, 0.30)
        win2, pan2 = display_panel(win2_y, win2_x, win1_y,0, 94,94)
        for i,x in enumerate(dir_list):
            win2.addstr(i+1,1, x)
        curses.panel.update_panels();win2.refresh()

        #right_window
        win3_y, win3_x = layout(0.80, 0.70)
        win3, pan3 = display_panel(win3_y, win3_x, win1_y,win2_x, 94,94)
        curses.panel.update_panels();win3.refresh()

        key = stdscr.getch()

        #key events
        if key == ord("f"):
            os.chdir(dir_list[0])

        if key == ord("e"):
            os.chdir(dir_list[1])

        if key == ord("q"):
            break

    curses.endwin()
wrapper(main)
