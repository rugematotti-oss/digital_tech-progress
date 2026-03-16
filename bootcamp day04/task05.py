import requests

def team_channels(token: str, team_id: str) -> list:
    url = f"https://graph.microsoft.com/v1.0/teams/{team_id}/channels"
    headers = {"Authorization": f"Bearer {token}"
    }   

    response = requests.get(url, headers=headers)
    print(f"status code: {response.status_code}")
    if response.status_code == 200:
        user_data = response.json()
        return [channel["id"] for channel in user_data.get("value", [])]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []
    

