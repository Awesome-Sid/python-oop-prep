# Q11 — Predict the output

class A:
    def run(self):
        print("A", end=" ")


class B(A):
    def run(self):
        print("B", end=" ")
        super().run()


class C(A):
    def run(self):
        print("C", end=" ")
        super().run()


class D(B, C):
    def run(self):
        print("D", end=" ")
        super().run()


D().run()

# Your prediction:


# --- ANSWERS ---
# Output: D B C A 
# Why: D.mro() is D,B,C,A,object — cooperative super() visits each once.
