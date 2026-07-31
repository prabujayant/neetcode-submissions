from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, freqCount in count.items():
            freq[freqCount].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
