import csv
import sys


def lag_pct(row):
    produced = int(row["produced"])
    queryable = int(row["queryable"])
    return round((produced - queryable) / produced * 100, 2) if produced else 0


def status(row):
    return "lagging" if lag_pct(row) > float(row["max_lag_pct"]) else "ok"


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['index']} {status(row)} {lag_pct(row)}%")


if __name__ == "__main__":
    main(sys.argv[1])
