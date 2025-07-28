from github_repository_service import GithubRepositoryService

def run(username):
    service = GithubRepositoryService(username)
    repositories = service.get_repositories()

    for repo in repositories:
        print(repo)

if __name__ == "__main__":
    run("basaran3mir")