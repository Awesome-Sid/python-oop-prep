# Q17 — Predict the output

class A:
    def go(self):
        print("A", end=" ")


class B(A):
    def go(self):
        print("B", end=" ")
        super().go()


class C(A):
    def go(self):
        print("C", end=" ")
        super().go()


class D(B, C):
    def go(self):
        print("D", end=" ")
        super().go()


D().go()

# Your prediction:


# --- ANSWERS ---
# Output: D B C A 
# Why: Cooperative super() along MRO D,B,C,A,object — each go() called once.
