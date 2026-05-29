# Q16 — Predict the output

class A:
    def f(self):
        return 1


class B(A):
    def f(self):
        return 2 + super().f()


class C(A):
    def f(self):
        return 100


class D(B, C):
    def f(self):
        return 10 + super().f()


print(D().f())

# Your prediction:


# --- ANSWERS ---
# Output: 112
# Why: MRO is D, B, C, A. D.f → 10 + B.f → 2 + C.f → 100. C.f does not call super(), so A.f is never used.
