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
