import argparse
import sys

import matplotlib.pyplot as plt

from dataset import load_data
from model import estimate_price
from params import load_params


def parse_args():
    parser = argparse.ArgumentParser(
        description="Plot a dataset and the line saved by train.py."
    )

    parser.add_argument(
        "csv_path",
        help="dataset to plot (CSV with km and price columns)",
    )

    return parser.parse_args()


def plot_fit(mileage, price, theta0, theta1):
    line_x = [min(mileage), max(mileage)]
    line_y = [estimate_price(x, theta0, theta1) for x in line_x]

    plt.scatter(mileage, price, marker="+", label="data")
    plt.plot(line_x, line_y, color="red", label="model")
    plt.xlabel("mileage (km)")
    plt.ylabel("price (€)")
    plt.legend()
    plt.show()


def main():
    args = parse_args()

    try:
        mileage, price = load_data(args.csv_path)
        theta0, theta1 = load_params()
    except (OSError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    plot_fit(mileage, price, theta0, theta1)


if __name__ == "__main__":
    main()
