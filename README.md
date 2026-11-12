# Embedding Index Lag Watcher

Detects vector index lag by comparing produced, indexed, and queryable embedding counts.

Focus: AI/ML platform search reliability.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 index_lag.py sample_indexes.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

```mermaid
flowchart LR
    A["Produced and queryable embedding counts"]
    B["Calculate percentage gap"]
    C{"Lag exceeds per-index limit?"}
    D["Mark index lagging"]
    E["Mark index OK"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
