# 01 — Classes and Objects

## Definition

A **class** is a blueprint; an **object** is a runtime instance with its own state (`self.attr`) and behavior (methods bound to `self`).

## Python specifics

- First parameter of instance methods is conventionally `self` (any name works; don't change it in interviews).
- `__new__(cls)` creates the instance; `__init__(self, ...)` initializes it.
- `type(obj)` and `obj.__class__` identify the class; `id(obj)` is identity in CPython.

## SDET angle

Each page object instance wraps one `WebDriver` session state for a screen.

## Exercises

`exercises/predict_output/easy/q01_*`, `q02_*`

## Trap

Thinking `__init__` allocates memory — `__new__` does.
