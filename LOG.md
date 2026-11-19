# Log

| Date | Problem | Time | What tripped me |
|---|---|---|---|
| 2026-11-14 | First Unique Reading (Week 2) | ~1h | Confused Counter vs Grouping; forgotten `.items()` for efficient key-value iteration. |
| 2026-11-18 | Reverse Words (Week 1 backfill) | ~25 min | Predicted the wrong output for `split(" ")`. It leaves empty strings, not spaces. Also did not know `[::-1]` allocates a second list of `k` pointers. |
| 2026-11-18 | Valid Palindrome (Week 1 backfill) | ~75 min | Did not know `isalnum()`. `isalpha()` silently drops digits, so digits never got compared. Then a `result` flag made the failing case pass for the wrong reason and hid the bug. |

## Review queue

- Big-O: the coach drops constants. The user read "O(n)" as "costs nothing". Fix: always say the real constant out loud, then the class.
- Memory model: the user does not track how many objects exist at one moment. Drills: `[::-1]` versus `reverse()` versus `reversed()`.
- Unknown: iterators and generators. Scheduled for Day 3.
- Habit: the user states an output without running it. Every claim goes through an assert.
- Day overran the 40 minute block by about an hour. The O(1) two-pointer variant was the cause. Rule set: ship the simple correct version, then offer the optimization.

