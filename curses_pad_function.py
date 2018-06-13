#curses_pad_function.py
import curses
from curses import panel
from curses import wrapper
from time import sleep
import os

y_position = 0

def main(stdscr):
    stdscr = curses.initscr()
    curses.curs_set(0)
    y_position = 0

##        def up_down(up_key, down_key):
##        global y_position
##        key = stdscr.getch()
##        #pad up_key
##        if key == ord(up_key):
##            y_position -= 1
##            return y_position,key
##        #pad down_key
##        if key == ord(down_key):
##            y_position += 1
##            return y_position,key
##        else:
##            return y_position,key


    def panel_setup(h,l, y,x, down,up, iterable, *args):
        global y_position
        win = stdscr.subwin(h,l, y,x)
        win.box(*args)
        pad = win.subpad(y+2,x+2)
        pan = curses.panel.new_panel(win)
        curses.panel.update_panels();win.refresh();pad.refresh()

        for i, x in enumerate(iterable):
            if y_position == i:
                mod = curses.A_REVERSE  
            else:
                mod = curses.A_NORMAL

            pad.addstr(i ,0, x, mod)

        key = pad.getch()

        #pad down
        if key == ord(down) and y_position < len(iterable)-1:
            y_position += 1
            if key == ord("j") and y_offset < len(iterable)-h-1:
                y_offset +=1

        #pad up
        if key == ord(up) and y_position > -0:
            y_position -= 1
            if key == ord("k") and y_offset > 0:
                y_offset -=1

        return y_position, win, pad, pan, key

    def for_addstr(widget, iterable):
        for i, x in enumerate(iterable):
            widget.addstr(i ,0, x )

    ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    #stdscr.addstr(1,1, str(y_position))
    #stdscr.refresh()

    while True:
        #return y_position, win, pad, pan, key
        #panel_setup(h,l, y,x, down,up, iterable *box)
        y1, win1, pad1, pan1, key = panel_setup(10,10, 1,1, "d","e", ls, 94,94)
        curses.panel.update_panels();win1.refresh();pad1.refresh()

        if key == ord("q"):
            break
        #y = up_down("e", "d")
        #pan1.move(y, 1)

#       y, key = up_down("e", "d")
#       stdscr.erase()
#       stdscr.addstr(1,1, str(y))
#       stdscr.refresh()
#       if key == ord("q"):
#           stdscr.clear()
#           break

wrapper(main)
