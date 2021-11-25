from logging import getLogger
from typing import Callable

import urwid

logger = getLogger(__name__)


class OneTimeTokenBox():
    callback: Callable

    def __init__(self, callback: Callable) -> None:
        self.callback = callback

    def render(self):
        parent = self
        edit = urwid.Edit('One Time Token:\n')

        class Wrap(urwid.Filler):
            def keypress(self, size, key):
                if key != 'enter':
                    return super().keypress(size, key)

                parent.callback(parent, self, edit.edit_text)

        self.view = Wrap(edit)

        return self.view
