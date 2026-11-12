# Embedding Index Lag Watcher walkthrough

## Business problem

Detects vector index lag by comparing produced, indexed, and queryable embedding counts.

## Reproduce the workflow

Run `python3 index_lag.py sample_indexes.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
products ok 1.0%
docs lagging 20.0%
```

The sample supplies these fields. `index`, `produced`, `queryable`, `max_lag_pct`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
