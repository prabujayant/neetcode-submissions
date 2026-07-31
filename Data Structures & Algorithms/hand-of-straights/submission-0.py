class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If total cards aren't divisible evenly, it's impossible
        if len(hand) % groupSize != 0:
            return False

        # Count frequency of each card
        count = Counter(hand)
        
        # Create a min-heap of card values to process lowest first
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]  # Start of the current group

            # Try to build a group of groupSize starting from 'first'
            for i in range(first, first + groupSize):
                if count[i] == 0:
                    return False  # Missing a number in sequence

                count[i] -= 1

                # If count becomes 0, remove from heap
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False  # Should be next min in heap
                    heapq.heappop(minHeap)

        return True
