#Python3
#Edit Distance
def dist(a, b):
    """
    Calculate edit distance between two strings using a dynamic programming approach
    """
    
    #Create the matrix of distances filled with zeros
    #Matrix dimensions are the lengths of the strings plus 1
    array = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    #Iterate through the matrix calculating the best way to reach that position
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            #If i is zero, must have thrown away j letters in word b to get here
            if i == 0:
                array[i][j] = j
                     
            #If j is zero, must have thrown away i letters in word a to get here
            elif j == 0:
                array[i][j] = i
            
            else:
                #We can always throw away a single letter in either word a or b, or both letters
                #Find the minimum moves for these three prior states, and add a penalty
                mindist = min(array[i-1][j], array[i][j-1], array[i-1][j-1]) + 1
                             
                #If the current letter under consideration is the same for a and b, we can avoid a penalty
                if a[i-1] == b[j-1] and array[i-1][j-1] <= mindist:
                    array[i][j] = array[i-1][j-1]
                    
                #The letters aren't the same, so we have to use the mindist calculated earlier
                else:
                    array[i][j] = mindist
                         
    #The final element in the matrix contains the optimal number of moves
    return array[-1][-1]

#%%
#blah = dist("editing", "distance")
print(dist(input(), input()))