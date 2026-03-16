import requests
def my_mail(token: str) -> str:
    url = "https://graph.microsoft.com/v1.0/me"
    headers = {"Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get("mail") or ("user email not found")
    else:
        return f"Error: {response.status_code}"
    
