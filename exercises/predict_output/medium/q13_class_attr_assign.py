# Q13 — Predict the output

class A:
    x = 1


class B(A):
    pass


b = B()
b.x = 2
print(A.x, B.x, b.x)
B.x = 3
print(A.x, B.x, b.x)

# Your prediction:


# --- ANSWERS ---
# Output: 1 1 2 then 1 3 2
# Why: b.x=2 is instance attr; B.x=3 sets class attr on B, b still has own x=2.
