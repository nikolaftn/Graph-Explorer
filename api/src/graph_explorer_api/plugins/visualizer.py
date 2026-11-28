"""Interface for plugins that visualize graphs."""

from abc import ABC, abstractmethod

from graph_explorer_api.models.graph import Graph


class VisualizerPlugin(ABC):
    """Base class for visualizer plugins."""

    @property
    @abstractmethod
    def id(self) -> str:
        """Unique plugin identifier."""
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable plugin name."""
        raise NotImplementedError

    @abstractmethod
    def render(self, graph: Graph) -> str:
        """Render a graph as HTML."""
        raise NotImplementedError