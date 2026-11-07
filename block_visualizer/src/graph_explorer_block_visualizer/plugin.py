"""Block visualizer scaffold."""

from graph_explorer_api.plugins.visualizer import VisualizerPlugin


class BlockVisualizer(VisualizerPlugin):
    @property
    def name(self) -> str:
        return "Block"

    def render(self, graph):
        raise NotImplementedError("Block graph rendering is not implemented yet.")
