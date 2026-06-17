import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(root_dir, "src"))

from github_repo_service import GithubRepoService

def run(username):
    service = GithubRepoService(username)
    repositories = service.get_repositories()

    for repo in repositories:
        print(repo)

if __name__ == "__main__":
    run("basaran3mir")