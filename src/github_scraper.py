import requests
from bs4 import BeautifulSoup

class GithubRepoScraper:
    def __init__(self, username):
        self.username = username
        self.URL = f"https://github.com/{username}?tab=repositories"
        self.page = requests.get(self.URL)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def get_repositories(self):
        repositories = []

        try:
            repository_list = self.soup.find(id="user-repositories-list")
            if not repository_list:
                raise ValueError("Repository list not found. Content might be loaded via JavaScript.")

            links = repository_list.find_all("a", itemprop="name codeRepository")

            for link in links:
                href = link.get("href")
                if href and href.startswith(f"/{self.username}/"):
                    repositories.append(f"https://github.com{href}")

        except Exception as e:
            print(f"[HATA] Data could not received: {e}")

        return repositories