#Python3
#Num Components
class Graph(object):
    class Vertex(object):
        def __init__(self, key, data = None):
            self.key = key
            self.edges = set()
            self.data = data
            
        def explore(self):
            #print("Exploring vertex {}".format(self.key))
            for edge in self.edges:
                if not edge.other.visited:
                    edge.other.visited = True
                    edge.other.explore()
    
    class Edge(object):
        def __init__(self, other, data = None):
            self.other = other
            self.data = data
    
    def __init__(self):
        self.nodes = {}
        
    def add_vertex(self, key, data = None):
        self.nodes[key] = self.Vertex(key, data)
    
    def add_undirected(self, u, v, w = None):
        if u not in self.nodes:
            self.nodes[u] = self.Vertex(u, None)
        if v not in self.nodes:
            self.nodes[v] = self.Vertex(v, None)
        self.nodes[u].edges.add(self.Edge(self.nodes[v], w))
        self.nodes[v].edges.add(self.Edge(self.nodes[u], w))
    
    def add_directed(self, u, v, w = None):
        if u not in self.nodes:
            self.nodes[u] = self.Vertex(u, None)
        if v not in self.nodes:
            self.nodes[v] = self.Vertex(v, None)
        self.nodes[u].edges.add(self.Edge(self.nodes[v], w))
        
    def n_components(self):
        for node in self.nodes.values():
            node.visited = False
            
        num_components = 0
        for node in self.nodes.values():
            if not node.visited:
                node.visited = True
                node.explore()
                num_components += 1
        
        return num_components
#%%
nodes, edges = map(int, input().split())
g = Graph()

for i in range(nodes):
    g.add_vertex(i+1)

for _ in range(edges):
    u, v = map(int, input().split())
    g.add_undirected(u, v)

print(g.n_components())