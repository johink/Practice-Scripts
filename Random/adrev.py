#Python3
#Ad Revenue

def adrev(values, probs):
    """
    Matching problem for optimizing revenue
    Greedy approach is appropriate here:  Match the most profitable commercial with the most successful time-slot
    """
    return sum([a * b for a, b in zip(sorted(values, reverse = True), sorted(probs, reverse = True))])

#print(adrev([1,-5,3], [-2, 4, 1]))

#%%
_ = input()
values = list(map(int, input().split()))
probs = list(map(int, input().split()))

print(adrev(values, probs))