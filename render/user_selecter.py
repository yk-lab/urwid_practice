from __future__ import annotations

from logging import getLogger
from typing import Callable

from user import User

from .base import BaseSelecter

logger = getLogger(__name__)


class UserSelecter(BaseSelecter):
    title = 'Select User'
    user: User

    def __init__(self, user: User, callback: Callable) -> None:
        self.user = user
        super().__init__(callback)

    def options(self) -> list[str]:
        return self.user.names

    def get_str(self, choice: str) -> str | list[str]:
        return [choice, '\n', 'Email: ', self.user.get_email(choice), '\n']

    def pre_callback(self, button, choice: str) -> None:
        self.user.switch_user(choice)
