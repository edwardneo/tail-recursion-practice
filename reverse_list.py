from trampoline import trampoline

def reverse_list(lst):
    """Basic recursive list reversal function"""

    if not lst:
        return []
    return lst[-1:] + reverse_list(lst[:-1])

@trampoline
def reverse_list_tr(lst):
    """Tail recursive list reversal function"""

    def reverse_list_helper(lst, reversed):
        if not lst:
            return reversed
        return lambda: reverse_list_helper(lst[:-1], reversed + lst[-1:])
    return reverse_list_helper(lst, [])