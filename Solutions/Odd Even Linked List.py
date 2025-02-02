# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

#####################################################################################################
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, nodes_ = head, head
        even_head= head.next
        loop_count = 0
        # Shift link
        # all nodes_.next to nodes_.next.next
        while nodes_ and nodes_.next:
            prev = nodes_
            tmp = nodes_.next
            nodes_.next = nodes_.next.next
            nodes_ = tmp
            loop_count += 1
        
        if loop_count % 2 == 0:     # if loop ended in even number, nodes_.next == last odd node
            nodes_.next = even_head
        else:                       
            prev.next = even_head   # if loop ended in odd number, nodes_.next == last even node

        return head
#####################################################################################################
# More efficient
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head  
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = even.next

            even.next = odd.next
            even = odd.next
        
        odd.next = even_head

        return head
#####################################################################################################
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
print_list(head1)

s = Solution()
res = s.oddEvenList(head1)
print_list(res)