import requests
def github_search(query):
    response = requests.get(
        "https://api.github.com/search/repositories",
        params={
            "q": query,
            "per_page": 5
        },
        headers={
            "Accept": "application/vnd.github+json"
        }
    )

    data = response.json()

    return [
        {
            "name": repo["full_name"],
            "description": repo["description"],
            "url": repo["html_url"],
            "stars": repo["stargazers_count"]
        }
        for repo in data.get("items", [])
    ]