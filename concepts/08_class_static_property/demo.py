"""classmethod factory, staticmethod util, property."""


class DriverFactory:
    default_browser = "chrome"

    def __init__(self, headless: bool):
        self.headless = headless

    @classmethod
    def from_env(cls, headless: bool = False) -> "DriverFactory":
        print(f"building {cls.default_browser}, headless={headless}")
        return cls(headless)

    @staticmethod
    def is_valid_browser(name: str) -> bool:
        return name in {"chrome", "firefox", "edge"}

    @property
    def label(self) -> str:
        return f"{DriverFactory.default_browser}-{'headless' if self.headless else 'headed'}"


def main():
    f = DriverFactory.from_env(headless=True)
    print(f.label)
    print(DriverFactory.is_valid_browser("chrome"))


if __name__ == "__main__":
    main()
