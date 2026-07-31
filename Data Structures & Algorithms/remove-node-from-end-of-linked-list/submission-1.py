# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy to handle head deletion
        slow = fast = dummy

        # Step 1: Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Step 2: Move both pointers until fast reaches end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Step 3: Remove the node
        slow.next = slow.next.next

        return dummy.next

        