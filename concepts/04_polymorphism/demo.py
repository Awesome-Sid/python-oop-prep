"""Polymorphism via duck typing — no common base required."""


class ChromeDriver:
  def quit(self):
    return "chrome quit"


class FirefoxDriver:
  def quit(self):
    return "firefox quit"


def close_browser(driver) -> str:
  """Accepts any object with quit() — duck typing."""
  return driver.quit()


def main():
  for driver in ChromeDriver(), FirefoxDriver():
    print(close_browser(driver))


if __name__ == "__main__":
  main()
