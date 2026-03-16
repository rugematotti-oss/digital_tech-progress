import requests
def groups_count(token: str) -> str:
    url = "https://graph.microsoft.com/v1.0/me:/groups"
    headers = {"Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return len(data.get("value", []))
    else:
        return 0
