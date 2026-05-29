# Q10 — Predict the output

class Result:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Result:{self.name}"

    def __repr__(self):
        return f"<Result name={self.name!r}>"


r = Result("login")
print(r)
print([r])

# Your prediction:


# --- ANSWERS ---
# Output: Result:login\n[<Result name='login'>]
# Why: print uses __str__; list displays elements with __repr__.
