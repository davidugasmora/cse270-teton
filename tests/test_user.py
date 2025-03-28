import pytest
import requests

def test_user_authentication_failure(requests_mock):
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }
    
    # Mock the GET request for the endpoint with the given parameters
    requests_mock.get(f"{url}?username=admin&password=admin", status_code=401, text="")

    response = requests.get(url, params=params)

    # Assert that the response status code is 401 (Unauthorized)
    assert response.status_code == 401
    # Assert that the response body is empty
    assert response.text == ""


def test_user_authentication_success_with_empty_response(requests_mock):
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the GET request with the given parameters, returning a 200 status and empty text
    requests_mock.get(f"{url}?username=admin&password=qwerty", status_code=200, text="")

    response = requests.get(url, params=params)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response body is empty
    assert response.text == ""