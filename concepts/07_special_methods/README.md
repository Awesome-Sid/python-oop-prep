# 07 — Special (Dunder) Methods

## Common dunders for interviews

| Method | Purpose |
|--------|---------|
| `__init__` | Initialize instance |
| `__str__` / `__repr__` | Human vs developer string |
| `__eq__` / `__hash__` | Equality and hashability |
| `__len__` | `len(obj)` |
| `__bool__` | Truthiness |
| `__getitem__` | Indexing |

## SDET angle

`__repr__` on a custom `TestResult` helps debug failures in logs.

## Exercises

`medium/q10_*`, `hard/q11_*`
