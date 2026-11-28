"""Interface for plugins that load data and produce graphs."""

from abc import ABC, abstractmethod
from typing import Any

from graph_explorer_api.models.graph import Graph


class DataSourcePlugin(ABC):
    """Base class for data source plugins."""

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
    def load(self, source: Any) -> Graph:
        """Load a source and return a graph model."""
        raise NotImplementedError