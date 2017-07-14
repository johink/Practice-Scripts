#Python3
#Fibonacci Last Digit
def fib_last(n):
    """
    Efficient algorithm for calculating the final digit of the nth Fibonacci number
    """
    if n <= 1:
        return n
    else:
        vals = [0] * (n+1)
        vals[1] = 1
        for i in range(2,n+1):
            vals[i] = (vals[i-1] + vals[i-2]) % 10
        return vals[-1]
#%%
n = int(input())
print(fib_last(n))