import pytest as pytest

from backend.data_for_tests.data_for_test import DataForTests
from backend.utils.assertions import assert_true
from backend.utils.helper import Helper
from backend.utils.pet_api import PetApi


@pytest.mark.usefixtures("test_config")
class TestPetAPI:
    @pytest.fixture(scope="class")
    def pet_api_client(self, test_config) -> PetApi:
        return PetApi(api_base_url=Helper.get_config_value_by_name(test_config, ["base_url", "pet_api"]))

    @pytest.mark.parametrize("pet_data", DataForTests.create_pet())
    def test_create_new_pet(self,  pet_data: dict, pet_api_client: PetApi) -> None:
        response = pet_api_client.create_pet(pet_data=pet_data)
        pet_api_client.check_response_status(response, 200)
        pet_id_response = response.json().get("id")
        assert_true(pet_id_response > 0, "Error: After creating new pet the id is 0")
        Helper.validate_json_response(pet_data, response.json(), exclude_properties=["id"])

    @pytest.mark.parametrize("pet_data", DataForTests.create_pet())
    def test_get_pet(self,  pet_data: dict, pet_api_client: PetApi) -> None:
        response = pet_api_client.create_pet(pet_data=pet_data)
        pet_id_response = response.json().get("id")
        response = pet_api_client.get_pet_by_id(pet_id=pet_id_response)
        pet_api_client.check_response_status(response, 200)
        response_with_id = response.json()
        pet_data["id"] = response_with_id["id"]
        Helper.validate_json_response(pet_data, response_with_id)

    @pytest.mark.parametrize("test_data", DataForTests.get_not_existing_pet())
    def test_get_nonexistent_pet_by_id(self, test_data: dict, pet_api_client: PetApi) -> None:
        response = pet_api_client.get_pet_by_id(pet_id=test_data["pet_id"])
        pet_api_client.check_response_status(response, 404)
        Helper.validate_json_response(test_data["response_error"], response.json())
