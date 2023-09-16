
class DataForTests:

    @staticmethod
    def create_pet() -> list:
        pet_data = {
            "id": 0,
            "category": {"id": 1, "name": "banana"},
            "name": "YourPetName",
            "photoUrls": [""],
            "tags": [{"id": 0, "name": ""}],
            "status": ""
        }
        return [pet_data]

    @staticmethod
    def get_not_existing_pet() -> list:
        test_data = {
            "pet_id": 9223372036804608607,
            "response_error": {
                "code": 1,
                "type": "error",
                "message": "Pet not found"
            }
        }
        return [test_data]
