from trampoline import trampoline

def sum_list(lst):
    """Basic recursive sum list function"""

    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

@trampoline
def sum_list_tr(lst):
    """Tail recursive sum list function"""

    def sum_list_helper(lst, lst_sum):
        if not lst:
            return lst_sum
        return lambda: sum_list_helper(lst[1:], lst_sum + lst[0])
    return sum_list_helper(lst, 0)