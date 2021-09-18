# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
#         a = ListNode(2)
#         b = ListNode(2)
#         c = ListNode(3)
#         a.next = c
#         b.next = c
        
#         print(a == b)            # -> False
#         print(a.next == b.next)  # -> True
        
        node_list = []
        curr_node = head
        
        while True:
            if (curr_node is None) or (curr_node.next is None):
                return False
            
            elif (curr_node.next not in node_list):
                # node_list.append(curr_node)    # pos를 return하는 문제는 아니니까 
                node_list.append(curr_node.next) # curr_node.next부터 append
                curr_node = curr_node.next
                
            else:
                return True