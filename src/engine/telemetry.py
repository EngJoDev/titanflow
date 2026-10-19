class GlobalTelemetry:
    def __init__(self):
        self.requests_total = 345
        self.cache_hits = 295
        self.dollars_saved = 548.90
        self.attacks_mitigated = 38
        self.kernel_rtt_us = 1180

    def hit(self, cost: float):
        self.requests_total += 1
        self.cache_hits += 1
        self.dollars_saved += cost

    def miss(self):
        self.requests_total += 1

    def attack(self):
        self.attacks_mitigated += 1

    def snapshot(self):
        ratio = (self.cache_hits / max(1, self.requests_total)) * 100
        return {
            "total_requests": self.requests_total,
            "cache_hits": self.cache_hits,
            "hit_ratio_percent": round(ratio, 1),
            "dollars_saved": round(self.dollars_saved, 2),
            "attacks_mitigated": self.attacks_mitigated,
            "kernel_rtt_ms": round(self.kernel_rtt_us / 1000.0, 2)
        }

telemetry = GlobalTelemetry()
