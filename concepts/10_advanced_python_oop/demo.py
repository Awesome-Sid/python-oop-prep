"""dataclass, Enum, __slots__."""

from dataclasses import dataclass
from enum import Enum


class BrowserType(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"


@dataclass(frozen=True)
class TestUser:
    username: str
    password: str


class LightPage:
    __slots__ = ("name", "url")

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url


def main():
    user = TestUser("standard_user", "secret_sauce")
    print(user)
    print(BrowserType.CHROME.value)
    page = LightPage("login", "/")
    # page.extra = 1  # AttributeError without __dict__
    print(page.name, page.url)


if __name__ == "__main__":
    main()
