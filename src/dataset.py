import csv


def load_data(path):
    mileage = []
    price = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames != ["km", "price"]:
            raise ValueError(
                f"Invalid headers: expected ['km', 'price'], got {reader.fieldnames}"
            )

        for row in reader:
            try:
                mileage.append(float(row["km"]))
                price.append(float(row["price"]))
            except (TypeError, ValueError) as e:
                raise ValueError(f"Invalid row: {row} ({e})") from e

    if not mileage:
        raise ValueError("The file contains no data.")

    return mileage, price
