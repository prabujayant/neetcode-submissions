class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(x, n):
            if n == 0:
                return 1.0
            if n % 2 == 0:
                return func(x * x, n // 2)
            else:
                return x * func(x * x, n // 2)
        if n < 0:
            x = 1 / x
            n = -n
        return func(x, n)
        #o(logn)
        #o(1)
        