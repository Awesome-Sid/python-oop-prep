# Q05 — Predict the output

class Driver:
    browser = "chrome"

    @classmethod
    def label(cls):
        return cls.browser

    @staticmethod
    def is_chrome(name):
        return name == "chrome"


class HeadlessDriver(Driver):
    browser = "chrome-headless"


print(Driver.label())
print(HeadlessDriver.label())
print(Driver.is_chrome("chrome"))

# Your prediction:


# --- ANSWERS ---
# Output: chrome\nchrome-headless\nTrue
# Why: classmethod receives subclass as cls; staticmethod has no cls.
