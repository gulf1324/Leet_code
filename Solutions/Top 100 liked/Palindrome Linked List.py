# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#######################################################################################################################################
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find the middle of the list => slow
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Compare the first half and the reversed second half
        left, right = head, prev
        while right: # The reversed part might be shorter
            print(left.val, right.val)
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        print(left.val if left else left, right.val if right else right)
        return True        
#######################################################################################################################################
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(2)
head1.next.next.next.next = ListNode(1)

s = Solution()
print(s.isPalindrome(head1))

# >>> True
# >>> 1 1
# >>> 2 2
# >>> 3 3
# >>> None None
# ex) 1 → 2 → 3 ← 2 ← 1 
#             ↓
#            None

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)
print(s.isPalindrome(head1))

# >>> True
# >>> 1 1
# >>> 2 2
# >>> 2 None
# ex) 1 → 2 → 2 ← 1 
#             ↓
#            None