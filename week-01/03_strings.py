"""
Week 1: Strings: reverse words, palindrome, log line parsing

Problem 1: reverse the words in a sensor log message.


"grasp lift drop"        -> "drop lift grasp"
"robot"                  -> "robot"
""                       -> ""
"  robot   arm "         -> "arm robot"
"pick, place, lift"      -> "lift place, pick,"
"""
def word_reverse(line: str) -> str:
    return " ".join(reversed(line.split()))

assert word_reverse("grasp lift drop") == "drop lift grasp"
assert word_reverse("robot") == "robot"
assert word_reverse("") == ""
assert word_reverse("  robot   arm ") == "arm robot"
assert word_reverse("pick, place, lift") == "lift place, pick,"

"""
Problem 2

Task: decide if a sensor message is a palindrome.

Rules: ignore letter case. Ignore characters that are not letters or digits.

Test cases:

"RaceCar"    -> True
"grasp"      -> False
""           -> True
"ab"         -> False
"@!#$RaceCar"-> True
"""

def is_palindrome(word: str) -> bool:
    ln = len(word)
    i = 0
    result = False
    while i < len(word):
        r = i
        l = ln-1
        right = word[r]
        left = word[l]
        
        if right.isalnum() == False:
            i += 1
            continue
        if left.isalnum() == False:
            ln -= 1
            continue
        if right.lower() != left.lower():
            return False
        i += 1
        ln -= 1
    return True

assert is_palindrome("@!#$RaceCar") == True
assert is_palindrome("ab") == False
assert is_palindrome("grasp") == False
assert is_palindrome("RaceCar") == True
assert is_palindrome("12") == False
assert is_palindrome("1!2") == False
assert is_palindrome("") == True
assert is_palindrome("12321") == True
assert is_palindrome("1a") == False
is_palindrome("!!") == True