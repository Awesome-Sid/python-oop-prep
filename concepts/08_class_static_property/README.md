# 08 — classmethod, staticmethod, property

| Decorator | Receives | Typical use |
|-----------|----------|-------------|
| (none) | `self` | Instance behavior |
| `@classmethod` | `cls` | Alternative constructors, class config |
| `@staticmethod` | nothing | Utility in class namespace |
| `@property` | `self` | Computed or validated attribute |

## SDET angle

`create_chrome_driver()` fits a classmethod on a `DriverFactory` class.

## Exercises

`easy/q05_*`, `medium/q08_*`
