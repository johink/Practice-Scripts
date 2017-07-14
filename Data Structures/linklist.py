#Python3
#linked list

class mylist(object):
    """
    Implementation of a basic linked list with some indexing and pretty printing
    """
    class node(object):
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
    
    def add_front(self, data):
        if not self.head:
            self.head = self.node(data)
        
        else:
            temp = self.node(data)
            temp.next = self.head
            self.head = temp
            
    def remove_front(self):
        if not self.head:
            raise IndexError("Can't remove from empty list!")
        else:
            data = self.head.data
            self.head = self.head.next
            return data
        
    def add_back(self, data):
        if not self.head:
            self.head = self.node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = self.node(data)
            
    def remove_back(self):
        if not self.head:
            raise IndexError("Can't remove from empty list!")
        elif not self.head.next:
            data = self.head.data
            self.head = None
            return data
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            data = temp.next.data
            temp.next = None
            return data
        
    def __getitem__(self, index):
        i = 0
        temp = self.head
        while i < index and temp.next:
            i += 1
            temp = temp.next
        if i == index:
            return temp.data
        else:
            raise IndexError("Index outside of bounds!")
            
    def __str__(self):
        temp = self.head
        string = ""
        while temp:
            string += str(temp.data) + " "
            temp = temp.next
        return string
#%%