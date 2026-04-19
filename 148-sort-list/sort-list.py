# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):

        if head is None or head.next is None:
            return head

        slow =head
        fast = head
        prev = None

        if head.next is None:
            return head

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = head
        right = slow
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        return self.mergesortll(left_sorted,right_sorted)

    def mergesortll(self,l1,l2):

        dummy = ListNode(0)
        tail  = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next



