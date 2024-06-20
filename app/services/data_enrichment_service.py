from app.services.api_client_service import APIClient
class DataEnrichmentClient(APIClient):
    def __init__(self, base_url, api_key):
        super().__init__(base_url=base_url, api_key=api_key)

    def validate(self, data):
        endpoint = "enrich"
        return self._post(endpoint, json=data)

    def enrich(self, data):
        return self.validate(data)
