#Python3
#Most efficient way to connect a set of points
import math
class DisjointSet(object):
    #DisjointSet used in implementation of Kruskal's algorithm
    def __init__(self, lengths):
        self.lengths = lengths
        self.refs = list(range(len(lengths)))
        self.maxLen = 1
        
    def merge(self, dest, source):
        temp = []
        
        while self.refs[dest] != dest:
            temp.append(dest)
            dest = self.refs[dest]
        
        while self.refs[source] != source:
            temp.append(source)
            source = self.refs[source]
        
        for index in temp:
            self.refs[index] = dest
    
        if source != dest:
            self.lengths[dest] += self.lengths[source]
            self.lengths[source] = 0
            self.refs[source] = dest
        
        if self.lengths[dest] > self.maxLen:
            self.maxLen = self.lengths[dest]
            
    def same(self, dest, source):
        while self.refs[dest] != dest:
            dest = self.refs[dest]
        
        while self.refs[source] != source:
            source = self.refs[source]
            
        return dest == source


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
    
    def num_moves(self, orig, dest):
        impossible = len(self.nodes) + 1
        
        for key in self.nodes:
            self.nodes[key].distance = impossible
        
        self.nodes[orig].distance = 0
        fringe = [orig]
        
        while len(fringe) > 0:
            current = fringe.pop(0)
            for edge in self.nodes[current].edges:
                if edge.other.distance == impossible:
                    edge.other.distance = self.nodes[current].distance + 1
                    fringe.append(edge.other.key)
        
        if self.nodes[dest].distance == impossible:
            return -1
        else:
            return self.nodes[dest].distance
    
    def bipartite_check(self):
        impossible = len(self.nodes) + 1
        
        if impossible <= 3:
            return 1
                        
        for key in self.nodes:
            self.nodes[key].distance = impossible
        
        orig = next(iter(self.nodes.keys()))
        self.nodes[orig].distance = 0
        fringe = [orig]
        
        while len(fringe) > 0:
            current = fringe.pop(0)
            for edge in self.nodes[current].edges:
                if edge.other.distance == impossible:
                    edge.other.distance = (self.nodes[current].distance + 1) % 2
                    fringe.append(edge.other.key)
                elif self.nodes[current].distance == edge.other.distance:
                    return 0
        
        return 1
    
    def min_weight(self, orig, dest):
        impossible = 1e9
        
        for key in self.nodes:
            self.nodes[key].distance = impossible
        
        self.nodes[orig].distance = 0
        explored = set()
        distances = [impossible] * (len(self.nodes)+1)
        distances[orig] = 0
                 
        next_key = orig
        
        while next_key != impossible:
            if next_key == dest:
                return self.nodes[dest].distance
            
            explored.add(next_key)
            distances[next_key] = impossible
            
            current = self.nodes[next_key]
            for edge in current.edges:
                if current.distance + edge.data < distances[edge.other.key] and edge.other.key not in explored:
                    distances[edge.other.key] = current.distance + edge.data
                    edge.other.distance = current.distance + edge.data
            
            min_index = -1
            min_value = impossible
            
            for i, distance in enumerate(distances):
                if distance < min_value:
                    min_value = distance
                    min_index = i
            
            if min_value == impossible:
                next_key = impossible
            else:
                next_key = min_index
        
        return -1
    
    def _relax(self, key):
        #print("relaxing {}".format(key))
        node = self.nodes[key]
        change = False
        if node.distance == 1e9:
            return change
        
        for edge in node.edges:
            if node.distance + edge.data < edge.other.distance:
                #print("dist({}) + edge({}) < {}".format(node.distance, edge.data, edge.other.distance))
                edge.other.distance = node.distance + edge.data
                change = True
        return change
    
    def bellman(self):
        for node in self.nodes:
            self.nodes[node].distance = 1e9
        
        for source_key in self.nodes:
            if not all(map(lambda x: x.other.distance != 1e9, self.nodes[source_key].edges)):
                self.nodes[source_key].distance = 0
                for _ in range(len(self.nodes)):
                    changes = False
                    for node in self.nodes:
                        changes = changes or self._relax(node)
                    
                    if not changes:
                        break
                    
                changes = False
                for node in self.nodes:
                    changes = changes or self._relax(node)
                
                if changes:
                    return 1
        
        return 0
    
    def krushkal(self):
        edges = []
        subtree_ids = DisjointSet([1] * len(self.nodes))
        
        euclidean = lambda x, y: math.sqrt((x[0]-y[0]) ** 2 + (x[1]-y[1]) ** 2)
        
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                edges.append([euclidean(self.nodes[i].data, self.nodes[j].data), i, j])
        
        edges = sorted(edges)
        
        result = []
        
        while len(edges) > 0:
            dist, node1, node2 = edges.pop(0)
            if not subtree_ids.same(node1, node2):
                result.append(dist)
                subtree_ids.merge(node1, node2)
        
        return sum(result)
                    
        
#%%
nodes = int(input())
g = Graph()

for i in range(nodes):
    g.add_vertex(i, tuple(map(int, input().split())))

print(g.krushkal())