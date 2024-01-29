import json
import requests

with open("config/config.json", "r") as json_config:
    config = json.load(json_config)

with open("data/request_data.json", "r") as json_request:
    request_data = json.load(json_request)

with open("data/response_data.json", "r") as json_response:
    response_data = json.load(json_response)


class TestPytestDemo:
    def test_get_method(self):
        host = config.get("host")
        get_api = config.get("getAPI")
        get_api_response_data = response_data.get("getAPI")

        response = requests.get(host + get_api)

        assert response.status_code == 200
        assert response.json() == get_api_response_data

    def test_post_method(self):
        host = config.get("host")
        post_api = config.get("getAPI")
        post_api_request_data = request_data.get("postAPI")
        post_api_response_data = response_data.get("postAPI")
        # send request
        response = requests.post(host + post_api, post_api_request_data)
        # assert
        assert response.status_code == 201
        assert response.json() == post_api_response_data
