import argparse
import sys

from dataset import load_data
from model import gradient_descent


def parse_args():
    parser = argparse.ArgumentParser(
        description="Train a linear regression model."
    )
    parser.add_argument("csv_path", help="Path to the training dataset.")
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        mileage, price = load_data(args.csv_path)
    except (OSError, ValueError) as e:
        print(f"Error loading data: {e}", file=sys.stderr)
        sys.exit(1)

    theta0, theta1 = gradient_descent(mileage, price, 1000, 0.01)

    print("Training complete.")
    print(f"theta0: {theta0:.4f}")
    print(f"theta1: {theta1:.4f}")


if __name__ == "__main__":
    main()
