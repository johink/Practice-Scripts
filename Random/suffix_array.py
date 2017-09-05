#Python3
#Generate Suffix Array
def counting_sort(array):
    mapper = {'$':0,
              'A':1,
              'C':2,
              'G':3,
              'T':4}
    order = [0] * len(array)
    count = [0] * 5
    for i in range(len(array)):
        count[mapper[array[i]]] += 1
    
    for j in range(1, 5):
        count[j] += count[j-1]
    
    for i in range(len(array) - 1, -1, -1):
        pos = mapper[array[i]]
        count[pos] -= 1
        order[count[pos]] = i
    
    return order

def assign_classes(array, order):
    classes = [0] * len(array)
    for i in range(1, len(array)):
        letter = array[order[i]]
        last_letter = array[order[i-1]]
        if letter == last_letter:
            classes[order[i]] = classes[order[i-1]]
        else:
            classes[order[i]] = classes[order[i-1]] + 1
    return classes

def sort_doubled(array, L, order, classes):
    count = [0] * len(array)
    new_order = [0] * len(array)
    for i in range(len(array)):
        count[classes[i]] += 1
    for i in range(1, len(array)):
        count[i] += count[i-1]
    for i in range(len(array) - 1, -1, -1):
        start = (order[i] - L + len(array)) % len(array)
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order

def doubled_classes(new_order, classes, L):
    new_classes = [0] * len(new_order)
    for i in range(1, len(new_order)):
        current_first = new_order[i]
        previous_first = new_order[i-1]
        current_second = (current_first + L) % len(new_order)
        previous_second = (previous_first + L) % len(new_order)
        if classes[current_first] != classes[previous_first] or classes[current_second] != classes[previous_second]:
            new_classes[current_first] = new_classes[previous_first] + 1
        else:
            new_classes[current_first] = new_classes[previous_first]
    
    return new_classes

def gen_suffix_array(text):
    orders = counting_sort(text)
    classes = assign_classes(text, orders)
    L = 1
    while L < len(text):
        orders = sort_doubled(text, L, orders, classes)
        classes = doubled_classes(orders, classes, L)
        L *= 2
    return orders
#%%

text = input()
print(" ".join([str(x) for x in gen_suffix_array(text)]))