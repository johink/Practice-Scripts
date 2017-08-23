#UDEMY!
import scipy.stats as scs
import numpy as np
class Bandit(object):
    def __init__(self, p):
        self.p = p
        self.successes = 1
        self.failures = 1
    
    def pull(self):
        return int(np.random.rand() < self.p)
    
    def update(self, x):
        if x:
            self.successes += 1
        else:
            self.failures += 1
            
    def expectation(self):
        return scs.beta(self.successes, self.failures).rvs(1)
    
    def mean(self):
        return self.successes / (self.successes + self.failures)
    
#%%
probabilities = [.28,.3,.32]
bandits = [Bandit(p) for p in probabilities]

pulls = [0, 0, 0]
wins = [0, 0, 0]

epsilon = 1

for i in range(1000):
    index = np.argmax([bandit.expectation() for bandit in bandits])

    result = bandits[index].pull()
    pulls[index] += 1
    if result == 1:
        wins[index] += 1
    bandits[index].update(result)

print(pulls)
print(wins)

#%%
n = 10000
A = scs.beta(bandits[0].successes, bandits[0].failures).rvs(n)
B = scs.beta(bandits[2].successes, bandits[2].failures).rvs(n)

print((B - .04 > A).mean())