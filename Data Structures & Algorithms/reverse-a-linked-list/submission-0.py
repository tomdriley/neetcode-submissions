# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        remaining = head
        reversed_list = ListNode(head.val, None)
        while(remaining.next is not None):
            remaining = remaining.next
            reversed_list = ListNode(remaining.val, reversed_list)
        return reversed_list
