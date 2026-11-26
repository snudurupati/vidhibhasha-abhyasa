#using regular class definition
class Episode_c:
    def __init__(self, episode_id: str, robot: str, start_ts: float, frames: list[dict], actions: list[str]):
        self.episode_id = episode_id
        self.robot = robot
        self.start_ts = start_ts
        self.frames = frames
        self.actions = actions

    def frame_count(self) -> int:
        return len(self.frames)

    def duration(self) -> float:
        ts = [a.get('ts') for a in self.frames]
        return max(ts) - min(ts)

    def mean_frame_interval(self) -> float:
        n = self.frame_count()
        return self.duration()/((n - 1) if n > 1 else 1)

assert Episode_c("e1", "arm2", 0.0, [{"ts": 0.0, "pose": [1, 2, 3]}], []).mean_frame_interval() == 0.0
