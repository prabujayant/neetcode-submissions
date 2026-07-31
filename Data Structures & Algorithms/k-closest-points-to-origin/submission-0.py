class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        def dist(x,y):
            return x**2+y**2

        for x,y in points:
            d=dist(x,y)
            if len(heap)<k:
                heapq.heappush(heap,(-d,x,y))
            else:
                heapq.heappushpop(heap,(-d,x,y))
        return [(x,y) for d,x,y in heap]
        