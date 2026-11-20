# Log

| Date | Problem | Time | What tripped me |
|---|---|---|---|
| 2026-11-14 | First Unique Reading (Week 2) | ~1h | Confused Counter vs Grouping; forgotten `.items()` for efficient key-value iteration. |
| 2026-11-18 | Reverse Words (Week 1 backfill) | ~25 min | Predicted the wrong output for `split(" ")`. It leaves empty strings, not spaces. Also did not know `[::-1]` allocates a second list of `k` pointers. |
| 2026-11-18 | Valid Palindrome (Week 1 backfill) | ~75 min | Did not know `isalnum()`. `isalpha()` silently drops digits, so digits never got compared. Then a `result` flag made the failing case pass for the wrong reason and hid the bug. |
| 2026-11-19 | Episode class (Week 1 backfill, Day 2) | ~90 min active | Called `sorted` O(n), it is O(n log n). Called the mean of gaps equal to the mean of the values, so a one-frame episode returned `0.0`. Never used a decorator or `@dataclass`, so the `@dataclass` conversion is still open. |

## Review queue

- Big-O: the coach drops constants. The user read "O(n)" as "costs nothing". Fix: always say the real constant out loud, then the class.
- Memory model: the user does not track how many objects exist at one moment. Drills: `[::-1]` versus `reverse()` versus `reversed()`.
- Sorting cost: `sorted` is O(n log n) and O(n) extra. The user reached for it by default and did not price it. `max` minus `min` beat it twice in one problem.
- Aggregation semantics: the user conflated the mean of a set with the mean of consecutive differences. Redefine the quantity before choosing the formula.
- Python gaps found today: no exposure to decorators, `@dataclass`, the ternary `x if c else y`, or the `or` coalesce falsy trap.
- Still open from Day 1: iterators and generators. Scheduled for Day 3.
- Habit: the user states an output without running it. Every claim goes through an assert.
- Habit: the user skips asserts the coach marks "your call", so those paths ship untested. Coach must set the expected value, not defer it.
- Day overran the 40 minute block both days. The O(1) two-pointer variant caused Day 1. The decorator detour caused Day 2. Coach keeps detours off the critical path.
- The user does not like elementary analogies or Scala comparisons, and wants plain complete sentences with no fragment headings.

## Open for tomorrow

- Convert `Episode` to `@dataclass` and delete the hand written `__init__`.
- Then Day 3: iterators and generators, stream a large CSV in chunks.

