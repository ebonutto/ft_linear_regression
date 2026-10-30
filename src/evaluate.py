import argparse
import sys

from dataset import load_data
from model import estimate_price
from params import load_params


def calculate_r2(mileage, prices, theta0, theta1):
    mean_price = sum(prices) / len(prices)
    total_sum_of_squares = sum((price - mean_price) ** 2 for price in prices)

    if total_sum_of_squares == 0:
        raise ValueError("cannot calculate R²: all prices are identical")

    residual_sum_of_squares = sum(
        (price - estimate_price(km, theta0, theta1)) ** 2
        for km, price in zip(mileage, prices)
    )

    return 1 - residual_sum_of_squares / total_sum_of_squares


def calculate_mae(mileage, prices, theta0, theta1):
    errors = [
        abs(price - estimate_price(km, theta0, theta1))
        for km, price in zip(mileage, prices)
    ]

    return sum(errors) / len(errors)


def calculate_rmse(mileage, prices, theta0, theta1):
    squared_errors = [
        (price - estimate_price(km, theta0, theta1)) ** 2
        for km, price in zip(mileage, prices)
    ]

    return (sum(squared_errors) / len(squared_errors)) ** 0.5


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate the model saved by train.py on a dataset: "
            "print the R² score, and the MAE and RMSE in price units."
        ),
    )

    parser.add_argument(
        "csv_path",
        help="dataset to evaluate on (CSV with km and price columns)",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    try:
        mileage, prices = load_data(args.csv_path)
        theta0, theta1 = load_params()

        r2 = calculate_r2(mileage, prices, theta0, theta1)
        mae = calculate_mae(mileage, prices, theta0, theta1)
        rmse = calculate_rmse(mileage, prices, theta0, theta1)
    except (OSError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"R²:   {r2:.4f} ({r2 * 100:.2f}%)")
    print(f"MAE:  {mae:.2f} €")
    print(f"RMSE: {rmse:.2f} €")


if __name__ == "__main__":
    main()
