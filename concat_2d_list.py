from trampoline import trampoline

def concat_2d_list(lst_2d):
    """Basic recursive concatenating lists inside a list function"""

    if not lst_2d:
        return []
    return lst_2d[0] + concat_2d_list(lst_2d[1:])

@trampoline
def concat_2d_list_tr(lst_2d):
    """Tail recusive concatenating lists inside a list function"""

    def concat_2d_list_helper(lst_2d, sum_lst):
        if not lst_2d:
            return sum_lst
        return lambda: concat_2d_list_helper(lst_2d[1:], sum_lst + lst_2d[0])
    return concat_2d_list_helper(lst_2d, [])