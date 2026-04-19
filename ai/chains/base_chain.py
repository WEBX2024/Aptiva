import yaml
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_prompt(file_name: str) -> dict:
    path = os.path.join(BASE_DIR, "prompts", file_name)

    with open(path, "r") as f:
        return yaml.safe_load(f)