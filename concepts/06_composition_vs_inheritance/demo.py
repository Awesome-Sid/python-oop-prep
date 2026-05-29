"""Composition: page HAS-A wait helper instead of inheriting waits."""


class WaitHelper:
    def until_visible(self, locator: str) -> str:
        return f"visible: {locator}"


class ProductsPage:
    def __init__(self, driver_name: str):
        self.driver_name = driver_name
        self.waits = WaitHelper()  # HAS-A

    def add_to_cart(self, item_id: str) -> str:
        loc = f"[data-test='add-{item_id}']"
        self.waits.until_visible(loc)
        return f"{self.driver_name}: added {item_id}"


def main():
    page = ProductsPage("chrome")
    print(page.add_to_cart("sauce-labs-backpack"))


if __name__ == "__main__":
    main()
