import json
import math

MODEL_PARAMS_PATH = "model_params.json"


def save_params(theta0, theta1, cost_history, path=MODEL_PARAMS_PATH):
    with open(path, "w") as f:
        json.dump(
            {
                "theta0": theta0,
                "theta1": theta1,
                "cost_history": cost_history
            },
            f,
            indent=2,
        )
        f.write("\n")


def load_params(path=MODEL_PARAMS_PATH):
    with open(path, "r") as f:
        params = json.load(f)  # JSONDecodeError handled by ValueError

    if not isinstance(params, dict):
        raise ValueError("model parameters must be a JSON object")

    try:
        theta0 = float(params["theta0"])
        theta1 = float(params["theta1"])
        cost_history = [float(cost) for cost in params["cost_history"]]
    except (KeyError, TypeError, ValueError) as e:
        raise ValueError("invalid model parameters") from e

    if not (math.isfinite(theta0) and math.isfinite(theta1)):
        raise ValueError("theta0 and theta1 must be finite numbers")

    return theta0, theta1, cost_history
