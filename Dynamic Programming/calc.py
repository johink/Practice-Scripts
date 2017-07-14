#Python3
#Primitive Calculator
def calc(n):
    """
    Design a calculator which gives the shortest number of operations to reach a specified number
    Operations available are += 1, *= 2, and *= 3
    Solution utilizes a dynamic programming approach
    """
    
    #Initialize a list of zeroes
    moves = [0] * (n + 1)
    for i in range(2, n + 1):
        #The option always exists to just add one to the previous number
        #Number of moves is equal to the previous value plus one
        minmoves = moves[i - 1] + 1
        
        #If the number is divisible by two, check to see if multiplying some previous number by two is more efficient
        if i % 2 == 0:
            minmoves = min(minmoves, moves[i // 2] + 1)
        
        #Same as above
        if i % 3 == 0:
            minmoves = min(minmoves, moves[i // 3] + 1)
        moves[i] = minmoves
    
    #Reconstruct the path we took to get to n
    path = []
    while n > 1:
        #At each iteration, we find where the number of moves is one less than our current moves
        path.append(n)
        if moves[n] - moves[n-1] == 1:
            n -= 1
        elif n % 2 == 0 and moves[n] - moves[n // 2] == 1:
            n //= 2
        elif n % 3 == 0 and moves[n] - moves[n // 3] == 1:
            n //= 3
    path.append(1)
    path.reverse()
    return "{}\n{}".format(moves[-1], " ".join([str(x) for x in path]))




#%%
n = int(input())
print(calc(n))