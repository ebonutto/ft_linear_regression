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
    return float(params["theta0"]), float(params["theta1"])
