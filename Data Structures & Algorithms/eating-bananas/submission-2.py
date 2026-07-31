class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)

        while minSpeed < maxSpeed:
            mid = (minSpeed + maxSpeed) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours <= h:
                maxSpeed = mid
            else:
                minSpeed = mid + 1

        return minSpeed
