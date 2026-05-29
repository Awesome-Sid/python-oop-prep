"""Factory pattern — centralize browser creation (like driver_factory)."""


class ChromeDriver:
    def __init__(self, headless: bool):
        self.headless = headless

    def name(self) -> str:
        return "chrome-headless" if self.headless else "chrome"


class DriverFactory:
    @staticmethod
    def create(browser: str, *, headless: bool = False):
        if browser == "chrome":
            return ChromeDriver(headless)
        raise ValueError(f"unsupported browser: {browser}")


def main():
    driver = DriverFactory.create("chrome", headless=True)
    print(driver.name())


if __name__ == "__main__":
    main()
