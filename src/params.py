import json

MODEL_PARAMS_PATH = "model_params.json"


def save_params(theta0, theta1):
    with open(MODEL_PARAMS_PATH, "w") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f, indent=2)
        f.write("\n")
