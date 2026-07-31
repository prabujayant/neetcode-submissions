class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_n=0
        for _ in range(32):
            reverse_n=(reverse_n << 1) | (n&1)
            n>>=1
        return reverse_n
        