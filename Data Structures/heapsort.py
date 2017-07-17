#Python3
#Min-Heap Sort
class Heap(object):
    """
    Heap implemented as an array.  Tree structure allows sorting in n log n worst-case runtime
    """
    def __init__(self, array):
        self.array = array
        self.swaps = []
        self.num_swaps = 0
    
    
    """  This was an attempt to implement hashsort by sifting items up; didn't end up working
    def minsort(self):
        num_swaps = 0
        swaps = []
        for i in range(len(self.array)-1, 0, -1):
            temp = i
            while temp > 0 and self.up_shift(temp):
                num_swaps += 1
                swaps.append("{} {}".format((temp-1)//2, temp))
                temp = (temp - 1) // 2
                       
        return num_swaps, swaps
    
    def up_shift(self, index):
        above = (index - 1) // 2
        if self.array[index] < self.array[above]:
            self.array[index], self.array[above] = self.array[above], self.array[index]
            return True
        else:
            return False
    """
        
    def minsort(self):
        for i in range(len(self.array) - 1, -1, -1):
            temp = self.down_shift(i)
            while temp:
                self.num_swaps += 1
                temp = self.down_shift(temp)
                
        return self.num_swaps, self.swaps
        
    def down_shift(self, index):
        below1 = index * 2 + 1
        below2 = index * 2 + 2
        if below1 >= len(self.array):
            return 0
        elif below2 >= len(self.array):
            if self.array[index] > self.array[below1]:
                self.array[index], self.array[below1] = self.array[below1], self.array[index]
                self.swaps.append("{} {}".format(index, below1))
                return below1
        else:
            if self.array[below2] < self.array[below1] and self.array[below2] < self.array[index]:
                self.array[index], self.array[below2] = self.array[below2], self.array[index]
                self.swaps.append("{} {}".format(index, below2))
                return below2
            elif self.array[below1] < self.array[below2] and self.array[below1] < self.array[index]:
                self.array[index], self.array[below1] = self.array[below1], self.array[index]
                self.swaps.append("{} {}".format(index, below1))
                return below1
        return 0
            
        
#%%
_ = input()
h = Heap(list(map(int, input().split())))
num_swaps, swaps = h.minsort()
print(num_swaps)
print("\n".join(swaps))