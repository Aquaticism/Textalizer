import curses
from curses import wrapper
from curses.textpad import rectangle
from pygame import mixer
import tools

file = tools.TTZ()


def main(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.addstr(0, 0, f"Playing: {file.name}")

    editwin = curses.newwin(5,30, 2,1)
    rectangle(stdscr, 1, 0, 1+file.height+1, 1+file.width+1)
    stdscr.refresh()

    editwin.addstr(0, 0, "poop")


def init(filepath):

    wrapper(main)
