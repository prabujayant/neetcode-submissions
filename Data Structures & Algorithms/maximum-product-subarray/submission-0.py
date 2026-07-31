class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max_prod = min_prod = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if n < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(n, n * max_prod)
            min_prod = min(n, n * min_prod)

            res = max(res, max_prod)

        return res
