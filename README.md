# Embedding Index Lag Watcher

An embedding pipeline can report successful production while search still sees fewer queryable records than expected.

## What I built

I built a freshness check for vector indexes that compares produced embeddings with queryable embeddings and evaluates the percentage gap against each index's limit.

## How it works

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

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [index_lag.py](index_lag.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 index_lag.py sample_indexes.csv
```

Products is within its limit at 1%. Docs is lagging at 20%. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 index_lag.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

Use counts from the same window. A produced count of zero yields zero in this demo, so operators should check upstream activity independently.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
