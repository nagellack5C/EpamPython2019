"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""


class Graph:

    def __init__(self, E):
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


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': ['E', 'G'], 'E': ['A'], 'G': [], 'D': ['A']}
# for i in E:
#     print(i)
graph = Graph(E)

for vertice in graph:
    print(vertice)
    # break