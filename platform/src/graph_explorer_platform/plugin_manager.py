"""Discover and provide access to installed plugins."""

from importlib.metadata import entry_points

from graph_explorer_api.plugins.data_source import DataSourcePlugin
from graph_explorer_api.plugins.visualizer import VisualizerPlugin


class PluginManager:

    def __init__(self):
        self.data_sources: dict[str, DataSourcePlugin] = {}
        self.visualizers: dict[str, VisualizerPlugin] = {}

    def discover_plugins(self) -> None:
        self.data_sources.clear()
        self.visualizers.clear()

        for entry in entry_points(group="graph_explorer.data_sources"):
            plugin_class = entry.load()
            plugin = plugin_class()

            if isinstance(plugin, DataSourcePlugin):
                if plugin.id in self.data_sources:
                    raise ValueError(f"Duplicate data source ID: {plugin.id}")

                self.data_sources[plugin.id] = plugin

        for entry in entry_points(group="graph_explorer.visualizers"):
            plugin_class = entry.load()
            plugin = plugin_class()

            if isinstance(plugin, VisualizerPlugin):
                if plugin.id in self.visualizers:
                    raise ValueError(f"Duplicate visualizer ID: {plugin.id}")

                self.visualizers[plugin.id] = plugin

    def get_data_source(self, plugin_id: str) -> DataSourcePlugin:
        return self.data_sources[plugin_id]

    def get_visualizer(self, plugin_id: str) -> VisualizerPlugin:
        return self.visualizers[plugin_id]

    def get_data_sources(self) -> list[DataSourcePlugin]:
        return list(self.data_sources.values())

    def get_visualizers(self) -> list[VisualizerPlugin]:
        return list(self.visualizers.values())