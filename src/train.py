import argparse
import math
import sys

from dataset import denormalize_thetas, load_data, normalize
from model import gradient_descent
from params import save_params

DEFAULT_LEARNING_RATE = 0.01
DEFAULT_ITERATIONS = 1000


def positive_float(value):
    try:
        number = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"must be a number, got {value!r}.")

    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError(
            f"must be a finite number greater than 0, got {value!r}."
        )
    return number


def positive_int(value):
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"must be an integer, got {value!r}.")

    if number <= 0:
        raise argparse.ArgumentTypeError(
            f"must be greater than 0, got {value!r}."
        )
    return number


def parse_args():
    parser = argparse.ArgumentParser(
        description="Train a linear regression model."
    )
    parser.add_argument(
        "csv_path",
        help="Path to the CSV dataset containing mileage and price data."
    )
    parser.add_argument(
        "--learning-rate",
        type=positive_float,
        default=DEFAULT_LEARNING_RATE,
        help=f"Gradient descent learning rate (default: {DEFAULT_LEARNING_RATE}).",
    )
    parser.add_argument(
        "--iterations",
        type=positive_int,
        default=DEFAULT_ITERATIONS,
        help=f"Number of gradient descent iterations (default: {DEFAULT_ITERATIONS}).",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        mileage, price = load_data(args.csv_path)
        mileage_norm, mean, std = normalize(mileage)
        theta0_norm, theta1_norm = gradient_descent(
            mileage_norm,
            price,
            args.learning_rate,
            args.iterations,
        )
        theta0, theta1 = denormalize_thetas(theta0_norm, theta1_norm, mean, std)
        save_params(theta0, theta1)
    except (OSError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print("Training complete.")
    print(f"theta0: {theta0:.4f}")
    print(f"theta1: {theta1:.4f}")


if __name__ == "__main__":
    main()
