# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 index_lag.py sample_indexes.csv
products ok 1.0%
docs lagging 20.0%
test_flags_lagging_index (test_index_lag.IndexLagTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
