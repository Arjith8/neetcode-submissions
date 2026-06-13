# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        start = start2x = head
        while start and start2x:
            if start2x.next and start2x.next.next:
                start2x = start2x.next.next
                if start == start2x:
                    return True
            
            start = start.next

        return False
        