from __future__ import annotations

from logging import getLogger
from typing import Callable

from .base import BaseSelecter

logger = getLogger(__name__)


class AccountSelecter(BaseSelecter):
    title = 'Select Account'
    accounts: list[str]

    def __init__(self, accounts: list[str], callback: Callable) -> None:
        self.accounts = accounts
        super().__init__(callback)

    def options(self) -> list[str]:
        return self.accounts
