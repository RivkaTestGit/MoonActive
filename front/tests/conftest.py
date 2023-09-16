import json
import os

import pytest
from pytest import fixture
from front.utils.driver_manager import DriverManager

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


@fixture(autouse=True, scope="session")
def setup(test_config):
    driver = DriverManager.get_driver()
    DriverManager.maximized_window(driver)
    yield driver
    driver.quit()


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


