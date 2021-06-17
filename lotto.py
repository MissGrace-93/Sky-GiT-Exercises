# Write a Python script called lotto.py that will generate
# and display 6 unique random lottery numbers between 1 and 50.
# Think about which Python data structure is best suited to store the numbers.
# Use the Python help() function to find out which function to use from the python standard
# library called random.

# help()

import random

print(random.sample(range(1,50), k=6))
print(random.sample(range(1,50), k=6))

