#Python3
#Majority
def majority(array):
    results = dict()
    for item in array:
        results[item] = results.get(item, 0) + 1
    maxi = max(results.values())
    if maxi / len(array) > .5:
        return 1
    else:
        return 0
    
#%%
_ = input()
array = list(map(int, input().split()))
print(majority(array))