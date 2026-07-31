class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq1 = [0]*26
        freq2 = [0]*26
        for c in range(len(s1)):
            freq1[ord(s1[c]) - ord("a")] += 1
            freq2[ord(s2[c]) - ord("a")] += 1
        if freq1 == freq2:
            return True
        matches = 0
        for i in range(len(s1), len(s2)):
            freq2[ord(s2[i]) - ord("a")] += 1
            freq2[ord(s2[matches]) - ord("a")] -= 1
            matches += 1
            if freq1 == freq2:
                return True
        return False

