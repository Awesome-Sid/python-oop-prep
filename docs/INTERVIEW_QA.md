# Python OOP — Mock Interview Q&A (Senior SDET)

Practice aloud (60–90 seconds per **HIGH_LIKELIHOOD** question). Tags: **HIGH_LIKELIHOOD** | **MEDIUM** | **STRETCH**.

---

## Four pillars & fundamentals

### Q1 · HIGH_LIKELIHOOD · Four pillars
**Interviewer:** Explain the four pillars of OOP and give a test-automation example for each.

**Candidate:** Encapsulation bundles locators and driver inside a page class. Abstraction exposes `login()` while hiding waits. Inheritance lets `LoginPage` reuse `BasePage` actions. Polymorphism lets any page use the same `click()` contract or duck-typed helpers. Together they keep UI changes localized.

**Trap answer:** Listing definitions without framework examples.

**SDET angle:** Maps to `learning_project/pages/login_page.py`.

---

### Q2 · HIGH_LIKELIHOOD · Class vs object
**Interviewer:** What is the difference between a class and an object?

**Candidate:** A class is the blueprint; an object is a concrete instance at runtime with its own attribute values. Many page objects can share one class but each holds its own driver reference.

---

### Q3 · HIGH_LIKELIHOOD · `self`
**Interviewer:** What is `self` in Python?

**Candidate:** The instance passed as the first argument to instance methods—conventionally named `self`. It lets methods read and write that object's state, like `self.driver`.

---

### Q4 · MEDIUM · `__new__` vs `__init__`
**Interviewer:** Difference between `__new__` and `__init__`?

**Candidate:** `__new__` creates and returns the instance (rare to override except singletons, immutables). `__init__` initializes the already-created object. Memory allocation happens before `__init__`.

**See:** `exercises/hard/q18_new_vs_init.py`

---

### Q5 · HIGH_LIKELIHOOD · Instance vs class attribute
**Interviewer:** How do instance and class attributes differ? What if I assign on the instance?

**Candidate:** Class attributes live on the class and are shared until shadowed. `obj.x = 1` creates an instance attribute if `x` wasn't already on the instance—it does not change the class attribute for other instances.

**See:** `easy/q01_*`, `medium/q13_*`

---

### Q6 · HIGH_LIKELIHOOD · Mutable default argument
**Interviewer:** Why is `def __init__(self, items=[])` dangerous?

**Candidate:** The default list is created once at function definition time and reused across calls. Later instances share the same list. Use `items=None` and `self.items = items or []`.

**See:** `easy/q02_mutable_default.py`

---

### Q7 · MEDIUM · Shared mutable class attribute
**Interviewer:** What happens if a class has `errors = []` and instances append to it?

**Candidate:** All instances share one list object on the class. Use instance lists in `__init__` instead.

**See:** `medium/q09_shared_class_list.py`

---

## Encapsulation

### Q8 · HIGH_LIKELIHOOD · Encapsulation in Python
**Interviewer:** How does Python implement encapsulation?

**Candidate:** By convention: public attributes, `_protected` by convention, `__private` triggers name mangling to `_ClassName__attr`. Real enforcement uses `@property` and keeping internals off the public API—like hiding Selenium calls inside page methods.

---

### Q9 · HIGH_LIKELIHOOD · `@property`
**Interviewer:** Why use `@property` instead of a public attribute?

**Candidate:** You can validate on set, compute on get, or migrate from attribute to method without breaking callers. Example: ensuring timeout is always positive.

**See:** `medium/q08_property_side_effect.py`

---

### Q10 · MEDIUM · Name mangling
**Interviewer:** Does `__token` make a field truly private?

**Candidate:** No. It's mangled to `_ClassName__token` to avoid accidental overrides in subclasses—not security. Still accessible if you know the mangled name.

**See:** `easy/q03_name_mangling.py`

---

## Inheritance & MRO

### Q11 · HIGH_LIKELIHOOD · Inheritance purpose
**Interviewer:** Why use inheritance in a test framework?

**Candidate:** To reuse common behavior—waits, navigation, logging—from a base page so screen classes only define locators and screen-specific flows. Reduces duplication and centralizes fixes when Selenium usage changes.

---

### Q12 · HIGH_LIKELIHOOD · MRO
**Interviewer:** What is Method Resolution Order (MRO)?

**Candidate:** The order Python searches bases for an attribute or method—C3 linearization in Python 3. Inspect with `Class.mro()`. It matters for multiple inheritance and predictable `super()` chains.

**See:** `medium/q07_mro_print.py`, `concepts/09_mro_and_super/`

---

### Q13 · HIGH_LIKELIHOOD · Diamond problem
**Interviewer:** Explain the diamond problem and how Python handles it.

**Candidate:** When two parents share a grandparent, naive inheritance could call the grandparent twice. Python's MRO linearizes the hierarchy so each class appears once in a consistent order.

---

### Q14 · HIGH_LIKELIHOOD · `super()` semantics
**Interviewer:** What does `super()` do? Does it always call the parent class?

**Candidate:** `super()` returns a proxy to invoke the next method in the MRO—not necessarily the class listed as parent in source. In cooperative multiple inheritance, every class in the chain should call `super()` once.

**Trap answer:** "`super()` calls the parent class by name."

**See:** `medium/q11_*`, `medium/q16_*`

---

### Q15 · MEDIUM · Override vs overload
**Interviewer:** Does Python support method overloading?

**Candidate:** Not like Java. You override by redefining in a subclass. "Overloading" is usually default arguments, `*args`, or `@singledispatch`. Interviews often want you to say Python uses override + optional parameters.

---

### Q16 · MEDIUM · `super().__init__`
**Interviewer:** When must you call `super().__init__`?

**Candidate:** When the parent initializes required state—driver, base URL, session. If you override `__init__` in a child and skip `super()`, parent setup may never run.

---

## Polymorphism & abstraction

### Q17 · HIGH_LIKELIHOOD · Polymorphism
**Interviewer:** What is polymorphism? How does Python implement it?

**Candidate:** Same interface, different behavior. Python relies heavily on duck typing: if an object has `quit()`, teardown works—no shared base required. With ABCs you can enforce interfaces for larger frameworks.

---

### Q18 · HIGH_LIKELIHOOD · Duck typing
**Interviewer:** What is duck typing?

**Candidate:** "If it walks like a duck and quacks like a duck, use it." Types are less important than the methods an object provides at runtime. Useful for swapping real WebDriver with fakes in unit tests.

**See:** `medium/q15_duck_typing.py`

---

### Q19 · HIGH_LIKELIHOOD · LSP
**Interviewer:** Explain the Liskov Substitution Principle.

**Candidate:** Subtypes must be usable anywhere the base type is expected without breaking callers. Bad example: a `ReadOnlyPage` subclass whose `click()` raises—tests expecting a normal page would fail.

---

### Q20 · HIGH_LIKELIHOOD · Abstract class / ABC
**Interviewer:** How do you define an interface-like contract in Python?

**Candidate:** Use `abc.ABC` and `@abstractmethod`. Subclasses must implement abstract methods before instantiation. Good for `Browser` or `Page` contracts across implementations.

**See:** `concepts/05_abstraction/`, `medium/q14_*`

---

### Q21 · MEDIUM · ABC vs Protocol
**Interviewer:** ABC versus `typing.Protocol`?

**Candidate:** ABC enforces at inheritance/instantiation time. Protocol is structural typing for static checkers—useful when you can't change third-party classes but want type hints.

---

## classmethod, staticmethod, property

### Q22 · HIGH_LIKELIHOOD · Three method types
**Interviewer:** Compare instance method, `@classmethod`, and `@staticmethod`.

**Candidate:** Instance methods get `self`. Classmethods get `cls`—good for alternative constructors and reading class config. Staticmethods get neither—they're namespaced functions. Factory `from_config(cls)` is a classic classmethod.

**See:** `easy/q05_*`, `concepts/08_*`

---

### Q23 · MEDIUM · When staticmethod
**Interviewer:** When would you use `@staticmethod` in a test project?

**Candidate:** For utilities logically grouped with a class but not needing `self` or `cls`—e.g. validating browser name strings on `DriverFactory`.

---

## Composition vs inheritance

### Q24 · HIGH_LIKELIHOOD · Composition vs inheritance
**Interviewer:** When do you choose composition over inheritance?

**Candidate:** When behavior is optional, swapped, or combined from several sources—wait strategy, API client, reporter. Inheritance for true IS-A relationships like `LoginPage` is a `BasePage`. Composition for HAS-A: page has a wait helper or receives driver via fixture.

**See:** `concepts/06_*`, `patterns_for_sdet/strategy_demo.py`

---

### Q25 · HIGH_LIKELIHOOD · Deep inheritance trees
**Interviewer:** What's wrong with a deep page inheritance tree?

**Candidate:** Fragile MRO, tight coupling, and hard-to-trace behavior. Prefer shallow inheritance plus mixins or composition for cross-cutting concerns like logging.

---

## Special methods

### Q26 · HIGH_LIKELIHOOD · `__str__` vs `__repr__`
**Interviewer:** Difference between `__str__` and `__repr__`?

**Candidate:** `__repr__` should be unambiguous for developers; `__str__` is human-readable. `print(obj)` uses `__str__`, falls back to `__repr__`. For failed test logs, `repr` is often better for debugging state.

**See:** `medium/q10_str_repr.py`

---

### Q27 · HIGH_LIKELIHOOD · `__eq__` and `__hash__`
**Interviewer:** You define `__eq__` but not `__hash__`. What happens?

**Candidate:** Python sets `__hash__` to `None`—instances become unhashable. You can't put them in a set or use as dict keys unless you restore a consistent `__hash__`.

**See:** `medium/q12_eq_hash_set.py`

---

### Q28 · MEDIUM · `is` vs `==`
**Interviewer:** When do you use `is` versus `==`?

**Candidate:** `==` compares value (may call `__eq__`). `is` compares identity—same object in memory. In tests, assert on values with `==`; use `is` for singletons like `None`, `True`, `False`.

**See:** `hard/q22_is_vs_eq.py`

---

### Q29 · STRETCH · `__slots__`
**Interviewer:** What does `__slots__` do?

**Candidate:** Declares fixed instance attributes, avoids per-instance `__dict__` (unless you add `'__dict__'` in slots), saves memory, prevents arbitrary attribute assignment. Trade-off: less flexible objects.

**See:** `hard/q19_slots_dict.py`

---

### Q30 · STRETCH · Descriptors
**Interviewer:** What is a descriptor?

**Candidate:** An object defining `__get__`, `__set__`, or `__delete__` controlling attribute access. `@property` is implemented with descriptors. Class-level data descriptors can share state across instances—know the pitfall.

**See:** `hard/q20_descriptor_class_property.py`

---

## SDET / test automation (high value)

### Q31 · HIGH_LIKELIHOOD · Page Object Model
**Interviewer:** What is the Page Object Model and which OOP ideas does it use?

**Candidate:** One class per screen or component encapsulating locators and actions. Inheritance shares base interactions; encapsulation hides Selenium; abstraction exposes business-level methods like `login_as(user)`.

---

### Q32 · HIGH_LIKELIHOOD · Assertions in tests vs pages
**Interviewer:** Should page objects contain assertions?

**Candidate:** Generally no—pages return state or perform actions; tests or step definitions assert. Keeps pages reusable for positive and negative paths and avoids hidden failures in reusable components.

---

### Q33 · HIGH_LIKELIHOOD · BasePage responsibilities
**Interviewer:** What belongs in `BasePage` versus `LoginPage`?

**Candidate:** Base: driver, navigation, generic wait-backed `click`/`type`. Login: username/password locators, login flow, returning the next page object. Screen-specific locators stay out of base.

---

### Q34 · HIGH_LIKELIHOOD · Factory pattern in automation
**Interviewer:** How does a driver factory relate to OOP?

**Candidate:** Centralizes object creation—browser type, headless, options—so tests depend on `create_driver()` not scattered `webdriver.Chrome()` calls. Often implemented as a classmethod or module function; that's the Factory pattern.

**See:** `patterns_for_sdet/factory_demo.py`, `learning_project/core/driver_factory.py`

---

### Q35 · HIGH_LIKELIHOOD · Fluent API / chaining
**Interviewer:** Why return `self` from page methods?

**Candidate:** Enables fluent chaining: `page.enter_user(u).enter_pass(p).click_login()`—readable tests without repeating the page variable. Return a *different* page type when navigation changes screen, e.g. `ProductsPage`.

---

### Q36 · MEDIUM · Strategy pattern in tests
**Interviewer:** Give an example of the Strategy pattern in test code.

**Candidate:** Inject different wait strategies (explicit, fluent, none) into a page or helper without subclassing every page—composition over inheritance.

**See:** `patterns_for_sdet/strategy_demo.py`

---

### Q37 · MEDIUM · Fixtures and composition
**Interviewer:** How do pytest fixtures relate to OOP?

**Candidate:** Fixtures compose dependencies—driver, pages, API clients—into tests without deep class hierarchies. That's composition at the test harness level.

---

### Q38 · MEDIUM · Single Responsibility
**Interviewer:** What is Single Responsibility Principle? Example violation in automation?

**Candidate:** A class should have one reason to change. Violation: one page class that logs in, calls REST APIs, and parses PDFs—split by responsibility.

---

### Q39 · MEDIUM · Open/Closed Principle
**Interviewer:** Explain Open/Closed Principle with a framework example.

**Candidate:** Open for extension, closed for modification. Add a new `FirefoxPage` or browser driver without editing every test—extend via new classes or config-driven factory rather than changing stable base code.

---

### Q40 · MEDIUM · Dependency Injection in tests
**Interviewer:** What is dependency injection and why use it in automation?

**Candidate:** Pass dependencies (driver, config, clock) from outside instead of hard-coding inside the class. Makes unit tests easy with fakes and keeps environments configurable.

---

### Q41 · HIGH_LIKELIHOOD · Interface vs implementation in POM
**Interviewer:** How is abstraction used when you might support API and UI tests?

**Candidate:** Define an abstract `UserActions` with `login()`; UI implementation uses Selenium, API implementation uses HTTP client. Tests depend on the contract, not the technology.

---

### Q42 · MEDIUM · Mixins for logging
**Interviewer:** When are mixins appropriate?

**Candidate:** For cross-cutting behavior—logging, screenshots—mixed into page classes. Must use cooperative `super()` so MRO chains don't skip classes.

**See:** `hard/q23_mixin_log.py`

---

## Design & senior judgment

### Q43 · HIGH_LIKELIHOOD · Composition for test data
**Interviewer:** Would you subclass a page to add test data?

**Candidate:** Usually no—pass data as method arguments or load from JSON (`test_data.json`). Subclassing for data creates class explosion; configuration is not an IS-A relationship.

---

### Q44 · MEDIUM · Multiple inheritance in Python
**Interviewer:** Is multiple inheritance bad?

**Candidate:** Not inherently—Python uses MRO. It becomes risky without cooperative `super()` and clear mixin roles. Prefer few mixins with focused behavior.

---

### Q45 · MEDIUM · `@dataclass`
**Interviewer:** When would you use `@dataclass` in a test project?

**Candidate:** For immutable test data models—users, checkout payloads—with auto `__init__`, `__repr__`, optional ordering. `frozen=True` prevents accidental mutation.

**See:** `concepts/10_advanced/`, `hard/q24_*`

---

### Q46 · MEDIUM · `Enum` in frameworks
**Interviewer:** Why use `Enum` for browsers or environments?

**Candidate:** Named constants prevent typos like `"chrme"`, give autocomplete, and centralize valid values for factories and config.

---

### Q47 · STRETCH · Metaclasses
**Interviewer:** What is a metaclass?

**Candidate:** The class of a class—controls class creation. Rare in everyday SDET work unless building frameworks. Mention you know it exists; prefer simpler patterns unless role demands framework design.

---

### Q48 · STRETCH · `functools.cached_property`
**Interviewer:** How is `cached_property` different from `@property`?

**Candidate:** Computes once per instance on first access, then stores result on the instance—useful for expensive derived data, not for values that change each call.

---

### Q49 · HIGH_LIKELIHOOD · Strong vs dynamic typing
**Interviewer:** Is Python strongly or weakly typed?

**Candidate:** Strongly typed—types aren't silently coerced in surprising ways like `"1" + 1`. It's dynamically typed because variable types are checked at runtime, not compile time. Duck typing is separate from weak typing.

---

### Q50 · MEDIUM · SOLID recap for SDET
**Interviewer:** Which SOLID principles matter most in test automation?

**Candidate:** SRP for pages/helpers, OCP for extending browsers/tests without editing core, LSP for substitutable fakes, ISP for small interfaces, DIP for injecting driver/config. Most interviews want concrete examples, not acronyms alone.

---

### Q51 · HIGH_LIKELIHOOD · Code trace question
**Interviewer:** (Whiteboard) What is MRO of `class D(B, C)` and which `f` runs?

**Candidate:** Walk C3: list bases left-to-right, merge. Run `D.mro()` mentally or on paper. Call order follows MRO for overrides; `super()` follows MRO for cooperative methods.

**See:** all `predict_output/medium` MRO questions

---

### Q52 · HIGH_LIKELIHOOD · Maintainability when UI changes
**Interviewer:** How does OOP help when a locator changes?

**Candidate:** Update one constant in one page class; tests calling `login_page.login()` unchanged. That's encapsulation paying off—tests express intent, not CSS.

---

### Q53 · MEDIUM · Anti-pattern: God page object
**Interviewer:** What is a "God" page object?

**Candidate:** One class knowing every screen and API—violates SRP, hard to maintain. Split by screen or feature; use composition for shared widgets (header, cart badge).

---

### Q54 · MEDIUM · Testing private methods
**Interviewer:** Should you test private methods directly?

**Candidate:** Test public behavior. In Python, "private" is convention; testing `_click` couples tests to implementation. Test outcomes through public page API.

---

### Q55 · STRETCH · `__call__` on page object
**Interviewer:** When would you implement `__call__`?

**Candidate:** Rare—could make a page callable as shorthand. More common in custom decorators or callable fixtures; mention awareness, not required for POM.

---

### Q56 · HIGH_LIKELIHOOD · Monkey patching vs OOP
**Interviewer:** Monkey patching `driver.find_element` versus proper abstraction?

**Candidate:** Patching is brittle and global. Prefer wrapping driver in a class or injecting a fake implementing the same interface—clearer OOP and reversible in tests.

---

### Q57 · MEDIUM · Parallel runs and class state
**Interviewer:** Can class attributes break parallel pytest?

**Candidate:** Yes—mutable class state is shared across workers in the same process. Prefer instance attributes or session-scoped fixtures with isolation; avoid shared lists on page classes.

---

### Q58 · MEDIUM · Copy vs deepcopy for test data
**Interviewer:** How does mutability relate to OOP test data?

**Candidate:** Shallow copy shares nested objects; deep copy duplicates nested structures. If a class holds a list of users, mutating one test's copy can affect another without proper copy discipline.

---

### Q59 · STRETCH · `__getattr__` vs `__getattribute__`
**Interviewer:** Difference between `__getattr__` and `__getattribute__`?

**Candidate:** `__getattribute__` runs on every attribute access; `__getattr__` only when normal lookup fails. Easy to break expectations—rare in page objects.

---

### Q60 · HIGH_LIKELIHOOD · Your project walkthrough
**Interviewer:** Walk me through OOP in a framework you've built.

**Candidate:** (Prepare your story) "We have `BasePage` with waits, screen classes inherit locators, `DriverFactory` creates browsers, fixtures compose driver into pages, assertions stay in pytest/BDD steps, negative tests reuse `submit_login` without returning next page." Tie to this repo's `learning_project`.

---

## Quick revision: top 15 must-know (all HIGH_LIKELIHOOD)

| # | Topic |
|---|--------|
| Q1 | Four pillars + SDET examples |
| Q5 | Instance vs class attr |
| Q6 | Mutable default arg |
| Q8 | Encapsulation in Python |
| Q12 | MRO |
| Q14 | `super()` not "parent" |
| Q17–18 | Polymorphism / duck typing |
| Q22 | classmethod vs static vs instance |
| Q24 | Composition vs inheritance |
| Q26–27 | `__str__`/`__repr__`, `__eq__`/`__hash__` |
| Q31–33 | POM, assertions, BasePage split |
| Q34 | Factory |
| Q51 | Trace MRO / output questions |
| Q60 | Your framework story |

---

*Total: 60 Q&A pairs. Linked exercises in `exercises/predict_output/`.*
