"""
Week 2: Arrays and Hashing.
Problem: The First Unique Reading.

Given a stream of status codes, find the first code that appears exactly once.
Return None if no unique reading exists.

Example: [10, 20, 30, 10, 40, 20] -> 30
"""

# Task: Implement a function to identify the first unique status code in a stream.
from collections import Counter, defaultdict

codes = [5, 6, 7, 8]

def find_first_unique(codes):
    countdict = Counter(codes)
    for x, y in countdict.items():
        if y == 1:
            return x
    return None

# --- Test Cases ---
assert find_first_unique([10, 20, 30, 10, 40, 20]) == 30
assert find_first_unique([1, 2, 1, 2]) == None
assert find_first_unique([5, 6, 7, 8]) == 5
assert find_first_unique([]) == None

def longest_sequence(codes):
    dd = defaultdict(int)
    st = 0
    longest = 0
    for n in range(len(codes)):
        if codes[n] in dd.keys():
            st = max(st, dd[codes[n]] + 1)
        dd[codes[n]] = n
    longest = (n - st) + 1
    
    return longest

assert longest_sequence(['A', 'B', 'C']) == 3
assert longest_sequence(['A', 'B', 'C'])	== 3	            #Sanity check: All distinct.
assert longest_sequence(['A', 'A', 'A'])	== 1	            #Minimum: All identical.
assert longest_sequence(['A', 'B', 'A', 'C']) == 3	            #Basic repeat: Forces a small shift.
assert longest_sequence(['A', 'B', 'C', 'A', 'D', 'B']) == 4	#The "Ghost": Tests if you handle repeats that occurred before the current start.
assert longest_sequence(['A', 'B', 'A', 'B', 'A'])	== 2	    #Oscillation: Constant shifting.
assert longest_sequence(['A', 'B', 'C', 'D', 'E', 'A'])	== 5    #Boundary: Repeat happens at the very end of a long sequence.
