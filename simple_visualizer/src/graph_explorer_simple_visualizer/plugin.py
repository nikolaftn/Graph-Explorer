"""Simple visualizer scaffold."""

from graph_explorer_api.plugins.visualizer import VisualizerPlugin


class SimpleVisualizer(VisualizerPlugin):
    @property
    def name(self) -> str:
        return "Simple"

    def render(self, graph):
        raise NotImplementedError("Simple graph rendering is not implemented yet.")
