import math
import networkx as nx
from networkx.algorithms import approximation as ax

def length(point1, point2):
    diff_x = point1[0] - point2[0]
    diff_y = point1[1] - point2[1]
    return math.sqrt(diff_x ** 2 + diff_y ** 2)


def get_graph(nodes, connectivity_range):
    """Connects all nodes in nodes if they are within connectivity_range of each other"""
    graph = nx.Graph()

    # add all nodes to the graph
    for node in nodes:
        graph.add_node((node[0], node[1]))

    # Checks all nodes with all other nodes later in the list (to prevent double counting)
    for i in range(len(nodes)):
        for j in range(len(nodes) - i):
            if connectivity_range > length(nodes[i], nodes[i+j]):
                graph.add_edge((nodes[i][0], nodes[i][1]), (nodes[i+j][0], nodes[i+j][1]))
    return graph


def solve_steiner_tree(graph, terminal_nodes):
    """Solve the steiner tree problem with networkx"""
    term_nodes_as_tuples = []
    for node in terminal_nodes:
        term_nodes_as_tuples += [(node[0], node[1])]
    return ax.steinertree.steiner_tree(graph, term_nodes_as_tuples, weight='length')
