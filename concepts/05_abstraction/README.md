# 05 — Abstraction

## Definition

Expose essential operations; hide implementation. In Python use `abc.ABC` and `@abstractmethod`.

## SDET angle

Abstract `Browser` or `Page` contract: tests depend on `open()`, not Chrome vs Firefox internals.

## Exercises

`medium/q07_*`

## Trap

Instantiating a class that still has unimplemented abstract methods → `TypeError`.
