#Python3
#Binary Search
def find(array, findlist):
    """
    Implementation of iterative binary search algorithm
    """
    results = []
    for item in findlist:
        lb = 0
        ub = len(array) - 1
        i = (lb + ub + 1) // 2
        #While the lower and upper bounds haven't crossed and we haven't found our item
        while  lb <= ub and array[i] != item:
            #Toss the appropriate half of the array
            if item < array[i]:
                ub = i - 1
            else:
                lb = i + 1
            i = (lb + ub + 1) // 2
        #Check if we're in the array to avoid out-of-bounds error
        if 0 <= i < len(array) and array[i] == item:
            results.append(i)
        else:
            results.append(-1)
    return " ".join([str(num) for num in results])

#%%
array = list(map(int, input().split()))[1:]
findlist = list(map(int, input().split()))[1:]

print(find(array, findlist))