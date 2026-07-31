class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(arr):
            n = len(arr)
            if n <= 2:
                return max(arr)
            dp = [0] * n
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(rob_range(nums[:-1]), rob_range(nums[1:]))
