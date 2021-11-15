from trampoline import trampoline

def fact(n):
    """Basic recursive factorial function"""

    if n == 0:
        return 1
    return n * fact(n-1)

@trampoline
def fact_tr(n):
    """Tail recursion factorial function"""

    def fact_helper(n, k):
        if n == 0:
            return k
        return lambda: fact_helper(n-1, n*k)
    return fact_helper(n, 1)