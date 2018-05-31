#curses_2rows.py
import subprocess as sub 
import curses
from curses import panel
from curses import wrapper

##get a list of ls
ls = sub.Popen(["ls"], stdout = sub.PIPE)
ls_out = ls.communicate()[0]
ls_list = ls_out.split("\n")

def main(stdscr):
    stdscr = curses.initscr()
    sub1 = stdscr.subwin(24, 20, 0, 0)
    sub2 = stdscr.subwin(24, 40, 0, 0)

    sub1_list = []
    sub2_list = []

    y = stdscr.getmaxyx()[0]
    stdscr.addstr(str(y))

    for index,item in enumerate(ls_list):
        sub1.refresh()
        sub2.refresh()
    
        #subwindow1 file list
        if int(index) < y:
            sub1_list.append(item)
            for n,i in enumerate(sub1_list):
                sub1.refresh()
                sub1.addstr(n,0, i)

        #subwindow2 file list
        if int(index) > y and int(index) < y+y: 
            sub2_list.append(item)
            for n,i in enumerate(sub2_list):
                sub2.refresh()
                sub2.addstr(n,20, i)

    stdscr.getch()
    curses.endwin()
wrapper(main)
