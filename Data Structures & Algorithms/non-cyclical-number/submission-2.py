class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))
        
        slow = fast = n
        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False