class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        m, n = len(a), len(b)
        i = j = 0
        merged = []
        while i < m and j < n:
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1        
        while i < m:
            merged.append(a[i])
            i += 1        
        while j < n:
            merged.append(b[j])
            j += 1
        size = len(merged)
        if size % 2 == 0:
            return (merged[size // 2 - 1] + merged[size // 2]) / 2.0
        else:
            return merged[size // 2]
