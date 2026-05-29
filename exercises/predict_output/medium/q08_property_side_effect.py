# Q08 — Predict the output

class Counter:
    def __init__(self):
        self._n = 0

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = value * 2


c = Counter()
c.n = 5
print(c.n)
c.n = 3
print(c.n)

# Your prediction:


# --- ANSWERS ---
# Output: 10\n6
# Why: setter stores value * 2.
