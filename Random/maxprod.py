#Python3
input()
nums = [int(x) for x in input().split()]
big = 0
big2 = 0
for num in nums:
    if num > big:
        big2 = big
        big = num
    elif num > big2:
        big2 = num

result = big * big2
print(result)
#%%