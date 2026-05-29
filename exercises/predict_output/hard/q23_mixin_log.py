# Q23 — Predict the output

class LogMixin:
    def action(self):
        print("log", end=" ")
        return super().action()


class BasePage:
    def action(self):
        print("base", end=" ")
        return "done"


class LoginPage(LogMixin, BasePage):
    def action(self):
        print("login", end=" ")
        return super().action()


print(LoginPage().action())

# Your prediction:


# --- ANSWERS ---
# Output: login log base done
# Why: MRO LoginPage, LogMixin, BasePage, object; print() also prints return value "done".
