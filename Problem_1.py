def print_depth(d, depth=0):
    
    for key, value in d.items():
        return(key, depth + 1)
        if isinstance(value, dict):
            print_depth(value, depth=depth+1)

#Dictionary from the given problem
D = {"key1":1, "key2":{"key3":1,"key4":{"key5":4}}}
#Custom Dictionary for testing
C = {"key1":{"key2":1,"key3":{"key4":4}},"key5":1}
