# 09 — MRO and super()

## MRO

Python 3 uses **C3 linearization**. Inspect with `Class.mro()`.

## super()

Returns a proxy to call the **next** method in MRO — essential in multiple inheritance.

## Diamond pattern

```text
    A
   / \
  B   C
   \ /
    D
```

`D.mro()` → `[D, B, C, A, object]`

## Exercises

`medium/q05_*`, `hard/q12_*`, `q13_*`
