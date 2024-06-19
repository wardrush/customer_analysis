from app.services.api_client_service import APIClient

class PhoneValidationClient(APIClient):
    def __init__(self, user_id, api_key):
        super().__init__(base_url="https://neutrinoapi.net", user_id=user_id, api_key=api_key)

    def validate(self, phone_number, country_code=None):
        endpoint = "phone-validate"
        params = {"number": phone_number}
        if country_code:
            params["country-code"] = country_code
        return self._get(endpoint, params=params)



if __name__ == "__main__":
    import requests
    def main():
        # Replace with your actual Neutrino API user ID and API key
        user_id = "wrush_customer_analysis"
        api_key = "KtEOxK9tfEAtWVmhGxICJzmq9rr71wMVz1w3KFTjyGw0LKRU"

        # Initialize the client
        client = PhoneValidationClient(user_id=user_id, api_key=api_key)

        # Test phone validation
        test_phone_number = "2145025253"
        test_country_code = "US"  # Optional: specify the country code
        try:
            result = client.validate(test_phone_number, test_country_code)
            print("API Response:", result)
        except requests.exceptions.HTTPError as e:
            print("HTTP error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)


    main()
