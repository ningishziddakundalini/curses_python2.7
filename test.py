
import curses
from curses import panel
from curses import wrapper

def main(stdscr):
    stdscr = curses.initscr()

    def window(h,l, y,x, ry,ly, hx,lx):
        win1 = curses.newwin(h,l, y,x)
        #win1.addstr(1,1, "O.o")
        win1.border(ry,ly, hx,lx)
        win1.refresh()
        return win1
        #win1.box(94,94)

    #while True:
    #window(h,l, y,x, ry,ly, hx,lx)
    win2 = window(6,0, 0,0, 0,0, 0,ord("_"))
    win2.addstr(2,2, "O.o")
    win2.refresh()
    #win3 = window(28,30, 6,0, 0,94, 0,0)
    #win3 = window(28,60, 6,30, 0,0, 0,0)
        #win3 = window(8,0, 8,0, 0,94)
        #win2.getch()
        #win3.getch()



#        win2.getch()
#        win3.getch()


    curses.endwin()
wrapper(main)
