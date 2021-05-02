# 9
# https://leetcode.com/problems/palindrome-number/

## 5/1/21
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        # is string equal to reverse string
        return s == s[::-1]