#Python3
#LCM
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)
    
def lcm(a, b):
    temp = gcd(a, b)
    return a * b // temp
#%%
a, b = list(map(int, input().split()))
print(lcm(a, b))