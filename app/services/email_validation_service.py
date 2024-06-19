from app.services.api_client_service import APIClient

class EmailValidationClient(APIClient):
    def __init__(self, user_id, api_key):
        super().__init__(base_url="https://neutrinoapi.net", user_id=user_id, api_key=api_key)

    def validate(self, email):
        endpoint = "email-validate"
        params = {"email": email}
        return self._get(endpoint, params=params)



if __name__ == "__main__":
    import requests
    def main():
        # Replace with your actual Neutrino API user ID and API key
        user_id = "wrush_customer_analysis"
        api_key = "KtEOxK9tfEAtWVmhGxICJzmq9rr71wMVz1w3KFTjyGw0LKRU"

        # Initialize the client
        client = EmailValidationClient(user_id=user_id, api_key=api_key)

        # Test email validation
        test_email = "ward@gmail.com"
        try:
            result = client.validate(test_email)
            print("API Response:", result)
        except requests.exceptions.HTTPError as e:
            print("HTTP error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)


    main()
