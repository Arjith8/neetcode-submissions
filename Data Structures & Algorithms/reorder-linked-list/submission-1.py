# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5]
        root = head
        track = []
        while head:
            temp = head.next
            head.next = None
            track.append(head)
            head = temp
        
        left, right = 0, len(track) - 1
        while left < right:
            track[left].next = track[right]

            if right - left == 1 and len(track)%2 == 0:
                break

            track[right].next = track[left+1]
            left += 1
            right -= 1

