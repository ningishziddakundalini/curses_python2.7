#curses_up_down_left_right.py
import curses
from curses import panel
from curses import wrapper
from time import sleep
import os

def main(stdscr):
    stdscr = curses.initscr()

    def up_down_left_right(up, down, left, right):
        x_position = 0
        y_position = 0

        key = stdscr.getch()

        #pad up
        if key == ord(up) and x_position > -0:
            x_position -= 1
#            if key == ord("up") and x_offset > 0:
#                x_offset -=1

        #pad down
        if key == ord(down) and x_position < len(file_list)-1:
            x_position += 1
#            if key == ord("down") and x_offset < len(file_list)-pad_length-1:
#                x_offset +=1

        #pad left
        if key == ord(left) and y_position < len(file_list)-1:
            y_position += 1
#            if key == ord("left") and y_offset < len(file_list)-pad_length-1:
#                y_offset +=1

        #pad right
        if key == ord(right) and y_position > -0:
            y_position -= 1
#            if key == ord("right") and y_offset > 0:
#                y_offset -=1
        return y_position, x_position

    def panel_setup(h,l, y,x, *args):
        win = curses.newwin(h,l, y,x)
        win.box(*args)
        pan = curses.panel.new_panel(win)
        return win,pan

    while True:
        win1, pan1 = panel_setup(1,0, 0,0)
        win1.addstr("O.o")
        up_down, left_right = up_down_left_right("e", "d", "s", "f")
        pan1.move(up_down, 0)
        curses.panel.update_panels()
        win1.refresh()
        #for_addstr(widget, iterable):win1y, win1x = layout(0.20, 1.00)

wrapper(main)
