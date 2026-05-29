# Q18 — Predict the output

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = 0


a = Singleton()
a.value = 1
b = Singleton()
b.value = 2
print(a is b, a.value, b.value)

# Your prediction:


# --- ANSWERS ---
# Output: True 2 2
# Why: Same instance; __init__ runs on every "construction", so value ends as 2 on shared object.
