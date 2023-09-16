class PetEndpoint:
    BASE_URL = "/pet"

    CREATE_PET = f"{BASE_URL}"
    GET_PET_BY_ID = f"{BASE_URL}/{{pet_id}}"
