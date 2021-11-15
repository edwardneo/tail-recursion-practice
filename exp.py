from trampoline import trampoline

def exp(x, n):
    """Basic recursive power function"""

    if n == 0:
        return 1
    return x * exp(x, n-1)

@trampoline
def exp_tr(x, n):
    """Tail recursive power function"""
    
    def exp_helper(x, n, k):
        if n == 0:
            return k
        return lambda: exp_helper(x, n-1, k * x)
    return exp_helper(x, n, 1)