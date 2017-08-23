#Python3
#Trie Generation
class Trie(object):
    class Node(object):
        def __init__(self, num):
            self.num = num
            self.edges = {}
            self.leaf = False
            
    def __init__(self):
        self.root = self.Node(0)
        self.count = 1
        
    def add_word(self, word):
        temp = self.root
        
        for letter in word:
            if letter not in temp.edges:
                temp.edges[letter] = self.Node(self.count)
                self.count += 1
            temp = temp.edges[letter]
        temp.leaf = True

    def output(self):
        temp = self.root
        
        return "\n".join(self._output(temp))
    
    def _output(self, node):
        results = []
        
        for child in node.edges:
            results.append("{}->{}:{}".format(node.num, node.edges[child].num, child))
            results.extend(self._output(node.edges[child]))
        
        return results
    
    def find_substring(self, text):
        results = []
        for i in range(len(text)):
            substring = text[i:]
            temp = self.root
            for letter in substring:
                if letter in temp.edges:
                    temp = temp.edges[letter]
                    if temp.leaf:
                        results.append(str(i))
                        break
                else:
                    break
        
        return results
#%%
text = input()
patterns = int(input())
t = Trie()
for _ in range(patterns):
    t.add_word(input())
    
print(" ".join(t.find_substring(text)))