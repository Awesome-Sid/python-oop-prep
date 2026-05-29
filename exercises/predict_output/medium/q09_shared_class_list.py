# Q09 — Predict the output

class Page:
    errors = []

    def add_error(self, msg):
        self.errors.append(msg)


p1 = Page()
p2 = Page()
p1.add_error("timeout")
p2.add_error("stale")
print(p1.errors is p2.errors)
print(Page.errors)

# Your prediction:


# --- ANSWERS ---
# Output: True\n['timeout', 'stale']
# Why: errors is a class-level list; all instances share the same list object.
