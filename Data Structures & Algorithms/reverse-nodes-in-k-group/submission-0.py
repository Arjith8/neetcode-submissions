# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_ll(root):
            sub_ll_head = root
            prev = None
            for i in range(k):
                temp = root.next
                root.next = prev
                prev = root
                root = temp
            return sub_ll_head, prev, root
        
        def check_if_nodes_mt_k(root):
            fast = root
            for i in range(k):
                if not fast:
                    return False
                fast = fast.next
            return True

        if not check_if_nodes_mt_k(head):
            return head
        
        prev_head, new_head, next_node = reverse_ll(head)

        while True:
            
            if not check_if_nodes_mt_k(next_node):
                print(prev_head.val)
                prev_head.next = next_node
                break
            ph, nh, nn = reverse_ll(next_node)
            prev_head.next = nh
            prev_head = ph
            next_node = nn

        return new_head
                 
        