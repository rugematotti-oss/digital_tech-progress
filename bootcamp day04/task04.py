import requests

def my_teams(token: str) -> list:
    url = "https://graph.microsoft.com/v1.0/me/joinedTeams"
    headers = {"Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    print(f"status code: {response.status_code}")
    if response.status_code == 200:
        user_data = response.json()
        print(f"user data: {user_data}")
        return [team["displayName"] for team in user_data.get("value", [])]
    else:
        print(f"Error responce: {response.text}")
        return []
