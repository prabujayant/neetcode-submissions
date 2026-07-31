# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def height(node):
            if not node:
                return 0
            leftHeight=height(node.left)
            rightHeight=height(node.right)
            self.diameter=max(leftHeight+rightHeight,self.diameter)
            return 1+max(leftHeight,rightHeight)
        height(root)
        return self.diameter



        