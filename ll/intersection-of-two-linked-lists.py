# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visitedNodes = set()
        while headA is not None:
          visitedNodes.add(headA)
          headA = headA.next
        while headB is not None:
          if headB in visitedNodes:
            return headB
          headB = headB.next
        return None

class Solutionv2:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      a, b = headA, headB
      if a is not None and b is not None:
        while a != b:
          a = headB if a is None else a.next
          b = headA if b is None else b.next
        return a
      return None