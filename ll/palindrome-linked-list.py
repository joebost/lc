# 234
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 4/18/21
class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		og = ""
		node = head
		while node:
			og += str(node.val)
			node = node.next
		return og[::-1] == og