import json
import math

MODEL_PARAMS_PATH = "model_params.json"


def save_params(path, theta0, theta1):
    with open(path, "w") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f, indent=2)
        f.write("\n")


def load_params(path):
    with open(path, "r") as f:
        params = json.load(f)

    if not isinstance(params, dict):
        raise ValueError("model parameters must be a JSON object")

    try:
        theta0 = float(params["theta0"])
        theta1 = float(params["theta1"])
    except (KeyError, TypeError, ValueError) as e:
        raise ValueError("invalid model parameters") from e

    if not (math.isfinite(theta0) and math.isfinite(theta1)):
        raise ValueError("model parameters must be finite numbers")

    return theta0, theta1
