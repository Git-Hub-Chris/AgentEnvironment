# Contributing to AgentEnvironment

Thank you for your interest in contributing to AgentEnvironment! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions within this project.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip or your preferred Python package manager

### Setup Development Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Git-Hub-Chris/AgentEnvironment.git
   cd AgentEnvironment
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   ```

## Development Workflow

### Running Tests

Run the full test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=src --cov-report=html
```

Run specific test file:
```bash
pytest tests/test_agents.py -v
```

### Code Quality

Before submitting changes, ensure:

1. **Pre-commit checks pass:**
   ```bash
   pre-commit run --all-files
   ```

2. **Tests pass:**
   ```bash
   pytest
   ```

3. **No security issues:**
   ```bash
   gitleaks detect
   ```

## Making Changes

### Creating a Branch

Create a branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/` for new features
- `fix/` for bug fixes
- `docs/` for documentation updates
- `refactor/` for refactoring

### Commit Messages

Write clear, concise commit messages:
- Use imperative mood ("add feature" not "added feature")
- Reference issues when applicable: "fix: resolve issue #123"
- Keep the first line under 50 characters

Examples:
- `feat: add agent timeout configuration`
- `fix: handle agent error states correctly`
- `docs: update setup instructions`
- `test: add fixture for mock agents`

### Testing Requirements

- All new features must include tests
- Maintain or improve code coverage (aim for >80%)
- Tests should be in the `tests/` directory
- Use pytest fixtures from `tests/conftest.py` when possible

## Project Structure

```
src/
  agents/           # Agent implementation modules
    __init__.py
    base_agent.py   # Base Agent class
tests/
  __init__.py
  conftest.py       # Pytest fixtures
  test_agents.py    # Agent tests
docs/               # Documentation
  architecture.md   # Architecture overview
pyproject.toml      # Project metadata and pytest config
requirements.txt    # Development dependencies
```

## Adding New Features

### 1. Create Agent Subclass

Extend the `Agent` base class in `src/agents/`:

```python
from src.agents import Agent, AgentConfig

class MyAgent(Agent):
    def _process_task(self, task: str) -> Any:
        # Implement custom task processing
        return result
```

### 2. Write Tests

Add tests in `tests/test_agents.py` or create a new test file:

```python
def test_my_agent_feature(agent_config):
    agent = MyAgent(agent_config)
    result = agent.execute("test_task")
    assert result == expected_value
```

### 3. Update Documentation

Update `README.md` and `docs/` as needed.

## Submitting Changes

1. **Push your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request:**
   - Write a clear PR title and description
   - Reference related issues
   - Ensure CI/CD checks pass
   - Request review from maintainers

3. **Address Review Feedback:**
   - Make requested changes
   - Re-run tests
   - Push updates (no need to close and reopen)

## Reporting Issues

Report bugs or suggest features using GitHub Issues:

1. **Check existing issues** first to avoid duplicates
2. **Provide clear reproduction steps** for bugs
3. **Include your environment** (OS, Python version, etc.)
4. **Use descriptive titles** and labels

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue or reach out to the maintainers with questions about contributing.

Thank you for helping improve AgentEnvironment! 🚀
