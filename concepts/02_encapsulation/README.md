# 02 — Encapsulation

## Definition

Bundle data and methods; restrict how internal state is read or changed.

## Python specifics

- No true `private` — use `_single_leading` (protected by convention) and `__double_leading` (name mangling to `_ClassName__attr`).
- `@property` / setter for validated access.

## SDET angle

Page objects hide locator tuples and driver; tests call `login()`, not `driver.find_element`.

## Exercises

`easy/q03_*`, `medium/q08_*`

## Trap

Believing `__x` cannot be accessed — it's `_ClassName__x` and still reachable.
