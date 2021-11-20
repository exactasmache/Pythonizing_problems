from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Idea: Iterate over the list inverting the pointers direction
               [v0, 0] -> [v1, 1], -> [v2, 2] ->>> [vn-1, n-1]
        prev     head
                 prev        head
        '''
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def reverseList_rec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
          Solving recursively
        '''
        if not head or not head.next:
            return head
        rev = self.reverseList_rec(head.next)
        head.next.next = head
        head.next = None
        return rev
