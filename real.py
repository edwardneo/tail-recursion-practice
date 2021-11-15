from trampoline import trampoline

def real(n):
    """Basic recursive int to float function"""

    if n == 0:
        return 0.0
    return real(n-1) + 1.0

@trampoline
def real_tr(n):
    """Tail recursive int to float function"""

    def real_helper(n, k):
        if n == 0:
            return k
        return lambda: real_helper(n-1, k+1.0)
    return real_helper(n, 0.0)