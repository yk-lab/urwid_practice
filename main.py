#!/usr/bin/env python3

from logging import getLogger

import urwid
from render import AccountSelecter, OneTimeTokenBox, UserSelecter
from user import User
from time import sleep

logger = getLogger(__name__)


class Main():
    user: User

    def __init__(self, filename='user.ini') -> None:
        self.user = User(filename)


def exit_program(button):
    logger.info(button)
    raise urwid.ExitMainLoop()


def confirm_item(button, choice):
    logger.info(button)
    raise urwid.ExitMainLoop()


def account_chosen(selecter, button, choice):
    exit_program(button)


def user_chosen(selecter, button, choice):
    def callback(box, widget, code):
        main.original_widget = AccountSelecter(
            ['A', 'B', 'C'], account_chosen).render()

    main.original_widget = OneTimeTokenBox(callback).render()


if __name__ == '__main__':
    _main = Main()

    main = UserSelecter(_main.user, user_chosen).render()

    top = urwid.Overlay(
        main,
        urwid.SolidFill('\N{MEDIUM SHADE}'),
        align='center',
        valign='middle',
        width=('relative', 60),
        height=('relative', 60),
        min_width=20, min_height=9)
    urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

    print('もしかして')
    for i in range(10):
        print(i)
        sleep(3)
