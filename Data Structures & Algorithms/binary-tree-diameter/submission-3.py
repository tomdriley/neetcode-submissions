# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepthMemoized(root: Optional[TreeNode], cache={}) -> int:
            if root in cache:
                return cache[root]
            result = 0
            if root is None:
                result = 0
            elif root.left is None and root.right is None:
                result = 1
            else:
                result = 1 + max(maxDepthMemoized(root.left, cache), maxDepthMemoized(root.right, cache))
            cache[root] = result
            return result

        def diameterOfBinaryTreeMemoized(root: Optional[TreeNode], cache={}) -> int:
            if root is None or (root.left is None and root.right is None):
                cache[root] = 0
                return 0
            
            max_depth_cache = {}

            result = max(
                diameterOfBinaryTreeMemoized(root.left, cache),
                diameterOfBinaryTreeMemoized(root.right, cache),
                maxDepthMemoized(root.left, max_depth_cache) + maxDepthMemoized(root.right, max_depth_cache)
            )
            cache[root] = result
            return result

        cache = {}
        return diameterOfBinaryTreeMemoized(root, cache)