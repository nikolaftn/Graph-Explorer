import unittest

from datetime import date
from graph_explorer_api.models.graph import Edge, Graph, Node
from graph_explorer_platform.graph_operations import filter_graph, search_graph


class GraphOperationsTests(unittest.TestCase):

    def setUp(self):
        self.graph = Graph({}, [], directed=True)
        self.graph.add_node(Node("a", {"name": "Ana","age": 25,"birthday": date(2001, 1, 1),}))
        self.graph.add_node(Node("b", {"name": "Anastasija", "age": 30}))
        self.graph.add_node(Node("c", {"name": "Marko"}))
        self.graph.add_edge(Edge("a", "b", {}))
        self.graph.add_edge(Edge("b", "c", {}))

    
    def test_search_by_attribute_name(self):
        result=search_graph(self.graph,"age")
        self.assertEqual(set(result.nodes),{"a","b"})
    
    def test_search_by_attribute_value_keeps_matching_edges(self):
        result = search_graph(self.graph, "Ana")
        self.assertEqual(set(result.nodes), {"a", "b"})
        self.assertEqual(
            [(edge.source_id, edge.target_id) for edge in result.edges],
            [("a", "b")],
        )
    

    def test_filter_by_age(self):
        result=filter_graph(self.graph,"age >= 30")
        self.assertEqual(set(result.nodes),{"b"})

    def test_filter_by_date(self):
        result=filter_graph(self.graph,"birthday > 2000-01-01")
        self.assertEqual(set(result.nodes),{"a"})
    
    def test_filter_rejects_invalid_input(self):
        for expression in ("age","age>= abc", "name===Ana"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    filter_graph(self.graph,expression)

    


    def test_search_after_filter(self):
        filtered = filter_graph(self.graph, "age >= 30")
        result = search_graph(filtered, "Ana")
        self.assertEqual(set(result.nodes), {"b"})
