#Python3
#Network Flows
class Graph(object):
    class Vertex(object):
        def __init__(self, label):
            self.label = label
            self.edges = {}
            self.previous = None
            self.outflow = 0
        
        def add_edge(self, edge):
            self.edges[edge.dest.label] = edge
        
        def __str__(self):
            return "Vertex {} with {} Edges, Previous == {}".format(self.label, len(self.edges), bool(self.previous))
        
        def __repr__(self):
            return "Vertex(label={},previous={})".format(self.label, self.previous)
        
    class Edge(object):
        def __init__(self, orig, dest, weight, inverse = False):
            self.orig = orig
            self.dest = dest
            self.capacity = weight
            self.flow = 0 if not inverse else self.capacity
            
        def __str__(self):
            return "From {} to {}, {}/{}".format(self.orig, self.dest, self.flow, self.capacity)
        
        def __repr__(self):
            return "Edge(from={}, to={}, flow={}, capacity={})".format(self.orig, self.dest, self.flow, self.capacity)
    
    def __init__(self):
        self.vertices = {}
        self.inverse = None
    
    def __str__(self):
        return "\n".join([str((v, [edge for edge in self.vertices[v].edges])) for v in self.vertices])
    
    def add_vertex(self, label):
        self.vertices[label] = self.Vertex(label)
    
    def add_edge(self, orig_label, dest_label, weight, inverse = False):
        if self.vertices[orig_label].edges.get(dest_label, None):
            self.vertices[orig_label].edges[dest_label].capacity += weight
        else:
            orig = self.vertices[orig_label]
            dest = self.vertices[dest_label]
            orig.add_edge(self.Edge(orig, dest, weight, inverse))
    
    def invert(self):
        g = Graph()
        for vertex in self.vertices:
            g.add_vertex(vertex)
        
        for vertex in self.vertices.values():
            for edge in vertex.edges.values():
                g.add_edge(edge.dest.label, edge.orig.label, edge.capacity, True)
        
        self.inverse = g
    
    def breadth_first(self, start_label, end_label):
        while True:
            for vertex_label in self.vertices:
                self.vertices[vertex_label].previous = None
                self.inverse.vertices[vertex_label].previous = None
            
            start_vertex = self.vertices[start_label]
            start_vertex.previous = None
            to_explore = [start_vertex]
            
            while len(to_explore) > 0:
                current = to_explore.pop(0)
                inv_current = self.inverse.vertices[current.label]
                
                if current.label == end_label:
                    break
                else:
                    for edge in current.edges.values():
                        if edge.flow < edge.capacity and not edge.dest.previous:
                            edge.dest.previous = edge, False
                            to_explore.append(edge.dest)
                    
                    for edge in inv_current.edges.values():
                        if edge.flow < edge.capacity and not self.vertices[edge.dest.label].previous:
                            self.vertices[edge.dest.label].previous = edge, True
                            to_explore.append(self.vertices[edge.dest.label])
            
            if self.vertices[end_label].previous:
                min_flow = None
                vertex = self.vertices[end_label]
                #print(vertex)
                while vertex.label != start_label:
                    edge, inversion = vertex.previous
                    #print(edge)
                    #print(inversion)
                    if not inversion:
                        flow = edge.capacity - edge.flow
                        #print(flow)
                    else:
                        inverse_edge = self.inverse.vertices[edge.orig.label].edges[edge.dest.label]
                        flow = inverse_edge.capacity - inverse_edge.flow
                        #print(flow)
                    if not min_flow or flow < min_flow:
                        min_flow = flow
                        #print(min_flow)
                    if not inversion:
                        vertex = edge.orig
                    else:
                        vertex = self.vertices[edge.orig.label]
                    #print("\n\n")
                
                vertex = self.vertices[end_label]
                vertex.outflow += min_flow
                
                while vertex.label != start_label:
                    edge, inversion = vertex.previous
                    if not inversion:
                        inverse_edge = self.inverse.vertices[edge.dest.label].edges[edge.orig.label]
                    else:
                        inverse_edge = self.vertices[edge.dest.label].edges[edge.orig.label]
                    
                    if not inversion:
                        edge.flow += min_flow
                        inverse_edge.flow -= min_flow
                    else:
                        inverse_edge.flow += min_flow
                        edge.flow -= min_flow
                    
                    if not inversion:
                        vertex = edge.orig
                    else:
                        vertex = self.vertices[edge.orig.label]
                        
                
            else:
                return self.vertices[end_label].outflow
"""      
testcase = 10 28
1 1 8
1 3 4
1 5 35
1 6 39
1 7 97
1 8 62
1 8 89
2 5 63
2 5 74
2 10 75
3 9 45
3 10 40
4 2 22
4 3 31
4 10 10
5 8 77
6 3 50
6 5 61
7 3 12
7 4 27
7 10 49
8 2 66
8 6 19
8 9 51
8 10 54
8 10 98
9 6 4
10 10 91
testcase = [[int(item) for item in line.split()] for line in testcase.split('\n')]
vertices, edges = testcase[0]
g = Graph()
for i in range(1,vertices+1):
    g.add_vertex(i)

for row in testcase[1:]:
    orig, dest, cap = row
    g.add_edge(orig, dest, cap)

g.invert()
print(g.breadth_first(1, vertices))
"""
#%%
vertices, edges = map(int, input().split())
g = Graph()
for i in range(1,vertices+1):
    g.add_vertex(i)

for _ in range(edges):
    orig, dest, cap = map(int, input().split())
    g.add_edge(orig, dest, cap)
g.invert()
print(g.breadth_first(1, vertices))
