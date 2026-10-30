import sys

from model import estimate_price
from params import load_params


def ask_mileage():
    raw = input("Enter a mileage (km): ")
    mileage = float(raw)

    if mileage < 0:
        raise ValueError("mileage must be positive")

    return mileage


def main():
    try:
        theta0, theta1, _ = load_params()
        mileage = ask_mileage()
    except (OSError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("\nError: input interrupted", file=sys.stderr)
        sys.exit(1)

    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price: {price:.2f}")


if __name__ == "__main__":
    main()
