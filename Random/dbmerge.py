#Python3
#Merging Databases
class DB(object):
    """
    Implementation of efficient disjoint set algorithm to simulate merging of database tables
    """
    def __init__(self, lengths):
        self.lengths = lengths
        self.refs = list(range(len(lengths)))
        self.maxLen = max(lengths)
        
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

#%%
n_table, n_merge = map(int, input().split())
db = DB(list(map(int, input().split())))
for _ in range(n_merge):
    dest, source = map(lambda x: int(x) - 1, input().split())
    db.merge(dest, source)
#    print("Lengths array: {}\nReference array: {}".format(db.lengths, db.refs))
    print(db.maxLen)