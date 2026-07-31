class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # count of characters we need from t
        need = Counter(t)
        missing = len(t)

        l = 0
        start = 0
        minlen = float("inf")

        # r goes from 0 to end of s
        for r in range(len(s)):
            # use one char from s[r]
            if need[s[r]] > 0:
                missing -= 1
            need[s[r]] -= 1

            # when we have all characters
            while missing == 0:
                # update answer if this window is smaller
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    start = l

                # move left side to shrink window
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1

        # if we never found a window
        if minlen == float("inf"):
            return ""
        return s[start:start + minlen]
