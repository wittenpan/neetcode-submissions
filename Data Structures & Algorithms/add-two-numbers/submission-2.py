# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        returnHead = ListNode()
        curr = returnHead
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = (l1val+l2val+carry)%10
            carry = 1 if l1val+l2val+carry>=10 else 0
            curr.next = ListNode(val)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return returnHead.next