# GitHub Repository Service

A lightweight Python service that fetches public GitHub repositories for a given user. The service attempts to retrieve repository data via the GitHub API first and falls back to HTML scraping if the API response fails.

**Key features**

- API-first repository retrieval using the GitHub REST API.
- Automatic fallback to HTML scraping when API requests fail.
- Minimal dependency footprint.
- Easy to integrate into scripts and automation workflows.
- Provides repository URLs in a simple list format.

## Getting Started

These instructions will help you run the service locally and explore the repository fetcher.

### Prerequisites

- Python 3.10 or newer
- Internet access
- A GitHub username to query
- A virtual environment is recommended

### Install

1. Clone the repository or download the project files.
2. Create and activate a Python virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Usage

Run the example script from the project root:

```powershell
python src/usage_example..py
```

Alternatively, use the service directly in your own script:

```python
from main_service import GithubRepositoryService

service = GithubRepositoryService("basaran3mir")
repositories = service.get_repositories()
for repo in repositories:
    print(repo)
```

## Project Structure

- `src/main_service.py` - Main wrapper service that selects API or scraper retrieval.
- `src/scrapers/github_auto_scraper.py` - Fetches repository URLs from the GitHub REST API.
- `src/scrapers/github_manuel_scraper.py` - Parses a user's GitHub profile page with BeautifulSoup as a fallback.
- `src/usage_example..py` - Example entry-point script showing how to use the service.
- `requirements.txt` - Python dependency list.
- `LICENSE` - Project license.
- `README.md` - Project documentation.

## Configuration

This project is intentionally simple and does not require a separate configuration file.

- `GithubRepositoryService` is configured by passing a GitHub username.
- The API endpoint is hard-coded in `src/scrapers/github_auto_scraper.py`.
- Scraper behavior is defined in `src/scrapers/github_manuel_scraper.py`.

If you want to extend the project, you can add:

- GitHub authentication support (API token)
- configurable request timeouts
- user-selectable output formats
- pagination handling for large repository lists

## Development

To contribute or change the code:

1. Activate your virtual environment.
2. Install the dependencies.
3. Update code in `src/`.
4. Run the example or create your own script against `GithubRepositoryService`.

```powershell
python src/usage_example..py
```

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request with a clear description of the update.

If you find issues or want improvements, open an issue describing the problem or feature request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, please reach out via GitHub:

- GitHub: https://github.com/basaran3mir
