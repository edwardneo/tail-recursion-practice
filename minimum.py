from trampoline import trampoline

def minimum(lst, key=lambda x: x):
    """Basic recursive minimum function"""

    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]

    min_val = minimum(lst[1:], key)
    if key(lst[0]) < key(min_val):
        return lst[0]
    else:
        return min_val

@trampoline
def minimum_tr(lst, key=lambda x: x):
    """Tail recursive minimum function"""

    def minimum_helper(lst, min_val):
        if len(lst) == 0:
            return min_val
        elif min_val == None or key(lst[0]) < key(min_val):
            return lambda: minimum_helper(lst[1:], lst[0])
        else:
            return lambda: minimum_helper(lst[1:], min_val)
    return minimum_helper(lst, None)
        
    