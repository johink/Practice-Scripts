#Python3
#Bipartite Graph
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
                            if edge.flow > 1 or edge.flow < 0:
                                continue
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
                
                assert min_flow <= 1
                vertex = self.vertices[end_label]
                vertex.outflow += min_flow
                
                while vertex.label != start_label:
                    edge, inversion = vertex.previous
                    if not inversion:
                        inverse_edge = self.inverse.vertices[edge.dest.label].edges[edge.orig.label]
                    else:
                        inverse_edge = self.vertices[edge.dest.label].edges[edge.orig.label]
                    
                    if not inversion:
                        assert edge.flow == 0
                        edge.flow += 1
                        assert inverse_edge.flow == 1
                        inverse_edge.flow -= 1
                    else:
                        #assert inverse_edge.flow == 0
                        inverse_edge.flow += 1
                        #assert edge.flow == 1
                        edge.flow -= 1
                    
                    if not inversion:
                        vertex = edge.orig
                    else:
                        vertex = self.vertices[edge.orig.label]
                        
                
            else:
                return self.vertices[end_label].outflow

#%%
flights, crews = map(int, input().split())
g = Graph()
g.add_vertex('start')
g.add_vertex('end')

for i in range(1,flights+1):
    g.add_vertex('flight'+str(i))
    g.add_edge('start','flight'+str(i), 1)

for i in range(1, crews+1):
    g.add_vertex('crew'+str(i))
    g.add_edge('crew'+str(i), 'end', 1)

for i in range(1, flights+1):
    indicators = list(map(int, input().split()))
    for j in range(crews):
        if indicators[j] == 1:
            g.add_edge('flight'+str(i), 'crew'+str(j+1), 1)

g.invert()
g.breadth_first('start', 'end')

results = []
for i in range(1, flights+1):
    vertex = g.vertices['flight'+str(i)]
    if not vertex.edges:
        results.append("-1")
    else:
        found = False
        for edge in vertex.edges.values():
            if edge.flow == 1 and edge.dest.label:
                results.append(edge.dest.label[4:])
                found = True
        if not found:
            results.append('-1')
print(" ".join(results))
            
