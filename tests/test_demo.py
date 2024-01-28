import requests


class TestPytestDemo:
    def test_get_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        response = requests.get(f"{base_url}/posts/1")
        assert response.status_code == 200
        assert response.json()["userId"] == 1
        assert response.json()["id"] == 1

    def test_post_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        requests_data = {"title": "point", "body": "blank", "userId": 1}

        response = requests.post(f"{base_url}/posts", requests_data)
        assert response.status_code == 201
        print(response.json())
        assert response.json()["userId"] == "1"
        assert response.json()["body"] == "blank"
