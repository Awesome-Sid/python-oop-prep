"""Single inheritance and method override."""


class BasePage:
  def __init__(self, driver_name: str):
    self.driver_name = driver_name

  def open(self, path: str = ""):
    return f"[{self.driver_name}] GET {path or '/'}"


class LoginPage(BasePage):
  def open(self, path: str = ""):
    parent_msg = super().open(path)
    return parent_msg + " -> login screen ready"


def main():
  page = LoginPage("chrome")
  print(page.open())
  print("is BasePage?", isinstance(page, BasePage))


if __name__ == "__main__":
  main()
