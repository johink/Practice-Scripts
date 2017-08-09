#Python3
#Curriculum Ordering
class Graph(object):
    class Vertex(object):
        def __init__(self, key, data = None):
            self.key = key
            self.edges = set()
            self.data = data
            self.previsit = None
            self.postvisit = None
            
        def explore(self):
            #print("Exploring vertex {}".format(self.key))
            for edge in self.edges:
                if not edge.other.visited:
                    edge.other.visited = True
                    edge.other.explore()
        
        def __str__(self):
            return "Vertex {}: {}/{} - Edges to {}".format(self.key, self.previsit, self.postvisit, [str(edge) for edge in self.edges])
    
    class Edge(object):
        def __init__(self, other, data = None):
            self.other = other
            self.data = data
            
        def __str__(self):
            return str(self.other.key)
    
    def __init__(self):
        self.nodes = {}
        self.sources = set()
        
    def add_vertex(self, key, data = None):
        self.nodes[key] = self.Vertex(key, data)
        self.sources.add(key)
    
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
        self.sources.difference_update(set([v]))
        
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
    
    def is_reachable(self, u, v):
        for node in self.nodes.values():
            node.visited = False
        
        self.nodes[u].visited = True
        self.nodes[u].explore()
        
        if self.nodes[v].visited:
            return 1
        else:
            return 0
    
    def is_consistent(self):
        for key in self.nodes:
            visited = set([key])
            to_visit = list(self.nodes[key].edges)

            while len(to_visit) > 0:
                temp = to_visit.pop().other

                if temp.key == key:
                    return 1
                elif temp.key not in visited:
                    visited.add(temp.key)
                    to_visit.extend(list(temp.edges))
        
        return 0
                
    def DFS(self):
        self.ordering = []
        for key in self.nodes:
            self.nodes[key].visited = False
                      
        n = 0
    
        for source in self.sources:
            n = self._DFS(source, n)
            
        return " ".join([str(x) for x in self.ordering[::-1]])
    
    def _DFS(self, key, n):
        self.nodes[key].previsit = n
        for edge in self.nodes[key].edges:
            if not edge.other.visited:
                n = self._DFS(edge.other.key, n + 1)
        self.nodes[key].visited = True
        self.nodes[key].postvisit = n
        self.ordering.append(key)
        return n + 1
    
    def __str__(self):
        result = []
        for node in self.nodes:
            result.append(str(self.nodes[node]))
        return "\n".join(result)
        
#%%
nodes, edges = map(int, input().split())
g = Graph()

for i in range(nodes):
    g.add_vertex(i+1)

for _ in range(edges):
    u, v = map(int, input().split())
    g.add_directed(u, v)

print(g.DFS())