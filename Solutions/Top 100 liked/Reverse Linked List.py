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
    print("None")

#######################################################################################################################################    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current is not None:
            temp = current.next              # temp for not losing current.next(should assign this as current for next loop)  -----|
                                             #                                                                                     |
            current.next = prev              # cut link and link current.next to the previous node(1st case: None)                 |
                                             #                                                                                     |
            prev = current                   # assign "previous node" as "current node"                                            |
            current = temp                   # assign "next node" as "current node"     <------------------------------------------|
        
        return prev
#######################################################################################################################################
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

s = Solution()
print_list(s.reverseList(head1))
# >>> 5 -> 4 -> 3 -> 2 -> 1 -> None
