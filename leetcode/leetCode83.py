# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current_node = head
        
        while True:
            if current_node is None or current_node.next is None:
                break
                
            elif current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
                
            else:
                current_node = current_node.next
                
        return head