class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp, count = head, 0
        while temp and count < k:
            temp = temp.next
            count += 1
        if count < k:
            return head

        prev, cur = None, head
        for _ in range(k):
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        head.next = self.reverseKGroup(cur, k)
        return prev
