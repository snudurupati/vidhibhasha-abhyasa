# Week 1: lists, slicing, comprehensions. 2026-10-17

a = [0, 1, 2, 3, 4, 5]

# 1. Every second item of a, starting from the first

result = a[::2]
assert result == [0, 2, 4]

#2. The last 3 items

result = a[-3:]
assert result == [3, 4, 5]

#3 The first 3 items

result = a[:3]
assert result == [0, 1, 2]

#4 Reverse a list (as a new list)

result = a[::-1]
assert result == [5, 4, 3, 2, 1, 0]

#5 Squares of all items

result = [x**2 for x in a]
assert result == [0, 1, 4, 9, 16, 25]

#6 Only the even items

result = [x for x in a if x % 2 == 0]
assert result == [0, 2, 4]

#7 Squares of y the even items

result = [x**2 for x in a if x % 2 ==0]
assert result == [0, 4, 16]

#8 Flatten [[1, 2], [3, 4]] into [1, 2, 3, 4]

matrix = [[1, 2], [3, 4]]
result = [x for sublist in matrix for x in sublist]
assert result == [1, 2, 3, 4]

#9 Items at odd indicies

result = [a[i] for i in range(0, len(a)) if i % 2 != 0]
assert result == [1, 3, 5]

#10 Make a copy of a list

result = a[:]
a.append(6)
assert result != [0, 1, 2, 3, 4, 5, 6]
