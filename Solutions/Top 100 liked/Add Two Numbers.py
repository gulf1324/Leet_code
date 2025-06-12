# Definition for singly-linked list.
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
    # print("None")

#######################################################################################################################################    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current_node = dummy_head
        tmp_excess = 0
        while l1 or l2 or tmp_excess:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + tmp_excess
            
            tmp_excess = total_sum // 10
            digit = total_sum % 10

            # new_node
            current_node.next = ListNode(digit)
            current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next
#######################################################################################################################################
head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

s = Solution()
print_list(s.addTwoNumbers(head1, head2))
# >>> 7 -> 0 -> 8 -> None
