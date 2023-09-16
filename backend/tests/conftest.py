import os
import pytest
import json

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


@pytest.fixture(scope="session")
def test_config():
    config_file_path = os.path.join(ROOT_DIR, "config", "config.json")

    try:
        with open(config_file_path, "r") as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        pytest.fail(f"Config file not found at {config_file_path}")
    except json.JSONDecodeError:
        pytest.fail(f"Invalid JSON format in the config file at {config_file_path}")
