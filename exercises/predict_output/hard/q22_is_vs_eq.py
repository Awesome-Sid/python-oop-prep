# Q22 — Predict the output

class Locator:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Locator) and self.value == other.value


a = Locator("id")
b = Locator("id")
print(a == b)
print(a is b)

# Your prediction:


# --- ANSWERS ---
# Output: True\nFalse
# Why: __eq__ compares value; is checks object identity (two separate instances).
