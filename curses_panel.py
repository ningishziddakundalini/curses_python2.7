#curses_panel.py
from time import sleep
import curses, curses.panel

def make_panel(h,l, y,x, str):
    win = curses.newwin(h,l, y,x)
    win.erase()
    win.box()
    win.addstr(2, 2, str)

    panel = curses.panel.new_panel(win)

    return win, panel

def test(stdscr):
    try:
        curses.curs_set(0)
    except:
        pass

    stdscr.box()
    stdscr.addstr(0, 2, "panels everywhere")
    win1, panel1 = make_panel(3,12, 1,1, "Panel 1")
    win2, panel2 = make_panel(3,12, 4,8, "Panel 2")
    curses.panel.update_panels(); stdscr.refresh()
    sleep(1)

    panel2.top(); curses.panel.update_panels(); stdscr.refresh()
    sleep(1)

    for i in range(40):
        panel2.move(5, 8+i)
        curses.panel.update_panels(); stdscr.refresh()
        sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(test)

