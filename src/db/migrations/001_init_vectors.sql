-- Migration 001: Initial Vector Store & Telemetry Tables
ALTER TABLE vector_embeddings ADD COLUMN model_origin TEXT DEFAULT 'local-llama3';
