# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tree_hash(root: Optional[TreeNode]) -> str:
    if root is None:
        return "#"
    return f"{root.val}{tree_hash(root.left)}{tree_hash(root.right)}"

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return tree_hash(subRoot) in tree_hash(root)
