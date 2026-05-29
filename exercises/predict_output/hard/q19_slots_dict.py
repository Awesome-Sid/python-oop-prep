# Q19 — Predict: output or exception?

class SlotPage:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name


p = SlotPage("login")
print(p.name)
# p.url = "/"  # predict if uncommented

# Your prediction:


# --- ANSWERS ---
# Output: login
# Uncommented p.url = "/" raises AttributeError: no '__dict__' and no 'url' slot.
