import requests
from requests import Response, RequestException


class APIClient:
    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url

    def send_request(self, request_method: str, request_url: str, request_headers=None,
                     request_body=None, raise_for_status: bool = True) -> Response:

        url = f"{self.api_base_url}{request_url}"

        try:
            response = requests.request(
                request_method,
                url,
                headers=request_headers,
                data=request_body
            )
            if raise_for_status:
                response.raise_for_status()

        except RequestException as e:
            raise APIClientError(f"Request error: {str(e)}")

        return response

    @staticmethod
    def check_response_status(response: Response, expected_status_code: int):
        if response.status_code != expected_status_code:
            raise APIClientError(f"Expected status code {expected_status_code}, but got {response.status_code}")


class APIClientError(Exception):
    def __init__(self, message):
        super().__init__(message)
