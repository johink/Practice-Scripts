#Python3
#Huge Fib Mod M
def fib_mod(n, mod):
    """
    Efficient algorithm for calculating the nth Fibonacci number mod x
    Takes advantage of the fact that the values of the mod are a finite, repeating series beginning with (0,1)
    """
    if n <= 1:
        return n
    else:
        vals = [0,1]
        oneback = 1
        twoback = 0
        while True:
            nextval = (oneback + twoback) % mod
            if (oneback, nextval) == (0, 1):
                period = len(vals[:-1])
                return vals[n % period]
            else:
                vals.append(nextval)
                twoback = oneback
                oneback = nextval

#%%
n, mod = list(map(int, input().split()))
print(fib_mod(n, mod))