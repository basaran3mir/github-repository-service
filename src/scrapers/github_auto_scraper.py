import requests

class GithubRepoFetcher:
    def __init__(self, username):
        self.username = username
        self.url = f"https://api.github.com/users/{username}/repos"

    def get_repositories(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            print("[ERROR] Failed to retrieve data from GitHub API. Status code:", response.status_code)
            return []

        repos = response.json()
        return [repo["html_url"] for repo in repos]