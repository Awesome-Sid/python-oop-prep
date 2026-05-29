"""Strategy pattern — swap wait strategy without changing page API."""


class ExplicitWait:
    def wait_for(self, locator: str) -> str:
        return f"explicit wait: {locator}"


class NoWait:
    def wait_for(self, locator: str) -> str:
        return f"no wait: {locator}"


class BasePage:
    def __init__(self, wait_strategy):
        self.wait_strategy = wait_strategy

    def click(self, locator: str) -> str:
        self.wait_strategy.wait_for(locator)
        return f"clicked {locator}"


def main():
    fast = BasePage(NoWait())
    stable = BasePage(ExplicitWait())
    print(fast.click("#login"))
    print(stable.click("#login"))


if __name__ == "__main__":
    main()
