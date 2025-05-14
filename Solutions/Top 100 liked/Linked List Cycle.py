from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
##############################################################################################################################               
# # My 1st solution 
# 10 minutes, passed (6%/56%)
# O(n), O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cache = set()
        node = head
        while node:
            if node in cache:
                return True
            cache.add(node)
            node = node.next
        return False
##############################################################################################################################
# **Follow up: Can you solve it using O(1) (i.e. constant) memory?** 
# more efficient (97%/98%)
# O(n), O(1)
# Floyd’s Cycle Detection Algorithm (aka. tortoise and hare)
""" 'fast' will eventually lap 'slow' within the loop """
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False
##############################################################################################################################                
head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1
# print_list(head1)


s = Solution2()
print(s.hasCycle(head1))
# >>> True
