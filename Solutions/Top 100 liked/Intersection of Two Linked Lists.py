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
# How would I know this in the first attempt??
# 2 pointers
# move the same distances
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        p = headA 
        q = headB

        while p is not q:
            p = headB if p is None else p.next
            q = headA if q is None else q.next

        return p
#######################################################################################################################################
head1 = ListNode(4)
head1.next = ListNode(1)
head1.next.next = ListNode(8)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(1)
head2.next.next.next = head1.next.next

# print_list(head1)
# # 4 -> 1 -> 8 -> 4 -> 5 -> None
# print_list(head2)
# 5 -> 6 -> 1 -> 8 -> 4 -> 5 -> None

s = Solution()
print(s.getIntersectionNode(head1, head2).val)
# >>> 8


# Explanation 
# ex)
# A:     4 → 1 \
#               8 → 4 → 5
# B: 5 → 6 → 1 /

# p: 4 → 1 → 8 → 4 → 5 → "5" → 6 → 1 → 8
# > (2 + 2) + 3
# q: 5 → 6 → 1 → 8 → 4 → 5 → "4" → 1 → 8
# > (3 + 2) + 2