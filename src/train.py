import argparse
import sys

from dataset import load_data


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

    print("Training complete.")


if __name__ == "__main__":
    main()
