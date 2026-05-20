# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tree_hash(root: Optional[TreeNode]) -> str:
    if root is None:
        return ""
    return f"{root.val}{tree_hash(root.left)}{tree_hash(root.right)}"

def compare_tree_hash(root: Optional[TreeNode], cmp_hash: int) -> bool:
    if root is None:
        return False
    return (
        tree_hash(root) == cmp_hash
        or compare_tree_hash(root.left, cmp_hash)
        or compare_tree_hash(root.right, cmp_hash)
    )

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        subRootHash = tree_hash(subRoot)
        # assertion: subRootHash is non zero due to above check
        return compare_tree_hash(root, subRootHash)
