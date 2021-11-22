from trampoline import trampoline

def maximum(lst, key=lambda x: x):
    """Basic recursive maximum function"""

    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]

    max_val = maximum(lst[1:], key)
    if key(lst[0]) > key(max_val):
        return lst[0]
    else:
        return max_val

@trampoline
def maximum_tr(lst, key=lambda x: x):
    """Tail recursive maximum function"""

    def maximum_helper(lst, max_val):
        if len(lst) == 0:
            return max_val
        elif max_val == None or key(lst[0]) > key(max_val):
            return lambda: maximum_helper(lst[1:], lst[0])
        else:
            return lambda: maximum_helper(lst[1:], max_val)
    return maximum_helper(lst, None)
        
    