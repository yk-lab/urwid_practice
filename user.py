from __future__ import annotations

from configparser import ConfigParser


class User:
    config: ConfigParser
    active: str | None = None

    def __init__(self, filename) -> None:
        self.config = ConfigParser()
        self.config.read(filename)

    def switch_user(self, section: str) -> None:
        if section not in self.config.sections():
            raise ValueError
        self.active = section

    def get_email(self, user: str):
        return self.config[user]['Email']

    @property
    def names(self) -> list[str]:
        return self.config.sections()

    @property
    def _user(self):
        if self.active is None:
            raise ValueError

        return self.config[self.active]

    @property
    def email(self):
        return self._user['Email']

    @property
    def password(self):
        return self._user['Password']
