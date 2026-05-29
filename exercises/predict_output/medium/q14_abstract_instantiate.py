# Q14 — Predict: output or exception?

from abc import ABC, abstractmethod


class Page(ABC):
    @abstractmethod
    def load(self):
        pass


class LoginPage(Page):
    def load(self):
        return "login loaded"


print(LoginPage().load())
# p = Page()

# Your prediction for uncommented Page():


# --- ANSWERS ---
# Output: login loaded
# Page() would raise TypeError: Can't instantiate abstract class Page with abstract method load
