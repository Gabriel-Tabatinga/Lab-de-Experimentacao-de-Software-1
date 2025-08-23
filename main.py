import requests

with open('token.txt', 'r') as file:
    token = file.read().strip()

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json",
    "User-Agent": "repo-fetcher/1.0"
}

base_url = "https://api.github.com/search/repositories"
params = {
    "q": "stars:>0",
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}

todos = []

for page in range(1, 11):
    params["page"] = page
    response = requests.get(base_url, headers=headers, params=params, timeout=30)

    if response.status_code != 200:
        raise Exception(f"Erro na página {page}: {response.status_code} - {response.text}")

    data = response.json()
    items = data.get("items", [])

    if not items:
        print(f"Página {page}: 0 itens. Encerrando paginação.")
        break

    todos.extend(items)
    print(f"Página {page}: {len(items)} itens (acumulado: {len(todos)})")

