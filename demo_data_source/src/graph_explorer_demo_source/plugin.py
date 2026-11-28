from typing import Any

from graph_explorer_api.models.graph import Graph, Node, Edge
from graph_explorer_api.plugins.data_source import DataSourcePlugin


class DemoDataSource(DataSourcePlugin):

    @property
    def id(self) -> str:
        return "demo"

    @property
    def name(self) -> str:
        return "Demo Data Source"

    def load(self, source: Any) -> Graph:
        graph = Graph({}, [], directed=True)

        graph.add_node(Node("1", {"name": "Ana", "age": 20}))
        graph.add_node(Node("2", {"name": "Marko", "age": 22}))
        graph.add_node(Node("3", {"name": "Petar", "age": 25}))

        graph.add_edge(Edge("1", "2", {}))
        graph.add_edge(Edge("2", "3", {}))

        return graph