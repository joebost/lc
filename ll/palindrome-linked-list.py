# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		og = ""
		node = head
		while node:
			og += str(node.val)
			node = node.next
		return og[::-1] == og