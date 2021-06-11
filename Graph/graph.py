from networkx import draw, Graph, coloring
from pylab import show

from graph_coloring import greedy_coloring
#
g = Graph()
ggg = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


def get_index_zero_in_row(matrix_adj, index_row):
    index = -1
    for i in range(len(matrix_adj[0])-1):
        if matrix_adj[index_row][i] == 0:
            index = i
            break
    return index


def coloring_by_manapulating_rows(matrix_adj):
    for i in range(len(matrix_adj[0])-1):
        for j in range(len(matrix_adj[0])-1):
            if i == j:
                matrix_adj[i][j] = 1

    available_rows = [True for x in range(len(matrix_adj[0])-1)]
    colors = [-1 for x in range(len(matrix_adj[0])-1)]
    color = 0
    continye_cycle = True

    for i in range(len(matrix_adj[0])-1):
        if available_rows[i]:
            while 0 in matrix_adj[i] and continye_cycle:
                j = get_index_zero_in_row(matrix_adj, i)
                if available_rows[j]:
                    for k in range(len(matrix_adj[0])-1):
                        if matrix_adj[i][k] == 1 and matrix_adj[j][k] == 1:
                            matrix_adj[i][k] = 1
                        else:
                            matrix_adj[i][k] = matrix_adj[i][k] + matrix_adj[j][k]
                    available_rows[j] = False
                    colors[j] = color
                else:
                    continye_cycle = False
            colors[i] = color
            available_rows[i] = False
            color += 1
    for i in range(len(matrix_adj[0])-1):
        print(str(i) + ": " + str(colors[i]))



def get_first_avaiable_color_vert(unavailable_colors, id_vert):
    color = 0
    equal = False
    while True:
        for i in range(len(unavailable_colors[id_vert])):
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print(color)
            print(unavailable_colors[id_vert][i])
            if color == unavailable_colors[id_vert][i]:
                equal = True
                break
        if equal:

            color += 1
            equal = False
        else:
            break
    return color


class Graph:
    def __init__(self):
        self.matrix_adj = [[]]
        self.matrix_incidence = [[]]
        self.list_adj = {}
        self.list_arc = []
        self.count_vert = 0

    def _init_list_adj(self):
        self.list_adj = {}
        for i in range(self.count_vert):
            self.list_adj.update({i: []})

    def matr_adj_from_list_adj(self):
        self.count_vert = len(self.list_adj)
        self.matrix_adj = [[0 for j in range(0, self.count_vert)] for i in range(0, self.count_vert)]
        for i in self.list_adj:
            for j in self.list_adj[i]:
                self.matrix_adj[i][j] = 1

    def matr_adj_from_lisc_arc(self):
        self.count_vert = max(self.list_arc[0])
        self.matrix_adj = [[0 for j in range(0, self.count_vert)] for i in range(0, self.count_vert)]

        for arc in self.list_arc:
            self.matrix_adj[arc[0]][arc[1]] = 1
            self.matrix_adj[arc[1]][arc[0]] = 1

    def matr_adj_from_matrix_incedent(self):
        self.count_vert = len(self.matrix_incidence)
        self.matrix_adj = [[0] * self.count_vert] * self.count_vert
        t = len(self.matrix_incidence[0])
        first = -1
        second = -1
        for i in range(t):
            for j in range(self.count_vert):
                if self.matrix_incidence[j][i] == 1 and first == -1:
                    first = j
                elif self.matrix_incidence[j][i] == 1 and second == -1:
                    second = 1
                    break
            self.matrix_adj[first][second] = 1
            self.matrix_adj[second][first] = 1

    def list_arc_from_matr_adj(self):
        self.count_vert = len(self.matrix_adj[0])
        self.list_arc = []
        for i in range(self.count_vert):
            for j in range(i + 1, self.count_vert):
                if self.matrix_adj[i][j] > 0:
                    self.list_arc.append([i, j])

    def list_arc_from_matrix_incedent(self):
        self.count_vert = len(self.matrix_incidence)
        count_arc = len(self.matrix_incidence[0])
        first = -1
        second = -1
        for i in range(count_arc):
            for j in range(self.count_vert):
                if self.matrix_incidence[j][i] == 1 and first == -1:
                    first = j
                elif self.matrix_incidence[j][i] == 1 and second == -1:
                    second = 1
                    break
            self.list_arc.append([first, second])

    def list_arc_from_list_adj(self):
        self.count_vert = len(self.list_adj)
        self.list_arc = []
        for i in self.list_adj:
            for j in self.list_adj[i]:
                if i < j:
                    self.list_arc.append([i, j])

    def list_adj_from_list_arc(self):
        self._init_list_adj()
        for arc in self.list_arc:
            self.list_adj.get(arc[0]).append(arc[1])
            self.list_adj.get(arc[1]).append(arc[0])

    def list_adj_from_matix_adj(self):
        self.count_vert = len(self.matrix_adj[0])
        self._init_list_adj()
        for i in range(self.count_vert):
            for j in range(self.count_vert):
                if self.matrix_adj[i][j] > 0:
                    self.list_adj.get(i).append(j)

    def list_adj_from_matrix_incedent(self):
        self.count_vert = len(self.matrix_incidence)
        self._init_list_adj()
        count_arc = len(self.matrix_incidence[0])
        first = -1
        second = -1
        for i in range(count_arc):
            for j in range(self.count_vert):
                if self.matrix_incidence[j][i] == 1 and first == -1:
                    first = j
                elif self.matrix_incidence[j][i] == 1 and second == -1:
                    second = 1
                    break
            self.list_adj.get(first).append(second)
            self.list_adj.get(second).append(first)

    def greedy_coloring(self, graphh):
        return coloring.greedy_color(graphh, strategy="largest_first")

    def matrix_incedent_from_matix_adj(self):
        self.count_vert = len(self.matrix_adj[0])
        self.list_arc_from_matr_adj()
        count_arc = len(self.list_arc)
        self.matrix_incidence = [[0 for j in range(0, count_arc)] for i in range(0, self.count_vert)]

        tmp = 0
        for i in range(self.count_vert):
            for j in range(i, self.count_vert):
                if self.matrix_adj[i][j] > 0:
                    print(tmp)
                    print(i)

                    self.matrix_incidence[tmp][i] = 1
                    self.matrix_incidence[tmp][j] = 1
            tmp += 1

    def matrix_incedent_from_list_arc(self):
        if self.count_vert == 0:
            self.count_vert = max(self.list_arc[0])
        count_arc = len(self.list_arc)
        self.matrix_incidence = [[0 for j in range(0, count_arc)] for i in range(0, self.count_vert)]

        for i, arc in enumerate(self.list_arc):
            self.matrix_incidence[arc[0]][i] = 1
            self.matrix_incidence[arc[1]][i] = 1

    def matrix_incedent_from_list_adj(self):
        self.list_arc_from_list_adj()
        self.matrix_incedent_from_list_arc()

    def add_vert(self):
        self.count_vert += 1
        self.list_adj.update({self.count_vert: []})
        self.matrix_incedent_from_list_arc()
        self.list_arc_from_list_adj()
        self.matr_adj_from_list_adj()

    def del_arc(self, vert1, vert2):
        self.list_arc.remove([vert1, vert2])
        self.list_adj_from_list_arc()
        self.matr_adj_from_list_adj()
        self.matrix_incedent_from_list_arc()

    def del_vert(self, vert):
        del (self.list_adj[vert])
        self.matrix_incedent_from_list_arc()
        self.list_arc_from_list_adj()
        self.matr_adj_from_list_adj()

    def show(self):
        print("Матрица смежности")
        print(self.matrix_adj)
        print("Матрица инцидентности")
        print(self.matrix_incidence)
        print("Cписок дуг")
        print(self.list_arc)
        print("Cписок смежности")
        print(self.list_adj)

    def DFSUtil(self, v, visited):
        visited.add(v)
        for neighbour in self.list_adj[v]:
            if neighbour not in visited:
                print(str(v) + "->" + str(neighbour), end=' ')

                self.DFSUtil(neighbour, visited)
                print(str(neighbour) + '->' + str(v), end=' ')

    def DFS(self, start_vert):
        visited = set()
        self.DFSUtil(start_vert, visited)

    def add_arc(self, vert1, vert2):
        self.list_arc.append([vert1, vert2])
        self.list_adj_from_list_arc()
        self.matr_adj_from_list_adj()
        self.matrix_incedent_from_list_arc()

    def get_id_vert_max_degree(self, degrees):
        id_vert = -1
        max_vert_degree = -1
        for i in range(self.count_vert - 1):
            if degrees[i][1] >= max_vert_degree:
                max_vert_degree = degrees[i][1]
                id_vert = i

        return id_vert

    def reduce_degree_adj_vert(self, degrees, adj_list, id_vert):
        i = 0
        while i < degrees[id_vert][1]:
            reducing_vert = adj_list[id_vert][i + 1]
            degrees[reducing_vert - 1][1] -= 1
            i += 1
        degrees[id_vert][1] = -1

    def is_color_exist(self, unavailable_colors, color, id_vert):
        exist = False
        for i in range(len(unavailable_colors[id_vert])):
            if color == unavailable_colors[id_vert][i]:
                exist = True
                break

        return exist

    def set_unavaible_colors(self, unavailable_colors, id_vert, color, adj_list):
        for i in range(len(adj_list[id_vert])):
            vert = adj_list[id_vert][i + 1]
            if not self.is_color_exist(unavailable_colors, color, vert - 1):
                unavailable_colors[vert - 1].append(color)

    def greeedy_coloring(self):
        adj_list = self.list_adj
        colors = [-1 for i in range(self.count_vert)]
        unavailable_colors_vert = [[0 for i in range(self.count_vert-1)] for j in range(self.count_vert-1)]


        degrees = [[0 for i in range(2)] for j in range(7)]
        for i in range(self.count_vert - 1):
            degrees[i][0] = adj_list[i][0]
            degrees[i][1] = len(adj_list[i]) - 1

        for i in range(self.count_vert - 1):
            idMaxVert = self.get_id_vert_max_degree(degrees)
            color = get_first_avaiable_color_vert(unavailable_colors_vert, idMaxVert)
            colors[idMaxVert] = color
            self.reduce_degree_adj_vert(degrees, adj_list, idMaxVert)

        return colors


# graph=Graph()
# graph.matrix_adj=[[0,1,1,1,0,0,1],
#                 [1,0,1,0,0,0,1],
#                 [1,1,0,1,0,0,0],
#                 [1,0,1,0,1,1,0],
#                 [0,0,0,1,0,1,0],
#                 [0,0,0,1,1,0,1],
#                 [1,1,0,0,0,1,0]]

# graph.show()
# g.add_edges_from(graph.list_arc)
# draw(g, with_labels=True)
# show()

graph = Graph()
# graph.matrix_adj = [[0, 1, 1, 1, 0, 0, 1],
#                     [1, 0, 1, 0, 0, 0, 1],
#                     [1, 1, 0, 1, 0, 0, 0],
#                     [1, 0, 1, 0, 1, 1, 0],
#                     [0, 0, 0, 1, 0, 1, 0],
#                     [0, 0, 0, 1, 1, 0, 1],
#                     [1, 1, 0, 0, 0, 1, 0]]
#------------------------------------------------
graph.matrix_adj = [
    [0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0]
]
#==================================================================
# graph.matrix_adj =[
#     [0, 1, 1, 1],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [1, 1, 1, 0]
# ]



graph.list_arc_from_matr_adj()
graph.list_adj_from_matix_adj()
graph.matrix_incedent_from_matix_adj()
graph.add_vert()
graph.add_arc(4, 1)
graph.show()
#graph.greedy_coloring()
g.add_edges_from(graph.list_arc)

print("DFS")
print(graph.DFS(0))
print("BFS")
print(bfs(visited, graph.list_adj, 0))

d = graph.greedy_coloring(g)
print("coloring by row")
coloring_by_manapulating_rows(graph.matrix_adj)
print("coloring greedy algo")
print("=================================================================")
print(d)
print("=================================================================")

draw(g, with_labels=True)
show()

