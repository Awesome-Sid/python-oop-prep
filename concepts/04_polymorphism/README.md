# 04 — Polymorphism

## Definition

Same interface, different implementations. Python uses **duck typing**: if it quacks (`click()`), use it.

## Liskov Substitution Principle (LSP)

Subtypes must be usable wherever the base type is expected without breaking callers.

## SDET angle

Any page with `click(locator)` works in a generic helper — no shared base required in duck typing, but POM uses a base for consistency.

## Exercises

`medium/q06_*`

## Trap

Subclass that strengthens preconditions (e.g. `click` that requires login first) can violate LSP for generic helpers.
