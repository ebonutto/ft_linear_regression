import csv


def load_data(path):
    mileage = []
    price = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames != ["km", "price"]:
            raise ValueError(
                f"invalid headers: expected ['km', 'price'], got {reader.fieldnames}"
            )

        for row in reader:
            try:
                mileage.append(float(row["km"]))
                price.append(float(row["price"]))
            except (TypeError, ValueError) as e:
                raise ValueError(f"invalid row: {row} ({e})") from e

    if not mileage:
        raise ValueError("the file contains no data")

    return mileage, price


def normalize(values):
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    std = variance ** 0.5

    if std == 0:
        raise ValueError(
            "cannot normalize: all values are identical (standard deviation is 0)"
        )

    normalized = [(x - mean) / std for x in values]
    return normalized, mean, std


def denormalize_thetas(theta0_norm, theta1_norm, mean, std):
    theta0 = theta0_norm - theta1_norm * mean / std
    theta1 = theta1_norm / std
    return theta0, theta1
