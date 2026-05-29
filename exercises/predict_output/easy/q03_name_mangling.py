# Q03 — Predict the output (or error)

class Config:
    def __init__(self):
        self.__env = "prod"

    def get_env(self):
        return self.__env


c = Config()
print(c.get_env())
print(c._Config__env)
# print(c.__env)  # uncomment mentally — what happens?

# Your prediction:


# --- ANSWERS ---
# Output: prod\nprod
# Uncommented c.__env would raise AttributeError (name mangled to _Config__env).
