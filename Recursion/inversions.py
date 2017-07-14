with open("c:/users/john/desktop/intarray.txt") as f:
    text = f.read()
    
def countInversions(array):
    """
    Use a modification of the recursive merge sort algorithm to count the number of inversions (out of order items) in an array
    """
    if len(array) <= 1:
        return 0, array
    else:
        left, arr1 = countInversions(array[:len(array) // 2])
        right, arr2 = countInversions(array[len(array) // 2:])
        
        split, i, j = 0, 0, 0
        
        merged = []
        
        #i indexes into the left array, j into the right
        while i < len(arr1) and j < len(arr2):
            #If the item in the left array is lower, we're good
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            #If the item in the right array is lower, then it is inverted with every remaining element in the left array
            else:
                merged.append(arr2[j])
                split += len(arr1[i:])
                j += 1
                
        #Add whichever array didn't get finished
        if j < len(arr2):
            merged.extend(arr2[j:])
        if i < len(arr1):
            merged.extend(arr1[i:])
        
        
        return left + split + right, merged
#%%                

countInversions([2,1,3,51,2,4,21,3,12,412,5,2135,1,3,26,23,4,314,12,231,24,3,523,5,234,12,4312345,235,1,2341,23,12])
#%%
nums = text.split()
nums = list(map(int, nums))
#%%
result = countInversions(nums)