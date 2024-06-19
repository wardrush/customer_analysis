import requests
from abc import ABC, abstractmethod

class APIClient(ABC):
    def __init__(self, base_url, user_id=None, api_key=None):
        self.base_url = base_url
        self.user_id = user_id
        self.api_key = api_key

    def _get_headers(self):
        headers = {}
        if self.user_id:
            headers["User-ID"] = self.user_id
        if self.api_key:
            headers["API-Key"] = self.api_key
        return headers

    def _get(self, endpoint, params=None):
        headers = self._get_headers()
        response = requests.get(f"{self.base_url}/{endpoint}", headers=headers, params=params)
        return self._handle_response(response)

    def _post(self, endpoint, data=None, json=None):
        headers = self._get_headers()
        response = requests.post(f"{self.base_url}/{endpoint}", headers=headers, data=data, json=json)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @abstractmethod
    def validate(self, *args, **kwargs):
        pass
