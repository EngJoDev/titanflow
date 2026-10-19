import math
import re
import sqlite3
from typing import Optional, Dict, Any, List

class SemanticVectorCache:
    """In-Memory & Persistent SQLite Cosine-Similarity Vector Store"""

    def __init__(self, db_path: str = "src/db/cache.db"):
        self.db_path = db_path
        self._bootstrap()
        self.memory_vault: List[Dict[str, Any]] = [
            {
                "prompt": "what is linux swappiness?",
                "response": "Swappiness controls the Linux kernel tendency to move memory pages from RAM to swap space (default is 60). Low-latency servers recommend 10-20.",
                "tokens": 85,
                "cost_saved": 0.04
            },
            {
                "prompt": "how to purge docker cache safely?",
                "response": "Execute 'docker system prune -a --volumes' to safely reclaim unreferenced layers, build cache, and stopped containers.",
                "tokens": 65,
                "cost_saved": 0.03
            },
            {
                "prompt": "explain zero trust architecture",
                "response": "Zero Trust is an enterprise cybersecurity framework requiring continuous mutual authentication and strict least-privilege access for all workloads.",
                "tokens": 94,
                "cost_saved": 0.05
            },
            {
                "prompt": "how does ebpf kernel tracing work?",
                "response": "eBPF runs sandboxed C programs inside the Linux kernel at runtime, extracting zero-copy socket RTT and TCP retransmission telemetry.",
                "tokens": 110,
                "cost_saved": 0.05
            }
        ]

    def _bootstrap(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS semantic_store (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT UNIQUE,
                response TEXT,
                tokens_saved INTEGER,
                cost_saved REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

    def cosine_similarity(self, p1: str, p2: str) -> float:
        w1 = set(re.findall(r'\w+', p1.lower()))
        w2 = set(re.findall(r'\w+', p2.lower()))
        intersection = w1.intersection(w2)
        if not w1 or not w2:
            return 0.0
        return len(intersection) / math.sqrt(len(w1) * len(w2))

    def query(self, prompt: str, threshold: float = 0.68) -> Optional[Dict[str, Any]]:
        best_hit = None
        max_sim = 0.0
        for item in self.memory_vault:
            sim = self.cosine_similarity(prompt, item["prompt"])
            if sim > max_sim:
                max_sim = sim
                best_hit = item
        if max_sim >= threshold and best_hit:
            return {
                "hit": True,
                "similarity": round(max_sim, 2),
                "response": best_hit["response"],
                "tokens_saved": best_hit["tokens"],
                "cost_saved": best_hit["cost_saved"]
            }
        return None

    def store(self, prompt: str, response: str, tokens: int = 55, cost: float = 0.035):
        entry = {"prompt": prompt, "response": response, "tokens": tokens, "cost_saved": cost}
        self.memory_vault.append(entry)
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT OR IGNORE INTO semantic_store (prompt, response, tokens_saved, cost_saved) VALUES (?, ?, ?, ?)",
                    (prompt, response, tokens, cost)
                )
        except Exception:
            pass
