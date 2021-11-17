from trampoline import trampoline

def combine_ord_lists(lst1, lst2): # lst1 and lst2 are ordered
    """Basic recursive combining ordered lists function"""

    if not lst1 or not lst2:
        return lst1 or lst2
    elif lst1[0] <= lst2[0]:
        return lst1[:1] + combine_ord_lists(lst1[1:], lst2)
    else:
        return lst2[:1] + combine_ord_lists(lst1, lst2[1:])

@trampoline
def combine_ord_lists_tr(lst1, lst2): # lst1 and lst2 are ordered
    """Tail recursive combining ordered lists function"""
    
    def combine_ord_lists_helper(lst1, lst2, final_lst):
        if not lst1 or not lst2:
            return final_lst + (lst1 or lst2)
        elif lst1[0] <= lst2[0]:
            return lambda: combine_ord_lists_helper(lst1[1:], lst2, final_lst + lst1[:1])
        else:
            return lambda: combine_ord_lists_helper(lst1, lst2[1:], final_lst + lst2[:1])
    return combine_ord_lists_helper(lst1, lst2, [])