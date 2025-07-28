from github_fetcher import GithubRepoFetcher
from github_scraper import GithubRepoScraper

class GithubRepositoryService:
    def __init__(self, username):
        self.username = username
        self.api_fetcher = GithubRepoFetcher(username)
        self.scraper = GithubRepoScraper(username)

    def get_repositories(self):
        print("[INFO] Trying to fetch repositories via GitHub API...")
        repos = self.api_fetcher.get_repositories()

        if repos:
            print(f"[SUCCESS] Found {len(repos)} repositories via API.")
            return repos

        print("[WARNING] API failed or returned empty. Switching to scraping method...")
        repos = self.scraper.get_repositories()

        if repos:
            print(f"[SUCCESS] Found {len(repos)} repositories via scraping.")
        else:
            print("[ERROR] Could not fetch repositories via API or scraping.")

        return repos
