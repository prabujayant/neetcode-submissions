class Solution:
    def reverse(self, x: int) -> int:
        is_neg=x<0
        x=abs(x)
        res=0
        
        while x:
            digit=x%10
            x//=10
            res=res*10+digit
            if res > 2**31 -1:
                return 0
        return res*-1 if is_neg else res

        