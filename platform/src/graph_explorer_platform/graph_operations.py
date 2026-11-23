from graph_explorer_api.models.graph import Graph


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
        for attribute,value in node.attributes.values():
            if query in attribute or query in str(value):
                node_ids.append(node.id)
                break


    return induced_subgraph(graph,node_ids)