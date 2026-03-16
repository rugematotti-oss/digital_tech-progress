import requests

def groups_dict(token: str) -> dict:
    url = "https://graph.microsoft.com/v1.0/me/memberOf"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        return {group["id"]: group["displayName"] for group in user_data.get("value", [])}
    else:
        print(f"Error: {response.status_code}")
        return {}
    
