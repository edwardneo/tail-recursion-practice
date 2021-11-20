from trampoline import trampoline

def count_hailstone(n):
    """Basic recursive hailstone length function"""

    if n == 1:
        return 1
    elif n % 2 == 0:
        return count_hailstone(n // 2) + 1
    else:
        return count_hailstone(3 * n + 1) + 1

@trampoline
def count_hailstone_tr(n):
    """Tail recursive hailstone length function"""

    def count_hailstone_helper(n, k):
        if n == 1:
            return k
        elif n % 2 == 0:
            return lambda: count_hailstone_helper(n // 2, k + 1)
        else:
            return lambda: count_hailstone_helper(3 * n + 1, k + 1)
    return count_hailstone_helper(n, 1)