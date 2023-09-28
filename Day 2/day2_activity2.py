"""
Random password generator
----Joel Cabuyao----
"""

import random

random_number = random.randint(0, 1_000_00)

random_letters = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))

random_special_character = "".join(random.choices("!@#$%^&*()+=", k=3))

generated_password = random_letters + random_special_character + str(random_number)

print(generated_password)
