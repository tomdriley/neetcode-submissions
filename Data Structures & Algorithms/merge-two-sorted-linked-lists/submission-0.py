# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = None
        tail = ListNode()
        list1_ptr = list1
        list2_ptr = list2

        while(list1_ptr is not None or list2_ptr is not None):
            next_item = int()
            if list1_ptr is not None and list2_ptr is not None:
                if list1_ptr.val <= list2_ptr.val:
                    next_item = list1_ptr.val
                    list1_ptr = list1_ptr.next
                else:
                    next_item = list2_ptr.val
                    list2_ptr = list2_ptr.next
            elif list1_ptr is not None:
                next_item = list1_ptr.val
                list1_ptr = list1_ptr.next
            elif list2_ptr is not None:
                next_item = list2_ptr.val
                list2_ptr = list2_ptr.next
            if merged_list is None:
                merged_list = ListNode(next_item, None)
                tail = merged_list
            else:
                tail.next = ListNode(next_item, None)
                tail = tail.next

        return merged_list