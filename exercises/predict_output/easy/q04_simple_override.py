# Q04 — Predict the output

class A:
    def who(self):
        return "A"


class B(A):
    def who(self):
        return "B"


class C(B):
    pass


print(C().who())
print(A().who())

# Your prediction:


# --- ANSWERS ---
# Output: B\nA
# Why: C inherits who from B; B overrides A.
