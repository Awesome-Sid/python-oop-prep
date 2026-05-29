# Q01 — Predict the output (do not run until you answer)

class Page:
    timeout = 10


p1 = Page()
p2 = Page()
p1.timeout = 20
print(Page.timeout, p1.timeout, p2.timeout)

# Your prediction:


# --- ANSWERS ---
# Output: 10 20 10
# Why: p1.timeout = 20 creates an instance attribute on p1 only. Class attr Page.timeout stays 10; p2 still reads class attr.
