import argparse
import math
import sys

from dataset import denormalize_thetas, load_data, normalize
from model import gradient_descent
from params import MODEL_PARAMS_PATH, save_params

DEFAULT_LEARNING_RATE = 0.01
DEFAULT_ITERATIONS = 1000


def positive_float(value):
    number = float(value)  # Errors handled by argparse

    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError(
            f"must be a finite number greater than 0, got {value!r}"
        )

    return number


def positive_int(value):
    number = int(value)  # Errors handled by argparse

    if number <= 0:
        raise argparse.ArgumentTypeError(
            f"must be greater than 0, got {value!r}"
        )

    return number


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Train a linear regression model that predicts a car's price "
            "from its mileage, and save the parameters to "
            f"{MODEL_PARAMS_PATH}."
        ),
    )

    parser.add_argument(
        "csv_path",
        help="path to the training dataset (CSV with km and price columns)",
    )
    parser.add_argument(
        "--learning-rate",
        type=positive_float,
        default=DEFAULT_LEARNING_RATE,
        help=(
            "gradient descent learning rate "
            f"(default: {DEFAULT_LEARNING_RATE})"
        ),
    )
    parser.add_argument(
        "--iterations",
        type=positive_int,
        default=DEFAULT_ITERATIONS,
        help=(
            "number of gradient descent iterations "
            f"(default: {DEFAULT_ITERATIONS})"
        ),
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
        theta0, theta1 = denormalize_thetas(
            theta0_norm,
            theta1_norm,
            mean,
            std,
        )
        save_params(theta0, theta1)
    except (OSError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print("Training complete.")
    print(f"theta0: {theta0:.4f}")
    print(f"theta1: {theta1:.4f}")


if __name__ == "__main__":
    main()
