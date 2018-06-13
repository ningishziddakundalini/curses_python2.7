#subpan_proj_curses.py
import curses
from curses import panel
from curses import wrapper
from time import sleep
import os

y_position = 0

def main(stdscr):
    stdscr = curses.initscr()
    stdscr.idcok(0)
    curses.putp("ls")
    curses.curs_set(0)

    wnlines = 6
    pnlines = 6
    range1 = 3
    ncols = 40
    begin_y = 1
    begin_x = 1
    pos = 0
    #idcok = 0
    #scrollok = 1
    #scroll  = 1

    ls =  [i+1 for i in range(12)]
    pad_ls = []
    pos = 0
    
    win1 = stdscr.subwin(wnlines, ncols, begin_y, begin_x)
    win1.box(0,ord("_"))
    subpad1 = win1.subpad(pnlines, ncols, begin_y, begin_x)

    for index,x in enumerate(ls):
        if index+pos <= pnlines:
            pad_ls.append(x)
            

#    def for_addstr(widget, iterable):
#        for i, x in enumerate(iterable):
#            widget.addstr(i ,0, str(x))
#    for_addstr(win1, pad_ls)
#    win1.refresh()


    while True:

        for i,x  in enumerate(range(pnlines)):
            if pos == i:
                mod = curses.A_REVERSE
            else:
                mod = curses.A_NORMAL
            subpad1.addstr(x,0, str(ls[i+pos]), mod)

        key = subpad1.getch()
        subpad1.refresh()
        #stdscr.addstr(10,30, str(pos))
        stdscr.refresh()
        #subpad1.scroll(1)
#        #if pos == 11:
#            pos = 0

        #if key == ord("f") and pos <= 7:
        if key == ord("f"):

            pos += 1
            subpad1.touchwin()
            subpad1.scrollok(1)
            subpad1.scroll(1)

            if pos == pnlines+1:
                subpad1.clear()
                pos = 0

            for i,x  in enumerate(range(pnlines)):
#                if pos == i:
#                    mod = curses.A_REVERSE
#                else:
#                    mod = curses.A_NORMAL

                subpad1.addstr(x,0, str(ls[i+pos]), mod)
                subpad1.refresh()

                stdscr.addstr(10, 40, str(pos))
                stdscr.addstr(10, 30, str(i+pos))

        elif key == ord("d") and pos >= 0:
            pos -=1
            subpad1.touchwin()
            subpad1.scrollok(1)
            subpad1.scroll(-1)

            if pos < 0:
                subpad1.clear()
                pos = pnlines

                

            for i,x  in enumerate(range(pnlines)):
                subpad1.addstr(x,0, str(ls[i+pos]))
        else:
            pass

            
#            subpad1.addstr(ls[1+pos])
#            subpad1.addstr(ls[2+pos])
#            subpad1.addstr(ls[3+pos])
#            subpad1.addstr(ls[4+pos])
#            subpad1.refresh()

#            for_addstr(subpad1, ls)
#            subpad1.refresh()
#            subpad1.refresh();win1.refresh()
#            curses.doupdate()
#            win1.immedok(1)
#            subpad1.idcok(idcok)
#            subpad1.untouchwin()
#            for_addstr(subpad1, ls)
#            subpad1.idlok(1)
#            subpad1.scrollok(scrollok)

#            subpad1.idcok(idcok)
#            subpad1.untouchwin()
#            for_addstr(subpad1, ls)
#            subpad1.idlok(1)
#            subpad1.immedok(1)
#            subpad1.scrollok(scrollok)
#            for_addstr(subpad1, ls)
#            subpad1.refresh();win1.refresh()
#            subpad1.refresh();win1.refresh()
#            curses.doupdate()

        if key == ord("q"):
            break
        
    curses.curs_set(0)
wrapper(main)       
