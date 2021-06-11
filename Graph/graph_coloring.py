from networkx import draw, Graph, coloring

def greedy_coloring(graph):
    return coloring.greedy_color(graph, strategy="largest_first")