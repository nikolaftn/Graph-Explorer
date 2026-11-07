"""Interface for plugins that load data and produce graphs."""

from abc import ABC, abstractmethod
from typing import Any


class DataSourcePlugin(ABC):
    """Base class for data source plugins."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable plugin name."""
        raise NotImplementedError

    @abstractmethod
    def load(self, source: Any) -> Any:
        """Load a source and return a graph model."""
        raise NotImplementedError
