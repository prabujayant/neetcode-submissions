class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(','}':'{',']':'['}
        stack=[]
        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped=stack.pop()
                    if popped!=hashmap[c]:
                        return False
        return not stack

        