#Python3
#Tree Orders
class Tree(object):
    #Implementation of tree data structure
    class Node(object):
        def __init__(self, key, parent, depth, data = None):
            self.data = data
            self.parent = parent
            self.key = key
            self.depth = 1
            self.left = None
            self.right = None
            
        def __str__(self):
            return self._to_string(0)
        
        def _to_string(self, depth):
            words = []
            if self.right:
                words.append(self.right._to_string(depth + 1))
            words.append("{}{}".format(" " * 3 * depth, self.key))
            if self.left:
                words.append(self.left._to_string(depth + 1))
            
            return "\n".join(words)
            
        
    def __init__(self):
        self.root = None
        
    def find(self, key):
        if self.root:
            return self._find(key, self.root)
    
    def _find(self, key, node):
        if node.key == key:
            return node
        elif key < node.key:
            if node.left:
                return self._find(key, node.left)
            else:
                return node
        elif key > node.key:
            if node.right:
                return self._find(key, node.right)
            else:
                return node
    
    def _next_node(self, node):
        if node.right:
            return self._left_descendant(node.right)
        else:
            return self._right_ancestor(node)
    
    def _left_descendant(self, node):
        while node.left:
            node = node.left
        
        return node
    
    def _right_ancestor(self, node):
        if not self.parent:
            return None
        
        if node.key < node.parent.key:
            return node.parent
        else:
            return self._right_ancestor(node.parent)
        
    def add(self, key, data = None):
        if not self.root:
            self.root = self.Node(key, None, 1)
        else:
            self._add(self.root, key, data)
    
    def _add(self, node, key, data):
        if key < node.key:
            if node.left:
                self._add(node.left, key, data)
            else:
                node.left = self.Node(key, node, node.depth + 1, data)
        elif key > node.key:
            if node.right:
                self._add(node.right, key, data)
            else:
                node.right = self.Node(key, node, node.depth + 1, data)                
    
    def range_search(self, x, y, base_node = None):
        if not base_node and not self.root:
            return []
        elif not base_node:
            base_node = self.root
        
        temp = self.find(base_node)
        results = []
        
        while temp.key <= y:
            if temp.key >= x:
                results.append(temp)
            temp = self._next_node(temp)
        
        return results        

    def __str__(self):
        if self.root:
            return self._to_string(self.root, 0)
        else:
            return ""
        
    def _to_string(self, node, depth):
        if node:
            return self._to_string(node.right, depth + 1) + "{}{}\n".format(" " * 3 * depth, node.key) + self._to_string(node.left, depth + 1)
        else:
            return ""
            
    def traverse(self, func, method = "inorder"):
        if self.root:
            node = self.root
            results = []
            self._traverse(func, method, node, results)
            return results
    
    def _traverse(self, func, method, node, results):
        if node:
            if method == "inorder":
                self._traverse(func, method, node.left, results)
                results.append(func(node))
                self._traverse(func, method, node.right, results)
            elif method == "preorder":
                results.append(func(node))
                self._traverse(func, method, node.left, results)
                self._traverse(func, method, node.right, results)
            elif method == "postorder":
                self._traverse(func, method, node.left, results)
                self._traverse(func, method, node.right, results)   
                results.append(func(node))
                
    def is_bst(self):
        if not self.root:
            return True
        temp = self.root
        left_max = temp.key - 1
        right_min = temp.key
        
        return self._is_bst(temp.left, -1e99, left_max) and self._is_bst(temp.right, right_min, 1e99)
    
    def _is_bst(self, node, min_allowed, max_allowed):
        if not node:
            return True
        else:
            if min_allowed <= node.key <= max_allowed:
                return self._is_bst(node.left, min_allowed, node.key - 1) and self._is_bst(node.right, node.key, max_allowed)
            else:
                return False
        
#%%
import sys, threading
sys.setrecursionlimit(10**7) 
threading.stack_size(2**26)  

def main():

    lines = int(input())
    tree = Tree()
    commands = []
    node_keys = set(range(lines))
    node_children = set()
    for _ in range(lines):
        key, left, right = map(int, input().split())
        node_children.update([left,right])
        commands.append((key, left, right))
    
    if len(commands) == 0:
        print("CORRECT")
        return
    
    root_index = (node_keys - node_children).pop()
    
    def recursive_build(index):
        key, left_idx, right_idx = commands[index]
        
        n = Tree.Node(key, None, 0)
        if left_idx != -1:
            n.left = recursive_build(left_idx)
        if right_idx != -1:
            n.right = recursive_build(right_idx)
            
        return n
    
    tree.root = recursive_build(root_index)
    
    if tree.is_bst():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
