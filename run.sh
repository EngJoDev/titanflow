#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$DIR"

if [ -d "$DIR/venv" ]; then
    source "$DIR/venv/bin/activate"
fi

case "$1" in
    up|start)
        echo "⚡ Starting Mega-TitanFlow Polyglot Platform on http://localhost:8080..."
        python3 -m uvicorn src.engine.gateway:app --host 0.0.0.0 --port 8080 --reload
        ;;
    bench|benchmark)
        bash scripts/benchmark.sh
        ;;
    *)
        echo "Usage: ./run.sh {up|bench}"
        exit 1
        ;;
esac
