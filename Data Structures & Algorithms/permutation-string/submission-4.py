class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s2 is shorter than s1, it's impossible
        if len(s2) < len(s1):
            return False

        # Frequency arrays for 26 lowercase letters
        freq1 = [0] * 26   # count of chars in s1
        freq2 = [0] * 26   # count of chars in current window of s2

        # Step 1: Fill frequencies for s1 and first window of s2
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord("a")] += 1
            freq2[ord(s2[i]) - ord("a")] += 1

        # Step 2: Check if first window matches
        if freq1 == freq2:
            return True

        # Step 3: Slide window across s2
        left = 0
        for right in range(len(s1), len(s2)):
            # include new char (expand window to right)
            freq2[ord(s2[right]) - ord("a")] += 1
            # remove old char (shrink window from left)
            freq2[ord(s2[left]) - ord("a")] -= 1
            left += 1

            # check if window matches s1’s freq
            if freq1 == freq2:
                return True

        return False
