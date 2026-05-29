"""Encapsulation: convention, name mangling, property."""


class Config:
    def __init__(self, base_url: str):
        self._base_url = base_url  # "protected" by convention
        self.__token = "secret"  # mangled to _Config__token

    @property
    def base_url(self) -> str:
        return self._base_url

    @base_url.setter
    def base_url(self, value: str):
        if not value.startswith("http"):
            raise ValueError("URL must start with http")
        self._base_url = value


def main():
    c = Config("https://www.saucedemo.com")
    print("property:", c.base_url)
    print("mangled access possible:", c._Config__token)
    c.base_url = "https://staging.example.com"
    print("updated:", c.base_url)


if __name__ == "__main__":
    main()
