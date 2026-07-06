"""Pytest configuration and fixtures for agent testing."""

import pytest

from src.agents import Agent, AgentConfig, AgentState


@pytest.fixture
def agent_config():
    """Provide a basic agent configuration."""
    return AgentConfig(
        name="TestAgent",
        description="A test agent for pytest fixtures",
        timeout=10,
        max_retries=2,
        debug=True,
    )


@pytest.fixture
def basic_agent(agent_config):
    """Provide an initialized basic agent."""
    agent = Agent(agent_config)
    agent.initialize()
    return agent


@pytest.fixture
def agent_with_history(basic_agent):
    """Provide an agent with execution history."""
    basic_agent.execute("task_1")
    basic_agent.execute("task_2")
    basic_agent.reset()
    return basic_agent


@pytest.fixture(autouse=True)
def cleanup_agents():
    """Cleanup fixture to ensure agents are properly reset."""
    yield
    # Cleanup code runs after each test


class MockAgent(Agent):
    """Mock agent for testing custom behavior."""

    def _process_task(self, task: str) -> str:
        """Override task processing for testing."""
        return f"Mock processed: {task}"


@pytest.fixture
def mock_agent(agent_config):
    """Provide a mock agent for testing."""
    agent = MockAgent(agent_config)
    agent.initialize()
    return agent
