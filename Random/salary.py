#Python3
#Maximize Salary
def maxSal(numbers):
    return int("".join(numbers))

#%%
_ = input()
print(maxSal(sorted(input().split(), key = lambda x: x + x[0], reverse = True)))