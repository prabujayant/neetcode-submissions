# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev,cur = None , slow.next
        slow.next=None
        while cur:
            cur.next,prev,cur=prev,cur,cur.next
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


