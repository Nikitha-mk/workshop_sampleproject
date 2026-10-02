import csv
from pathlib import Path
from statistics import mean, median, mode, quantiles, stdev, variance


DATA_FILE = Path(__file__).with_name("scores.csv")


def main() -> None:
    with DATA_FILE.open(newline="", encoding="utf-8") as csv_file:
        scores = [float(row["score"]) for row in csv.DictReader(csv_file)]

    first_quartile, _, third_quartile = quantiles(scores, n=4, method="inclusive")

    print(f"Number of scores: {len(scores)}")
    print(f"Mean: {mean(scores):.2f}")
    print(f"Median: {median(scores):.2f}")
    print(f"Mode: {mode(scores):.2f}")
    print(f"Minimum: {min(scores):.2f}")
    print(f"Maximum: {max(scores):.2f}")
    print(f"Range: {max(scores) - min(scores):.2f}")
    print(f"First quartile (Q1): {first_quartile:.2f}")
    print(f"Third quartile (Q3): {third_quartile:.2f}")
    print(f"Sample variance: {variance(scores):.2f}")
    print(f"Sample standard deviation: {stdev(scores):.2f}")


if __name__ == "__main__":
    main()