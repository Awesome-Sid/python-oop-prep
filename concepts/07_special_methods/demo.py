"""__str__, __repr__, __eq__, __hash__."""


class TestResult:
    def __init__(self, name: str, passed: bool):
        self.name = name
        self.passed = passed

    def __repr__(self) -> str:
        return f"TestResult(name={self.name!r}, passed={self.passed!r})"

    def __str__(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        return f"{self.name}: {status}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TestResult):
            return NotImplemented
        return self.name == other.name and self.passed == other.passed


def main():
    a = TestResult("login", True)
    b = TestResult("login", True)
    print("str:", str(a))
    print("repr:", repr(a))
    print("equal?", a == b)
    # After __eq__ without __hash__: unhashable
    try:
        {a}
    except TypeError as e:
        print("set error:", e)


if __name__ == "__main__":
    main()
