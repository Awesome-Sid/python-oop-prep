# Q15 — Predict the output

class FakeDriver:
    def quit(self):
        print("fake quit")


class RealDriver:
    def quit(self):
        print("real quit")


def teardown(driver):
    driver.quit()


teardown(FakeDriver())
teardown(RealDriver())

# Your prediction:


# --- ANSWERS ---
# Output: fake quit\nreal quit
# Why: duck typing — teardown only needs quit().
