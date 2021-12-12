filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day12.txt"

class Node:
    def __init__(self, id):
        self.id = id
        if self.id.isupper():
            self.big = True
        else:
            self.big = False
        self.connections = []

    def add_connection(self, id):
        self.connections.append(id)

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, start, end):
        if start not in self.nodes:
            self.nodes[start] = Node(start)
        if end not in self.nodes:
            self.nodes[end] = Node(end)
        self.nodes[start].add_connection(end)
        self.nodes[end].add_connection(start)

    def print(self):
        for node in self.nodes.values():
            print(node.id + " : " )
            print(node.connections)

    def get_connections(self, id):
        return self.nodes[id].connections

class Path():
    def __init__(self, connections, finished, has_double_small):
        self.path = connections
        self.finished = finished
        self.valid = self.path[-1] == 'end'
        self.has_double_small=has_double_small

    def step(self, graph):
        connections = graph.get_connections(self.path[-1])
        valid_paths = []
        new_paths = []
        for connection in connections:
            if connection == 'end':
                valid_paths.append(Path(self.path+[connection],True, self.has_double_small))
            elif connection == 'start':
                continue
            elif graph.nodes[connection].big or connection not in self.path:
                new_paths.append(Path(self.path+[connection], False, self.has_double_small))
            elif not self.has_double_small:
                new_paths.append(Path(self.path + [connection], False, True))
        return valid_paths, new_paths



graph = Graph()
with open(filename) as f:
    for line in f:
        start, end = line.rstrip().split('-')
        graph.add_edge(start,end)

running_paths = [Path(['start'], False, False)]
valid_paths = []

while len(running_paths) > 0:
    new_paths = []
    for path in running_paths:
        additional_valid_paths, additional_paths = path.step(graph)
        new_paths = new_paths + additional_paths
        valid_paths = valid_paths + additional_valid_paths
    running_paths = new_paths

print('assignment1: ' + str(len(valid_paths)))