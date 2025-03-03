# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    "backend_url", default="http://localhost:3030"
)
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url",
    default="http://localhost:5050/",
)


def get_request(endpoint, **kwargs):
    """Send a GET request to the backend with optional query parameters."""
    params = ""

    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return None


def analyze_review_sentiments(text):
    """Retrieve sentiment analysis for a given text."""
    request_url = f"{sentiment_analyzer_url}analyze/{text}"

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected error: {err}, {type(err)}")
        print("Network exception occurred")
        return None


def post_review(data_dict):
    """Send a POST request to submit a review."""
    request_url = f"{backend_url}/insert_review"

    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return None
