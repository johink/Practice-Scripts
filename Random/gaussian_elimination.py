#Python3
#Gaussian Elimination
def eliminate(sys_eq):
    n_eq = len(sys_eq)
    n_found = 0
    for pivot_idx in range(n_eq):
        for i in range(n_found, n_eq):
            if sys_eq[i][pivot_idx] != 0:
                sys_eq[0], sys_eq[i] = sys_eq[i], sys_eq[0]
                break
        if sys_eq[0][pivot_idx] == 0:
            continue
        else:
            n_found += 1
            sys_eq[0] = [value / sys_eq[0][pivot_idx] for value in sys_eq[0]]
            for i in range(1, n_eq):
                coeff = sys_eq[i][pivot_idx]
                sys_eq[i] = [current - top * coeff for current, top in zip(sys_eq[i], sys_eq[0])]
    return sys_eq





#%%
n_equations = int(input())
eqs = []
for _ in range(n_equations):
    eqs.append(list(map(int, input().split())))

result = eliminate(eqs)
result = sorted(result, reverse = True)
print(" ".join([str(row[-1]) for row in result]))