# Q02 — Predict the output

class Suite:
    def __init__(self, tests=[]):
        self.tests = tests

    def add(self, name):
        self.tests.append(name)


s1 = Suite()
s1.add("login")
s2 = Suite()
s2.add("checkout")
print(s1.tests, s2.tests)

# Your prediction:


# --- ANSWERS ---
# Output: ['login', 'checkout'] ['login', 'checkout']
# Why: Default list is created once at function definition time and shared by all instances using the default.
