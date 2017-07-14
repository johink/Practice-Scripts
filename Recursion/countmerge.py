with open("c:/users/john/desktop/sortme.txt") as f:
    text = f.read()
    
def countMerge(array, lb = 0, rb = -1, pType = 1):
    """
    Recursive implementation of quicksort which counts the number of comparisons made under three different pivoting schemes
    pTypes:  Pivot using first element (1), last element (2), or the median of [first, last, middle] (3)
    """
    
    #Base case, no comparisons made
    if len(array[lb:rb+1]) <= 1:
        return 0
    
    #Pivot with the lowest index under consideration
    if pType == 1:
        pivot = lb
        
    #Pivot with the highest index under consideration
    elif pType == 2:
        pivot = rb
        
    #Pivot with the median of the first, middle, and highest indices
    elif pType == 3:
        end = rb
        middle = (lb + rb) // 2
        possibilities = [(lb, array[lb]), (middle, array[middle]), (end, array[end])]
        pivot = sorted(possibilities, key = lambda x: x[1])[1][0]
    else:
        Exception("Invalid pType")
    
    #Number of comparisons is equal to length of array under consideration
    swap = len(array[lb:rb])
    
    #Swap the pivot to become the first element
    array[lb], array[pivot] = array[pivot], array[lb]
    
    i, j = lb + 1, lb + 1
    
    #Partition step - Make two subarrays which are > and < pivot value
    while j <= len(array[:rb]):
        if array[j] < array[lb]:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    
    #Swap the pivot element to be between the two subarrays
    array[lb], array[i-1] = array[i-1], array[lb]
    
    #Recurse on the two subarrays
    left = countMerge(array, lb = lb, rb = i - 2, pType = pType)
    right = countMerge(array, lb = i, rb = rb, pType = pType)
    
    return swap + left + right

nums = [int(x) for x in text.split()]
results1 = countMerge(nums.copy(), rb = len(nums)-1, pType = 1)
results2 = countMerge(nums.copy(), rb = len(nums)-1, pType = 2)
results3 = countMerge(nums, rb = len(nums)-1, pType = 3)
#%%