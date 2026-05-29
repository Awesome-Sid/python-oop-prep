"""
Page Object sketch — mirrors learning_project BasePage → LoginPage without Selenium.
"""


class BasePage:
    def __init__(self, driver: str):
        self.driver = driver

    def open(self, path: str = "") -> str:
        return f"{self.driver} navigates to {path or '/'}"

    def click(self, locator: str) -> str:
        return f"{self.driver} clicks {locator}"


class LoginPage(BasePage):
    USERNAME = ("id", "user-name")

    def enter_username(self, username: str) -> "LoginPage":
        self.click(self.USERNAME[1])
        return self

    def login(self, username: str, password: str) -> "ProductsPage":
        self.enter_username(username)
        self.click("password")
        self.click("login-button")
        return ProductsPage(self.driver)


class ProductsPage(BasePage):
    def is_loaded(self) -> bool:
        return True


def main():
    page = LoginPage("chrome-session")
    products = page.login("standard_user", "secret")
    print(products.open("inventory.html"))
    print("loaded?", products.is_loaded())


if __name__ == "__main__":
    main()
