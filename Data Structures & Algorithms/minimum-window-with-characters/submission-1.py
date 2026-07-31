class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t is "":
            return ""

        countT=Counter(t)
        window={}
        have,need=0,len(countT)
        result=""
        minLength=float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLength:
                    result = s[l:r + 1]
                    minLength = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return result
        