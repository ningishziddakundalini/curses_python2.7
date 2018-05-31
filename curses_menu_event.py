#curses_menu_event.py
import subprocess as sub 
import curses
from curses import panel
from curses import wrapper

#get a list of ls
ls = sub.Popen(["ls"], stdout = sub.PIPE)
ls_out = ls.communicate()[0]
ls_list = ls_out.split("\n")

#init
def main(stdscr):
    curses.curs_set(0)                                                   
    window1 = curses.newwin(0,0,0,0)
    win1_ls = ["show string", "delete string", "three", "four", "five", "six"]
    pos = 0

    while True:
        #display list menu
        for index, item in enumerate(win1_ls):

            #modifier
            if pos == index:
                mod = curses.A_REVERSE
            if pos != index:
                mod = curses.A_NORMAL

            #display
            if index < 3: 
                window1.addstr(index, 0, item, mod)
            if index >= 3:
                window1.addstr(index-3, 20, item, mod)
            
        #navigate
        key = window1.getch()
        if key == ord("j"):
            pos +=1
        if key == ord("k"):
            pos -=1

        #bounderies
        if pos >= len(win1_ls):
            pos = len(win1_ls)-1
        if pos <= 0:
            pos = 0

        #keyevents
        if key == ord("q"):
            break
        if pos == 0 and key == 10:
            window1.addstr(0, 40, 'pressed enter')
        if pos == 1 and key == 10:
            window1.erase()

        
    curses.endwin()
wrapper(main)
