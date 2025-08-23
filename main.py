import requests

with open('token.txt', 'r') as file:
    token = file.read().strip()

headers = {"Authorization": f"token {token}"}
url = f"https://api.github.com/search/repositories?q=stars:%3E0&sort=stars&order=desc&per_page=100&page=1"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()["items"]
else: 
    raise Exception

print(data)