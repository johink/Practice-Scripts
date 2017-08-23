#Python3
#Burrows-Wheeler Transform
def bwt(text):
    bwt_matrix = [text[-i:] + text[:-i] for i in range(len(text))]
    bwt_matrix = sorted(bwt_matrix)
    return "".join([word[-1] for word in bwt_matrix])

def invert_bwt(text):
    d = {}
    text_positions = []
    for letter in text:
        if letter == "$":
            text_positions.append("$")
        else:
            d[letter] = d.get(letter, 0) + 1
            text_positions.append(letter + str(d[letter]).zfill(10))
    first_col = sorted(text_positions)
#    print(first_col)
    lookup = {letter : i for i, letter in enumerate(first_col)}
    
    result = ["$"]
    letter = "$"
    
    for _ in range(len(text)-1):
        result.append(text[lookup[letter]])
        letter = text_positions[lookup[letter]]
    result.reverse()
    return "".join(result)
#%%
print(invert_bwt(input()))

#%%
#Stress testing
"""
import numpy as np
letters = np.array(["A","G","T","C"])
for i in range(10000):
    indices = np.random.randint(0,4, size = i)
    test_string = "".join(letters[indices]) + "$"
    assert test_string == invert_bwt(bwt(test_string)), "Failed on case {}\n{}\n{}\n{}".format(i, test_string, bwt(test_string), invert_bwt(bwt(test_string)))
"""