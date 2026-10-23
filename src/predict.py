import sys

from params import MODEL_PARAMS_PATH, load_params
from model import estimate_price


def ask_mileage():
    raw = input("Enter a mileage (km): ")
    mileage = float(raw)

    if mileage < 0:
        raise ValueError("mileage must be positive")
    return mileage


def main():
    try:
        theta0, theta1 = load_params(MODEL_PARAMS_PATH)
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
