# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = set()
        curr_node = head
        while(curr_node is not None):
            if curr_node in seen_nodes:
                return True
            seen_nodes.add(curr_node)
            curr_node = curr_node.next
        return False