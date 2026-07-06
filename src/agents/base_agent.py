"""Base agent class and configuration."""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional


class AgentState(Enum):
    """Enumeration of possible agent states."""

    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    ERROR = "error"
    COMPLETED = "completed"


@dataclass
class AgentConfig:
    """Configuration for agent initialization."""

    name: str
    description: str = ""
    timeout: int = 30
    max_retries: int = 3
    debug: bool = False


class Agent:
    """Base class for all agents."""

    def __init__(self, config: AgentConfig):
        """Initialize the agent with configuration.

        Args:
            config: AgentConfig instance containing agent settings.
        """
        self.config = config
        self.state = AgentState.IDLE
        self.execution_history: List[Dict[str, Any]] = []

    def initialize(self) -> None:
        """Initialize the agent resources."""
        if self.state != AgentState.IDLE:
            raise RuntimeError(
                f"Cannot initialize agent in {self.state.value} state"
            )

    def execute(self, task: str) -> Any:
        """Execute a task.

        Args:
            task: The task description or input for the agent.

        Returns:
            The result of task execution.
        """
        if self.state not in [AgentState.IDLE, AgentState.PAUSED]:
            raise RuntimeError(
                f"Cannot execute task in {self.state.value} state"
            )

        self.state = AgentState.RUNNING
        try:
            result = self._process_task(task)
            self.state = AgentState.COMPLETED
            self.execution_history.append(
                {"task": task, "result": result, "status": "success"}
            )
            return result
        except Exception as e:
            self.state = AgentState.ERROR
            self.execution_history.append(
                {"task": task, "error": str(e), "status": "failed"}
            )
            raise

    def _process_task(self, task: str) -> Any:
        """Process the task (to be overridden by subclasses).

        Args:
            task: The task to process.

        Returns:
            The task result.
        """
        return f"Processed: {task}"

    def reset(self) -> None:
        """Reset the agent to idle state."""
        self.state = AgentState.IDLE
        self.execution_history.clear()

    def get_history(self) -> List[Dict[str, Any]]:
        """Get the execution history.

        Returns:
            List of execution records.
        """
        return self.execution_history.copy()
