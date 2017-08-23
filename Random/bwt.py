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
            text_positions.append(letter + str(d[letter]))
    first_col = sorted(text_positions)

    lookup = {letter : i for i, letter in enumerate(first_col)}
    
    result = []
    letter = text_positions[0]
    
    print(lookup)
    print(first_col)
    print(text_positions)
    
    while text_positions[lookup[letter]] != "$":
        result.append(text[lookup[letter]])
        letter = text_positions[lookup[letter]]

    
    return "".join(result) + "$"
#%%
print(bwt(input()))