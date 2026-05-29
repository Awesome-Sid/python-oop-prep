# Q25 — Predict the output

class Suite:
    def __init__(self, tests):
        self.tests = tests

    def __bool__(self):
        return len(self.tests) > 0


empty = Suite([])
full = Suite(["a"])
print(bool(empty), bool(full))
if full:
    print("run")

# Your prediction:


# --- ANSWERS ---
# Output: False True\nrun
# Why: __bool__ defines truthiness; if full uses it.
