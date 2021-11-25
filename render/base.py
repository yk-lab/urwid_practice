from __future__ import annotations

from logging import getLogger
from typing import Callable

import urwid

logger = getLogger(__name__)


class BaseSelecter():
    title = 'Select'
    callback: Callable

    def __init__(self, callback: Callable) -> None:
        self.callback = callback

    def options(self) -> list[str]:
        raise NotImplementedError

    def get_str(self, choice: str) -> str | list[str]:
        return choice

    def pre_callback(self, button, choice: str) -> None:
        pass

    def render(self) -> urwid.Widget:
        body = [urwid.Text(self.title), urwid.Divider()]
        for option in self.options():
            button = urwid.Button(option)
            urwid.connect_signal(button, 'click', self.confirmation, option)
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        self.view = urwid.Padding(
            urwid.ListBox(urwid.SimpleFocusListWalker(body)), left=2, right=2)

        return self.view

    def confirmation(self, button, choice: str) -> None:
        response = urwid.Text(self.get_str(choice))
        done = urwid.Button('Ok')
        urwid.connect_signal(done, 'click', self.confirm, choice)
        self.view.original_widget = urwid.Filler(
            urwid.Pile([
                response,
                urwid.AttrMap(done, None, focus_map='reversed')]))

    def confirm(self, button, choice: str) -> None:
        self.pre_callback(button, choice)
        self.callback(self, button, choice)
