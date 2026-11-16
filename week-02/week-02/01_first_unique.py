"""
Week 2: Arrays and Hashing.
Problem: The First Unique Reading.

Given a stream of status codes, find the first code that appears exactly once.
Return None if no unique reading exists.

Example: [10, 20, 30, 10, 40, 20] -> 30
"""

# Task: Implement a function to identify the first unique status code in a stream.
from collections import Counter

codes = [5, 6, 7, 8]

def find_first_unique(codes):
    countdict = Counter(codes)
    print(countdict)
    for x, y in countdict.items():
        if y == 1:
            return x
    return None

# --- Test Cases ---
assert find_first_unique([10, 20, 30, 10, 40, 20]) == 30
assert find_first_unique([1, 2, 1, 2]) == None
assert find_first_unique([5, 6, 7, 8]) == 5
assert find_first_unique([]) == None