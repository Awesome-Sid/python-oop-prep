# Q20 — Predict the output

class Validator:
    def __init__(self):
        self.value = 0

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, val):
        self.value = max(0, val)


class Config:
    retries = Validator()


c1 = Config()
c2 = Config()
c1.retries = -1
c2.retries = 5
print(c1.retries, c2.retries)

# Your prediction:


# --- ANSWERS ---
# Output: 5 5
# Why: retries is a data descriptor on the class; one Validator instance shared by all Config instances.
