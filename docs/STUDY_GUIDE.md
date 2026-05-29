# Python OOP Study Guide (Senior SDET)

## The four pillars (Python lens)

| Pillar | Meaning | SDET example |
|--------|---------|--------------|
| **Encapsulation** | Bundle data + behavior; control access | Page holds `driver`; locators are class attrs; tests don't touch raw Selenium |
| **Abstraction** | Expose *what*, hide *how* | `BasePage.click()` hides waits; abstract `Browser` interface |
| **Inheritance** | IS-A reuse | `LoginPage(BasePage)` |
| **Polymorphism** | Same operation, different behavior | Any page calls `find()`; duck typing with `Protocol` for helpers |

## Module index

| # | Folder | Focus |
|---|--------|-------|
| 01 | `concepts/01_classes_and_objects/` | `self`, `__init__`, identity |
| 02 | `concepts/02_encapsulation/` | `_`, `__mangle`, `@property` |
| 03 | `concepts/03_inheritance/` | override, `super()` basics |
| 04 | `concepts/04_polymorphism/` | duck typing, LSP |
| 05 | `concepts/05_abstraction/` | `abc.ABC` |
| 06 | `concepts/06_composition_vs_inheritance/` | HAS-A |
| 07 | `concepts/07_special_methods/` | dunders |
| 08 | `concepts/08_class_static_property/` | decorators |
| 09 | `concepts/09_mro_and_super/` | MRO, diamond |
| 10 | `concepts/10_advanced_python_oop/` | dataclass, slots, Enum |

Exercises: `exercises/predict_output/{easy,medium,hard}/`  
Interview: `docs/INTERVIEW_QA.md`

---

## Exam cram sheet

### Instance vs class attribute

- **Class attr** shared by all instances unless shadowed.
- **Assignment on instance** (`obj.x = 1`) creates/overwrites **instance** attr; class attr unchanged.
- **Mutable class attr** (list/dict): one object shared — classic bug.

### Mutable default in `__init__`

```python
def __init__(self, items=[]):  # BAD — same list every instance
```

Use `items=None` then `self.items = items or []`.

### MRO (C3 linearization)

- Order Python searches methods: `Class.mro()` or `Class.__mro__`.
- Multiple inheritance: left-to-right in class header matters: `class D(B, C)`.
- **Diamond:** one linear order, no duplicate class in MRO.

### `super()` is cooperative

- `super()` returns a proxy; next class in **MRO**, not always "parent" by name.
- In multiple inheritance, all mixins should call `super()` for chains to work.

### `__eq__` and `__hash__`

- Defining `__eq__` without `__hash__` sets `__hash__ = None` → unhashable (can't use in `set`/`dict` keys).
- If `a == b` then `hash(a) == hash(b)` must hold for dict keys.

### `__str__` vs `__repr__`

- `__repr__`: unambiguous, for developers (`repr(obj)`).
- `__str__`: readable, for users (`str(obj)`, `print(obj)`).
- `print` uses `__str__`, falls back to `__repr__`.

### Composition vs inheritance

- **Inheritance:** IS-A (`LoginPage` is a `BasePage`).
- **Composition:** HAS-A (`CheckoutPage` has a `CartHelper`).
- Prefer composition when behavior is optional, swapped, or combined from many sources.

### Python "privacy"

- `_name`: convention only (protected).
- `__name`: name mangling to `_ClassName__name` (not security).

---

## Pre-exam checklist

- [ ] Trace MRO for 3-level hierarchy + diamond
- [ ] Explain `super()` without saying "parent class"
- [ ] Spot mutable default and shared class list bugs
- [ ] Compare `@classmethod`, `@staticmethod`, instance method
- [ ] Explain POM using all four pillars
- [ ] Answer 10 **HIGH_LIKELIHOOD** questions in `INTERVIEW_QA.md` aloud
- [ ] Complete all `hard/` predict-output files

---

## Common wrong answers (avoid these)

| Wrong | Right |
|-------|-------|
| "`super()` always calls the parent" | Calls next in MRO |
| "Python has private fields" | Convention + mangling only |
| "Duck typing means no types" | Types exist; behavior matters at runtime |
| "Put assertions in page objects" | Assert in tests/steps; pages return state |
| "`__init__` creates the object" | `__new__` creates; `__init__` initializes |
