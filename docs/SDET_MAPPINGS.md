# OOP Concepts → Selenium Learning Project

Maps each topic to files in [`learning_project/`](../learning_project/).

| OOP idea | Where in learning_project | Why it matters |
|----------|---------------------------|----------------|
| **Inheritance** | `pages/login_page.py` → `BasePage` | Shared `open`, `find`, `click`, `type_text` |
| **Encapsulation** | Locators as class constants on page classes | UI changes touch one page file |
| **Polymorphism** | Any `*Page` uses same base API | Tests don't care which page implements `click` |
| **Abstraction** | `BasePage` hides wait + driver details | Tests read at business level |
| **Composition** | `conftest.py` fixtures inject `driver` into pages | HAS-A driver, not subclassing WebDriver |
| **Factory** | `core/driver_factory.py` | `create_chrome_driver()` centralizes browser creation |
| **Fluent interface** | `return self` on `LoginPage` methods | Readable test steps |
| **Single responsibility** | Pages interact; tests assert | `get_error_message()` vs `assert "locked" in msg` |

## Trace exercise

1. Open `core/base_page.py` — list instance vs class attributes.
2. Open `pages/login_page.py` — what does `login()` return and why (type hint `ProductsPage`)?
3. Open `conftest.py` — how is `driver` passed into page objects?
4. Compare with `patterns_for_sdet/page_object_sketch.py` (no Selenium).

## Interview sound-bite

> "Our framework uses inheritance for shared Selenium actions, encapsulation for locators and driver, and composition via pytest fixtures. Assertions stay in tests so page objects stay reusable across positive and negative scenarios."
