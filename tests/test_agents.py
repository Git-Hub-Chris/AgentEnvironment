"""Tests for agent implementations."""

import pytest

from src.agents import Agent, AgentConfig, AgentState


class TestAgentInitialization:
    """Test agent initialization."""

    def test_agent_initializes_with_config(self, agent_config):
        """Test that agent initializes correctly with config."""
        agent = Agent(agent_config)
        assert agent.config.name == "TestAgent"
        assert agent.state == AgentState.IDLE

    def test_agent_initialize_method(self, basic_agent):
        """Test agent.initialize() method."""
        assert basic_agent.state == AgentState.IDLE

    def test_agent_cannot_reinitialize(self, basic_agent):
        """Test that agent cannot be reinitialized from non-idle state."""
        basic_agent.state = AgentState.RUNNING
        with pytest.raises(RuntimeError):
            basic_agent.initialize()


class TestAgentExecution:
    """Test agent task execution."""

    def test_agent_executes_task(self, basic_agent):
        """Test basic task execution."""
        result = basic_agent.execute("test_task")
        assert "test_task" in result
        assert basic_agent.state == AgentState.COMPLETED

    def test_agent_records_history(self, basic_agent):
        """Test that execution history is recorded."""
        basic_agent.execute("task_1")
        basic_agent.reset()
        basic_agent.execute("task_2")
        history = basic_agent.get_history()
        assert len(history) == 1
        assert history[0]["task"] == "task_2"

    def test_agent_cannot_execute_during_run(self, basic_agent):
        """Test that agent cannot execute during another execution."""
        basic_agent.state = AgentState.RUNNING
        with pytest.raises(RuntimeError):
            basic_agent.execute("task")

    def test_agent_error_handling(self, basic_agent):
        """Test agent error handling."""

        class FailingAgent(Agent):
            def _process_task(self, task: str):
                raise ValueError("Task failed")

        failing_agent = FailingAgent(basic_agent.config)
        failing_agent.initialize()

        with pytest.raises(ValueError):
            failing_agent.execute("failing_task")

        assert failing_agent.state == AgentState.ERROR
        history = failing_agent.get_history()
        assert history[0]["status"] == "failed"


class TestAgentState:
    """Test agent state transitions."""

    def test_state_transitions(self, basic_agent):
        """Test valid state transitions."""
        assert basic_agent.state == AgentState.IDLE
        basic_agent.state = AgentState.RUNNING
        assert basic_agent.state == AgentState.RUNNING

    def test_reset_returns_to_idle(self, basic_agent):
        """Test that reset returns agent to idle state."""
        basic_agent.execute("task")
        assert basic_agent.state == AgentState.COMPLETED
        basic_agent.reset()
        assert basic_agent.state == AgentState.IDLE

    def test_reset_clears_history(self, basic_agent):
        """Test that reset clears execution history."""
        basic_agent.execute("task_1")
        assert len(basic_agent.get_history()) == 1
        basic_agent.reset()
        assert len(basic_agent.get_history()) == 0


class TestMockAgent:
    """Test mock agent behavior."""

    def test_mock_agent_custom_processing(self, mock_agent):
        """Test that mock agent uses custom task processing."""
        result = mock_agent.execute("custom_task")
        assert "Mock processed" in result
        assert "custom_task" in result

    def test_mock_agent_history(self, mock_agent):
        """Test mock agent history tracking."""
        mock_agent.execute("task_1")
        mock_agent.execute("task_2")
        history = mock_agent.get_history()
        assert len(history) == 2
        assert all(h["status"] == "success" for h in history)
