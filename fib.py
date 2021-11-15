from trampoline import trampoline

def fib(n):
    """Basic recursive fibonacci function"""

    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

@trampoline
def fib_tr(n):
    """Tail recursive factorial function"""
    
    def fib_helper(n, fib1, fib2):
        if n == 0:
            return fib1
        return lambda: fib_helper(n-1, fib2, fib1+fib2)
    return fib_helper(n, 0, 1)