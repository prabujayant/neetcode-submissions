class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1 to both ends to simplify edge multiplication
        nums = [1] + nums + [1]
        dp = {}  # Memoization dictionary: stores (l, r) → max coins
        # Recursive function to calculate max coins from nums[l] to nums[r]
        def dfs(l, r):
            # Base case: no balloons to burst in this range
            if l > r:
                return 0            
            # If already computed, return the stored result
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0  # Initialize max coins for this range
            # Try bursting each balloon i last in the range [l, r]
            for i in range(l, r + 1):
                # Coins from bursting i last (nums[l-1]*nums[i]*nums[r+1])
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # Recurse on left and right subarrays (excluding i)
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                # Store the maximum coins we can collect in this range
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        # Start from the full range excluding the two virtual 1s added
        return dfs(1, len(nums) - 2)
