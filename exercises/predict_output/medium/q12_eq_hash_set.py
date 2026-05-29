# Q12 — Predict what happens (output or exception)

class Tag:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Tag) and self.name == other.name


t1 = Tag("smoke")
t2 = Tag("smoke")
print(t1 == t2)
s = {t1, t2}
print(len(s))

# Your prediction:


# --- ANSWERS ---
# Output: True then TypeError: unhashable type: 'Tag'
# Why: Defining __eq__ without __hash__ sets __hash__ to None in Python 3.
