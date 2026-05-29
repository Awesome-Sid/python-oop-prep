"""Abstract base class for a browser contract."""

from abc import ABC, abstractmethod


class Browser(ABC):
  @abstractmethod
  def start(self) -> str:
    ...

  @abstractmethod
  def quit(self) -> str:
    ...


class ChromeBrowser(Browser):
  def start(self) -> str:
    return "Chrome started"

  def quit(self) -> str:
    return "Chrome stopped"


def main():
  b: Browser = ChromeBrowser()
  print(b.start())
  print(b.quit())
  # Browser()  # TypeError: Can't instantiate abstract class


if __name__ == "__main__":
  main()
