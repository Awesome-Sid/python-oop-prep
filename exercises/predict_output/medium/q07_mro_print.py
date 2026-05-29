# Q07 — Predict the output

class A:
    def f(self):
        return "A"


class B(A):
    def f(self):
        return "B"


class C(A):
    def f(self):
        return "C"


class D(B, C):
    pass


print(D().f())
print([c.__name__ for c in D.mro()])

# Your prediction:


# --- ANSWERS ---
# Output: B\n['D', 'B', 'C', 'A', 'object']
# Why: MRO picks B before C; B.f overrides A.f.
