import requests

token = ""

headers = {"Authorization": f"token {token}"}
url = f"https://api.github.com/search/repositories?q=stars:%3E0&sort=stars&order=desc&per_page=100&page=1"
response = requests.get(url, headers=headers)

if responses.status_code == 200:
    return response.json()["items"]
else 
    raise Exception