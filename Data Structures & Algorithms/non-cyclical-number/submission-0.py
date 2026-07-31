class Solution:
    def calc(self, n):
        cur = 0
        while n > 0:
            digit = n % 10
            cur += digit * digit
            n //= 10
        return cur

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.calc(n)
        return True
