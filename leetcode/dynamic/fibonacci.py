# not trying to be elegant but easy to read
def fib(self, n: int) -> int:
    if n < 2:
        return n
    a = 0
    b = 1
    s = 0
    while n > 1:
        s = a + b
        a = b
        b = s
        n -= 1
    return s
