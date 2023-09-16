import json
from typing import Dict

from backend.endpoints.pet_endpoint import PetEndpoint
from backend.utils.api_client import APIClient


class PetApi(APIClient):
    def __init__(self, api_base_url):
        super().__init__(api_base_url)

    def create_pet(self, pet_data):
        return self.send_request(request_method="POST", request_url=PetEndpoint.CREATE_PET,
                                 request_body=json.dumps(pet_data),
                                 request_headers=self.get_basic_headers())

    def get_pet_by_id(self, pet_id):
        return self.send_request(request_method="GET",
                                 request_url=PetEndpoint.GET_PET_BY_ID.format(pet_id=pet_id),
                                 request_headers=self.get_basic_headers(), raise_for_status=False)

    @staticmethod
    def get_basic_headers() -> Dict[str, str]:
        return {
            'Content-Type': 'application/json'
        }

