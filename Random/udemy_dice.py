import numpy as np
class MysteryDice(object):
    def __init__(self, p):
        self.p = p
        self.counts = np.array([1,1,1,1,1,1])
        
    def roll(self):
        rand = np.random.rand()
        bools = rand > self.p.cumsum()
        return bools.sum() + 1
    
    def update(self, result):
        self.counts[result-1] += 1
        
    def expectation(self):
        return self.counts / self.counts.sum()

#%%
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
plt.style.use('ggplot')

probabilities = np.array([[.3,.02,.3,.03,.3,.05], [.05,.1,.15,.2,.25,.25], [.01,.01,.48,.48,.01,.01],[.05, .3, .03, .3, .02, .3]])
dice = [MysteryDice(prob) for prob in probabilities]

wins = []

for i in range(10000):
    initial_roll = np.random.randint(1,7)
    to_win = [7 - initial_roll]
    
    if initial_roll in [5,6]:
        to_win.append(11-initial_roll)
    
    to_win = np.array(to_win)
    prob_success = np.array([sum(die.expectation()[to_win-1]) for die in dice])
    if i < 1000:
        chosen_die = np.random.choice(range(len(dice)), p = prob_success / prob_success.sum())
    else:
        chosen_die = np.argmax(prob_success)
    
    result = dice[chosen_die].roll()
    dice[chosen_die].update(result)
    
    if result + initial_roll in [7,11]:
        wins.append(1)
    else:
        wins.append(0)

for i, die in enumerate(dice):
    print("Expected distribution for die {}".format(i))
    print("{}".format(die.counts / die.counts.sum()))
plt.plot(range(len(wins)), np.array(wins).cumsum())
plt.title("Win pct = {}".format(np.mean(wins)))