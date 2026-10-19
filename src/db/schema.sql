-- TitanFlow Enterprise Production Schema
CREATE TABLE IF NOT EXISTS vector_embeddings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt_hash TEXT UNIQUE NOT NULL,
    prompt_text TEXT NOT NULL,
    response_text TEXT NOT NULL,
    embedding_blob BLOB,
    tokens_saved INTEGER DEFAULT 0,
    cost_saved_usd REAL DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL, -- CACHE_HIT, CACHE_MISS, ATTACK_BLOCKED, PII_REDACTED
    latency_ms REAL NOT NULL,
    client_ip TEXT DEFAULT '127.0.0.1',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_prompt_hash ON vector_embeddings(prompt_hash);
