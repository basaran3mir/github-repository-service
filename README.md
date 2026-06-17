# GitHub Repository Service

A lightweight Python service that retrieves a GitHub user's public repositories using the GitHub REST API, with a web scraping fallback when the API is unavailable.

## Key features

- API-first repository retrieval via GitHub REST API.
- HTML scraping fallback for repository listing when the API fails.
- Simple, reusable service interface for integration into other Python projects.
- Clean separation between API fetching and scraper implementations.
- Minimal dependencies and easy setup.

## Getting Started

Follow these instructions to set up the project locally and start retrieving GitHub repository lists.

### Prerequisites

- Python 3.10 or newer
- Git (optional, for cloning the repository)
- A terminal or command prompt

### Install

1. Clone the repository or download the source.

   ```bash
   git clone https://github.com/basaran3mir/github-repository-service.git
   cd github-repository-service
   ```

2. Create and activate a virtual environment.

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Install the required dependencies.

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

## Usage

Run the example script to fetch repositories for a GitHub username.

```bash
python examples/usage_example..py
```

Update the username in `examples/usage_example..py` or import `GithubRepoService` into your own code:

```python
from src.github_repo_service import GithubRepoService

service = GithubRepoService("your-github-username")
repos = service.get_repositories()
for repo in repos:
    print(repo)
```

## Project Structure

- `src/github_repo_service.py` � Entry point for the repository service.
- `src/github_repo_tools/github_repo_fetcher.py` � Retrieves repositories via the GitHub API.
- `src/github_repo_tools/github_repo_scraper.py` � Scrapes GitHub HTML when the API call fails.
- `src/usage_example..py` � Example script demonstrating how to use the service.
- `requirements.txt` � Python package dependencies.
- `README.md` � Project documentation.

## Configuration

This project has a minimal configuration surface.

- `GithubRepoFetcher` builds requests using `https://api.github.com/users/{username}/repos`.
- `GithubRepoScraper` scrapes the repository page at `https://github.com/{username}?tab=repositories`.

If you need custom behavior, extend `GithubRepoService` or the scraper/fetcher classes.

## Development

1. Activate the virtual environment.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Edit the source files in `src/`.
4. Test your changes by running the example script or importing the service:

```bash
python examples/usage_example..py
```

Optional: add your own unit tests and a test runner for CI integration.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Add or improve functionality.
4. Open a pull request with a clear description of your changes.

Please follow standard Python coding conventions and keep dependencies minimal.

## License

This project is available under the MIT License. See `LICENSE` for details.

## Contact

For questions, feature requests, or bug reports, please open an issue in this repository.
