def trampoline(fn):
    """Trampolining wrapper"""

    def trampoline_helper(*args):
        value = fn(*args)
        while callable(value):
            value = value()
        return value
    return trampoline_helper