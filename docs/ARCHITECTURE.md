# Embedding Index Lag Watcher architecture

Detects vector index lag by comparing produced, indexed, and queryable embedding counts.

```mermaid
flowchart LR
    N0["sample_indexes.csv"]
    N1["index_lag.py"]
    N2["lag pct / status"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
