from datetime import date

AttributeValue = int | str | float | date

class Node:
    id: str
    attributes: dict[str, AttributeValue]

    def __init__(self, node_id: str, attributes: dict[str, AttributeValue]):
        self.id = node_id
        self.attributes = attributes

class Edge:
    source_id: str
    target_id: str
    attributes: dict[str, AttributeValue]

    def __init__(self, source_id: str, target_id: str, attributes: dict[str, AttributeValue]):
        self.source_id = source_id
        self.target_id = target_id
        self.attributes = attributes

class Graph:
    nodes: dict[str, Node]
    edges: list[Edge]
    directed: bool

    def __init__(self, nodes: dict[str, Node], edges: list[Edge], directed: bool):
        self.nodes = nodes
        self.edges = edges
        self.directed = directed

    def add_node(self, node):
        if node.id in self.nodes:
            raise ValueError("Node already exists")
        self.nodes[node.id] = node

    def add_edge(self, edge):
        if edge.source_id not in self.nodes:
            raise ValueError("Source node does not exist")
        if edge.target_id not in self.nodes:
            raise ValueError("Target node does not exist")
        self.edges.append(edge)

    def get_node(self, node_id):
        return self.nodes[node_id]
