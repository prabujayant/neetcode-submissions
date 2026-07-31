"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        old_to_new = {}

        # Step 1: Create new nodes and map them
        while cur:
            copy = Node(cur.val)
            old_to_new[cur] = copy
            cur = cur.next

        # Step 2: Set next and random pointers
        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next = old_to_new.get(cur.next)
            copy.random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]
