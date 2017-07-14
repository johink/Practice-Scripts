#Python3
#Number of Coins
def num_coins(cents):
    """
    Find the number of dimes, nickels, and pennies to make the specified number of cents
    Since higher coins are LCMs of all lower coins, greedy approach works fine
    """
    coins = [10, 5, 1]
    result = 0
    for coin in coins:
        result += cents // coin
        cents %= coin
    return result

num_coins(239)

#%%
cents = int(input())
print(num_coins(cents))