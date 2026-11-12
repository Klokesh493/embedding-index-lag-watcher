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

## Business problem

An embedding pipeline can report successful production while search still sees fewer queryable records than expected.

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

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 index_lag.py sample_indexes.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.
