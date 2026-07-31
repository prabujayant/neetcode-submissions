class Solution:
    def isHappy(self, n: int) -> bool:
        # returns sum of squares of digits
        def get_next(num):
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        # Floyd's cycle detection
        slow = fast = n
        while True:
            slow = get_next(slow)             # move 1 step
            fast = get_next(get_next(fast))   # move 2 steps

            if slow == 1 or fast == 1:
                return True                   # reached 1 → happy number

            if slow == fast:
                return False                  # cycle detected → not happy
