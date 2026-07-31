class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        count=Counter(hand)
        sorted_keys=sorted(count)
        for card in sorted_keys:
            if count[card]>0:
                num=count[card]
                for i in range(groupSize):
                    if count[card + i] < num:
                        return False
                    count[card+i]-=num
        return True
