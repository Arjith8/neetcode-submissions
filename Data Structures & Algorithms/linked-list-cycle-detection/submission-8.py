# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        start = start2x = head
        while start2x and start2x.next:
            start2x = start2x.next.next
            start = start.next
            if start == start2x:
                return True
    
        return False
        