import unittest
from unittest.mock import patch, MagicMock
from app.services.email_validation_service import EmailValidationClient
from app.services.phone_validation_service import PhoneValidationClient
from app.services.data_enrichment_service import DataEnrichmentClient

class TestAPIClient(unittest.TestCase):

    @patch('app.services.api_client_service.requests.get')
    def test_email_validation(self, mock_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'valid': True}
        mock_get.return_value = mock_response

        # Initialize the client
        client = EmailValidationClient(user_id="test_user", api_key="test_key")

        # Call the validate method
        result = client.validate("test@example.com")

        # Assertions
        mock_get.assert_called_once_with(
            "https://neutrinoapi.net/email-validate",
            headers={"User-ID": "test_user", "API-Key": "test_key"},
            params={"email": "test@example.com"}
        )
        self.assertEqual(result, {'valid': True})

    @patch('app.services.api_client_service.requests.get')
    def test_phone_validation(self, mock_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'valid': True}
        mock_get.return_value = mock_response

        # Initialize the client
        client = PhoneValidationClient(user_id="test_user", api_key="test_key")

        # Call the validate method
        result = client.validate("1234567890", country_code="US")

        # Assertions
        mock_get.assert_called_once_with(
            "https://neutrinoapi.net/phone-validate",
            headers={"User-ID": "test_user", "API-Key": "test_key"},
            params={"number": "1234567890", "country-code": "US"}
        )
        self.assertEqual(result, {'valid': True})

    @patch('app.services.api_client_service.requests.post')
    def test_data_enrichment(self, mock_post):
        # Mock the response from requests.post
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'enriched': True}
        mock_post.return_value = mock_response

        # Initialize the client
        client = DataEnrichmentClient(base_url="https://api.dataenrichment.com", api_key="test_key")

        # Call the enrich method
        data = {"name": "John Doe"}
        result = client.enrich(data)

        # Assertions
        mock_post.assert_called_once_with(
            "https://api.dataenrichment.com/enrich",
            headers={"API-Key": "test_key"},
            json=data
        )
        self.assertEqual(result, {'enriched': True})

if __name__ == '__main__':
    unittest.main()
