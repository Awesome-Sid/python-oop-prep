# 03 — Inheritance

## Definition

Subclass **IS-A** superclass: reuse and extend behavior; override methods.

## Python specifics

- `class Child(Parent):`
- Call parent logic: `super().__init__(...)` or `Parent.method(self, ...)`
- `isinstance(child, Parent)` is True

## SDET angle

`LoginPage(BasePage)` inherits waits and navigation.

## Exercises

`easy/q04_*`, `medium/q05_*`

## Trap

Forgetting `super().__init__` when parent sets required state (e.g. `self.driver`).
