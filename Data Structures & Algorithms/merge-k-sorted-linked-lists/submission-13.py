# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        response = lists[0]
        for i in lists[1:]:
            response = self.mergePairOfLists(response, i)
        
        return response

    def mergePairOfLists(self, list1, list2):
        prev = ListNode()
        node = prev
        while list1 and list2:
            if list1.val > list2.val:
                prev.next = list2
                list2 = list2.next

            else:
                prev.next = list1
                list1 = list1.next
            
            prev = prev.next
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2

        return node.next
