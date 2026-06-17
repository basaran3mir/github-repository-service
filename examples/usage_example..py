from github_repo_service import GithubRepoService

def run(username):
    service = GithubRepoService(username)
    repositories = service.get_repositories()

    for repo in repositories:
        print(repo)

if __name__ == "__main__":
    run("basaran3mir")