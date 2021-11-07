def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    else:
        a = 1
        b = 2
        s = 0
        n -= 2
        while n:
            s = a + b
            a = b
            b = s
            n -= 1
        return s
