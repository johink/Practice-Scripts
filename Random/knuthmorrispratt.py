#Python3
#Knuth-Morris-Pratt

def compute_prefix(pattern):
    prefix = [0] * len(pattern)
    border = 0
    for i in range(1, len(pattern)):
        while border > 0 and pattern[i] != pattern[border]:
            border = prefix[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        prefix[i] = border
    
    return prefix

def kmp(text, pattern):
    combined = pattern + "$" + text
    prefix = compute_prefix(combined)
    results = [str(i - 2 * len(pattern))
    for i in range(len(pattern) + 1, len(combined))
    if prefix[i] == len(pattern)]
    
    return results
    
#%%
pattern = input()
text = input()

print(" ".join(kmp(text, pattern)))