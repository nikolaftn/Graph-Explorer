from graph_explorer_api.models.graph import Graph
from graph_explorer_api.plugins.visualizer import VisualizerPlugin


class DemoVisualizer(VisualizerPlugin):

    @property
    def id(self) -> str:
        return "demo"

    @property
    def name(self) -> str:
        return "Demo Visualizer"

    def render(self, graph: Graph) -> str:
        return (
            f"<h1>Demo Graph</h1>"
            f"<p>Number of nodes: {len(graph.nodes)}</p>"
            f"<p>Number of edges: {len(graph.edges)}</p>"
        )