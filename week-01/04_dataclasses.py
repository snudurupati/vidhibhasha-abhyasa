"""
An Episode is one recording of a robot performing one task. The class must be declared with @dataclass.

It stores five values, in this order: 
episode_id as a str, 
robot as a str, 
start_ts as a float, 
frames as a list, and 
actions as a list of strings. 

Each element of frames is a dict with a key ts holding a float and a key pose holding three numbers.
It provides three methods.
frame_count returns how many frames the episode holds.
duration returns the length of the time span the frames cover, in seconds. It is the largest frame time minus the smallest frame time. It never returns a negative number.
mean_frame_interval returns the average gap between neighbouring frames, in seconds. It is the duration divided by the number of gaps. If the episode has n frames, it has n minus 1 gaps.
"""

# Using @Dataclass
from dataclasses import dataclass

@dataclass
class Episode:

    episode_id: str
    robot: str
    start_ts: float
    frames: list[dict]
    actions: list[str]

    def frame_count(self) -> int:
        return len(self.frames)

    def duration(self) -> float:
        ts = [a.get('ts') for a in self.frames]
        return max(ts) - min(ts)

    def mean_frame_interval(self) -> float:
        n = self.frame_count()
        return self.duration()/((n - 1) if n > 1 else 1)

#frame_count tests
assert Episode("e1", "arm2", 0.0, [], []).frame_count() == 0

assert Episode("e1", "arm2", 0.0, [{"ts": 0.0, "pose": [1, 2, 3]}], ["reach"]).frame_count() == 1

assert Episode("e1", "arm2", 0.0, [
    {"ts": 0.0, "pose": [1, 2, 3]},
    {"ts": 0.1, "pose": [1, 2, 3]},
    {"ts": 0.2, "pose": [1, 2, 3]},
], ["a", "b", "c"]).frame_count() == 3

assert Episode("e1", "arm2", 0.0, [
    {"ts": 0.0, "pose": [1, 2, 3]},
    {"ts": 0.1, "pose": [1, 2, 3]},
    {"ts": 0.1, "pose": [1, 2, 3]},
], ["a", "b", "c"]).frame_count() == 3

#Duration tests
assert Episode("e1", "arm2", 0.0, [{"ts": 0.0, "pose": [1, 2, 3]}], []).duration() == 0.0

assert Episode("e1", "arm2", 0.0, [
    {"ts": 0.0, "pose": [1, 2, 3]},
    {"ts": 0.1, "pose": [1, 2, 3]},
    {"ts": 0.2, "pose": [1, 2, 3]},
], []).duration() == 0.2

assert Episode("e1", "arm2", 0.0, [
    {"ts": 0.2, "pose": [1, 2, 3]},
    {"ts": 0.0, "pose": [1, 2, 3]},
    {"ts": 0.1, "pose": [1, 2, 3]},
], []).duration() == 0.2

assert Episode("e1", "arm2", 0.0, [
    {"ts": 100.0, "pose": [1, 2, 3]},
    {"ts": 0.0, "pose": [1, 2, 3]},
], []).duration() == 100.0

#mean_frame_interval tests
assert Episode("e1", "arm2", 0.0, [
    {"ts": 0.0, "pose": [1, 2, 3]},
    {"ts": 0.1, "pose": [1, 2, 3]},
    {"ts": 0.2, "pose": [1, 2, 3]},
], []).mean_frame_interval() == 0.1

assert Episode("e1", "arm2", 0.0, [
    {"ts": 0.0, "pose": [1, 2, 3]},
    {"ts": 0.3, "pose": [1, 2, 3]},
], []).mean_frame_interval() == 0.3

assert Episode("e1", "arm2", 0.0, [{"ts": 0.0, "pose": [1, 2, 3]}], []).mean_frame_interval() == 0.0