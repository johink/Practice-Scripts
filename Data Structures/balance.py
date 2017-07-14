#Python3
#Balance Checker
class Stack(object):
    """
    Implementation of stack data structure
    
    A stack is perfect to check for imbalanced parentheses, brackets, braces
    """
    def __init__(self):
        self.head = None
    
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def push(self, data):
        temp = self.Node(data)
        temp.next = self.head
        self.head = temp
        
    def pop(self):
        if self.head:
            value = self.head.data
            self.head = self.head.next
            return value
        else:
            raise IndexError("Can't pop from empty stack!")
            
    def peek(self):
        if self.head:
            return self.head.data
        else:
            raise IndexError("Can't peek at empty stack!")
            
    def empty(self):
        if self.head:
            return False
        else:
            return True

def isBalanced(text):
    #One stack to hold the characters of interest, one stack to hold index positions
    char_stack = Stack()
    pos_stack = Stack()
    for i, char in enumerate(text):
        #If we see an opening character, push it and its position
        if char in list("([{"):
            char_stack.push(char)
            pos_stack.push(i + 1)
        #If we see a closing character, more work to do
        elif char in list(")]}"):
            #If there's no opening character, we've found an error
            if char_stack.empty():
                return i + 1
            #If the opening character doesn't match the closing character, error
            elif (char_stack.peek(), char) not in [("(",")"), ("[","]"), ("{","}")]:
                return i + 1
            #Otherwise, we have a match.  Remove the matched character and its index
            else:
                char_stack.pop()
                pos_stack.pop()
    #If we get here, we're successful as long as the opening stack is empty
    return "Success" if char_stack.empty() else pos_stack.peek()

#%%
print(isBalanced(input()))