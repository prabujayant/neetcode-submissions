class Solution:
    def reverseBits(self, n: int) -> int:
        # Start with an empty binary string
        res = ""
        
        # Go through all 32 bits
        for i in range(32):
            # Get the i-th bit (0 or 1)
            bit = (n >> i) & 1
            # Add it to the result string
            res += str(bit)
        
        # Convert the reversed binary string back to integer
        return int(res, 2)
#o(1) o(1)