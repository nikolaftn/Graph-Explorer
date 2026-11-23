from graph_explorer_api.models.graph import Graph
import re
from datetime import date
import operator


COMPARATORS={
    "==":operator.eq,
    "!=": operator.ne,
    ">=":operator.ge,
    "<=":operator.le,
    ">":operator.gt,
    "<":operator.lt,
}
def induced_subgraph(graph, node_ids):
    if not isinstance(node_ids, (list, tuple, set)):
        raise TypeError("node_ids must be a list, tuple, or set")

    selected_ids = set(node_ids)

    unknown_ids = selected_ids - set(graph.nodes)
    if unknown_ids:
        raise ValueError("One or more node IDs do not exist in the graph")

    selected_nodes = {}
    for node_id in selected_ids:
        selected_nodes[node_id] = graph.nodes[node_id]

    selected_edges = []
    for edge in graph.edges:
        if edge.source_id in selected_nodes and edge.target_id in selected_nodes:
            selected_edges.append(edge)

    return Graph(selected_nodes, selected_edges, graph.directed)



def search_graph(graph,query):
    node_ids=[]
    for node in graph.nodes.values():
        for attribute,value in node.attributes.items():
            if query in attribute or query in str(value):
                node_ids.append(node.id)
                break


    return induced_subgraph(graph,node_ids)


def filter_graph(graph,filter_expression):
    node_ids=[]
    match = re.fullmatch(r"\s*([^<>=!]+?)\s*(==|!=|>=|<=|>|<)\s*(.+?)\s*", filter_expression)

    if match is None or not all(part.strip() for part in match.groups()):
        raise ValueError("Invalid filter expression")
    
    attribute,comparator,raw_value=(part.strip() for part in match.groups())

    if raw_value.startswith(("<",">","=","!")):
        raise ValueError("Ivnalid filter expression")
    
    if not attribute or not raw_value:
        raise ValueError("invalid filter expression")


    compare=COMPARATORS[comparator]
    for node in graph.nodes.values():
        if attribute not in node.attributes:
            continue
        value=node.attributes[attribute]

        try:
            if isinstance(value,date):
                expected_value=date.fromisoformat(raw_value)
            else:
                expected_value=type(value)(raw_value)
        except ValueError as error:
            raise ValueError(f"Value of {raw_value} isn't valid for attribute {attribute}") from error
        
        if compare(value,expected_value):
            node_ids.append(node.id)
    
    return induced_subgraph(graph,node_ids)


