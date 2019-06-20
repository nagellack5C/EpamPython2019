"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""
from time import time

class Graph:

    def __init__(self, E, mode):
        if not isinstance(E, dict) or len(E) < 1:
            raise TypeError("Please supply non-empty dict")
        if any([not isinstance(x, list) for x in E.values()]):
            raise TypeError("Values must be lists!")
        # optional validation of graph connectivity
        # graph_keys = E.keys()
        # graph_values = set(x for i in E.values() for x in i)
        # if graph_keys != graph_values:
        #     raise AttributeError("List is not connected!")
        self.E = E
        self.mode = mode

    def __iter__(self):
        if self.mode == "S":
            return GraphIteratorStaticVerts(self)
        else:
            return GraphIteratorDynamicVerts(self)


class GraphIteratorDynamicVerts:
    def __init__(self, graph):
        self.E = graph.E
        first_key = list(self.E.keys())[0]
        self.verts = [first_key] + self.E[first_key]
        self.iter_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.iter_index += 1
        if self.iter_index > len(self.verts) - 1:
            raise StopIteration
        new_verts = self.E[self.verts[self.iter_index]]
        for vert in new_verts:
            if vert not in self.verts:
                self.verts.append(vert)
        return self.verts[self.iter_index]


class GraphIteratorStaticVerts:
    def __init__(self, graph):
        self.E = graph.E
        first_key = list(self.E.keys())[0]
        self.verts = [first_key]
        self.iter_index = 0
        self.list_builder(first_key)

    def list_builder(self, key):
        if key not in self.verts:
            self.verts += self.E[key]
        new_verts = []
        for vert in self.E[key]:
            if vert not in self.verts:
                self.verts.append(vert)
                new_verts.append(vert)
        for vert in new_verts:
            self.list_builder(vert)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_index + 1 < len(self.verts):
            self.iter_index += 1
            return self.verts[self.iter_index - 1]
        else:
            raise StopIteration


if __name__ == "__main__":
    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': ['E', 'G'], 'E': ['A'], 'G': [], 'D': ['A']}
    # E = {1: [], 2: []}

    start = time()
    for i in range(100000):
        graph_s = Graph(E, "S")
        x = [vert for vert in graph_s]
    print("execution time", time() - start)

    start = time()
    for i in range(100000):
        graph_d = Graph(E, "d")
        x = [vert for vert in graph_d]
    print("execution time", time() - start)