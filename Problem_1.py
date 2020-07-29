L = []
def print_depth(d, depth=0):
    
    for key, value in d.items():
        L.append('{} {}'.format(key, depth + 1))
        if isinstance(value, dict):
            print_depth(value, depth=depth+1)
    return(L)

#Dictionary from the given problem
D = {"key1":1, "key2":{"key3":1,"key4":{"key5":4}}}
