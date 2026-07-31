class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) 
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always breakable

        for i in range(1, n + 1):
            for j in range(i):
                # If s[0:j] is breakable, and s[j:i] is a valid word
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # No need to check more splits

        return dp[n]  # Can we break the whole string?

        #o(nmk)
        #(n)



        