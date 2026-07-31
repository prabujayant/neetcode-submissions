class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=list(zip(position,speed))
        car.sort(reverse=True)
        stack=[]
        for pos,spd in car:
            time = (target-pos)/spd
            while not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)
