# _GitHub Repository Service_

**Key features**

- Fetches public repositories from a GitHub user via the GitHub REST API
- Falls back to HTML scraping when the API is unavailable or returns no data
- Clean service-based architecture with separate fetcher and scraper modules
- Minimal dependencies and easy installation

## Getting Started

This project provides a lightweight Python service for retrieving repository URLs from a GitHub user profile. It is ideal for automation scripts, reporting tools, or simple repository discovery workflows.

### Prerequisites

- Python 3.10+
- Git (optional, for cloning the repository)
- Internet access for GitHub API and HTML scraping

### Install

1. Clone the repository:

```bash
git clone https://github.com/basaran3mir/github-repository-service.git
cd github-repository-service
```

2. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the example script to fetch repositories for a GitHub user:

```bash
python examples/usage_example..py
```

Or use the service directly from your own script:

```python
from github_repo_service import GithubRepoService

service = GithubRepoService("basaran3mir")
for repo in service.get_repositories():
    print(repo)
```

## Project Structure

- `README.md` - Project documentation
- `LICENSE` - MIT license text
- `requirements.txt` - Python dependencies
- `examples/usage_example..py` - Example usage script
- `src/github_repo_service.py` - Main service orchestration class
- `src/github_repo_tools/github_repo_fetcher.py` - GitHub API fetcher implementation
- `src/github_repo_tools/github_repo_scraper.py` - HTML scraper fallback implementation

## Configuration

This project does not require a separate configuration file. The only runtime input is the GitHub username passed to `GithubRepoService`.

- `GithubRepoService(username)`
  - `username`: GitHub account name to inspect

If you want to extend the project, consider adding support for environment variables, config files, or command-line arguments.

## Development

To contribute or extend the service:

1. Create a feature branch:

```bash
git checkout -b feature/your-feature-name
```

2. Install dependencies in a virtual environment.
3. Add or update code inside `src/`.
4. Test your changes by running the example or adding unit tests.

### Recommended workflow

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python examples/usage_example..py
```

## Contributing

Contributions are welcome! Please follow these guidelines:

- Open an issue for bugs or feature requests.
- Submit pull requests with clear descriptions.
- Keep changes focused and testable.
- Adhere to the existing module structure.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contact

For questions, feature requests, or bug reports, please open an issue in this repository.
