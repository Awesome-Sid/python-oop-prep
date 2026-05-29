"""Classes, objects, __init__, and method binding."""


class TestCase:
    """Minimal test metadata — mirrors how you might model a test in a runner."""

    def __init__(self, name: str):
        self.name = name
        self.status = "pending"

    def run(self):
        self.status = "passed"
        return f"{self.name}: {self.status}"


def main():
    tc = TestCase("test_login_valid_user")
    print(tc.run())
    print("class:", TestCase)
    print("instance class:", tc.__class__)
    print("same class?", isinstance(tc, TestCase))
    # Bound method: tc.run — self is tc
    bound = tc.run
    print("bound method:", bound)
    print("call bound:", bound())


if __name__ == "__main__":
    main()
