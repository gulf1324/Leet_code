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
#######################################################################
from typing import Optional
from copy import deepcopy
class Solution:
    def find_mid_node(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse_llist(self, head: Optional[ListNode]) -> int:
        current = head
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head.next.next == None:
            return head.val + head.next.val
        head_ = deepcopy(head)
        slow, fast = head, head
        rev_head = self.reverse_llist(head_)
        max_pairSum = float("-inf")
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            max_pairSum = max(head.val + rev_head.val, max_pairSum)
            rev_head = rev_head.next
            head = head.next
        max_pairSum = max(head.val + rev_head.val, max_pairSum)
        return max_pairSum
#######################################################################
# mid_node/ reverse second half/ find max pair
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # now find max_sum
        max_sum = 0
        first = head 
        second = prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next 
                   
        return max_sum
#######################################################################
# mid_node, reverse first half/ find max pair
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        rev_head = None
        current, currHalf = head, head

        # reverse while mid_node
        while currHalf and currHalf.next:
            currHalf = currHalf.next.next
            temp = current.next
            current.next = rev_head
            rev_head = current
            current = temp

        while current:
            # None <- (5) <- (4) <- (2) / (1) -> (5) -> (6) -> None
            ans = max(ans, rev_head.val + current.val)
            current = current.next
            rev_head = rev_head.next
        return ans
#######################################################################
# just with a list
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        temp = head
        max_sum = 0
        while temp:
            l.append(temp.val)
            temp = temp.next
        
        n = len(l)
        for i in range(n // 2):
            max_sum = max(max_sum, l[i] + l[n - i - 1])
        return max_sum
#######################################################################
head1 = ListNode(5)
head1.next = ListNode(4)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
print_list(head1)

s = Solution()
# print(s.find_mid_node(head1))
# print_list(s.reverse_llist(head1))

res = s.pairSum(head1)
print(res)