"""MRO and cooperative super() in a diamond."""


class A:
    def greet(self):
        return "A"


class B(A):
    def greet(self):
        return "B->" + super().greet()


class C(A):
    def greet(self):
        return "C->" + super().greet()


class D(B, C):
    def greet(self):
        return "D->" + super().greet()


def main():
    d = D()
    print(d.greet())
    print("MRO:", [c.__name__ for c in D.mro()])


if __name__ == "__main__":
    main()
