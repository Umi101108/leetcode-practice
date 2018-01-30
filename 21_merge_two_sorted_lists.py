"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

        # if None in (l1, l2):
        #     return l1 or l2
        # dummy = cur = ListNode(0)
        # dummy.next = l1
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         l1 = l1.next
        #     else:
        #         nxt = cur.next
        #         cur.next = l2
        #         tmp = l2.next
        #         l2.next = nxt
        #         l2 = tmp
        #     cur = cur.next
        # cur.next = l1 or l2
        # return dummy.next

l1 = ListNode(1)
l1.next = ListNode(3)
l2 = ListNode(2)
l2.next = ListNode(4)
l1.next.next = ListNode(5)

so = Solution()
l =  so.mergeTwoLists(l1, l2)

while l:
    print l.val
    l = l.next
