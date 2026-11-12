# Embedding Index Lag Watcher architecture

Detects vector index lag by comparing produced, indexed, and queryable embedding counts.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
