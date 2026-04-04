# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        #find middle
        if not head and head.next is None:
            return True
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        #reverse second half array
        prev = None
        while slow:
            front = slow.next
            slow.next = prev
            prev = slow
            slow = front

        #compare both elements

        right = prev
        left = head
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True

            

        

        