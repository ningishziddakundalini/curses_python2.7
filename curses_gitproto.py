#curses_gitproto.py
import curses
from curses import panel
import os

class Widgets(object):
    
    def __init__(self, stdscr):
        stdscr.clear()
        curses.initscr()
        curses.start_color()
        #curses.init_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

        self.win1 = curses.newwin(0, 0, 0, 0)
        self.win2 = curses.newwin(0, 0, 0, 0)

        panel.update_panels();curses.doupdate()

#        while True:
#            self.win1.addstr(1, 0, "window1", curses.color_pair(1))
#            self.win2.addstr(2, 0, "window2")

class App(object):
    def __init__(self, stdscr):

        widgets = Widgets(stdscr) 

        key = stdscr.getch()
        while True:

            if key == ord("j"):
                #set up curses to display os.system normally
                curses.endwin()
                os.system("git status")

            elif key == ord("k"):
                break
            
#                if key == ord("1"):
#                    #set up curses to display os.system normally
#                    curses.initscr() 
#                    #widgets = Widgets(stdscr) 

curses.wrapper(App)

