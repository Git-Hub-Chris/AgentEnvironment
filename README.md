# Agent Environment

[![CodeQL](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/github-code-scanning/codeql)
[![Dependabot Updates](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/dependabot/dependabot-updates)
[![Dependency Graph](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/dependabot/update-graph/badge.svg)](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/dependabot/update-graph)
[![Dependency Review](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/dependency-review.yml)
[![Scorecard supply-chain security](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/scorecards.yml/badge.svg)](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/scorecards.yml)
[![Tests](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/tests.yml/badge.svg)](https://github.com/Git-Hub-Chris/AgentEnvironment/actions/workflows/tests.yml)

## Overview

**AgentEnvironment** is a lightweight Python-based testing environment designed to validate and experiment with agent implementations. Created as an active development project, it provides a minimal, secure sandbox for iterating on agent behavior and testing strategies.

## Stack

- **Language:** Python
- **Testing Framework:** pytest
- **Code Quality Tools:** pre-commit hooks with gitleaks (secret scanning), end-of-file fixer, trailing-whitespace remover
- **CI/CD:** GitHub Actions with CodeQL, Dependabot, SBOM scorecard, and dependency review

## Project Structure

```
.github/                  GitHub Actions workflows and configs
test_example.py           Basic pytest suite with sanity tests
.pre-commit-config.yaml   Pre-commit hooks configuration
README.md                 Project documentation
LICENSE                   MIT License
```

## How It Works

This is a minimal, bootstrapped testing framework. Tests run via pytest, with security gates managed through pre-commit hooks and GitHub Actions. The setup is designed as a sandbox for iterating on agent implementations.

## Getting Started

### Prerequisites

- **Python 3.8+** installed on your system
- **pip** (comes with Python)
- **Git** for cloning the repository

### Installation (Optional)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Git-Hub-Chris/AgentEnvironment.git
   cd AgentEnvironment
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

Execute the test suite using pytest:

```bash
pytest test_example.py
```

For verbose output with detailed test information:

```bash
pytest test_example.py -v
```

For running tests with coverage:

```bash
pytest test_example.py --cov
```

### Setting Up Pre-commit Hooks

Pre-commit hooks automatically run security checks and code formatting on each commit:

1. **Install pre-commit:**
   ```bash
   pip install pre-commit
   ```

2. **Install the git hook scripts:**
   ```bash
   pre-commit install
   ```

3. **Run hooks manually (optional):**
   ```bash
   pre-commit run --all-files
   ```

Hooks will now automatically run on `git commit`. This includes:
- **gitleaks:** Secret detection
- **trailing-whitespace:** Whitespace cleanup
- **end-of-file-fixer:** File formatting

### Next Steps

- Review `test_example.py` to understand the test structure
- Modify or add your own tests for agent implementations
- Push to GitHub to trigger CI/CD workflows

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
