# 06 — Composition vs Inheritance

## Definition

- **Inheritance (IS-A):** `LoginPage` is a `BasePage`.
- **Composition (HAS-A):** `CheckoutPage` owns a `WaitHelper` or receives `driver` via fixture.

## When to prefer composition

- Behavior is optional or swappable (logging, retry, API client).
- Multiple unrelated capabilities (avoid deep trees).
- Test doubles: inject a fake `Mailer` instead of subclassing.

## SDET angle

`conftest` composes driver + page: `LoginPage(driver)` — page **has** driver, doesn't subclass WebDriver.

## Exercises

`medium/q09_*`
