#Python3
#Candies
def candies(n):
    """
    How many different prizes can we create out of n candies given that the size of the prize must be monotonically-decreasing
    Greedy approach is sufficient here:  Make a prize of 1, 2, etc candies, and dump all the extra candies in the top prize
    """
    prizes = 0
    sizes = []
    next_prize = 1
    while n > 0:
        prizes += 1
        n -= next_prize
        sizes.append(next_prize)
        next_prize += 1
        if next_prize > n:
            sizes[-1] += n
            n = 0
    return "{}\n{}".format(prizes, " ".join([str(x) for x in sizes]))
 
#%%
print(candies(int(input())))