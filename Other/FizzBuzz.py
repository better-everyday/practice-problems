# type:ignore
import time
"""
--- Description ---

For an increasing sequence of numbers starting at 0, every multiple of 3 is replaced with "Fizz", and
every mutliple of 5 is replaced with "Buzz." Multiples of both 3 and 5 are replaced with "FizzBuzz."
"""

# "Dodgy"
n = 1
while n:
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    n += 1
    time.sleep(1)
