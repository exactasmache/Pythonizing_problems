from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) \
      -> Optional[ListNode]:
        '''
            Idea: having two pointers with a window of n elements.
            - Note: If the amount of nodes is assured to be greater than 0,
            we do not need to receive an Optional.

            [v1, 0] -> .. -> [v2, k-n+1] .. -> [v3, k-1] -> [v4, k] -> None
        '''
        nth = head
        last = head
        for i in range(n):
            # if last is None:    # Since n <= len(list), this is not necessary
            #     return None
            last = last.next

        if last is None:
            return nth.next

        while True:
            last = last.next
            if last is None:
                nth.next = nth.next.next
                return head
            nth = nth.next
