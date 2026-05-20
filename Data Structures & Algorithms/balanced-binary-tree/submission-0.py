# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def treeHeight(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    else:
        return 1 + max(treeHeight(root.left), treeHeight(root.right))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        height_diff = abs(treeHeight(root.left) - treeHeight(root.right))

        return (height_diff <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)