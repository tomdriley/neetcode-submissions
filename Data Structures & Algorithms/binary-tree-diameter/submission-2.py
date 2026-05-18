# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root: Optional[TreeNode], cache={}) -> int:
            if root in cache:
                return cache[root]
            result = 0
            if root is None:
                result = 0
            elif root.left is None and root.right is None:
                result = 1
            else:
                result = 1 + max(maxDepth(root.left), maxDepth(root.right))
            cache[root] = result
            return result

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        
        cache = {}

        return max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
            maxDepth(root.left, cache) + maxDepth(root.right, cache)
        )