class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False  # If total sum is odd, we can't split it equally

        target = total // 2
        n = len(nums)

        # dp[i] will be True if a subset sum of i is possible
        dp = [False] * (target + 1)
        dp[0] = True  # We can always make sum 0 with empty subset

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
