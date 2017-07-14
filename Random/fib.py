#Python3
#Fibonacci
def fib(n):
    """
    Iterative definition of Fibonacci series
    Introduction to basic dynamic programming concepts
    """
    if n <= 1:
        return n
    else:
        vals = [0] * (n+1)
        vals[1] = 1
        for i in range(2,n+1):
            vals[i] = vals[i-1] + vals[i-2]
        return vals[-1]
#%%
n = int(input())
print(fib(n))