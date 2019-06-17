"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""


class Graph:

    def __init__(self, E):
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

    def __iter__(self):
        first_key = list(self.E.keys())[0]
        self.verts = [first_key] + self.E[first_key]
        self.iter_index = -1
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


if __name__ == "__main__":
    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': ['E', 'G'], 'E': ['A'], 'G': [], 'D': ['A']}
    # E = {1: [], 2: []}
    graph = Graph(E)
    print([vert for vert in graph])