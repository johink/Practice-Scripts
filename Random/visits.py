#Python3
#Signatures

def signatures(availabilities):
    """
    Given the time window availabilities of tenants, find the minimum number of trips to get all of their signatures
    A greedy algorithm suffices here, where visits are planned for the hour of the earliest-ending tenant availability window
    """
    visiting_times = []
    num_visits = 0
    i = 0
    visit_hour = availabilities[i][1]
    visiting_times.append(visit_hour)
    num_visits += 1
    i += 1
    while True:
        if i >= len(availabilities):
            break
        elif availabilities[i][0] <= visit_hour <= availabilities[i][1]:
            i += 1
        else:
            num_visits += 1
            visit_hour = availabilities[i][1]
            visiting_times.append(visit_hour)
            i += 1
    
    return "{}\n{}".format(num_visits, " ".join([str(x) for x in visiting_times]))

    
#%%
cases = int(input())
availabilities = []
for _ in range(cases):
    availabilities.append(tuple(map(int, input().split())))
availabilities = sorted(availabilities, key = lambda x: x[1])
print(signatures(availabilities))