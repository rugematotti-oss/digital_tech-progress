import requests
def test_connection(token: str) -> int:
    url = "https://graph.microsoft.com/v1.0/me"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:
        response = requests.get(url, headers=headers)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return -1

    