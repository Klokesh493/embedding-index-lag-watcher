# Skills and verification

## What this repository demonstrates

A freshness check for vector indexes that compares produced embeddings with queryable embeddings and evaluates the percentage gap against each index's limit.

## Reproduce the result

Products is within its limit at 1%. Docs is lagging at 20%. Reproduce the primary fixture with `python3 index_lag.py sample_indexes.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

Use counts from the same window. A produced count of zero yields zero in this demo, so operators should check upstream activity independently.

Check that produced and queryable counts come from the same index and time window.

[index_lag.py](../index_lag.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
