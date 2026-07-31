class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # stores indices of days
        result = [0] * len(temperatures)        
        for i in range(len(temperatures)):
            # While current temp is higher than the last stored index temp
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ind = stack.pop()
                result[ind] = i - ind
            stack.append(i)        
        return result
        #o(n)
        #o(n)