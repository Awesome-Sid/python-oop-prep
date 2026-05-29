# Q06 — Predict the output

class Base:
    def __init__(self):
        print("Base", end=" ")


class Child(Base):
    def __init__(self):
        print("Child", end=" ")
        super().__init__()


Child()

# Your prediction:


# --- ANSWERS ---
# Output: Child Base 
# Why: Child.__init__ runs first, then super() calls Base.__init__.
