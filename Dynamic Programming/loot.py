#Python3
#Grab the gold
def gold(bars, capacity):
    """
    Discrete knapsack problem; greedy approach is sub-optimal, so dynamic programming is used
    """
    array = [[0] * (capacity + 1) for _ in range(len(bars) + 1)]
    
    #Each row in the matrix indicates the addition of a new weight of gold bar being considered
    for i, bar in enumerate([0] + bars):
        for j in range(capacity + 1):
            if i > 0 and j > 0:
                maxval = max(array[i-1][j], array[i][j-1])
                
                #If the capacity of the backpack is greater than the weight of the bar, 
                #we can add the bar as long as our backpack isn't already more valuable
                if j >= bar:
                    maxval = max(maxval, array[i-1][j-bar] + bar)
                array[i][j] = maxval
                     
    #Final element contains the optimal amount of gold
    return array[-1][-1]


#%%
weight, numbars = list(map(int, input().split()))
bars = list(map(int, input().split()))
print(gold(bars, weight))