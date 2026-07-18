import unittest

from index_lag import status


class IndexLagTest(unittest.TestCase):
    def test_flags_lagging_index(self):
        row = {"index": "docs", "produced": "50000", "queryable": "40000", "max_lag_pct": "5"}
        self.assertEqual(status(row), "lagging")


if __name__ == "__main__":
    unittest.main()
