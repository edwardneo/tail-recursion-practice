from trampoline import trampoline

def create_range(start, end=None, interval=1):
    """Basic recursive range function"""

    if end == None:
        start, end = 0, start

    if start >= end:
        return []
    elif (end - start) * interval <= 0: # Prevents infinite loop
        return None
    return [start] + create_range(start + interval, end, interval)

@trampoline
def create_range_tr(start, end=None, interval=1):
    """Tail recursive range function"""

    if end == None:
        start, end = 0, start

    def create_range_helper(start, lst):
        if start >= end:
            return lst
        elif (end - start) * interval <= 0: # Prevents infinite loop
            return None
        return lambda: create_range_helper(start + interval, lst + [start])
    return create_range_helper(start, [])