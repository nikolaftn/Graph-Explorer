"""Interface for plugins that render graphs."""

from abc import ABC, abstractmethod
from typing import Any


class VisualizerPlugin(ABC):
    """Base class for graph visualizer plugins."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable plugin name."""
        raise NotImplementedError

    @abstractmethod
    def render(self, graph: Any) -> Any:
        """Render a graph using this visualizer."""
        raise NotImplementedError
