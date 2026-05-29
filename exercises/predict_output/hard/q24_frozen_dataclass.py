# Q24 — Predict: output or exception?

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str


u = User("standard_user")
print(u.name)
# u.name = "other"  # predict if uncommented

# Your prediction:


# --- ANSWERS ---
# Output: standard_user
# Uncommented assignment raises dataclasses.FrozenInstanceError.
