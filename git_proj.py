#git_proj.py
import curses
import os
from glob import glob
from curses import panel
from curses import wrapper

def main(stdscr):
    curses.curs_set(0)
    win1 = curses.newwin(4,0, 0,0)
    win1.box()
    win1.refresh()

    win2 = curses.newwin(4,0, 5,0)
    win2.box()
    win2.refresh()

    git_commands = (
        "1. git pull",
        "2. git add -A",
        "3. git commit -m comment",
        "4. git push -u curses https://ningishziddatao@github.com/curses",
        "5. git push -u curses https://ningishziddatao@github.com/vim"
        )

    stdscr.box()

    def display_menu():
        for i, x in enumerate(git_commands):
            stdscr.addstr(i,0, git_commands[i])

    display_menu()

    while True:
        key = stdscr.getch()

        if key == 10:
            stdscr.clear()
            stdscr.box()

            display_menu()


        if key == ord("1"):
            #stdscr.box()
            curses.endwin()
            os.system("git pull")
            os.system("git status")
            stdscr = curses.initscr()
            stdscr.addstr(23,0 ,"press enter to continue, q to quit")

        if key == ord("2"):
            #stdscr.box()
            curses.endwin()
            os.system("git add -A")
            os.system("git status")
            stdscr = curses.initscr()
            stdscr.addstr(23,0 ,"press enter to continue, q to quit")

        if key == ord("3"):
            curses.endwin()
            os.system("git commit -m comment")
            stdscr = curses.initscr()
            stdscr.addstr(23,0 ,"press enter to continue, q to quit")

        if key == ord("4"):
            curses.endwin()
            os.system("git push -u https://ningishziddatao@github.com/ningishziddakundalini/python2.7_curses")
            #os.system("git status")
            stdscr = curses.initscr()
            stdscr.addstr(23,0 ,"press enter to continue, q to quit")
        if key == ord("q"):
            break


        if key == ord("5"):
            curses.endwin()
            os.system("git push -u https://ningishziddatao@github.com/ningishziddakundalini/vim")
            #os.system("git status")
            stdscr = curses.initscr()
            stdscr.addstr(23,0 ,"press enter to continue, q to quit")
        if key == ord("q"):
            break
if __name__ == '__main__':
    curses.wrapper(main)

