# Q21 — Predict the output

class Page:
    def click(self):
        return "instance"


p = Page()
bound = p.click
unbound = Page.click
print(bound())
print(unbound(p))

# Your prediction:


# --- ANSWERS ---
# Output: instance\ninstance
# Why: bound method injects self; unbound function access needs explicit self.
