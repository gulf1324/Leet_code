# Definition for singly-linked list.
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

###############################################################################
# 1st attempt => Slow Runtime
from typing import Optional
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        """Finding mid_node"""
        l_list_len = 0
        head_ = head
        current = head_
        while current:
            current = current.next
            l_list_len += 1
        current = head_
        # ceiling division
        mid_node = ((l_list_len-1)+2-1)//2 +1     # 0-based index +1
        
        """Transfering links"""
        # previous node of the mid_node needed    # mide_node -1
        current = head
        for i in range(1, mid_node):              # (1) node ~ (mid -1) node 
            # print(f'i:{i}')
            if i == mid_node-1:                 
                # print(current.val,'!!')
                current.next = current.next.next
            else:
                current= current.next
        return head
###############################################################################
# Using two -slow,fast- pointers to find the mid node
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        """Finding mid_node"""
        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow         # mid node -1
            slow = slow.next    # mid node
            fast = fast.next.next
        # print(prev.val)
        # print(slow.val)
        
        """Transfering links"""
        prev.next = prev.next.next
        return head
###############################################################################
head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(4)
head1.next.next.next = ListNode(7)
head1.next.next.next.next = ListNode(1)
head1.next.next.next.next.next = ListNode(2)
head1.next.next.next.next.next.next = ListNode(6)
print_list(head1)

s = Solution()
res = s.deleteMiddle(head1)
print_list(res)