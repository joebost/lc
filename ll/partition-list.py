# 86
# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 5/9/21
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        greaterHead = ListNode(0)
        lesserHead = ListNode(0)
        greater = greaterHead
        lesser = lesserHead
        while head is not None:
            if head.val < x:
                lesser.next = head
                lesser = lesser.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        greater.next = None
        lesser.next = greaterHead.next
        return lesserHead.next