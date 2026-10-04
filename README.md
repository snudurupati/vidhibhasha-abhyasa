# robotics-coding-reps

Daily coding practice. One hour a day, Mon to Sat, October to December 2026.

## Why

I'm a data engineer moving into robotics data. Earlier this year I made it through several interview rounds at a robotics company and then got stopped at live coding. I could manipulate a billion rows of data in my sleep, but writing a linked list from scratch while someone watched was a different muscle, and that muscle had gone soft.

So this is the gym. Same as lifting, nothing fancy, just reps, every day.

## Rules

1. No AI and no autocomplete during the hour
2. 40 minutes to solve, 20 to review
3. Talk out loud, because that's the actual interview skill
4. Stuck at 25 minutes: read a solution, then re-solve it from memory the next day
5. Log every day in [LOG.md](LOG.md), including the bad ones

## Layout

```
week-01/
  01_lists_and_slicing.py
  02_dicts_and_sets.py
  ...
```

One file per problem. The solution on top, `assert` tests at the bottom. Run any file with `python week-01/01_lists_and_slicing.py`. No output means it passed.

## The plan

| Weeks | Focus |
|---|---|
| 1 | Python by hand |
| 2 to 4 | Arrays, hashing, two pointers, stacks, queues, linked lists, sliding window, binary search |
| 5 to 6 | Trees, recursion, graphs, heaps, A* on a grid |
| 7 to 8 | numpy, rotations, quaternions, kinematics |
| 9 | Sensor data: timestamp alignment, ring buffers, producer-consumer |
| 10 to 11 | Dynamic programming, system design for a robot data platform |
| 12 | PyTorch from scratch |
| 13 | Timed mock interviews |

Some problems are standard interview fare. Others are robotics flavored, like finding the nearest timestamp in a sensor stream, because that's the kind of question I want to be ready for.

## What this is not

These are practice solutions, not reference solutions. Some will be clumsy, some will be slow, a few will be wrong at first. That's the point.
