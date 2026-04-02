import time
from collections import defaultdict

class AgentMonitor:
    def __init__(self):
        self.metrics = defaultdict(float)
        self.counts = defaultdict(int)

    def track_request(self):
        self.counts["total_requests"] += 1

    def track_latency(self, sec: float):
        self.metrics["last_latency"] = sec
        self.metrics["avg_latency"] = (self.metrics["avg_latency"] * self.counts["total_requests"] + sec) / (self.counts["total_requests"] + 1)

    def track_tool_use(self, tool_name: str):
        self.counts[f"tool_{tool_name}_used"] += 1

    def get_metrics(self):
        return dict(self.metrics), dict(self.counts)