class MedianFinder:

    def __init__(self):
        self.maxHeap=[]
        self.minHeap=[]        

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        else:
            heapq.heappush(self.minHeap, num)
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return float(self.minHeap[0])
        #o(logn) o(1)