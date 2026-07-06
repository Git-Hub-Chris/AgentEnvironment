# AgentEnvironment Architecture

## Overview

AgentEnvironment is a lightweight testing framework for agent implementations. It provides a structured base for creating, testing, and managing agent behavior.

## Core Components

### 1. Agent Base Class (`src/agents/base_agent.py`)

The `Agent` class is the foundation for all agent implementations. It provides:

- **Lifecycle Management**: Agents move through well-defined states (IDLE, RUNNING, PAUSED, ERROR, COMPLETED)
- **Task Execution**: Standardized interface for executing tasks through the `execute()` method
- **History Tracking**: Automatic recording of all task executions
- **Configuration**: Agents are configured via `AgentConfig` dataclass

#### Agent States

```
IDLE (initial state)
  ↓
execute() called
  ↓
RUNNING
  ├→ Success: COMPLETED
  └→ Error: ERROR
  ↓
reset() called
  ↓
IDLE
```

### 2. AgentConfig

Agents are configured through the `AgentConfig` dataclass:

```python
@dataclass
class AgentConfig:
    name: str              # Agent identifier
    description: str       # Human-readable description
    timeout: int          # Execution timeout in seconds
    max_retries: int      # Maximum retry attempts
    debug: bool           # Enable debug mode
```

### 3. Task Execution Flow

When `agent.execute(task)` is called:

1. **Validation**: Check if agent is in a valid execution state (IDLE or PAUSED)
2. **State Transition**: Move to RUNNING
3. **Processing**: Call `_process_task()` (overridden by subclasses)
4. **Result Handling**:
   - Success: Record in history, transition to COMPLETED
   - Error: Record error in history, transition to ERROR, re-raise exception
5. **History**: All executions are recorded for auditing

### 4. Extending Agent

To create a custom agent, extend the `Agent` base class and override `_process_task()`:

```python
from src.agents import Agent, AgentConfig

class CustomAgent(Agent):
    def _process_task(self, task: str) -> str:
        # Custom implementation
        return f"Custom: {task}"
```

## Testing Architecture

### Fixtures (`tests/conftest.py`)

The test suite provides reusable fixtures for agent testing:

- **`agent_config`**: Base configuration fixture
- **`basic_agent`**: Pre-initialized agent for common tests
- **`agent_with_history`**: Agent with pre-populated execution history
- **`mock_agent`**: MockAgent with custom task processing
- **`cleanup_agents`**: Auto-use fixture for test cleanup

### Test Organization

Tests are organized by functionality:

- **`TestAgentInitialization`**: Agent setup and configuration
- **`TestAgentExecution`**: Task execution and error handling
- **`TestAgentState`**: State transitions and lifecycle
- **`TestMockAgent`**: Custom agent implementations

## Configuration

### Pytest Configuration (`pyproject.toml`)

```toml
[tool.pytest.ini_options]
addopts = "-v --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
```

This configuration:
- Runs tests in verbose mode
- Generates coverage reports (terminal + HTML)
- Scans the `tests/` directory for test files

## Running the Application

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_agents.py -v
```

### CI/CD

GitHub Actions workflow (`.github/workflows/tests.yml`) automatically:
- Runs tests on Python 3.10, 3.11, 3.12
- Generates coverage reports
- Uploads to Codecov for tracking

## Future Enhancements

1. **Async Agent Support**: Add async task execution
2. **Middleware Pipeline**: Request/response processing hooks
3. **Agent Communication**: Inter-agent messaging
4. **Persistence**: Save/load agent state
5. **Metrics**: Built-in performance tracking
